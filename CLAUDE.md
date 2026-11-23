# Regeln für Claude (Technikerarbeit Janek Bauer)

Version 2, freigegeben von Janek am 23.11.2026. Vorgänger: `cockpit/_Versionen/CLAUDE_vor-Regeln-v2_2026-11-23.md`.

## 0. Grundregeln

- Janek wird mit „Janek“ angesprochen. Antworten auf Deutsch.
- **Vor jeder Aufgabe zuerst `git pull`** (Branch `main`). Janek ändert im Web-Cockpit; die Änderungen kommen als Vorschläge ins Postfach.
- **Maßgeblich für den Projektstand** sind die Dokumente im Repo. Die Dateien in `cockpit/daten/*.json` sind die Abbildung davon. Weichen sie voneinander ab, gewinnt das Dokument, und die Abweichung wird als Postfach-Vorschlag angelegt.
- **Jede Änderung an Projektdaten läuft über das Postfach.** Ausnahmen stehen in Abschnitt 9.
- **Änderungen an der Cockpit-Oberfläche** (Felder, Ansichten, Layout, Abläufe in `cockpit/vorlage.html` und `cockpit/build.py`) sind keine Daten. Sie kommen als Auftrag im Chat, werden direkt umgesetzt und auf `main` committet. Sie erscheinen nie im Postfach.
- Was in den Daten fehlt, wurde gelöscht. Was dort „erledigt“ ist, ist erledigt. Keine älteren Chat-Stände als Wahrheit nehmen.

## 1. Wo was liegt

| Ort | Inhalt | Wer schreibt |
|---|---|---|
| `cockpit/daten/<sammlung>.json` | Abbild des Projektstands, einzige Datenquelle der Seite | Nur Übernahmen aus dem Postfach (Janek bestätigt) |
| `cockpit/daten/postfach.json` | Eingang: alle Vorschläge, Aufgaben, Entscheidungen, Änderungen, Logbuch-Einträge | Claude Code und Janek (Web) |
| `cockpit/vorlage.html` | Oberfläche (Quelle der Seite) | Claude Code, nach Absprache |
| `docs/index.html` | Erzeugte Seite | Nur die GitHub-Action `cockpit-bauen.yml`. Nie von Hand committen. |
| `docs/archiv/<Ordner>/<Dokument>/` | Dokumente und Versionen | Janek (Web oder Hochladen) |
| `cockpit/daten/files.json` | Metadaten zu den Dokumenten im Archiv | Siehe Ausnahmen, Abschnitt 9 |
| `projekt/` | Analysen, Entwürfe, Notizen. Inhalte landen nur über das Postfach in den Daten. | Claude Code |
| `cockpit/_Versionen/` | Alte Stände von Dateien und Sammlungen | Nichts wird gelöscht, nur dorthin verschoben |

## 2. Präfixe für IDs

Bestehende IDs bleiben unverändert. Neue Einträge bekommen den Präfix ihrer Sammlung und eine dreistellige Nummer. Die Nummer ist die höchste bisher vergebene +1, auch über offene Postfach-Vorschläge. Für die Seite wird das automatisch vergeben.

| Sammlung / Typ | Präfix | Beispiel |
|---|---|---|
| Aufgaben (`tasks.json`, ohne `typ: entscheidung`) | `t-` | `t-034` |
| Entscheidungen (`tasks.json`, `typ: entscheidung`) | `e-` | `e-025` |
| Postfach | `p-` | `p-085` |
| KI-Logbuch (`kilog.json`) | `k-` | `k-032` |
| Termine (`deadlines.json`) | `d-` | `d-013` |
| Anforderungen (`reqs.json`) | `r-` | `r-019` |
| Sensoren (`sensors.json`) | `s-` | `s-070` |
| Quellen (`sources.json`) | `q-` | `q-011` |
| Dokumente im Archiv (`files.json`) | `f-` | `f-069` |
| Dokumentation (`doku.json`) | `dk-` | `dk-010` |
| Checklisten (`checks.json`) | `c-` | `c-015` |
| Werkzeuge (`tools.json`) | `wz-` | `wz-004` |
| Optionen (`optionen.json`) | `o-` | `o-005` |
| Freitage (`freitage.json`) | `fr-` | `fr-001` |
| Pakete (`packages.json`) | `pk-` | `pk-013` |
| Änderungsdoku (`changes.json`, nur nach Freigabe des Pflichtenhefts) | `ae-` | `ae-001` |

Archiviert (keine neuen IDs mehr): `decisions.json`, `questions.json`, `conflicts.json` liegen in `cockpit/_Versionen/daten_2026-11-23/`. Entscheidungen leben nur noch in `tasks.json` mit `typ: "entscheidung"`.

