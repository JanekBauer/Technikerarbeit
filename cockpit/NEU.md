# Neue Cockpit-Version (Branch `main_neu`)

Das ist eine **Testversion**. Die aktuelle Seite auf `main` (`docs/index.html`) ist unverändert.

## Öffnen
Datei `docs/index_neu.html` herunterladen (auf GitHub: Branch `main_neu` → `docs` → `index_neu.html` → „Download raw file“) und per Doppelklick im Browser öffnen. Die Daten sind eingebettet, die Seite läuft ohne Server.

**Wichtig:** Änderungen, die du in dieser Datei mit Token speicherst, gehen nur auf den Branch `main_neu`, nicht auf `main`. So kannst du ohne Risiko ausprobieren.

## Neu gegenüber der aktuellen Version
- **Suche und Befehle (Strg+K oder `/`)**: Durchsucht Punkte, Termine, Fragen, Anforderungen, Entscheidungen, Widersprüche, Quellen, Kapitel, Sensoren, Dateien und KI-Logbuch. Springt zu Seiten und legt neue Einträge an („Neuer Termin“ usw.). Umlaute und Groß-/Kleinschreibung sind egal.
- **Offene Punkte als Board**: Umschalter Tabelle / Board. Karten lassen sich zwischen „offen“, „in Arbeit“, „wartet“, „erledigt“ ziehen (nur mit Bearbeiten-Token; Karte antippen öffnet wie bisher das Detailfenster).
- **Termine als Kalenderdatei**: Knopf „In Kalender übernehmen (.ics)“ in der Terminleiste. Alle offenen Termine als ganztägige Einträge, importierbar in Outlook, Google Kalender, Handy.
- **Übersicht**: Karte „Dokumentation“ (Seiten geschrieben/geplant, Wochen bis zur Abgabe, Kapitel nach Status) und „Diese Woche geändert“ mit Knopf **Wochenbericht kopieren** (Text mit Erledigtem, nächsten Schritten und Terminen, z. B. für Hr. Graudejus oder Hr. Baidinger). Ersetzt den früheren Wochenrückblick.
- Hinweis-Banner „Neue Version (Test)“ ganz oben.

## Aus der Recherche, bewusst noch nicht umgesetzt
- Entscheidungen mit Anforderungen verknüpfen (Rückverfolgbarkeit, z. B. wie bei Doorstop) und bei Entscheidungen einen Status „ersetzt durch“ führen. Bräuchte neue Felder und Pflege der vorhandenen Daten.
- Gantt-Ansicht im Cockpit (der Projektplan liegt in Rillsoft).
- Kalender-Abo (Live-Kalender statt Datei): braucht einen Server.

## Quellen der Recherche
- Thesis-Dashboards (Notion): [Complete Thesis Planner](https://dianayukari.com/templates/complete-thesis-planner), [How I Use Notion for Writing a Thesis](https://simonesmerilli.com/writing/thesis-notion)
- Dashboards und Ansichten (Obsidian): [Planner](https://community.obsidian.md/plugins/planner), [Xove Dashboard](https://community.obsidian.md/plugins/xove-dashboard), Befehlspalette/Suche: [Cove](https://github.com/codejunkie99/cove)
- Rückverfolgbarkeit: [Doorstop](https://doorstop.readthedocs.io/)
- Entscheidungsprotokolle: [Decision Log Template](https://playcode.io/blog/decision-log-template)
- Zeitplanung: [Schreibzeit planen (TH Nürnberg)](https://www.th-nuernberg.de/fileadmin/zentrale-einrichtungen/leko/Dokumente/%C3%9Cberfachliche_Kompetenzen/SZHandouts_2022/09_-_Schreibzeit_planen.pdf), [Tipps und Tricks (TUM)](https://www.tum.de/studium/studienabschluss/abschlussarbeit/tipps-und-tricks)

## Live schalten
Wenn die Testversion gefällt: `vorlage_neu.html` wird zu `vorlage.html`, `build.py` baut wieder nur eine Seite. Vorher `main` in `main_neu` mergen, weil du auf `main` Daten änderst.
