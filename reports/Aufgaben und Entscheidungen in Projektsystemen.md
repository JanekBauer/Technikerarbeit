# Aufgaben und Entscheidungen in Projektsystemen: Speichermodell für das Cockpit

Stand: 2026-11-23. Grundlage: die drei Recherche-Notizen im Ordner `research_notes/Aufgaben und Entscheidungen in Projektsystemen/` (`aufgabenmodell.md`, `entscheidungsdokumentation.md`, `erp_verknuepfung.md`) sowie eine eigene Prüfung des Ist-Zustands in `cockpit/daten/tasks.json`, `cockpit/daten/postfach.json` und `cockpit/vorlage.html` am selben Tag.

Kennzeichnung der Aussagen:
- **[Ist]**: selbst im Repo geprüft (2026-11-23).
- **[Primär, gelesen]**: Quelle in den Notizen direkt gelesen (nur MADR-Templates 4.0.0, MADR-Projektseite, Joel-Parker-Henderson-Repository). Die MADR-Vorlage wurde über einen Zusammenfassungsschritt gelesen: Feldnamen sind zuverlässig, der Wortlaut nicht.
- **[Snippet]**: nur aus Suchausschnitten. Dazu gehören alle Aussagen zu Jira, Linear, GitHub, Notion, Redmine, OpenProject, Asana, ERPNext, Odoo, Jama, codebeamer, Polarion und zu ISO 9001 Klausel 8.5.6 (letztere aus einer Beratungsseite, nicht aus der Norm).
- **[Ableitung]**: Schlussfolgerungen der Notizen oder dieses Berichts. Sie sind keine belegten Befunde.

---

## Kurzantwort

1. **Aufgabe und Entscheidung bleiben zwei Typen in `tasks.json`** (`typ: "aufgabe"` bzw. `typ: "entscheidung"`). Die Trennung über Typ plus eigener Statusmenge entspricht dem Muster der Tracker in Jira, Redmine und GitHub [Snippet]. Ein eigener Sammlungswechsel ist nicht nötig.
2. **Die Statusmenge für Entscheidungen wird geschärft.** Heute nutzen beide Typen dieselben Werte (`offen`, `in Arbeit`, `erledigt`, `entfallen`). Für Entscheidungen soll `erledigt` durch `entschieden` ersetzt werden. Eine getroffene Entscheidung ist nicht „erledigt“, sie ist gültig. Gültigkeit ist der Kern eines Entscheidungsregisters [Primär, gelesen: MADR-Status `accepted`, `superseded`, `deprecated`, `rejected`].
3. **Widerruf läuft als Paar.** Eine Entscheidung wird nie gelöscht. Die alte bekommt `status: "entfallen"` und `ersetzt_durch: <neue ID>`, die neue bekommt `ersetzt: <alte ID>`. Die Rückrichtung gehört dazu, weil die Notizen einseitige Verweise als häufige Fehlerquelle nennen [Primär, gelesen: MADR-Hinweise und Snippet].
4. **Die ID-Präfixe bleiben** (`t-`, `e-`, `p-`, `k-`, `d-`, `r-`, `s-`, `q-`, `f-`, `dk-`, `c-`, `wz-`, `o-`, `fr-`, `pk-`, `ae-`). Es gibt keinen belegten Grund zur Änderung. Was sich ändern muss, ist die Anwendung: Die bestehenden Datensätze tragen keine Präfixe (Ist, siehe unten).
5. **Verweise werden benannt statt überladen.** Das Feld `ziel` hat heute zwei Bedeutungen (Postfach: Zieldatensatz; Aufgabe: Verweis auf die Entscheidung nach CLAUDE.md §5). Empfohlen: `entscheidung` (Aufgabe → Entscheidung), `bezug` (Liste von r-, q-, f-, dk-IDs), `ersetzt` und `ersetzt_durch` (Entscheidung ↔ Entscheidung). Das Feld `refs` ist in keinem der 33 Datensätze belegt und sollte durch `bezug` ersetzt werden.
6. **Verlauf ist das Postfach.** Jede Änderung ist ein Vorschlag mit `alt`-Snapshot, übernommene Vorschläge werden nie gelöscht. Das ist die Änderungsspur. Eine zusätzliche Feld-Historie pro Datensatz ist nicht nötig.

