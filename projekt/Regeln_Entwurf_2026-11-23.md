# Arbeitsregeln Cockpit – Entwurf v2 (23.11.2026)

Entwurf zur Prüfung. Ersetzt noch nicht die `CLAUDE.md`. Nach deiner Freigabe wird die CLAUDE.md umgeschrieben, `cockpit/README.md` angeglichen und die Umbauten am Cockpit gemacht (siehe Abschnitt 9).

## 1. Wo was liegt

| Ort | Inhalt | Wer schreibt |
|---|---|---|
| `cockpit/daten/<sammlung>.json` | Der Projektstand. Einzige Datenquelle der Seite. | Nur Übernahmen aus dem Postfach (siehe 3) |
| `cockpit/daten/postfach.json` | Eingang für alle neuen Einträge, Vorschläge, Änderungen und Fragen | Claude Code und Janek (über das Web) |
| `cockpit/vorlage.html` | Oberfläche (Quelle) | Claude Code, nach Absprache |
| `docs/index.html` | Erzeugte Seite. Nie von Hand bearbeiten. | Nur GitHub-Action `cockpit-bauen.yml` (lokal nur zum Testen per `python cockpit/build.py`) |
| `docs/archiv/<Ordner>/<Dokument>/` | Dokumente und Versionen | Janek (Web oder Hochladen) |
| `cockpit/daten/files.json` | Metadaten zu den Dokumenten im Archiv | Janek und Claude Code |
| `projekt/` | Analysen, Entwürfe, Notizen. Ihr Inhalt wird nur über das Postfach in die Daten übernommen. | Claude Code |
| `cockpit/_Versionen/` | Alte Stände von Dateien und Sammlungen. Nichts wird gelöscht, nur dorthin verschoben. | Claude Code |

## 2. Präfixe für IDs

Bestehende IDs bleiben unverändert. Neue Einträge bekommen den Präfix ihrer Sammlung und eine laufende Nummer mit drei Stellen (z. B. `t-034`).

| Sammlung / Typ | Präfix | Beispiel |
|---|---|---|
| Aufgaben (`tasks.json`, `typ` nicht „entscheidung“) | `t-` | `t-034` |
| Entscheidungen (`tasks.json`, `typ: "entscheidung"`) | `e-` | `e-025` |
| Postfach | `p-` | `p-085` |
| KI-Logbuch (`kilog.json`) | `k-` | `k-032` |
| Termine (`deadlines.json`) | `d-` | `d-013` |
| Anforderungen (`reqs.json`) | `r-` | `r-019` |
| Sensoren (`sensors.json`) | `s-` | `s-070` |
| Quellen (`sources.json`) | `q-` | `q-011` |
| Dokumente im Archiv (`files.json`) | `f-` | `f-069` |
| Dokumentation (`doku.json`) | `dk-` | `dk-010` |
| Prüfungen (`checks.json`) | `c-` | `c-015` |
| Werkzeuge (`tools.json`) | `wz-` | `wz-004` |
| Optionen (`optionen.json`) | `o-` | `o-005` |
| Freitage (`freitage.json`) | `fr-` | `fr-001` |
| Pakete (`packages.json`) | `pk-` | `pk-013` |
| Änderungsdoku (`changes.json`, nur nach Freigabe) | `ae-` | `ae-001` |
| Widersprüche (`conflicts.json`, archiviert) | `wd-` | nicht mehr vergeben |
| Fragen (`questions.json`, archiviert) | `fg-` | nicht mehr vergeben |

Die laufende Nummer ist je Präfix die nächste freie Nummer. Gelöschte oder verworfene Nummern werden nicht wiederverwendet.

## 3. Postfach: Pflichtfelder und Status

Jeder neue Eintrag im `postfach.json` hat:

- `id`: Präfix `p-` plus Nummer
- `kind`: `aufgabe`, `entscheidung`, `aenderung`, `kilog`, `abschluss`, `daten`
- `title`: kurzer Titel
- `detail`: Begründung, Quelle, Kontext
- `vorschlag`: Urheber, Pflicht. Werte: `KI (Claude Code)`, `Janek`, `Betrieb`, `Altbestand`
- `date`: Datum UTC, `date -u +%Y-%m-%d` (nie erfinden)
- `stand`: Stand des Inhalts (Datum der Quelle oder Stand des Projekts)
- `status`: `neu`, `übernommen`, `verworfen`
- `ziel` (optional): ID des Eintrags, auf den sich der Vorschlag bezieht
- `alt` (optional, bei `aenderung`): bisheriger Wert

Status-Regeln:
- Claude Code setzt nie `übernommen`. Das macht nur Janek.
- `verworfen` bleibt im Postfach sichtbar, damit nachvollziehbar ist, was abgelehnt wurde.
- Nach einer Übernahme schreibt Claude Code den Eintrag in die Zieldatei in `daten/` und setzt `updated` auf den Zeitstempel der Übernahme.

## 4. Wann Daten in `daten/` geschrieben werden

Die Dateien in `daten/` ändern sich nur durch:
1. eine Übernahme im Postfach (Janek bestätigt), oder
2. eine Änderung im Web, die vorher als Postfach-Eintrag angelegt wurde (Ziel nach dem Umbau, siehe 9).

