# TA-Cockpit (statische Fassung)

Lesefassung des Cockpits „Messanlage für Rohre“. Läuft ohne Claude, ohne Server und ohne Anmeldung.

- **Ansehen:** `docs/index.html` im Browser öffnen (funktioniert auch lokal als einzelne Datei).
- **Daten ändern:** Einträge in `cockpit/daten/<sammlung>.json` bearbeiten
  (tasks, deadlines, questions, reqs, decisions, conflicts, kilog, sensors, files, tools …).
- **Neu bauen:** `python cockpit/build.py` → schreibt `docs/index.html`.
- **Veröffentlichen (GitHub Pages):** Repo-Einstellungen → Pages → Branch `main`, Ordner `/docs`.

Nicht enthalten: vertrauliche Betriebsdateien (Spezifikationen, Angebote, Mails, Prüfanweisung)
und die Dateien selbst. Die Dateiliste zeigt nur Metadaten.