Alle Änderungen an Daten laufen über das Postfach (CLAUDE.md §0 und §4). Dieser Bericht ändert keine Daten.

---

## 1. Vergleich mit etablierten Modellen

### 1.1 Aufgabenmodelle

| Thema | Gängiges Muster | Quelle und Stärke |
|---|---|---|
| Status | Frei benennbare Status, jeder einer festen Kategorie zugeordnet (offen / in Arbeit / erledigt). Kategorie steuert Darstellung und Auswertung. | Jira Work Management: drei feste Kategorien; Notion: To-do / In Progress / Complete; Linear-Projekte: Backlog, Planned, Started, Completed, Canceled. [Snippet] |
| Abschluss | Abschluss als Kategorie oder Flag, nicht als Löschung. Abschlussgrund als eigenes Feld: Jira `Resolution`, GitHub `state_reason` (completed, not planned, duplicate). | [Snippet] |
| Abgelehnt | Linear verschiebt abgelehnte Eingänge in den Typ „Canceled“ mit Begründungskommentar, nicht in den Papierkorb. | [Snippet] |
| Eingang | Linear: eigene Kategorie „Triage“ als Team-Posteingang mit Annehmen, Ablehnen, Zurückstellen. Andere Tools: Standardstatus oder Filter. | Linear: [Snippet]; übrige: Notizen selbst als „nicht belegt“ markiert |
| Priorität | Fünfstufig bei Linear (No priority bis Urgent), fünfstufig bei Jira-Standard (Highest bis Lowest). | [Snippet] |
| Verknüpfung | Gemeinsames Vokabular: blockiert/blockiert von, verwandt, Duplikat, Vorgänger/Nachfolger, Eltern/Kind. Verbindungen zu Anforderungen oder Dokumenten laufen über Relations-Datenbanken oder Felder, nicht über einen festen Typ. | Jira, Redmine, GitHub Sub-Issues, Asana, Notion: [Snippet] |
| ID | Präfix plus Zähler je Projekt oder Team (Jira `ABC-123`, Linear `ENG-123`). GitHub: Zähler je Repository, Issues und PRs teilen sich die Folge. Verschieben über Teams vergibt neue Nummern, die alte bleibt auflösbar (Linear). | [Snippet], GitHub-Community-Quellen nicht offiziell |

**Befund:** Die Tools trennen Arbeitsart über Typ oder Tracker und den Ablauf über den Workflow. Kein geprüftes Tool führt „Entscheidung“ als Standard-Kernzustand [Snippet, Ableitung].

### 1.2 Entscheidungsdokumentation

| Thema | Muster | Quelle und Stärke |
|---|---|---|
| Minimalfelder | Titel, Kontext/Problem, betrachtete Optionen, gewählte Option mit Begründung, Konsequenzen, Status. Datum und Entscheider als Ergänzung. | MADR 4.0.0 Minimal und Full [Primär, gelesen, Feldnamen]; Nygard 2011 [Snippet, Original nicht abrufbar] |
| Status | `proposed`, `accepted`, `rejected`, `deprecated`, `superseded by ADR-xxxx`. Die Notizen nennen Zusatzstufen wie „Researching“ und „Evaluating“, aber kein verbindliches Set. | MADR 4.0.0 Front-Matter [Primär, gelesen]; Joel-Parker-Henderson [Primär, gelesen] |
| Unterschied Vorschlag / bindend | `proposed` ist ein Vorschlag, erst `accepted` gilt. Eine Entscheidung ohne Freigeber und Datum ist ein Vorschlag, auch wenn der Text nach Entscheidung klingt. | MADR [Primär, gelesen]; Ableitung |
| Ersetzung | Neuer Eintrag statt Überarbeitung des akzeptierten Eintrags. Alter Eintrag bekommt Status `superseded` mit Verweis auf den neuen. `deprecated` ohne Nachfolger ist davon getrennt. | MADR und Joel-Parker-Henderson: „Don't alter existing information in an ADR“ [Primär, gelesen]; Rückverweis-Problem [Snippet] |
| Datum | MADR-Feld `date` ist das Datum der letzten Aktualisierung, nicht das Entscheidungsdatum. | MADR 4.0.0 [Primär, gelesen] |
| ID | Laufende Nummer mit führenden Nullen (`ADR-0123`), Dateiname `nnnn-titel.md`. Präfixkonventionen in Decision Registern nicht belegt. | MADR [Primär, gelesen]; Register-Präfixe nicht gefunden |
| Begründung | Quellen sind sich einig, dass ein Eintrag verworfene Alternativen und Randbedingungen festhalten soll. | Mehrere Ratgeber [Snippet, schwach] |
| Owner | Ein namentlicher Verantwortlicher pro Eintrag, nicht eine Gruppe. | Vendor-Guides [Snippet, schwach] |