## 2a. Aufgaben und Entscheidungen (Speichermodell)

- Aufgabe und Entscheidung bleiben zwei Typen in `tasks.json`: `typ: "aufgabe"` bzw. `typ: "entscheidung"`. Fehlt `typ`, gilt „aufgabe“.
- **Statuswerte Aufgabe:** `offen`, `in Arbeit`, `erledigt`, `entfallen`.
- **Statuswerte Entscheidung:** `offen` (Frage, noch nicht entschieden), `entschieden` (gilt), `entfallen` (aufgehoben). `erledigt` gibt es bei Entscheidungen nicht mehr.
- **Pflichtfelder bei `entschieden`:** `by` (Entschieden von, ein Name) und `reason` (Begründung). Die Seite verlangt sie.
- **Entscheidungsfelder:** `optionen` (betrachtete Alternativen), `konsequenzen`, `date` (Datum der Entscheidung).
- **Widerruf als Paar:** Die alte Entscheidung bekommt `status: "entfallen"` und `ersetzt_durch: <neue ID>`. Die neue bekommt `ersetzt: <alte ID>`. Ohne Nachfolger steht der Grund in `grund_entfallen`. Nie löschen.
- **Verweise:** `entscheidung` (auf der Aufgabe, welche Entscheidung sie auslöst), `bezug` (Liste von IDs wie `r-`, `q-`, `f-`, `dk-`). Das Feld `refs` ist abgeschafft.
- **Verlauf** ist das Postfach mit dem Feld `alt`. Eine eigene Feld-Historie gibt es nicht.

## 3. Postfach: Aufbau

Jeder Eintrag im `postfach.json` hat diese Pflichtfelder:

- `id`: Präfix `p-` plus Nummer
- `kind`: siehe unten
- `title`: kurzer Titel
- `detail`: Begründung, Quelle, Kontext
- `vorschlag`: Urheber. Werte: `KI (Claude Code)`, `Janek (Web)`, `Janek`, `Betrieb`, `Altbestand`
- `status`: `neu`, `übernommen` oder `verworfen`
- `date`: Datum (UTC), `date -u +%Y-%m-%d`, nie erfunden
- `stand`: Stand der Quelle

**Arten (`kind`):**

| kind | Bedeutung | Zusatzfelder |
|---|---|---|
| `aufgabe` | Neue Aufgabe in `tasks.json` | optional `who`, `due`, `prio` |
| `entscheidung` | Neue Entscheidung (`tasks.json`, `typ: entscheidung`) | optional `who`, `due`, `prio` |
| `daten` | Vorschlag, einen Eintrag in einer Sammlung anzulegen, zu ändern oder zu löschen. Jede Änderung im Web ist ein `daten`-Vorschlag. | `coll` (Sammlung), `docId` (ID des Eintrags), `payload` (neuer Inhalt), `alt` (Stand vor dem ersten Vorschlag), `loeschen` (true bei Löschung) |
| `kilog` | KI-Logbuch-Eintrag (`kilog.json`) | `fach` (true/false) |
| `abschluss` | Beleg, dass ein offener Punkt erledigt ist | `beleg` (Dateiname), `ziel` |
| `aenderung` | Eintrag für die Änderungsdoku (`changes.json`). Nur nach Freigabe des Pflichtenhefts. | |

Ein Vorschlag mit `kind: "daten"` ist immer vollständig: Sammlung, ID, neuer Inhalt und der alte Stand gehören dazu.

**Status-Regeln:**
- Claude Code setzt nie `übernommen`. Das macht nur Janek.
- `verworfen` bleibt im Postfach sichtbar, damit nachvollziehbar ist, was abgelehnt wurde.
- Jeder Vorschlag hat ein `ziel` (`sammlung/ID`), sobald er übernommen ist.

**Ein offener Vorschlag je Eintrag:** Ändert sich ein Eintrag, der schon einen offenen Vorschlag hat, wird dieser Vorschlag aktualisiert. Er wird nicht doppelt angelegt. `alt` bleibt der Stand vor dem ersten Vorschlag.

## 4. Übernahme und Löschen

- Übernahme schreibt den Inhalt (`payload`) direkt in die Sammlung und setzt den Vorschlag auf `übernommen` mit `ziel`.
- Hat sich der Eintrag seit dem Vorschlag geändert, fragt die Seite nach, bevor sie übernimmt.
- Löschen wird ebenfalls als Vorschlag angelegt (`loeschen: true`). Erst die Übernahme entfernt den Eintrag.
- Ein Eintrag mit `verworfen` wird nie gelöscht.

## 5. Verknüpfung, Widerruf, Sortierung

