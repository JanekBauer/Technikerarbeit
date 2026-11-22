#!/usr/bin/env python3
"""Erzeugt die Vorbereitungsdatei (Word, .docx) für einen Freitag.

Standard: der nächste Freitag ab heute (Berliner Zeit).

Aufruf (im Repo-Hauptordner):
    python cockpit/vorbereitung.py                   # nächster Freitag ab heute
    python cockpit/vorbereitung.py --fr 2026-11-27   # bestimmter Freitag
    python cockpit/vorbereitung.py --fr 2026-11-27 --neu   # vorhandene Datei neu erzeugen

Schreibt docs/archiv/9 Termin-Vorbereitung/Freitag_<Datum>.docx und trägt die Datei in
cockpit/daten/files.json ein. Vorschläge von Claude Code stehen in
cockpit/vorbereitung/<Datum>_vorschlaege.md und werden beim Erzeugen in die Datei übernommen.
Ist die Datei schon da, bleibt sie unverändert (außer mit --neu).
"""
import argparse, datetime as dt, json, pathlib, zipfile
from xml.sax.saxutils import escape
from zoneinfo import ZoneInfo

BASIS = pathlib.Path(__file__).resolve().parent
DATEN = BASIS / "daten"
VORSCHLAEGE = BASIS / "vorbereitung"
ARCHIV_ORDNER = "9 Termin-Vorbereitung"
ZIEL = BASIS.parent / "docs" / "archiv" / ARCHIV_ORDNER


def laden(name):
    return json.loads((DATEN / f"{name}.json").read_text(encoding="utf-8"))


def freitag_ab(d):
    return d + dt.timedelta(days=(4 - d.weekday()) % 7)


def termin_fuer(faellig):
    """Gleiche Regel wie im Cockpit: früheste offene Termin am oder nach dem Datum, sonst der Freitag."""
    fri = freitag_ab(dt.date.fromisoformat(faellig)).isoformat()
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


# ---------- Word-Datei (ohne zusätzliche Pakete) ----------

def absatz(text, stil=None, fett=False):
    ppr = f'<w:pPr><w:pStyle w:val="{stil}"/></w:pPr>' if stil else ""
    rpr = "<w:rPr><w:b/></w:rPr>" if fett else ""
    return f'<w:p>{ppr}<w:r>{rpr}<w:t xml:space="preserve">{escape(text)}</w:t></w:r></w:p>'