**Befund:** Die stärkste belegte Aussage ist der Zusammenhang Status ↔ Ersetzung ↔ Datum. Jede Entscheidung braucht ein Datum und einen Entscheider; die Notizen belegen das nur über MADR-Felder und Vendor-Aussagen.

### 1.3 Nachvollziehbarkeit und Änderungsverlauf

| Thema | Muster | Quelle und Stärke |
|---|---|---|
| Feldverlauf | Jira speichert pro Vorgang eine History mit alt- und neu-Werten. Vollständiger Feldverlauf ist laut Notizen nur bei Jira belegt. | [Snippet] |
| Versionen statt Überschreiben | codebeamer: Jede Änderung erzeugt eine neue Version; Wiederherstellen erzeugt eine neue Nummer, löscht keine alte. ERPNext: Versionierung pro DocType; amendierte Belege bekommen neue Namen. | [Snippet] |
| Baselines | Benannte Snapshots (codebeamer, Polarion). Das Löschen einer Baseline lässt die Revision bestehen (Polarion). | [Snippet] |
| Suspect Link | Jama markiert nachgelagerte Elemente als verdächtig, wenn sich ein vorgelagertes ändert. Auslöser sind nur Felder, die der Administrator festlegt. Richtung laut Community-Aussage nur nachgelagert, Quelle nicht geprüft. | [Snippet, Community] |
| Änderungsprüfung | ISO 9001:2015 Klausel 8.5.6 verlangt laut Beratungsseite: Ergebnis der Prüfung, Autorisierer, Folgemaßnahmen, vor der Umsetzung. | [Snippet, Sekundärquelle, Norm nicht gelesen] |
| Abgelehnte Änderungen | ERPNext, Odoo ECO, Jama: Stufen wie New / In Progress / Validated / Effective (Odoo). Kein belegtes Feld „Grund“ pro Änderung in den geprüften Systemen. | [Snippet] |

**Befund:** Die gefundenen Systeme trennen Entwurf und gültigen Stand über Stufen oder Baselines. Das entspricht dem Verhältnis Postfach (Vorschlag) zu `tasks.json` (übernommen). Ein Eingangskorb mit Übernahme durch eine berechtigte Person ist in keiner geprüften Quelle belegt [Snippet, Lücke].

### 1.4 Nummerierung

- ERPNext: Naming Series aus Präfix, Datum und Zähler; Zähler lässt sich setzen, etwa für eine Übernahme aus einem Altsystem [Snippet].
- Jira, Linear: Präfix plus Zähler, je Projekt bzw. Team [Snippet].
- MADR: laufende Nummer mit führenden Nullen [Primär, gelesen].
- Nicht belegt: ob gelöschte Nummern wiederverwendet werden, und ob Zähler lückenlos sind. Die Notizen markieren das als offen.

---

## 2. Ist-Zustand im Cockpit

Alle Punkte in diesem Abschnitt sind mit Zählungen oder Feldnamen aus dem Repo belegt [Ist]. Es werden keine Inhalte wiedergegeben.

