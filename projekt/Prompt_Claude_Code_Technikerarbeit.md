# Prompt für Claude Code: Technikerarbeit weiterführen

Diesen Text komplett in eine neue Claude-Code-Sitzung auf dem Repo `JanekBauer/Technikerarbeit` einfügen. Empfohlenes Modell: Opus.

---

Du arbeitest selbstständig an der Technikerarbeit von Janek Bauer („Janek“, Deutsch, Anrede „Janek“). Janek ist danach nicht erreichbar. Arbeite so weit wie möglich ohne Rückfragen. Alles, was du in sein Cockpit einträgst, landet als Vorschlag im **Postfach**, und Janek übernimmt oder verwirft es später.

## 1. Erst lesen, dann handeln

1. `git pull` auf `main`. Arbeite direkt auf `main`, keine Branches.
2. Lies `CLAUDE.md` vollständig. Diese Datei gilt vor allen anderen Hinweisen hier.
3. Lies `projekt/Statusbericht_2026-11-22.md` vollständig. Er enthält Ziel, Anforderungen, Stand, offene Fragen und Arbeitspakete.
4. Das maßgebliche Pflichtenheft ist **V0.2**. Im Repo liegt es als `docs/archiv/3 Pflichtenheft/Pflichtenheft/V1.2_Bauer_TA_PH_V1.docx` (Stand 20.11.2026). Janek nennt es V0.2. Lies den Text (`word/document.xml` aus der .docx, Absätze trennen).
5. **Verboten:** Die frühere Fassung V8.7 existiert nicht mehr und darf nicht verwendet werden. Auch `projekt/_Versionen/` nicht als Quelle nutzen.
6. Lies die Cockpit-Daten in `cockpit/daten/*.json`. Bei Widersprüchen gewinnt das PH V0.2 (CLAUDE.md, Projektabgleich).

## 2. Was du selbstständig tun darfst

- **Recherche im Netz:** Hersteller-Datenblätter, Normen (AIAG MSA, ISO 13485, ASTM), Messprinzipien, Wiederholgenauigkeit und Linearität von Mikrometern, Messgeschwindigkeit, Einfluss von Auflage und Durchbiegung. Jede Angabe mit Quelle, Seitenzahl und Abrufdatum festhalten.
- **Datenblätter herunterladen,** nur öffentlich zugängliche Herstellerunterlagen. Ablage: `docs/archiv/6 Recherche Messtechnik/<Hersteller>/<Modell>_<Art>.pdf`. Keine internen Betriebsunterlagen, keine Rohrspezifikationen, keine Angebote mit Preisen anderer Firmen.
- **Sensoren und Varianten** recherchieren und vergleichen. Neue Sensoren als Vorschlag ins Postfach (Abschnitt 4).
- **Analysen** erstellen: Abgleich PH gegen Cockpit, Lücken im Morphologischen Kasten, Bewertungskriterien für die Variantenauswahl, Herstellerfragen als Entwurf, Gliederung der Dokumentation prüfen.
- **Dateien** im Repo anlegen, nur in: `projekt/`, `docs/archiv/6 Recherche Messtechnik/`, `cockpit/vorbereitung/`.

## 3. Was du nicht darfst

- **Keine direkten Änderungen** an `cockpit/daten/*.json` außer `postfach.json`. Also nicht in `tasks.json`, `sensors.json`, `reqs.json`, `tools.json`, `kilog.json`, `checks.json`, `deadlines.json` oder `files.json` schreiben.
- **Nichts senden:** keine Mails, keine Anfragen an Hersteller, keine Nachrichten an Herrn Baidinger, Graudejus oder die FSL.
- **Nichts löschen** und nichts verschieben, außer Dateien in den Unterordner `_Versionen`. Ältere Versionen niemals endgültig löschen.
- **Keine fachlichen Lösungen für Janek schreiben.** Die Formatvorlage erlaubt KI nur zur sprachlichen Optimierung. Du darfst analysieren, Lücken aufzeigen, Kriterien vorschlagen und Quellen finden. Eigene Konzepte, Ideen für den Morphologischen Kasten oder Textbausteine für die Dokumentation sind Vorschläge, die Janek ausdrücklich bestätigen muss. Kennzeichne jeden solchen Vorschlag im Postfach als „KI-Vorschlag“ im Titel und mit `fach: true`.
- **Keine Modellnamen** in Commits, Dateien oder Einträgen.

## 4. So legst du Vorschläge an: nur über das Postfach

Jeder Vorschlag ist ein Eintrag in `cockpit/daten/postfach.json`. Eine Zeile je Eintrag, `id` eindeutig, `status: "neu"`, `vorschlag: "KI (Claude Code)"`, `date` im Format JJJJ-MM-TT. Für `updated` nur den echten Zeitstempel aus `date -u +%Y-%m-%dT%H:%M:%S.000Z` verwenden. Nie erfinden.

**Art `aufgabe`, `entscheidung`, `aenderung`:** Felder `title`, `detail`, `who`, `ask`, `due`, `prio`, `stand`.

**Art `kilog`** (Pflicht für jede KI-Hilfe zur Technikerarbeit, vor dem Commit): Felder `date`, `detail` (was die KI gemacht hat), `fach` (`true`, wenn fachlicher Text entstanden ist). Ein Eintrag pro Arbeitspaket reicht, er muss aber alles beschreiben, was du in dieser Sitzung getan hast.

