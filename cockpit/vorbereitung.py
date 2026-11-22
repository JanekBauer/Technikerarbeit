#!/usr/bin/env python3
"""Erzeugt die Vorbereitungsdatei für einen Freitag (Standard: der nächste Freitag ab heute, Berliner Zeit).

Aufruf (im Repo-Hauptordner):
    python cockpit/vorbereitung.py                 # nächster Freitag ab heute
    python cockpit/vorbereitung.py --fr 2026-11-27 # bestimmter Freitag
    python cockpit/vorbereitung.py --fr 2026-11-27 --neu   # vorhandene Datei ersetzen

Schreibt docs/archiv/9 Termin-Vorbereitung/Freitag_<Datum>.md und trägt die Datei in
cockpit/daten/files.json ein. Ist die Datei schon da, bleibt sie unverändert (damit Vorschläge
von Claude Code nicht verloren gehen), außer mit --neu.
"""
import argparse, datetime as dt, json, pathlib, urllib.parse
from zoneinfo import ZoneInfo

BASIS = pathlib.Path(__file__).resolve().parent
DATEN = BASIS / "daten"
ARCHIV_ORDNER = "9 Termin-Vorbereitung"
ZIEL = BASIS.parent / "docs" / "archiv" / ARCHIV_ORDNER
CHK_FOR_TERMIN = {"d05": "m1", "d08": "m2", "d10": "m3", "d11": "abgabe", "d12": "praesi", "d13": "praesi"}


def laden(name):
    return json.loads((DATEN / f"{name}.json").read_text(encoding="utf-8"))


def freitag_ab(d):
    return d + dt.timedelta(days=(4 - d.weekday()) % 7)


def termin_fuer(faellig):
    """Gleiche Regel wie im Cockpit: früheste offene Termin am oder nach dem Datum, sonst der Freitag."""
    d = dt.date.fromisoformat(faellig)
    fri = freitag_ab(d).isoformat()
    echt = sorted(
        [x for x in laden("deadlines") if x.get("status") != "erledigt" and x.get("date") and x["date"] >= faellig],
        key=lambda x: x["date"],
    )
    if echt and echt[0]["date"] <= fri:
        return echt[0]["id"]
    return "fr-" + fri


def fd(iso):
    d = dt.date.fromisoformat(iso)
    return f"{d.day:02d}.{d.month:02d}.{d.year}"


def erzeuge(fri_iso, neu=False):
    fr_id = "fr-" + fri_iso
    dateiname = f"Freitag_{fri_iso}.md"
    ziel_datei = ZIEL / dateiname
    if ziel_datei.exists() and not neu:
        print("Datei gibt es schon, unverändert:", ziel_datei)
        return False

    jetzt_utc = dt.datetime.now(dt.timezone.utc)
    tasks = [t for t in laden("tasks") if t.get("due") and t.get("status") != "erledigt" and termin_fuer(t["due"]) == fr_id]
    checks = laden("checks")
    liste = next((c for c in checks if c.get("id") == fr_id), None)
    dateien = [f for f in laden("files") if f.get("deadline") == fr_id and not f.get("missing")]
    # Kerndokumente: jeweils neueste Version je Familie (Ordner 2, 3, 4)
    kern = {}
    for f in laden("files"):
        if f.get("missing") or not str(f.get("folder", "")).split(" ")[0] in ("2", "3", "4"):
            continue
        fam = f.get("family") or f.get("name")
        if fam not in kern or (f.get("seq") or 0) > (kern[fam].get("seq") or 0):
            kern[fam] = f
    dateien += [f for f in kern.values() if f not in dateien]

    zeilen = [f"# Vorbereitung Freitag, {fd(fri_iso)}", "",
              f"_Erstellt am {jetzt_utc.astimezone(ZoneInfo('Europe/Berlin')).strftime('%d.%m.%Y, %H:%M')} Uhr (Berliner Zeit) aus dem Cockpit._", "",
              "## Fragen und Entscheidungen", ""]
    if tasks:
        for t in sorted(tasks, key=lambda t: (t.get("typ") != "entscheidung", t.get("title", ""))):
            art = "Entscheidung" if t.get("typ") == "entscheidung" else "Aufgabe"
            zeilen += [f"- [ ] **{art}:** {t.get('title', '')}",
                       f"  Fällig: {fd(t['due'])} · Wer führt durch: {t.get('who') or '–'} · Wen fragen: {t.get('ask') or '–'}",
                       "  Antwort: ", ""]
    else:
        zeilen += ["Keine offenen Fragen oder Entscheidungen mit diesem Datum.", ""]

    items = (liste or {}).get("items", [])
    erledigt = sum(1 for i in items if i.get("done"))
    zeilen += [f"## Checkliste des Tages ({erledigt} von {len(items)} erledigt)", ""]
    if items:
        zeilen += [f"- [{'x' if i.get('done') else ' '}] {i.get('t', '')}" for i in items] + [""]
    else:
        zeilen += ["Keine Checkliste für diesen Tag.", ""]

    zeilen += ["## Dateien aus dem Archiv", ""]
    if dateien:
        for f in dateien:
            pfad = "../" + "/".join(urllib.parse.quote(teil) for teil in f["path"].split("/")[1:])
            zeilen.append(f"- [{f.get('name', '')}]({pfad}) · {f.get('folder', '')} · {f.get('ver', '')}")
        zeilen.append("")
    else:
        zeilen += ["Keine Dateien zugeordnet.", ""]

    zeilen += ["## Vorschläge (Claude Code)", "",
               "_Noch keine Vorschläge. Claude Code ergänzt diesen Abschnitt am Freitag, wenn es erreichbar ist._", ""]

    ZIEL.mkdir(parents=True, exist_ok=True)
    ziel_datei.write_text("\n".join(zeilen), encoding="utf-8")
    print("geschrieben:", ziel_datei)

    # Archiv-Eintrag, damit die Datei im Archiv und am Termin erscheint
    pfad_repo = f"archiv/{ARCHIV_ORDNER}/{dateiname}"
    dat_pfad = DATEN / "files.json"
    akt = json.loads(dat_pfad.read_text(encoding="utf-8"))
    eintrag = {
        "id": "vb-" + fri_iso, "src": "repo", "path": pfad_repo, "size": ziel_datei.stat().st_size,
        "mime": "text/markdown", "name": dateiname, "folder": ARCHIV_ORDNER, "family": "Termin-Vorbereitung",
        "ver": fd(fri_iso), "seq": int(fri_iso.replace("-", "")), "date": jetzt_utc.date().isoformat(),
        "note": "Automatisch aus dem Cockpit erstellt", "kind": "Vorbereitung", "missing": False,
        "by": "GitHub Action", "gilt": True, "updated": jetzt_utc.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "deadline": fr_id,
    }
    akt = [e for e in akt if e.get("id") != eintrag["id"]] + [eintrag]
    roh = "[\n" + ",\n".join(json.dumps(o, ensure_ascii=False, separators=(",", ":")) for o in akt) + "\n]\n"
    dat_pfad.write_text(roh, encoding="utf-8")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fr", help="Freitag als JJJJ-MM-TT")
    ap.add_argument("--neu", action="store_true", help="vorhandene Datei ersetzen")
    a = ap.parse_args()
    if a.fr:
        fri = dt.date.fromisoformat(a.fr)
        assert fri.weekday() == 4, "Das Datum ist kein Freitag"
    else:
        heute = dt.datetime.now(ZoneInfo("Europe/Berlin")).date()
        fri = freitag_ab(heute)
    erzeuge(fri.isoformat(), a.neu)


if __name__ == "__main__":
    main()