- **Datensätze in `tasks.json`:** 33 insgesamt. 24 mit `typ: "entscheidung"`, 9 ohne `typ` (Aufgaben).
- **IDs:** Keine der 33 IDs folgt dem Schema `t-NNN` oder `e-NNN`. Es sind zufällige 13-stellige Zeichenketten. CLAUDE.md §2 verlangt für neue Einträge Präfix und dreistellige Nummer, das Schema ist also noch nicht angewendet.
- **IDs im Postfach:** Die Vorschläge tragen Kennungen wie `pf-tasks-…` (aus Migration). Keine trägt ein `p-NNN`. Neue Vorschläge sollten dem Schema folgen; bestehende bleiben (CLAUDE.md §2).
- **Status bei Entscheidungen:** 22 offen, 2 erledigt. Die 22 offenen haben weder `by` noch `reason` gefüllt. Die 2 erledigten haben beide gefüllt. Die Daten zeigen also keine Vermischung von „Frage“ und „schon entschieden“ bei `offen`. Das Problem liegt im Begriff: `erledigt` heißt bei einer gültigen Entscheidung „fertig“, nicht „gültig“.
- **Widerruf:** Kein Datensatz hat `ersetzt_durch` oder `ersetzt`. Der Status `entfallen` ist in der Auswahl vorhanden (`vorlage.html`, Zeile 421 und 433), wird aber in den Daten nicht verwendet.
- **Feld `refs`:** In keinem Datensatz gefüllt (29 Leerwerte, 4 fehlen). Das Feld `docs` ist in einem Datensatz als Freitext gefüllt.
- **Feld `topic`:** In einem Datensatz gefüllt, `source` in 23.
- **Entscheidungsfelder:** `note` (Inhalt), `topic` (Bezug), `who`, `ask`, `due`, `prio`, `status`, `by` (Entschieden von), `date`, `reason` (Begründung), `source` (Quelle / Vorschlag von). Es fehlen: Optionen, Konsequenzen, Gültigkeitsende, Verweise auf Ersetzung.
- **Postfach:** Alle 84 Einträge sind `übernommen` bis auf einen `verworfen`. 41 Einträge tragen `alt` und `altColl` (Stand vor dem Vorschlag). Das Postfach ist damit faktisch die Änderungsspur.
- **Ziel-Felder im Postfach:** 78 Einträge tragen `ziel` (Stichprobe: Format `tasks/<ID>`; nicht vollständig geprüft).
- **Sammlung `optionen.json`:** Vorhanden, Beziehung zu Entscheidungen nicht geprüft.

---

## 3. Konkrete Empfehlungen

### 3.1 Felder für Aufgaben (`typ: "aufgabe"`)

| Feld | Typ | Pflicht | Bemerkung |
|---|---|---|---|
| `id` | `t-NNN` | ja | Neue Einträge ab `t-001` (Startnummer offen, siehe Abschnitt 5). Bestehende IDs bleiben. |
| `typ` | `"aufgabe"` | ja | Fehlt heute bei 9 Datensätzen. Nachtragen über Postfach-Vorschlag. |
| `title` | Text | ja | |
| `status` | `offen`, `in Arbeit`, `erledigt`, `entfallen` | ja | Wie heute. |
| `prio` | `1`, `2`, `3` | ja | Bedeutung dokumentieren: 1 = dringend (Vorschlag: Bedeutung in `cockpit/README.md` festhalten). |
| `who` | Auswahl | nein | Wer führt durch. |
| `due` | Datum | nein | Fälligkeit; Termine (`d-`) verweisen über `due` auf die Aufgabe (CLAUDE.md §5). |
| `entscheidung` | ID `e-NNN` | nein | Die Entscheidung, die diese Aufgabe auslöst. Ersetzt die Nutzung von `ziel` in `tasks.json`. |
| `bezug` | Liste von IDs (`r-`, `q-`, `f-`, `dk-`) | nein | Ersetzt das leere Feld `refs`. |
| `note`, `date`, `updated` | wie heute | | `updated` nur über `date -u`. |

### 3.2 Felder für Entscheidungen (`typ: "entscheidung"`)

