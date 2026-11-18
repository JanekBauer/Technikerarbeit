#!/usr/bin/env python3
"""Gleicht cockpit/daten/*.json (Repo, maßgeblich) mit dem Claude-Artefakt-Stand ab.

Verwendung (im Repo-Hauptordner):
  python cockpit/abgleich/abgleich.py diff  <artefakt_dump>
  python cockpit/abgleich/abgleich.py plan  <artefakt_dump> <versionen.json> <ausgabe_ordner>

<artefakt_dump>  Ordner mit <sammlung>/<doc_id>.json (ArtifactData-Abfrage mit out_dir).
<versionen.json> {"sammlung": {"doc_id": version, ...}, ...} aus der Listen-Ausgabe von ArtifactData.
<ausgabe_ordner> Ziel für je ein JSON pro Dokument; ausgegeben wird eine batch-Liste für ArtifactData.

Regel: Bei abweichenden Werten gewinnt das Repo. Dokumente, die nur im Artefakt stehen,
werden NICHT gelöscht; sie müssen vorher ins Repo übernommen werden (siehe README).
"""
import json, pathlib, sys

BASIS = pathlib.Path(__file__).resolve().parent.parent / "daten"
SAMMLUNGEN = ["tasks", "questions", "deadlines", "conflicts", "reqs", "kilog"]


def repo_stand(sammlung):
    liste = json.loads((BASIS / f"{sammlung}.json").read_text(encoding="utf-8"))
    return {e["id"]: {k: v for k, v in e.items() if k != "id"} for e in liste}


def artefakt_stand(dump, sammlung):
    ordner = pathlib.Path(dump) / sammlung
    return {f.stem: json.loads(f.read_text(encoding="utf-8")) for f in ordner.glob("*.json")}


def diff(dump):
    for c in SAMMLUNGEN:
        r, a = repo_stand(c), artefakt_stand(dump, c)
        neu = sorted(set(r) - set(a))
        nur_a = sorted(set(a) - set(r))
        abw = sorted(i for i in set(r) & set(a) if r[i] != a[i])
        print(f"{c}: Repo {len(r)} | Artefakt {len(a)} | nur Repo {neu} | nur Artefakt {nur_a} | abweichend {len(abw)}")


def plan(dump, versionen_datei, ziel):
    versionen = json.loads(pathlib.Path(versionen_datei).read_text(encoding="utf-8"))
    ziel = pathlib.Path(ziel)
    writes = []
    for c in SAMMLUNGEN:
        r, a = repo_stand(c), artefakt_stand(dump, c)
        for i in sorted(r):
            if i in a and a[i] == r[i]:
                continue
            datei = ziel / c / f"{i}.json"
            datei.parent.mkdir(parents=True, exist_ok=True)
            datei.write_text(json.dumps(r[i], ensure_ascii=False), encoding="utf-8")
            eintrag = {"op": "set", "collection": c, "doc_id": i, "file_path": str(datei)}
            if i in a:  # bestehendes Dokument: Version pinnen, sonst wird es abgelehnt
                eintrag["if_version"] = versionen[c][i]
            writes.append(eintrag)
    print(json.dumps(writes, ensure_ascii=False))
    print(f"{len(writes)} Schreibvorgänge; in Stapeln zu max. 50 an ArtifactData batch geben", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "diff":
        diff(sys.argv[2])
    elif len(sys.argv) == 5 and sys.argv[1] == "plan":
        plan(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print(__doc__)
        sys.exit(1)