- Einträge verweisen über `ziel` aufeinander. Die Entscheidung steht im `ziel` der Aufgabe, die sie auslöst.
- Termine (`d-`) verweisen auf Aufgaben über das Feld `due`.
- **Nichts wird gelöscht, wenn andere Einträge darauf verweisen.** Stattdessen Status `entfallen`.
- **Widerruf:** Eine Entscheidung wird nie gelöscht. Sie bekommt `status: "entfallen"` und ein Feld `ersetzt_durch` mit der neuen ID. Werte aus der aufgehobenen Entscheidung werden über einen neuen Vorschlag korrigiert, nicht stillschweigend überschrieben.
- **Sortierung** in der Oberfläche: Priorität, dann Termin, dann Titel.

## 6. Abgleich und Prüfung

- **Projektabgleich** (nur auf Zuruf „Projektabgleich“): `cockpit/daten` mit den Dokumenten im Repo vergleichen. Das Dokument gewinnt. Abweichungen gehen als `daten`-Vorschläge ins Postfach. Nichts wird automatisch übernommen.
- **Dokumente prüfen** (nur auf Zuruf): Neue Dateien unter `docs/archiv` lesen. Jeder Treffer wird ein Postfach-Eintrag `abschluss` mit `beleg`, `ziel` und `detail`. Nichts wird selbst auf erledigt gesetzt.
- Der Knopf „Dokumente prüfen“ im Postfach legt nur einen Prüfauftrag an. Die Prüfung läuft erst, wenn Janek das Stichwort gibt.

## 7. KI-Logbuch

- Jede KI-Hilfe für die Technikerarbeit wird zuerst als Postfach-Eintrag `kind: "kilog"` angelegt, mit `date`, `detail` (Art der Hilfe: was KI gemacht hat) und `fach` (true, wenn KI fachlichen Text erzeugt hat).
- Janek prüft und übernimmt. Erst dann landet der Eintrag in `kilog.json` (Präfix `k-`).
- Änderungen am Cockpit selbst (Umbau, Umkodierung, Layout) gehören nicht ins KI-Logbuch.

## 8. Zeitstempel und Versionen

- `updated` und `date` nie erfinden. Immer `date -u`.
- Ältere Versionen nie löschen, sondern nach `_Versionen` verschieben. Dazu gehört jede Datei, die ersetzt wird.

## 9. Ausnahmen (ausdrücklich)

Nur diese Schreibwege sind direkt, alles andere läuft über das Postfach:

0. **Cockpit-Oberfläche:** Änderungen an `cockpit/vorlage.html` und `cockpit/build.py` auf Auftrag im Chat, direkt committet. Kein Postfach-Vorschlag. Ein neues Feld im Formular ist keine Dateneingabe und erzeugt keinen Vorschlag.
1. **Das Postfach selbst** (neue Einträge anlegen, Status setzen).
2. **Spiegelung Aufgabe ↔ Checkliste:** Ändert Janek eine Aufgabe und übernimmt sie, wird die zugehörige Checkliste automatisch mitgeführt. Sie ist abgeleitet, kein eigener Vorschlag.
3. **Checklisten und Werkzeuge:** Haken in Checklisten (`checks`) und Eingaben in den Werkzeugen (Morph. Kasten, Bewertung: `tools`) werden direkt gespeichert. Sie sind laufende Arbeitsstände und würden das Postfach überfluten.
4. **Archiv-Upload:** Die Datei selbst wird direkt unter `docs/archiv` abgelegt (Binärdateien lassen sich nicht im Postfach vorschlagen). Der Metadaten-Eintrag in `files.json` läuft als Vorschlag. Bis zur Übernahme ist die Datei im Archiv vorhanden, aber in der Liste nicht sichtbar.

## 10. Branch und Commits

- **Claude-Sitzungen arbeiten direkt auf `main`** (Janek, 23.11.2026). Eigene Branches nur auf ausdrücklichen Wunsch.
- Nach jeder abgeschlossenen Aufgabe committen und pushen. Nachricht auf Deutsch: was und warum.
- Die Veröffentlichung läuft automatisch: Nach jedem Push, der die Oberfläche oder die Daten ändert, baut `cockpit-bauen.yml` die Seite neu und `cockpit-seite.yml` stellt sie unter derselben Adresse ins Netz. Kein manueller Schritt nötig.
- Committet werden `cockpit/daten/`, `cockpit/vorlage.html`, `cockpit/build.py`, `cockpit/README.md`, `projekt/` und `CLAUDE.md`. **Nicht** `docs/index.html`: die Action baut die Seite nach jeder Änderung neu.
- Lokaler Test der Seite: `python cockpit/build.py` (zum Anschauen, nicht committen).

## 11. Datenschutz