| Feld | Typ | Pflicht | Bemerkung |
|---|---|---|---|
| `id` | `e-NNN` | ja | Eigener Zähler (nicht geteilt mit `t-`). |
| `typ` | `"entscheidung"` | ja | |
| `title` | Text | ja | |
| `status` | `offen`, `entschieden`, `entfallen` | ja | Neu: `entschieden` statt `erledigt`. `offen` = Frage, noch nicht entschieden. `entfallen` = aufgehoben. |
| `note` | Text | ja | Die Frage bzw. Entscheidung kurz. |
| `optionen` | Text (Liste) | bei `entschieden` ja | Verworfene Alternativen. Quelle: MADR „Considered Options“ [Primär, gelesen]. Klären, ob `optionen.json` dafür genutzt wird. |
| `reason` | Text | bei `entschieden` ja | Begründung (MADR „Decision Outcome“). |
| `konsequenzen` | Text | nein | MADR „Consequences“, optional. |
| `by` | Auswahl | bei `entschieden` ja | Wer hat entschieden. Ein Name, nicht eine Gruppe [Snippet]. |
| `date` | Datum | bei `entschieden` ja | Datum der Entscheidung. Nicht mit `updated` verwechseln (MADR-Hinweis). |
| `ersetzt` | ID `e-NNN` | nein | Gesetzt, wenn diese Entscheidung eine frühere aufhebt. |
| `ersetzt_durch` | ID `e-NNN` | nein | Gesetzt, wenn diese Entscheidung aufgehoben ist. Pflicht bei `status: entfallen`, wenn es einen Nachfolger gibt. |
| `grund_entfallen` | Text | bei `entfallen` ohne Nachfolger | Z. B. „Projektziel entfallen“. Unterscheidet „ohne Nachfolger verworfen“ von „ersetzt“ (MADR: `deprecated` vs. `superseded`). |
| `bezug` | Liste von IDs | nein | Anforderungen, Dokumente, die betroffen sind. |
| `source` | Text | nein | Quelle / Vorschlag von. |
| `topic` | Text | nein | Bezug, z. B. Anforderungsnummer. Kann in `bezug` aufgehen; Entscheidung: bei Umbau behalten, bis geklärt. |

**Begründung der Statusänderung:** `offen` bleibt für Fragen. `entschieden` benennt, was heute `erledigt` heißt, und sagt, dass die Entscheidung gilt. `entfallen` deckt beide Fälle ab, die heute vermischt sind. Eine Entscheidung wird vor dem Status `entschieden` nicht in `tasks.json` übernommen; der Vorschlag liegt im Postfach mit dem Status `neu`. Damit ist `vorgeschlagen` nicht nötig: `tasks.json` enthält nur angenommene Stände und Fragen.

**Migration der 2 bestehenden erledigten Entscheidungen:** Umbenennung `erledigt` → `entschieden` als zwei `daten`-Vorschläge mit `alt`-Snapshot. Keine stille Änderung (CLAUDE.md §4).

### 3.3 Widerruf und Ersetzung

Eine Entscheidung wird nie gelöscht. Ablauf als Postfach-Vorgang:

1. Vorschlag `kind: "entscheidung"` für die neue Entscheidung `e-NNN+1`, Feld `ersetzt: <alte ID>`, Begründung im `detail`.
2. Vorschlag `kind: "daten"` für die alte Entscheidung, `coll: "tasks"`, `docId: <alte ID>`, Payload mit `status: "entfallen"` und `ersetzt_durch: <neue ID>`, `alt` mit dem bisherigen Stand.
3. Beide Vorschläge im `detail` gegenseitig nennen (z. B. „gehört zu p-NNN“). So bleibt der Vorgang auch ohne Gruppenfeld lesbar.
4. Übernahme nur gemeinsam, wenn die Seite das erlaubt, sonst zuerst die neue, dann die alte. Die Seite soll die Übernahme der alten verweigern, solange die neue nicht übernommen ist (Ableitung, Prüfung in der Oberfläche nötig).
5. Werte aus der aufgehobenen Entscheidung werden nicht überschrieben. Korrekturen laufen als neuer Vorschlag (CLAUDE.md §5).

Der Rückverweis `ersetzt` ist Pflicht, weil die Notizen einseitige Verweise als wiederkehrende Fehlerquelle nennen [Primär, gelesen, Snippet]. Die Seite sollte beim Anzeigen einer Entscheidung mit `ersetzt_durch` prüfen, ob der Nachfolger `ersetzt` zurückverweist, und sonst eine Warnung zeigen.

