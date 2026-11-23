# Regelaudit Cockpit (Stand 23.11.2026)

Geprüft: `CLAUDE.md`, `cockpit/README.md`, `cockpit/build.py`, `.github/workflows/`, die Dateien in `cockpit/daten/` sowie der Git-Verlauf (76 Commits auf `main`).

Ausgangslage: Ein Großteil des Projektstands ist inzwischen auf dem Weg über das Web-Cockpit entstanden, nicht über das Postfach. Die Regeln beschreiben aber fast nur den Postfach-Weg. Daraus folgen die meisten Widersprüche.

## 1. Wie du mit dem Cockpit arbeitest (aus Daten und Verlauf)

- **Viel Bearbeitung im Web.** Die Commits „Cockpit: N Änderungen aktualisiert (Web)“ umfassen 8 bis 69 Änderungen je Stapel. Sie schreiben direkt nach `cockpit/daten/*.json` auf `main` und gehen am Postfach vorbei.
- **Postfach als Eingang für KI-Vorschläge.** 84 Einträge: 83 übernommen, 1 verworfen. Entscheidungen (33) und Aufgaben (30) dominieren, dazu KI-Logbuch (13) und „daten“ (7).
- **Zurückgenommene Entwürfe.** Der Commit „Entwürfe 001–005 zurückgenommen (Seite, Postfach, KI-Logbuch-Eintrag)“ zeigt: KI-Ergebnisse sind direkt in die Daten gewandert und mussten wieder entfernt werden.
- **Viele Korrekturen bei Taktzeit und Entfallen.** „Taktzeit-Ampel korrigiert“, „Taktzeit komplett entfernt“, „Taktzeit neu gerechnet“, „Taktzeit aus den Fragetexten gestrichen“. Es gibt keine Regel dafür, wie eine widerrufene oder ersetzte Entscheidung behandelt wird.

## 2. Widersprüche

| # | Regel A | Regel B / Befund | Folge |
|---|---|---|---|
| W1 | CLAUDE.md: „Daten ändern: JSON bearbeiten, dann build.py“ und Postfach-Pflicht | `cockpit/README.md` beschreibt „Bearbeiten im Cockpit“: Änderungen werden direkt als Commit in `daten/*.json` geschrieben. Die Git-Historie bestätigt das (z. B. 69 und 50 Änderungen per Web). | Der Postfach-Weg wird im Alltag umgangen. Niemand prüft diese Änderungen, und das KI-Logbuch bekommt sie nicht. |
| W2 | CLAUDE.md: „`cockpit/daten/*.json` ist maßgeblich für den Projektstand“ | CLAUDE.md, Projektabgleich: „das Repo gewinnt bei Wertkonflikten“ | Zwei Quellen der Wahrheit. Unklar, ob Daten oder Dokument gelten, wenn beide abweichen. |
| W3 | CLAUDE.md: `decisions.json`, `questions.json`, `conflicts.json` sind „nicht mehr in Gebrauch“ | `decisions.json` enthält noch 6 Einträge, `build.py` lädt die Datei weiter, `cockpit/README.md` nennt sie noch als Sammlungen. Entscheidungen liegen in `tasks.json` (24 mit `typ: entscheidung`). | Zwei Orte für Entscheidungen. Die 6 Einträge in `decisions.json` sind nirgends verknüpft. |
| W4 | CLAUDE.md: Entscheidungen sind Aufgaben mit `typ: "entscheidung"` in `tasks.json` | Im Postfach sind 33 Entscheidungen übernommen, in `tasks.json` aber nur 24 mit diesem Typ. | Neun Entscheidungen aus dem Postfach fehlen in den Daten oder haben einen anderen Typ. Das ist nicht nachvollziehbar. |
| W5 | CLAUDE.md: `docs/index.html` zusammen mit den Daten committen (manuell per `build.py`) | `.github/workflows/cockpit-bauen.yml` baut die Seite nach jeder Datenänderung automatisch neu. | Doppelte Pflege. Manuelle Commits können mit dem Action-Commit kollidieren. |
| W6 | CLAUDE.md: Branch-Regel „direkt auf `main`“ | Die Session-Vorgabe verlangt einen eigenen Branch (`ccr-…`). | Für Claude-Sitzungen gibt es zwei Vorgaben. Für Claude Code im Chat gilt die CLAUDE.md nicht zwingend. |
| W7 | CLAUDE.md: `vorschlag` muss immer den Urheber nennen | 35 Postfach-Einträge haben kein `vorschlag`. | Die Regel wurde nicht eingehalten oder wurde erst später eingeführt. Den Urheber sieht man dann nicht. |
| W8 | CLAUDE.md: Vertrauliche Betriebsunterlagen bleiben im Repo (Entscheidung 20.11.) | `cockpit/README.md`: „Das Repo ist öffentlich: keine vertraulichen Betriebsunterlagen hochladen“ und „Nicht enthalten: … Spezifikationen …“. Im Archiv liegt aber ein Spezifikationsblatt (`RM021500502 – NiTi-Rohr … (Spezifikationsblatt)`). | Die Dokumentation sagt das Gegenteil dessen, was im Repo liegt. Das Repo ist öffentlich und die Seite über GitHub Pages erreichbar. Du hast entschieden, dass ich dazu nicht mehr nachfrage. Ich weise nur auf den Widerspruch in der README hin. |
| W9 | CLAUDE.md: `kilog` nur über das Postfach | `kilog.json` hat 31 Einträge, im Postfach gibt es 13 übernommene KI-Logbuch-Einträge. Die restlichen 18 haben keinen Postfach-Weg. Die Felder weichen ab: Regel `detail`, `fach`; Daten `help`, `ergebnis`, `tool`. | Das KI-Logbuch ist nicht vollständig prüfbar. |
| W10 | CLAUDE.md: `updated` nie erfinden, immer `date -u` | 9 Postfach-Einträge ohne `date`, 5 ohne `stand`. | Die Zeitstempel sind lückenhaft. Die Übersicht zeigt deshalb nicht immer den richtigen Stand. |