**Art `daten`** (für alles andere, z. B. Sensoren, Anforderungen, Morphologischer Kasten, Dateien):
- `coll`: Sammlung, z. B. `sensors`, `reqs`, `tools`, `files`, `sources`, `deadlines`.
- `docId`: ID des bestehenden Datensatzes zum Überschreiben. Ohne `docId` wird ein neuer Datensatz angelegt.
- `payload`: der **vollständige** Datensatz. Bei `tools` (Morphologischer Kasten, `id: "morph"`) ist der komplette Inhalt nötig, weil das ganze Dokument ersetzt wird. Vorher den bestehenden Datensatz aus `cockpit/daten/tools.json` lesen und nur die gewünschte Änderung einfügen.

Beispiel eines Sensor-Vorschlags, eine Zeile in `postfach.json`:
`{"id":"pv-sensor-<kurz>","kind":"daten","coll":"sensors","title":"Neuer Sensor: <Hersteller> <Modell>","detail":"Quelle: <URL>, Seite <n>, abgerufen <JJJJ-MM-TT>. Begründung: <kurz>","vorschlag":"KI (Claude Code)","status":"neu","date":"<JJJJ-MM-TT>","fach":false,"payload":{...}}`

Die `payload`-Felder für Sensoren sind wie in `cockpit/daten/sensors.json` (nr, ord, maker, model, principle, range, rmin, rmax, rep, repcond, lin, rate, build, trig, light, source, note, docs). Fehlende Werte mit leerem Text lassen, nicht schätzen.

**Art `kilog` bitte nicht vergessen.**

## 5. Was dein Ablauf ist

1. Lesen (Abschnitt 1).
2. Prüfen, welche Fragen des Statusberichts Abschnitt 5 schon beantwortet werden können, z. B. Toleranzwerte, Taktzeit, Platzbedarf oder Kontaktwerkstoffe, und ob dazu öffentliche Quellen existieren.
3. Recherche zu Sensorik (Abschnitt 4.2 im Statusbericht): Datenblätter für Ø 1 bis 6,5 mm, Wiederholgenauigkeit am bewegten Rohr, Messgeschwindigkeit bei 3 m. Herunterladen, abheften, Auszüge notieren.
4. Vorschläge als `daten`-Einträge und `aufgabe`/`entscheidung` anlegen (Abschnitt 4).
5. Analysen als Projektdateien unter `projekt/` schreiben, z. B. `projekt/Analyse_<Thema>_<Datum>.md`. Jede Datei nennt die Quellen.
6. Am Schluss: `python3 cockpit/build.py` ausführen. Dann `cockpit/daten/postfach.json`, `docs/archiv/6 Recherche Messtechnik/`, `projekt/` und `docs/index.html` committen (Nachricht auf Deutsch, was und warum, mit Co-Authored-By-Zeile) und direkt auf `main` pushen.
7. Zusammenfassung im Chat: was du angelegt hast, wie viele Postfach-Einträge, welche Quellen, welche drei Punkte Janek zuerst entscheiden sollte.

**Stoppen**, wenn: alle Arbeitspakete aus Abschnitt 6 erledigt sind oder die Quellen erschöpft sind. Laufende Arbeit bitte nicht unterbrechen, um eine Frage zu stellen. Schreibe Unklarheiten als `entscheidung` ins Postfach.

## 6. Arbeitspakete (Reihenfolge)

1. **Toleranzwerte und %GRR-Grenze.** Die Zylinderform-Toleranzen NiTi und Edelstahl sind im PH V0.2 offen [?]. Stelle die Rechnung aus dem Statusbericht (Abschnitt 4.1) als `entscheidung` ins Postfach, mit den drei Szenarien.
2. **Sensor-Shortlist.** Recherche zu Micro-Epsilon ODC2700, Keyence LS-9030, RIFTEK RF656/RF657 und weiteren Herstellern, falls passend. Neue Sensoren als `daten`-Vorschläge, nur mit Quelle. Die Vorprüfung im Statusbericht (Abschnitt 4.2) als `analyse`-Datei belegen.
3. **Messprinzip.** Entscheidungsgrundlage zu ThruBeam (Drehung) gegen 2D-Schattenbild, als Analyse und `entscheidung`.
4. **Morphologischer Kasten.** Lücken benennen: welche Teilfunktionen keine eigenen Ideen haben. Keine Lösungen. Kriterien aus den Anforderungen 2.5, 3.1, 3.2, 3.3 und 4.2 ableiten.
5. **Bewertungskriterien** für die Variantenauswahl (11.12.). Festanforderungen als K.-o.-Kriterien, Mindest- und Wunschanforderungen als gewichtete Kriterien. Vorschlag als `daten` für `tools`, Eintrag `eval`, mit Gewichtung „offen“.
6. **Cockpit an PH V0.2 angleichen.** Als `daten`-Vorschläge: Anforderung 2.1 von „Ovalität“ auf „Zylinderform“ (`reqs`, `docId` der bestehenden Anforderung 2.1), Entscheidung „Zylinderform“ als erledigt markieren, PH-Freigabe-Datum (PH 27.11., Cockpit 04.12.), Platzbedarf (5.1) auf offen.
7. **Herstellerfragen** als Entwurf unter `projekt/`, nicht versenden.
8. **Dubletten** im Cockpit auflisten (Projektabschluss, PH-Freigabe, Variantenauswahl) als `aufgabe` „Dubletten bereinigen“, nicht löschen.

## 7. Qualitätsregeln

- Jede Zahl mit Quelle (Dokument, Seite, Abrufdatum). Ohne Quelle nicht übernehmen.
- Unterscheide klar: Herstellerangabe, eigene Rechnung, Schätzung. Schätzungen als solche kennzeichnen.
- Rechnungen nachvollziehbar aufschreiben, so dass Janek sie prüfen kann.
- Keine vertraulichen Daten aus den Rohrspezifikationen zitieren, nur sinngemäß paraphrasieren (PH Kap. 5.2).
- Wenn eine Quelle nicht eindeutig ist, nichts übernehmen, sondern als Frage ins Postfach.