### 3.4 Verknüpfungen

| Feld | Richtung | Regel |
|---|---|---|
| `entscheidung` (auf Aufgabe) | Aufgabe → Entscheidung | Die Aufgabe nennt die Entscheidung, die sie auslöst (CLAUDE.md §5). Mehrere Aufgaben können dieselbe Entscheidung nennen. |
| `bezug` | Aufgabe/Entscheidung → Anforderung, Dokument, Datenblatt | Liste von IDs. Keine freien Textverweise. |
| `ersetzt` / `ersetzt_durch` | Entscheidung ↔ Entscheidung | Paar, siehe 3.3. |
| `ziel` | nur im Postfach | Zieldatensatz eines Vorschlags. Nicht mehr für Aufgabe → Entscheidung verwenden. |
| `due` | Termin → Aufgabe | Wie in CLAUDE.md §5. |

**Nichts wird gelöscht, solange darauf verwiesen wird** (CLAUDE.md §5). Der Status `entfallen` ist dafür da. Die Seite sollte beim Versuch, eine Aufgabe mit eingehenden Verweisen zu löschen, nur `entfallen` anbieten.

Einfache Verknüpfungstypen wie „blockiert“ oder „verwandt“ (Jira, Redmine, Asana) sind für dieses Projekt nicht nötig. Begründung: Aufgaben sind eine Person, eine Liste, keine Projektplanung mit Abhängigkeiten. Sollte das wechseln, kann `blockiert_von` nachgerüstet werden [Ableitung].

### 3.5 Eingang (Postfach)

- Jeder Vorschlag bleibt `neu`, bis Janek übernimmt oder verwirft (CLAUDE.md §3). Claude Code setzt nie `übernommen`.
- Ein offener Vorschlag je Datensatz. Wird ein Eintrag erneut geändert, wird der offene Vorschlag aktualisiert, nicht dupliziert (CLAUDE.md §3). `alt` bleibt der Stand vor dem ersten Vorschlag.
- `verworfen` bleibt sichtbar (CLAUDE.md §3). Der Eingang trennt damit Vorschlag und Übernahme, wie Linear mit Triage und Odoo mit Stufen, aber ohne eigene Kategorie. Das ist eine Ableitung: keine geprüfte Quelle beschreibt einen Eingang mit Übernahme durch eine berechtigte Person [Snippet, Lücke].
- Datensätze mit eingehendem Vorschlag, der `entfallen` setzt, dürfen nicht mehr als `offen` in Listen erscheinen, wenn sie als `entfallen` übernommen sind. Filter: Standardansicht zeigt `offen` und `in Arbeit`.

### 3.6 Verlauf und Nachvollziehbarkeit

- Die Spur ist das Postfach: jeder übernommene Vorschlag mit `alt`, `date`, `vorschlag`, `ziel`.
- Einträge im Postfach werden nicht gelöscht. Verworfene bleiben (CLAUDE.md §3).
- Keine zusätzliche Feld-Historie pro Datensatz. Der Aufwand lohnt bei einer Person und wenigen hundert Datensätzen nicht. Quelle für die Entscheidung: Jira-Historie als Standard, aber Jira ist eine Mehrbenutzer-Anwendung [Snippet, Ableitung].
- Stand-Dokumente (Vertrag, Pflichtenheft) bleiben über `_Versionen` nachvollziehbar (CLAUDE.md §8).

### 3.7 ID-Schema

- Präfixe bleiben (`t-`, `e-`, `p-`, `k-`, `d-`, `r-`, `s-`, `q-`, `f-`, `dk-`, `c-`, `wz-`, `o-`, `fr-`, `pk-`, `ae-`). Begründung: Die Notizen belegen Präfix plus Zähler als üblich (Jira, Linear, ERPNext), und die Präfixe trennen Sammlungen beim Lesen, auch ohne Nachschlagen. Es gibt keinen belegten Grund, das zu ändern.
- Zähler je Präfix, nicht je Datei. `t-` und `e-` haben getrennte Zähler, weil es getrennte Präfixe sind.
- IDs ändern sich nie, auch wenn eine Aufgabe zur Entscheidung wird. Das ist der Grundsatz der stabilen ID aus den Notizen (MADR: Dateiname ändert sich nicht bei Titeländerung; Notizen: Zähler nicht wiederverwenden [Primär, gelesen, Ableitung]).
- Nicht wiederverwenden: Auch nach Verwerfen oder Löschen bleibt eine Nummer belegt. Die Notizen markieren das nur als Ableitung, nicht als belegte Regel.
- Abweichungen zum Ist-Zustand werden als Vorschläge behandelt, nicht still umgestellt (CLAUDE.md §2, Migration über Postfach).

