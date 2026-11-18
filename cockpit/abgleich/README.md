# Abgleich-Pakete (Chat → GitHub-App)

Dieser Ordner nimmt die Abgleich-Pakete aus dem Chat „00 Cockpit“ auf (Skill `cockpit/skill/SKILL.md`).

- `eingang/` – neue, noch nicht verarbeitete Pakete `paket_JJJJ-MM-TT_HH-MM.json`
- `_Verarbeitet/` – bereits verarbeitete Pakete (nichts wird gelöscht, nur verschoben)

## Verarbeitung in der GitHub-App (Claude Code im Repo)

Nur auf ausdrücklichen Zuruf „Abgleich verarbeiten“ (nicht automatisch, damit keine Tokens verbraucht werden).

1. `git pull`. Alle Dateien in `eingang/` lesen.
2. Jede Änderung gegen `cockpit/daten/<sammlung>.json` prüfen:
   - `aendern` mit `id`: Eintrag suchen. Fehlt die `id`, in `rueckfragen` aufnehmen, nicht anlegen.
   - `neu`: vorhandene Einträge zum selben Thema suchen. Gibt es einen, ändern statt anlegen. Sonst neue `id` vergeben (wie bestehende Ids, z. B. `t-…`, `q-…`, `w01`).
   - Statuswerte nur aus der erlaubten Liste (siehe `SKILL.md`). Sonst nicht übernehmen, sondern melden.
3. **Vorrang Janek:** Hat Janek einen Eintrag seit dem Beleg-Datum selbst geändert (`updated` jünger als `beleg`), wird er nicht überschrieben. Die Abweichung kommt in den Bericht.
4. **Keine Löschungen.** Ältere Stände nach `_Versionen/` verschieben, falls eine Datei ersetzt wird.
5. Alle Änderungen in die JSON-Dateien schreiben (ein Eintrag pro Zeile, `id` beibehalten), dann `python cockpit/build.py`.
6. Paket nach `cockpit/abgleich/_Verarbeitet/` verschieben.
7. Commit mit `cockpit/daten`, `docs/index.html` und `cockpit/abgleich` zusammen, Nachricht auf Deutsch, dann push.
8. Bericht an Janek: übernommen (je Sammlung) · Abweichungen (nicht geändert) · Rückfragen · Ids, die fehlten.

Bei Widersprüchen zwischen Paket und Repo gilt: nachfragen, nicht raten.
