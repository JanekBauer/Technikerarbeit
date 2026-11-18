#!/usr/bin/env python3
"""Baut docs/index.html aus cockpit/vorlage.html und den Daten in cockpit/daten/*.json.
Gibt es cockpit/vorlage_neu.html, entsteht zusätzlich docs/index_neu.html (Testversion).

Aufruf (im Repo-Hauptordner):  python cockpit/build.py
Jede Datei daten/<sammlung>.json enthält eine Liste von Einträgen (mit "id").
"""
import json, pathlib

basis = pathlib.Path(__file__).resolve().parent
daten = {}
for datei in sorted((basis / "daten").glob("*.json")):
    daten[datei.stem] = json.loads(datei.read_text(encoding="utf-8"))

# </ im JSON entschärfen, damit das <script>-Element nicht vorzeitig endet
roh = json.dumps(daten, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

ziel = basis.parent / "docs"
ziel.mkdir(exist_ok=True)
for quelle, ausgabe in (("vorlage.html", "index.html"), ("vorlage_neu.html", "index_neu.html")):
    q = basis / quelle
    if not q.exists():
        continue
    html = q.read_text(encoding="utf-8").replace("<!--DATEN-->", roh)
    (ziel / ausgabe).write_text(html, encoding="utf-8")
    print(f"docs/{ausgabe} geschrieben:", len(html) // 1024, "KB;", sum(len(v) for v in daten.values()), "Einträge in", len(daten), "Sammlungen")
(ziel / ".nojekyll").write_text("", encoding="utf-8")