def word_bytes(absaetze):
    """Schreibt eine minimale, gültige .docx-Datei mit den übergebenen Absätzen (XML-Fragmente)."""
    dokument = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>'
        + "".join(absaetze) +
        '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134" w:header="708" w:footer="708" w:gutter="0"/></w:sectPr>'
        "</w:body></w:document>"
    )
    stile = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="22"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:after="200"/></w:pPr><w:rPr><w:b/><w:sz w:val="40"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:pPr><w:keepNext/><w:spacing w:before="280" w:after="120"/><w:outlineLvl w:val="0"/></w:pPr><w:rPr><w:b/><w:sz w:val="28"/></w:rPr></w:style>'
        '</w:styles>'
    )
    ct = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
        '</Types>'
    )
    rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
        '</Relationships>'
    )
    doc_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
        '</Relationships>'
    )
    import io
    puffer = io.BytesIO()
    with zipfile.ZipFile(puffer, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", ct)
        z.writestr("_rels/.rels", rels)
        z.writestr("word/document.xml", dokument)
        z.writestr("word/_rels/document.xml.rels", doc_rels)
        z.writestr("word/styles.xml", stile)
    return puffer.getvalue()


def vorschlaege_text(fri_iso):
    datei = VORSCHLAEGE / f"{fri_iso}_vorschlaege.md"
    if datei.exists():
        return [z.rstrip() for z in datei.read_text(encoding="utf-8").splitlines() if z.strip()]
    return None


def erzeuge(fri_iso, neu=False):
    fr_id = "fr-" + fri_iso
    dateiname = f"Freitag_{fri_iso}.docx"
    ziel_datei = ZIEL / dateiname
    if ziel_datei.exists() and not neu:
        print("Datei gibt es schon, unverändert:", ziel_datei)
        return False

    jetzt_utc = dt.datetime.now(dt.timezone.utc)
    tasks = [t for t in laden("tasks") if t.get("due") and t.get("status") != "erledigt" and termin_fuer(t["due"]) == fr_id]
    checks = laden("checks")
    liste = next((c for c in checks if c.get("id") == fr_id), None)
    dateien = [f for f in laden("files") if f.get("deadline") == fr_id and not f.get("missing")]
    kern = {}
    for f in laden("files"):
        if f.get("missing") or str(f.get("folder", "")).split(" ")[0] not in ("2", "3", "4"):
            continue
        fam = f.get("family") or f.get("name")
        if fam not in kern or (f.get("seq") or 0) > (kern[fam].get("seq") or 0):
            kern[fam] = f
    dateien += [f for f in kern.values() if f not in dateien]

    a = [absatz(f"Vorbereitung Freitag, {fd(fri_iso)}", "Title")]
    a.append(absatz(f"Erstellt am {jetzt_utc.astimezone(ZoneInfo('Europe/Berlin')).strftime('%d.%m.%Y, %H:%M')} Uhr (Berliner Zeit) aus dem Cockpit."))

    a.append(absatz("Fragen und Entscheidungen", "Heading1"))
    if tasks:
        for t in sorted(tasks, key=lambda t: (t.get("typ") != "entscheidung", t.get("title", ""))):
            art = "Entscheidung" if t.get("typ") == "entscheidung" else "Aufgabe"
            a.append(absatz(f"☐  {art}: {t.get('title', '')}", fett=True))
            a.append(absatz(f"Fällig: {fd(t['due'])} · Wer führt durch: {t.get('who') or '–'} · Wen fragen: {t.get('ask') or '–'}"))
            a.append(absatz("Antwort: ______________________________________________________________"))
    else:
        a.append(absatz("Keine offenen Fragen oder Entscheidungen mit diesem Datum."))

    items = (liste or {}).get("items", [])
    erledigt = sum(1 for i in items if i.get("done"))
    a.append(absatz(f"Checkliste des Tages ({erledigt} von {len(items)} erledigt)", "Heading1"))
    if items:
        for i in items:
            a.append(absatz(f"{'☒' if i.get('done') else '☐'}  {i.get('t', '')}"))
    else:
        a.append(absatz("Keine Checkliste für diesen Tag."))

    a.append(absatz("Dateien aus dem Archiv", "Heading1"))
    if dateien:
        for f in dateien:
            a.append(absatz(f"{f.get('name', '')}  ({f.get('folder', '')}, {f.get('ver', '')})"))
            a.append(absatz(f"Pfad im Repo: {f.get('path', '')}"))
    else:
        a.append(absatz("Keine Dateien zugeordnet."))

    a.append(absatz("Vorschläge (Claude Code)", "Heading1"))
    vs = vorschlaege_text(fri_iso)
    if vs:
        for z in vs:
            a.append(absatz(z[2:] if z.startswith("- ") else z))
    else:
        a.append(absatz("Noch keine Vorschläge. Claude Code ergänzt diesen Abschnitt am Freitag, wenn es erreichbar ist."))

    ZIEL.mkdir(parents=True, exist_ok=True)
    ziel_datei.write_bytes(word_bytes(a))
    print("geschrieben:", ziel_datei)

    pfad_repo = f"archiv/{ARCHIV_ORDNER}/{dateiname}"
    dat_pfad = DATEN / "files.json"
    akt = json.loads(dat_pfad.read_text(encoding="utf-8"))
    eintrag = {
        "id": "vb-" + fri_iso, "src": "repo", "path": pfad_repo, "size": ziel_datei.stat().st_size,
        "mime": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "name": dateiname, "folder": ARCHIV_ORDNER, "family": "Termin-Vorbereitung",
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
    ap.add_argument("--neu", action="store_true", help="vorhandene Datei neu erzeugen")
    a = ap.parse_args()
    if a.fr:
        fri = dt.date.fromisoformat(a.fr)
        assert fri.weekday() == 4, "Das Datum ist kein Freitag"
    else:
        fri = freitag_ab(dt.datetime.now(ZoneInfo("Europe/Berlin")).date())
    erzeuge(fri.isoformat(), a.neu)


if __name__ == "__main__":
    main()