- Janek hat am 20.11.2026 entschieden, dass die vorhandenen Rohrspezifikationen und die Prüfanweisung im Repo bleiben. Dazu nicht mehr nachfragen.
- Das Repo ist öffentlich. Keine Angebote, Mails oder anderen Unterlagen des Betriebs hochladen, die nicht bereits im Repo liegen.

## 12. Geplante Aufgaben

- Die Freitags-Vorbereitung (`vorbereitung.yml`) läuft automatisch. Aufbau, Zeitplan und Prompt stehen in `projekt/Geplante_Aufgabe_Wochenstatus_Freitag.md`.

## 13. Texte für die Technikerarbeit

- Jeder Text, den Claude Code für die Technikerarbeit schreibt, vor allem die Dokumentation, läuft vor der Abgabe durch zwei Prüfungen: den Unslop-Skill (deutsche Texte, Modus „Rewrite“) und den Humanizer. Für deutsche Texte gilt die Unslop-Regelbibliothek. Der Humanizer ist englischsprachig und greift bei deutschen Texten nur mit den allgemeinen Prinzipien.
- Der Ablauf: erst Inhalt und Quellen festlegen, dann die beiden Prüfungen. Keine Zahl, kein Name und kein Datum wird dabei ergänzt, was nicht in der Quelle steht. Fehlende Angaben werden als Lücke gemeldet.
- Der Schreibstil bleibt Janeks eigener. Bei Texten, die er selbst schreibt, bleiben seine Formulierungen erhalten. Die Prüfung meldet nur, was auffällt.
- Die Gestaltung der Oberfläche folgt dem Entwurf im Repo (Schrift IBM Plex, Mono für Kennungen, keine Schatten, Ecken mit 4 px). Neue Bereiche halten sich daran.

## 14. Formulierung von Aufgaben und Entscheidungen

Ziel: Die Einträge, die Claude Code anlegt, sind kurz, sachlich und ohne Rechnung lesbar, wie die, die Janek selbst schreibt.

**Titel**
- Höchstens 60 Zeichen. Beginnt mit dem Gegenstand oder der Handlung: „MS 1 nachfragen“, „Datenblätter Mitutoyo LSM-501S beschaffen“.
- Kein Präfix wie „KI-Vorschlag:“ oder „Frage an den Betrieb:“. Die Art steht bereits im Feld `kind`, `typ` oder `vorschlag`.
- Entscheidungen als offene Festlegung: „Bezug der Zylinderform festlegen (je Querschnitt oder über das Rohr)“.
- Keine Empfehlung im Titel.

**Inhalt (`note` bzw. `detail`)**
- Höchstens drei Sätze, etwa 50 Wörter. Erster Satz: die Frage oder was festgelegt werden muss. Zweiter Satz: der Grund mit Fundstelle, z. B. „(PH V1.2, Kap. 5.3)“. Dritter Satz, falls nötig: die Optionen als a) und b).
- Rechenwege, Formeln und Messreihen gehören nicht in den Eintrag. Der Eintrag verweist auf die Datei unter `projekt/`, in der sie stehen.
- Zahlen mit Einheit und Quelle. Fehlt eine Zahl, steht „offen“. Eine geschätzte Zahl wird nicht eingetragen.
- Abkürzungen beim ersten Auftreten ausschreiben, z. B. „Gage Repeatability and Reproducibility (GRR)“.
- Eine Empfehlung steht als eigener Satz, der mit „Vorschlag:“ beginnt.

**Umfang**
- Ein Eintrag enthält genau eine Frage, eine Entscheidung oder eine Aufgabe.
- Vor dem Anlegen wird gegen die offenen Einträge geprüft. Ein Duplikat wird nicht angelegt, sondern als Hinweis im bestehenden Eintrag ergänzt.

**Fragen aus einem neuen Dokument (z. B. Pflichtenheft)**
- Pro Anforderung mit echter Unklarheit eine Frage. Nicht jede Anforderung erzeugt einen Eintrag.
- Eine Entscheidung nur, wenn die Projektarbeit eine Festlegung braucht. Eine offene Zahl ist eine Frage, keine Entscheidung.
- Jeder Vorschlag nennt die Anforderungsnummer im Inhalt und setzt `vorschlag` auf „KI (Claude Code)“.
- Die Zahl der Vorschläge je Dokument wird im Eintrag des Prüfauftrags genannt. Mehr als zehn neue Vorschläge pro Dokument werden vorher mit Janek abgestimmt.

**Test vor dem Anlegen**
- Der Titel allein muss verständlich sein, ohne den Inhalt zu lesen.
- Der Inhalt muss in unter einer Minute erfassbar sein.
- Fachbegriffe bleiben, Floskeln und Füllwörter fallen weg. Die Sätze werden nach den Unslop-Regeln (Abschnitt 13) geprüft.