---

## 4. Offene Fragen an den Eigentümer

1. **Offene Fragen in `tasks.json`:** Sollen die 22 offenen Entscheidungen (ohne Entscheider, ohne Begründung) als Entscheidungen mit Status `offen` bleiben, oder als eigene Sammlung „Fragen“ geführt werden? Die alte Sammlung `questions.json` ist archiviert (CLAUDE.md §2).
2. **Umbenennung `erledigt` → `entschieden`:** Einverstanden für die zwei bestehenden Entscheidungen und die Auswahl in der Seite?
3. **Startnummern:** `t-001` und `e-001` als Startpunkt, da es keine bestehende Nummer gibt? Oder sollen die alten Datensätze eine Nummer bekommen (Umnummerierung widerspricht CLAUDE.md §2)?
4. **Paarige Widerrufe:** Genügt die gegenseitige Nennung im `detail`, oder soll ein Feld `vorgang` (gemeinsame Kennung für ein Paar) eingeführt werden?
5. **Feld `refs`:** Entfernen oder durch `bezug` ersetzen? In keinem Datensatz gefüllt.
6. **`optionen.json`:** Gehören die Optionen zu den Entscheidungen (Verweis `e-` → `o-`), oder sind das andere Dinge? Nicht geprüft.
7. **Begründungspflicht:** Soll `reason` bei `entschieden` verpflichtend sein? Das würde die Seite blockieren, bis die Begründung da ist.
8. **Entscheider:** Reicht ein einzelner Name (`by`), oder soll es bei Gremienentscheidungen eine Liste geben? Die Notizen empfehlen einen Verantwortlichen [Snippet].
9. **Prio-Bedeutung:** Ist `1` = dringend, und wo steht die Festlegung? Die Notizen liefern keine Vorgabe für Skalen mit drei Stufen.
10. **Pflichtfeld `typ`:** 9 Aufgaben ohne `typ`: Nachtragen über Postfach-Vorschläge?

---

## 5. Quellen und Grenzen

### Quellen mit Zugriff (Notizen, Zugriffsdatum 2026-11-23)

Primär gelesen (Feldnamen und Status, Wortlaut über Zusammenfassung):
- MADR, Full Template 4.0.0: https://github.com/adr/madr/blob/4.0.0/template/adr-template.md?plain=1
- MADR, Minimal Template 4.0.0 (wörtlich gelesen): https://github.com/adr/madr/blob/4.0.0/template/adr-template-minimal.md?plain=1
- MADR-Projekt: https://github.com/adr/madr
- Joel Parker Henderson, architecture-decision-record: https://github.com/joelparkerhenderson/architecture-decision-record

