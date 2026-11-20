# Regeln für Claude (Technikerarbeit Janek Bauer)

- Sprich Janek als „Janek“ an, antworte auf Deutsch.
- **Vor jeder Aufgabe zuerst `git pull`.** Janek ändert Daten auch selbst im Web-Cockpit; diese
  Änderungen kommen als Commits auf `main` ins Repo.
- **Maßgeblich für den Projektstand sind die Dateien in `cockpit/daten/*.json`**
  (offene Punkte = `tasks.json`, Termine = `deadlines.json`, Fragen = `questions.json`,
  Anforderungen = `reqs.json`, Widersprüche = `conflicts.json`, KI-Logbuch = `kilog.json` usw.).
  Was dort fehlt, wurde gelöscht; was dort „erledigt“ ist, ist erledigt. Verlasse dich nicht auf
  ältere Chat-Stände.
- Daten ändern: JSON-Datei bearbeiten (ein Eintrag pro Zeile, `id` beibehalten), danach
  `python cockpit/build.py` ausführen und `cockpit/daten` plus `docs/index.html` zusammen committen.
- **Postfach:** Neue Aufgaben, Entscheidungen und Änderungen landen zuerst als Eintrag in `cockpit/daten/postfach.json` (`status` „neu“, `kind`: aufgabe/entscheidung/aenderung, `title`, `detail`, `vorschlag`, `stand`, `date`). Janek übernimmt oder verwirft sie im Postfach. Eine Entscheidung ist eine Aufgabe mit `typ: "entscheidung"` in `tasks.json`; sie erscheint unter Aufgaben und unter Entscheidungen und hat überall denselben Status. Fragen an den Betrieb und Widersprüche sind Entscheidungen. Nicht direkt in `tasks.json` oder `changes.json` schreiben; `decisions.json`, `questions.json` und `conflicts.json` sind nicht mehr in Gebrauch.
- **Postfach-Vorschläge:** Neue Einträge im Postfach bekommen in `vorschlag` immer den Urheber, z. B. „KI (Claude Code)“, damit Janek sieht, woher der Vorschlag kommt.
- **Änderungsdoku:** `cockpit/daten/changes.json` bleibt leer, bis Janek sagt, dass das Pflichtenheft unterschrieben ist und eine Änderungsdoku nötig ist. Erst dann Einträge anlegen.
- **Zeitstempel:** `updated` nie erfinden. Immer `date -u +%Y-%m-%dT%H:%M:%SZ` verwenden. Die Übersicht zeigt den neuesten `updated`-Wert als Stand.
- Nach jeder abgeschlossenen Aufgabe: geänderte Dateien committen (Nachricht auf Deutsch: was und warum) und pushen.
- **Projektabgleich:** Auf Zuruf „Projektabgleich“ gleicht Claude Code die Daten in `cockpit/daten/*.json` mit den Dokumenten im Repo ab; das Repo gewinnt bei Wertkonflikten. Das frühere Verfahren mit dem Claude-Artefakt und dem Skill ist archiviert (`cockpit/_Versionen/abgleich_2026-11-18/`, `cockpit/skill/_Versionen/`). Nicht automatisch starten.
- Ältere Versionen nicht löschen, sondern in den Unterordner `_Versionen` verschieben. Nichts endgültig löschen.
- Jede KI-Hilfe in `cockpit/daten/kilog.json` bzw. `KI-Logbuch.md` eintragen (Datum, Aufgabe, Art der Hilfe).
- **Branch-Namen:** Neue Branches heißen `Main_JJJJ-MM-TT_HH-MM`, mit dem Datum und der Uhrzeit (deutsche Zeit,
  Europe/Berlin) des Erstellungszeitpunkts, z. B. `Main_2026-11-18_16-30`. Die Uhrzeit ermittelt man mit
  `TZ=Europe/Berlin date +%Y-%m-%d_%H-%M`. Bindestrich statt Doppelpunkt, weil Git Doppelpunkte in Branch-Namen nicht erlaubt.

- **Vertrauliche Betriebsunterlagen im Repo:** Janek hat am 20.11.2026 entschieden, dass die vorhandenen Rohrspezifikationen und die Prüfanweisung im Repo bleiben. Dazu nicht mehr nachfragen.
- **Geplante Aufgabe Wochenstatus (Freitag):** am 20.11.2026 gelöscht; Aufbau, Zeitplan und Prompt stehen in `projekt/Geplante_Aufgabe_Wochenstatus_Freitag.md`.