Direkt geänderte Daten ohne Postfach-Eintrag gelten als Fehler. Sie werden im Abgleich gemeldet.

## 5. Verknüpfung und Sortierung

- Entscheidungen (`e-`) und Aufgaben (`t-`) können mit `ziel` aufeinander verweisen. Die Entscheidung steht im `ziel` der Aufgabe, die sie auslöst.
- Termine (`d-`) verweisen auf Aufgaben über das Feld `due`, nicht umgekehrt.
- Ein Eintrag wird nie gelöscht, wenn andere Einträge auf ihn verweisen. Stattdessen Status `entfallen` mit Verweis auf die neue ID.
- Sortierung in der Oberfläche: Priorität, dann Termin, dann Titel. Die Regel gilt für Anzeige und Export.

## 6. Widerruf

- Eine Entscheidung wird nie gelöscht.
- Wird sie aufgehoben, bekommt sie `status: "entfallen"` und ein Feld `ersetzt_durch` mit der neuen ID.
- Eine neue Entscheidung zum selben Thema bekommt eine neue ID und ein `ziel` auf die alte.
- Werte, die aus der aufgehobenen Entscheidung stammen, werden über einen neuen Postfach-Eintrag (`aenderung`) korrigiert, nicht stillschweigend überschrieben.

## 7. Abgleich mit Dokumenten

- Auf Zuruf „Projektabgleich“ vergleicht Claude Code `daten/` mit den Dokumenten im Repo.
- Das Dokument gewinnt. Abweichungen werden als Postfach-Eintrag `aenderung` vorgeschlagen, mit `ziel` und `alt`.
- Nichts wird automatisch übernommen.

## 8. Weitere Regeln

- **Dokumente prüfen** (Zuruf): Claude Code liest neue Dateien unter `docs/archiv`. Jeder Treffer wird ein Postfach-Eintrag `abschluss` mit `beleg`, `ziel`, `detail`. Nichts wird selbst auf erledigt gesetzt.
- **KI-Logbuch**: jede KI-Hilfe wird zuerst als Postfach-Eintrag `kind: "kilog"` angelegt, mit `date`, `detail`, `fach` (true/false). Nach Übernahme landet er in `kilog.json` (`k-`). Änderungen am Cockpit selbst gehören nicht ins Logbuch.
- **Zeitstempel**: `updated` und `date` immer mit `date -u`, nie erfunden.
- **Branch**: Claude-Sitzungen arbeiten auf dem Branch, den die Sitzung vorgibt. Ohne Vorgabe direkt auf `main`. Eigene Branches nur auf ausdrücklichen Wunsch.
- **Commits**: nach jeder abgeschlossenen Aufgabe committen und pushen. Die Nachricht ist deutsch und sagt, was und warum. Nur `daten/`, `vorlage.html` und `projekt/` committen, nicht `docs/index.html` (das baut die Action).
- **Vertrauliche Betriebsunterlagen**: Janek hat entschieden, dass die vorhandenen Spezifikationen und die Prüfanweisung im Repo bleiben (Entscheidung vom 20.11.2026). Die README wird entsprechend angeglichen.
- **Ältere Versionen**: nie löschen, nach `_Versionen` verschieben.
- **Geplante Aufgabe Wochenstatus**: Aufbau und Prompt stehen in `projekt/Geplante_Aufgabe_Wochenstatus_Freitag.md`.

## 9. Was dafür im Cockpit umgebaut werden muss

Diese Punkte sind Code-Änderungen, keine Regeländerungen. Sie kommen nach deiner Freigabe der Regeln, in dieser Reihenfolge:

1. **Web-Bearbeitung über Postfach.** Die Speicherfunktion (`save()` in `vorlage.html`) legt bei jeder Änderung einen Postfach-Eintrag `aenderung` an, statt direkt `daten/*.json` zu schreiben. Die Übernahme im Postfach schreibt dann die Daten. Das ist der größte Eingriff.
2. **Archivieren von `decisions.json`, `questions.json`, `conflicts.json`.** Dateien nach `cockpit/_Versionen/` verschieben. Die Seiten „Fragen an den Betrieb“ und „Widersprüche“ sowie die Sammlung `decisions` in `vorlage.html` werden entfernt oder auf `tasks.json` mit `typ: "entscheidung"` umgestellt. Die bisherigen Einträge bleiben im Archiv nachvollziehbar.
3. **README angleichen** an die neuen Regeln (Sammlungen, Build durch Action, Datenschutz).
4. **Build-Hinweis** in `build.py` nur als Testhilfe kennzeichnen.

## 10. Offene Punkte für dich

- Soll die Web-Bearbeitung (Schritt 1) sofort umgebaut werden, oder erst nach Freigabe dieses Entwurfs?
- Soll bei Claude-Sitzungen der Branch-Regel (`main` oder Session-Branch) gefolgt werden, oder ist für die Seite ein PR-Weg gewünscht?
- Sind die Präfixe in Abschnitt 2 so in Ordnung, oder sollen einzelne Kürzel anders heißen?
