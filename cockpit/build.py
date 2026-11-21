#!/usr/bin/env python3
"""Baut docs/index.html aus cockpit/vorlage.html und den Daten in cockpit/daten/*.json.

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
import os, subprocess
# Bearbeiten im Cockpit schreibt in den Branch, auf dem diese Seite gebaut wird (nie fest auf main)
branch = os.environ.get("GITHUB_REF_NAME") or subprocess.run(["git","rev-parse","--abbrev-ref","HEAD"],cwd=basis,capture_output=True,text=True).stdout.strip() or "main"
repo = os.environ.get("GITHUB_REPOSITORY") or "JanekBauer/Technikerarbeit"
html = (basis / "vorlage.html").read_text(encoding="utf-8").replace("<!--DATEN-->", roh).replace("__REPO__", repo).replace("__BRANCH__", branch)

ziel = basis.parent / "docs"
ziel.mkdir(exist_ok=True)
(ziel / "index.html").write_text(html, encoding="utf-8")
(ziel / ".nojekyll").write_text("", encoding="utf-8")
print("docs/index.html geschrieben:", len(html) // 1024, "KB;", sum(len(v) for v in daten.values()), "Einträge in", len(daten), "Sammlungen")