## 3. Lücken: Regeln für Werte, Sortierung und Verknüpfung fehlen

Das ist der Teil, den du hervorgehoben hast. Heute gibt es kaum Regeln dafür:

- **Kennungen (IDs).** Im Postfach gibt es die Präfixe `pv` (39), `pf` (19), `mwp` (11) und weitere, im KI-Logbuch Muster wie `k-20261113-projektplan`. Eine Regel, wie IDs vergeben werden, fehlt.
- **Verknüpfung.** Das Feld `ziel` ist bei 78 Postfach-Einträgen gesetzt, `alt` bei 41. Es gibt keine Regel, was `ziel` und `alt` bedeuten, wann sie gesetzt werden und was passiert, wenn das Ziel gelöscht wird.
- **Status-Übergänge.** Erlaubt sind offensichtlich `neu` → `übernommen` oder `verworfen`. Nicht geregelt ist: Wer setzt den Status der Daten (`offen`, `erledigt`, `entfallen`), und was passiert bei einer Rücknahme?
- **Widerruf von Entscheidungen.** Die Taktzeit-Änderungen zeigen, dass Entscheidungen wieder fallen. Es fehlt eine Regel, wie der alte Eintrag bleibt (Historie) und welche Werte daraus folgen.
- **Sortierung.** Es ist nicht geregelt, nach welchen Feldern Einträge sortiert werden (Priorität, Termin, Datum des Eingangs). Die Anzeige sortiert nach Oberfläche, nicht nach Regel.
- **Herkunft.** Pflicht ist nur `vorschlag` (und das wird nicht eingehalten). Eine Regel, dass jeder Wert eine Quelle und ein Datum braucht, fehlt. Die Anforderungsliste verlangt das nur für „bestätigt“.
- **Typ `daten`.** 7 Postfach-Einträge tragen einen Typ, den die Regeln nicht kennen. `abschluss` ist definiert, kommt aber in den Daten nicht vor.

## 4. Vorschläge für Regeln (zum Entscheiden)

1. **Ein einziger Weg für Daten.** Entweder alle Änderungen laufen über das Postfach (auch Web-Änderungen als Postfach-Eintrag mit `kind`), oder das Web-Cockpit bekommt eine Option „nur Entwurf“. Beides ist besser als heute.
2. **Eine Quelle der Wahrheit pro Thema.** Entweder `cockpit/daten` gilt für den Projektstand, und das Repo-Dokument ist die Begründung. Dann wird der Projektabgleich zu „Daten prüfen gegen Dokument, Abweichung als Postfach-Eintrag“, statt das Repo pauschal gewinnen zu lassen.
3. **Eine Sammlung für Entscheidungen.** `decisions.json`, `questions.json` und `conflicts.json` löschen (archivieren nach `_Versionen`) und in den Regeln nur noch `tasks.json` nennen. `build.py` und README entsprechend anpassen.
4. **Pflichtfelder pro Postfach-Eintrag.** `id` (Schema festlegen), `kind`, `title`, `vorschlag` (Urheber), `date`, `stand`. Ein Eintrag ohne diese Felder wird nicht angelegt.
5. **Verknüpfung definieren.** `ziel` = Eintrag, auf den sich dieser bezieht. `alt` = ersetzter Wert. Regel: Ein Eintrag wird nicht gelöscht, sondern auf `verworfen` oder `ersetzt` gesetzt.
6. **Widerruf.** Eine Entscheidung wird nie gelöscht. Sie bekommt `status: entfallen` mit Verweis auf die neue Entscheidung.
7. **Ein Build-Weg.** Entweder das Action-Build (dann im CLAUDE.md streichen, dass Claude `docs/index.html` committet) oder das manuelle Build (dann die Action streichen).
8. **Datenschutz-Satz angleichen.** README und CLAUDE.md sollen denselben Satz zu Betriebsunterlagen im öffentlichen Repo sagen. Das ist deine Entscheidung. Ich frage dazu nicht erneut.

## 5. Offene Fragen an dich

- Welche der Vorschläge 1 bis 7 übernehmen wir?
- Soll das Web-Cockpit weiter direkt auf `main` schreiben, oder soll es nur noch Postfach-Einträge anlegen?
- Sollen die 18 KI-Logbuch-Einträge ohne Postfach-Weg nachträglich geprüft werden?
- Welche Quelle gilt bei Abweichungen zwischen Daten und Dokument (W2)?