Snippet, Sekundärquelle oder Community (nicht volltextgeprüft):
- Atlassian Jira Work Management, Workflows and statuses: https://support.atlassian.com/jira-work-management/docs/workflows-and-statuses-for-the-board
- Atlassian Jira Server, Workflows: https://confluence.atlassian.com/display/Jira/Configuring+Workflow (älterer Stand)
- Notion Help, Database properties: https://www.notion.com/en-gb/help/database-properties
- Linear, Configuring workflows: https://linear.app/docs/configuring-workflows
- Linear, Triage: https://linear.app/docs/triage (Seite nicht abgerufen)
- Linear, Priority: https://linear.app/docs/priority
- GitHub Docs, Quickstart for Projects: https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/quickstart-for-projects
- GitHub Docs, Adding sub-issues: https://docs.github.com/en/enterprise-cloud@latest/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues
- Redmine Wiki, Issue tracking setup: https://www.redmine.org/projects/redmine/wiki/RedmineIssueTrackingSetup
- OpenProject, Work package types und Status: https://www.openproject.org/docs/system-admin-guide/manage-work-packages/work-package-types/ (nicht abgerufen)
- Asana Developers, Tasks: https://developers.asana.com/docs/tasks
- Frappe/ERPNext, Tasks: https://docs.frappe.io/erpnext/tasks.md
- Frappe/ERPNext, Document Versioning: https://docs.frappe.io/erpnext/document-versioning.md
- Frappe/ERPNext, Naming series: https://docs.frappe.io/erpnext/naming-series
- Frappe Framework, Audit Trail: https://docs.frappe.io/framework/user/en/audit-trail
- Odoo 19, Engineering change orders: https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/plm/manage_changes/engineering_change_orders.html
- Odoo 19, ECO types and stages: https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/plm/manage_changes/eco_type.html
- Jama, Clear suspect links: https://help.jamasoftware.com/en/manage-content/coverage-and-traceability/relationships/clear-suspect-links.html
- codebeamer, Versioning and Access History (Release 3.0, älter): https://support.ptc.com/help/codebeamer/r3.0/en/codebeamer/user_guide/versioning_and_access_history.html
- Polarion, Document Baselines: https://docs.plm.automation.siemens.com/content/polarion/20/help/en_US/user_and_administration_help/user_guide/work_with_documents/document_baselines.html
- ISO 9001:2015, Klausel 8.5.6, Sekundärquelle (Beratungsseite, nicht die Norm): https://www.thecoresolution.com/clause-8-5-6-iso-9001-2015-explained
- Nygard 2011 (nur über Sekundärbeschreibungen, Original nicht abrufbar): https://albertml.com/Literature/Documenting+Architecture+Decisions+(Nygard)
- Confluence Decision-Blueprint, Forum ca. 2018 (veraltet): https://answers.seibert.group/t/confluence-can-you-explain-the-decision-blueprint/565

### Nicht erreichbar (laut Notizen, DNS-Fehler in der Sitzung)

adr.github.io, cognitect.com, en.wikipedia.org, confluence.atlassian.com (aktuell), www.nasa.gov, www.adr.zone, linear.app (Hauptseite), docs.github.com (Volltext), www.openproject.org, www.redmine.org (teils), support.atlassian.com, help.notion.com, developers.asana.com (Volltext), docs.frappe.io (Volltext), www.odoo.com (Volltext), support.ptc.com (Volltext), help.jamasoftware.com (Volltext), docs.plm.automation.siemens.com (Volltext), www.thecoresolution.com (Volltext). Aussagen aus diesen Quellen stammen aus Suchausschnitten.

### Widersprüche und Lücken in den Notizen

- Jira: `linkedIssues(issueKey, linkType)` oder `hasLinkType(linkType)` als JQL-Funktion, unentschieden.
- Linear: ob Duplicate eine eigene Kategorie oder unter Canceled liegt, widersprüchlich.
- Jama: Richtung der Suspect-Markierung nur durch Community-Aussage belegt.
- Keine Quelle zu Eingangskörben mit Übernahme, zu Revisionsbuchstaben, zu Löschregeln in Confluence oder Notion, zu Papier-Prozessen als Vergleich.
- Keine empirische Studie zu verlorenen Entscheidungen; die Ursachen (fehlender Ort, fehlender Owner, fehlende Begründung) sind Vendor-Aussagen [Snippet, schwach].
- Keine Quelle, die für dieses Projekt eine Traceability-Kette Anforderung → Aufgabe → Entscheidung → Nachweis beschreibt.

### Was dieser Bericht nicht prüft

- Die Ist-Zustands-Angaben beziehen sich auf den Stand am 2026-11-23 und nur auf die Felder und Zählungen in Abschnitt 2.
- Die Oberfläche (`vorlage.html`) wurde nur an den Auswahllisten gegengeprüft, nicht im Verhalten.
- `optionen.json`, `reqs.json` und `sensors.json` wurden nicht ausgewertet.
- Es wurden keine Daten, keine CLAUDE.md und kein Postfach verändert.
