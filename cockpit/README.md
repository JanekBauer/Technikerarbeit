# TA-Cockpit (statische Fassung)

Lesefassung des Cockpits „Messanlage für Rohre“. Läuft ohne Claude, ohne Server und ohne Anmeldung.

- **Ansehen:** `docs/index.html` im Browser öffnen (funktioniert auch lokal als einzelne Datei).
- **Daten ändern:** Einträge in `cockpit/daten/<sammlung>.json` bearbeiten
  (tasks, deadlines, questions, reqs, decisions, conflicts, kilog, sensors, files, tools …).
- **Neu bauen:** `python cockpit/build.py` → schreibt `docs/index.html`.
- **Veröffentlichen (GitHub Pages):** Repo-Einstellungen → Pages → Branch `main`, Ordner `/docs`.

Nicht enthalten: vertrauliche Betriebsdateien (Spezifikationen, Angebote, Mails, Prüfanweisung)
und die Dateien selbst. Die Dateiliste zeigt nur Metadaten.

## Bearbeiten im Cockpit
Oben rechts „Bearbeiten freischalten“ wählen und ein GitHub-Zugriffstoken einfügen
(fein abgestuftes Token, nur dieses Repo, Berechtigung „Contents: Read and write“).
Das Token bleibt nur im Browser. Danach speichern „Bearbeiten“ und „Löschen“ direkt als Commit
in `cockpit/daten/*.json`. Eine GitHub-Action (`.github/workflows/cockpit-bauen.yml`) baut
`docs/index.html` danach neu; die Seite zeigt Änderungen nach ca. 1 Minute auch nach einem Neuladen.
Claude liest beim nächsten `git pull` die geänderten Daten (siehe `CLAUDE.md`).

## Dateien hoch- und herunterladen
Im Archiv gibt es „Datei hochladen“, „Neue Version“ und „Datei hinzufügen“. Die Datei wird als Commit nach
`docs/archiv/<Ordner>/<Dokument>/<Version>_<Name>` gelegt (max. 20 MB), der Eintrag landet in `cockpit/daten/files.json`.
Herunterladen geht direkt über die Seite (frisch hochgeladene Dateien nach ca. 1 Minute).
Das Repo ist öffentlich: keine vertraulichen Betriebsunterlagen hochladen. Dateinamen mit Angebot, Quotation, RM0, IP0, Spez_
oder .eml löst eine Rückfrage aus.
Claude Code zu Hause bekommt die Dateien mit `git pull` (Ordner `docs/archiv`).
