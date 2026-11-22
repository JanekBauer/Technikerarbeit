# Auftrag und Statusbericht Technikerarbeit, Stand 22.11.2026

Für eine Claude-Code-Sitzung (Opus 5.5, Research, Skills). Vollständig, ohne weiteren Kontext lesbar.

---

## 0. Auftrag an die Sitzung

Du arbeitest an der Technikerarbeit von Janek Bauer („Janek“, Deutsch, Anrede „Janek“). Ziel: den Stand gegen das Pflichtenheft abgleichen, herausfinden, was als Nächstes erarbeitet werden kann, und das ohne Rückfragen so weit wie möglich vorbereiten. Janek ist danach im Betrieb und nicht erreichbar.

**Maßgeblich:**
- Pflichtenheft **V1.2** (Datei `docs/archiv/3 Pflichtenheft/Pflichtenheft/V1.2_Bauer_TA_PH_V1.docx`, Stand 20.11.2026). Janek nennt es „V0.2 Bauer_TA_PH_V1“, gemeint ist diese Datei.
- Cockpit-Daten in `cockpit/daten/*.json`. Laut CLAUDE.md gewinnt bei Wertkonflikten das Repo, also das PH.
- Regeln in `CLAUDE.md` (Repo-Wurzel): direkt auf `main` arbeiten, keine Branches, Zeitstempel nie erfinden, Postfach-Regeln, KI-Logbuch.

**Nicht verwenden:** Die frühere Fassung **V8.7** ist gelöscht und darf nicht genutzt werden. Auch der frühere Bericht auf Basis von V8.7 liegt nur noch unter `projekt/_Versionen/` und ist veraltet.

**Ergebnisse, die du liefern sollst:**
1. Abgleich PH V1.2 gegen den Cockpit-Stand: was ist erledigt, was fehlt, was ist widersprüchlich.
2. Liste der offenen Fragen an den Betrieb (Baidinger, Graudejus, FSL), jeweils mit Begründung.
3. Vorprüfung der Sensorik mit Katalog- und Datenblattwerten, ohne eigene Messung, mit Quellen.
4. Priorisierte Arbeitspakete: was man jetzt schon erarbeiten kann, mit Zeitbedarf und Abhängigkeiten.
5. Vorschläge als Postfach-Einträge (siehe Regeln unten), nicht als direkte Änderung an Janeks Daten.

**Regeln, die du einhalten musst:**
- **Keine fachlichen Lösungen für Janek schreiben.** Die Formatvorlage erlaubt KI nur zur sprachlichen Optimierung. Du darfst analysieren, Lücken und Kriterien aufzeigen, Quellen suchen und Fragen formulieren. Eigene technische Konzepte, Ideen für den Morphologischen Kasten oder Textbausteine für die Dokumentation gehören Janek.
- **Jede KI-Hilfe für die Technikerarbeit** wird vorher als Postfach-Eintrag angelegt: `kind: "kilog"`, `date`, `detail` (was KI gemacht hat), `fach` (`true`, wenn fachlicher Text entstanden ist), `status: "neu"`, `vorschlag: "KI (Claude Code)"`. Die Datei ist `cockpit/daten/postfach.json`. Dort einen Eintrag ergänzen, nicht direkt in `kilog.json` schreiben.
- **Neue Aufgaben, Fragen und Entscheidungen** kommen ebenfalls zuerst als Postfach-Eintrag (`kind`: `aufgabe`, `entscheidung` oder `aenderung`; `status: "neu"`; `vorschlag: "KI (Claude Code)"`). Nicht direkt in `tasks.json` schreiben.
- **Vertrauliche Unterlagen:** Rohrspezifikationen und interne Prüfanweisung dürfen nicht zitiert oder gezeigt werden, nur sinngemäß paraphrasiert (PH Kap. 5.2).
- **Nach der Arbeit:** `python3 cockpit/build.py` ausführen, `cockpit/daten` und `docs` committen (Nachricht auf Deutsch, was und warum), direkt auf `main` pushen.
- **Commits und Einträge:** keine Modellnamen in Commit-Nachrichten, Pull-Requests oder Dateien im Repo.
- **Kein Versand** an Dritte, keine Mails, keine Anfragen an Hersteller. Vorbereiten ja, verschicken nein.
- **Sparsam mit Tokens.** Lies Dateien gezielt. Die PH-Textdatei liegt nach Extraktion als Klartext vor, nutze sie statt der XML-Datei.

**Empfohlene Reihenfolge:**
1. `git pull` auf `main`, dann `CLAUDE.md` lesen.
2. PH V1.2 als Text extrahieren (`word/document.xml` aus der .docx lesen, Absätze und Tabellen trennen).
3. Cockpit-Daten lesen: `reqs.json`, `packages.json`, `tasks.json`, `deadlines.json`, `checks.json`, `sensors.json`, `tools.json` (Morphologischer Kasten `morph`, Sensorkatalog `sensorkat`), `doku.json`, `postfach.json`.
4. Abgleich durchführen (Abschnitt 3 bis 6 dieses Berichts als Vorlage nutzen).
5. Research zu Sensorik und Messprinzipien (Abschnitt 5), mit Quellenangaben.
6. Ergebnisse als Postfach-Einträge eintragen, Bericht unter `projekt/` aktualisieren (neue Datei mit Datum, alte Fassung nach `projekt/_Versionen/`).

---

## 1. Projekt in Kürze

**Titel:** Konzeption und Konstruktion einer automatisierten Messanlage zur Prüfung von Rohren im Wareneingang.
**Auftraggeber:** BD Gamer Lasertechnik GmbH, Bruchsal. **Durchführender:** Janek Bauer. **Betreuer Betrieb:** Paul Baidinger, Technische Leitung. **Schulischer Betreuer:** Björn Graudejus de Olio.

**Problem:** Die Rohre (Nitinol, Edelstahl, Tantal) werden im Wareneingang nur optisch geprüft. Zylinderform und Maßhaltigkeit werden nicht gemessen. Rohrfehler fallen erst beim Laserschneiden auf. Die Rohre sind lang und dünnwandig, es gibt kein prozesssicheres Spann- und Handhabungskonzept.

**Ziel:** Neukonzeption und CAD-Konstruktion einer automatisierten Messanlage für Rohre von 1 bis 3 m Länge. Enthalten sind Vorrichtungsmechanik, Spann- und Handhabungskonzept, Messprozess und Sensorintegration. CE-normgerecht.

**Abgrenzung (PH Kap. 4):** kein Bau, keine Inbetriebnahme, keine realen Messungen, keine Steuerungs- oder Auswertesoftware, keine Wandstärken-, Konzentrizitäts- und Geradheitsprüfung, keine MFU am realen System, keine Anbindung an IT- oder QM-Systeme, kein automatisches Einlegen (das Einlegen bleibt manuell), keine Beschaffung der Kaufteile (Angebote sind dagegen ein Ergebnis).

**Zu übergebende Ergebnisse (PH Kap. 3):**
1. CAD-Baugruppe der Messanlage (3D)
2. Fertigungszeichnungen
3. Stückliste (Eigenfertigungs- und Kaufteile)
4. Angebote für die Kaufteile
5. Beschreibung des Messprozesses inkl. Sensorkonzept
6. Funktionsbeschreibung der Anlage
7. Technische Dokumentation inkl. Pneumatikplan und Elektronikplan
8. Anforderungsliste

---

## 2. Anforderungsliste laut PH V1.2 (Stand 20.11.2026)

Art: F = Festanforderung, M = Mindestanforderung, W = Wunschanforderung. In V1.2 sind mehrere Werte mit [?] offen oder gelb markiert (mit dem Betrieb abzustimmen).

| Nr. | Art | Anforderung | Wert / Stand |
|---|---|---|---|
| 1.1 | F | Werkstoff NiTi / Edelstahl | Nitinol und Edelstahl, Tantal ist Wunsch (1.5) |
| 1.2 | F | Rohrlänge | 1000–3000 mm |
| 1.3 | F | Außendurchmesser | 1 bis 6,5 mm |
| 1.4 | F | Wandstärke | n. a. (nicht Bestandteil) |
| 1.5 | W | Werkstoff Tantal | Tantal ohne Toleranz (V1.2-Notiz) |
| 2.1 | F | Zylinderform (Ø max − Ø min) je Rohrtyp | **ΔD NiTi [?], Edelstahl [?]** |
| 2.2 | F | Erfassung Außendurchmesser, Maßhaltigkeit | ΔD ± 13 µm |
| 2.3 | M | Abstand der Messpunkte über die Länge | 2 mm |
| 2.4 | M | Reproduzierbarkeit %GRR (AIAG MSA) | ≤ 10 % |
| 2.5 | F | Auswertung je Messpunkt, keine Mittelwerte | jeder Messwert in der Toleranz |
| 2.6 | W | Rauheit messen | – |
| 2.7 | W | Beschädigung oder Kontamination feststellen | – |
| 3.1 | F | Keine plastische Verformung beim Messen | Spannung < 380 MPa (NiTi, oberes Plateau), < 690 MPa (Edelstahl) |
| 3.2 | F | Keine Beschädigung, Rohre sauber und ölfrei | lt. Rohrspezifikation |
| 3.3 | F | Durchbiegung und Lage verfälschen das Ergebnis nicht | Einfluss in 2.4 enthalten |
| 4.1 | W | Taktzeit pro Rohr (Reduzierung erwünscht) | **offen** |
| 4.2 | F | Rohr manuell einlegen, Messung und Auswertung automatisch | – |
| 5.1 | W | Max. Platzbedarf (L × B) | **offen** |

**Technische Rahmenbedingungen:** Werkstoffnormen ASTM F2633 und F2063 (NiTi), ASTM F138 (Edelstahl), ASTM F560-22 (Tantal). Rauheit nach DIN EN ISO 4287. Nitinol superelastisch, Af max. 0 °C. Rohre gerade verpackt, Schutz gegen Verbiegen. Umgebung Wareneingang, QM, Konstruktion. Medien: 230 V, Druckluft. Messprinzip berührungslos, Auflage und Führung zulässig. QM-Vorgaben (ISO 13485) für neues Prüfmittel werden mit dem QM geklärt. Kostenrahmen offen.

**Termine laut PH V1.2 (Kap. 5.2):**
- 23.10.2026: Kick-off (erledigt)
- 27.11.2026: Abstimmung und Freigabe des Pflichtenhefts
- 11.12.2026: Variantenauswahl
- 15.01.2027: Konstruktionsfreigabe
- 05.03.2027: Übergabe der Ergebnisse, Projektabschluss

**Schulische Termine laut Cockpit:** MS 1 am 20.11.2026 (erledigt), MS 2 am 15.01.2027, MS 3 am 19.03.2027, Abgabe Dokumentation am 05.04.2027 (10:00 Uhr, Sekretariat), Präsentation 17./18.06.2027. Gesetzliche Frist finale Aufgabenstellung Anfang Januar 2027 (ca. 08.01.2027).

---

## 3. Abgleich PH V1.2 gegen den Cockpit-Stand

### 3.1 Was ist konsistent
- **Termine:** Variantenauswahl (11.12.), Konstruktionsfreigabe (15.01.) und Projektabschluss (05.03.) stimmen zwischen PH und Cockpit überein.
- **Anforderungen 2.2, 2.3, 2.4, 2.5, 3.x, 4.2** sind im Cockpit bestätigt und im PH unverändert.
- **Werkstoffe, Länge 1–3 m, Außendurchmesser 1–6,5 mm** stimmen überein.

### 3.2 Abweichungen, die bereinigt werden müssen
1. **Ovalität → Zylinderform.** Das PH V1.2 ersetzt die Ovalität durch Zylinderform. Im Cockpit steht die Anforderung 2.1 noch als „Ovalität … bestätigt“ (`reqs.json`), und es gibt eine offene Entscheidung „Zylinderform“ (Cockpit-Eintrag, Frist 27.11.). Vorschlag: Die Anforderung im Cockpit auf „Zylinderform, Werte offen“ setzen und die Entscheidung als durch das PH V1.2 erledigt markieren. Janek entscheidet.
2. **Toleranzwerte 2.1 sind offen [?].** Im früheren Stand standen NiTi 0,010 mm und Edelstahl 0,025 mm. Diese Werte gelten nicht mehr als gesichert. Sie müssen mit dem QM und Herrn Baidinger geklärt werden. Das ist die wichtigste offene Frage für die Messtechnik.
3. **PH-Freigabe:** PH V1.2 nennt 27.11.2026. Das Cockpit hat die Aufgabe „PH-Freigabe + Unterschrift im Betrieb“ auf 04.12.2026. Der Eintrag muss angeglichen werden.
4. **Zusätzliche Festlegungen in V1.2:** Tantal ohne Toleranz; „Taktzeit reduziert erwünscht“; „Bild“ in der Problemstellung ist ein Platzhalter; „CE-normgerecht“ ist neu in Ziel und Rahmen. Diese Punkte sind im Cockpit nicht oder nicht vollständig erfasst.
5. **Cockpit-Reqs 4.1 und 5.1:** Im Cockpit ist 5.1 als bestätigt markiert, im PH V1.2 ist der Platzbedarf noch offen (gelb). Angleichen.
6. **Kontaktdaten:** Die E-Mail des schulischen Betreuers und die Telefonnummer von Herrn Baidinger sind in V1.2 anders als im früheren Stand. Nur zur Kenntnis, keine Änderung nötig.

### 3.3 Projektpakete laut Cockpit (`packages.json`, Stand 06.11.–20.11.)
| Paket | Ampel | Stand |
|---|---|---|
| Aufgabenstellung | gelb | AS V4.2 an PH angeglichen, 1 Seite. Offen: KI-Formulierung (W8), FSL-Prüfung (W5), Unterschriften bis 30.11. |
| Pflichtenheft | gelb | V1.2 nach MS 1 umgesetzt. Offen: Freigabe und Unterschrift, Termin im PH, Formfehler, Anforderungen W10–W14 (laut Cockpit), Bild und Platzbedarf |
| Projektplan (Rillsoft) | rot | seit 16.10. unverändert |
| Lösungsansätze (PDF für MS 1) | gelb | 1 Idee; Skizze, Denkfragen, zweite Variante und weitere Hersteller fehlen |
| MS-1-Termin und Vor-Ort-Termin | rot | Stand 06.11. nicht angefragt |
| Messtechnik-Recherche | rot | nur Keyence betrachtet; Herstellervergleich dringend |
| Spann- und Handhabungskonzept | gelb | Morphologischer Kasten V2 (12.11.): 13 Teilfunktionen plus 3 Querschnittsfunktionen. Ideen überwiegend KI-Vorschläge, eigene Ideen nur bei TF1, TF3 und TF4. Keine Gesamtvarianten. |
| Variantenbewertung | grau | nicht begonnen |
| CAD-Konstruktion (SolidWorks) | grau | nicht begonnen |
| Messprozess, Sensorintegration, Unterlagen | grau | nach Variantenwahl |
| Dokumentation | grau | Gliederungsentwurf 19.10. mit 9 Kapiteln, Doku-Speicher leer |
| Präsentation | grau | ab Mai 2027 |

### 3.4 Ergebnisse, die komplett fehlen
CAD-Baugruppe, Fertigungszeichnungen, Stückliste, Funktionsbeschreibung, Pneumatikplan, Elektronikplan. Angebote: bisher nur als Aufgabe „Angebote Sensorik für die Shortlist anfragen“ (offen).

### 3.5 Offene Entscheidungen und Aufgaben (Cockpit, Stand 22.11.)
- **27.11.:** Entscheidung „MS 1 nachfragen“, Entscheidung „Zylinderform“, Entscheidung „Variantenauswahl: Datum im PH klären“, Entscheidung „Projektabschluss: Datum im PH klären“, Aufgabe „Bilder Stents und Marker holen“.
- **04.12.:** Entscheidung „PH-Freigabe: Datum im PH klären“, Entscheidung „Taktzeit pro Rohr“, Aufgabe „Zulässige Kontaktstellen und Kontaktwerkstoffe für Auflage und Führung (PH 3.2)“.
- **27.01.:** Aufgabe „Bilder und Werte in der Präsentation“.
- **19.03.:** Aufgabe „Gliederung TA-Doku abstimmen“.

**Hinweis Dubletten:** Im Cockpit gibt es doppelte Einträge für „Projektabschluss: Datum im PH klären“ (`mwqieyis7lqnk`, `mwqziec7vx9bf`), „PH-Freigabe: Datum im PH klären“ (`mwqief827m65y`, `mwrst4h2yg4ju`) und „Variantenauswahl: Datum im PH klären“ (`mwqif9og0838q`, `mwqzj17mgv7lj`). Die älteren Kopien sollen nach Janeks Freigabe ins `_Versionen`-Archiv verschoben werden. Nicht selbst löschen.

---

## 4. Was man aus dem Stand heraus erarbeiten kann

### 4.1 Der zentrale Rechenpunkt: %GRR bei Zylinderform
Die Messsystemstreuung darf 10 % der Toleranz nicht überschreiten (Anf. 2.4, AIAG MSA). Die Grenze für die Standardabweichung der Messstreuung ergibt sich daraus:

σ_GRR ≤ (0,10 × Toleranzbreite) / 6

- **Szenario A, ΔD ± 13 µm für den Außendurchmesser (Anf. 2.2):** Toleranzbreite 26 µm, daraus σ ≤ 0,43 µm.
- **Szenario B, Zylinderform 10 µm (früherer Wert NiTi):** Toleranzbreite 10 µm, daraus σ ≤ 0,17 µm.
- **Szenario C, Zylinderform 25 µm (früherer Wert Edelstahl):** σ ≤ 0,42 µm.

Die Werte in B und C sind nur Platzhalter, weil V1.2 sie als [?] führt. Entscheidend ist der Wert, den Herr Baidinger bestätigt. Erst dann kann die Sensorauswahl gegen die Anforderung geprüft werden.

### 4.2 Sensor-Vorprüfung nach Katalogwerten (ohne Messung)
Im Cockpit liegen 26 Sensorvarianten von Keyence, Micro-Epsilon und RIFTEK (`sensors.json`). Vorprüfung nur nach Katalog- und Handbuchwerten, Quellen siehe `sensors.json` und die Kataloge im Archiv:

- **Laser-Mikrometer Micro-Epsilon ODC2520 und ODC1200:** Wiederholgenauigkeit ab ca. 5 µm (bis 140 µm). Für Szenario A (0,43 µm) und B (0,17 µm) zu grob. Voraussichtlich ausscheidend.
- **Lichtband-Mikrometer Keyence LS-9030 (LS-9030M, LS-9030D):** Wiederholgenauigkeit ±0,1 µm (2σ), Linearität ±2 µm, Messbereich 0,3–30 mm. Die Angabe gilt für ein ruhendes Normal Ø 10 mm. Für Ø 1–6,5 mm plausibel, muss vom Hersteller bestätigt werden. Die Linearität von ±2 µm liegt über Szenario A. Das ist kritisch.
- **LED-Mikrometer Micro-Epsilon ODC2700-10 und ODC2700-40:** Wiederholgenauigkeit ≤ 0,03 µm bzw. ≤ 0,1 µm, Linearität ≤ 0,5 µm bzw. ≤ 1 µm, Messbereich 10 mm bzw. 40 mm. Auf dem Papier die präzisesten Kandidaten. ODC2700-10 passt zu Ø 6,5 mm.
- **2D-Schattenbild-Mikrometer RIFTEK RF656.2D und RF657.2D:** Linearität ±0,8 bis ±4,5 µm je Größe. Wiederholgenauigkeit im Handbuch nicht angegeben. Vorteil: Zylinderform lässt sich aus einem Schattenbild direkt bestimmen. Einschränkung: Abtastrate 24 bis 65 Messungen pro Sekunde.

**Schlussfolgerung für die Vorprüfung:** Die Keyence- und RIFTEK-Werte sind vermutlich nicht ausreichend, wenn Szenario A oder B gilt. Die Micro-Epsilon-LED-Mikrometer sind die aussichtsreichsten Kandidaten. Diese Einschätzung muss mit Quellen belegt und vom Hersteller bestätigt werden.

**Research-Auftrag:** Herstellerdatenblätter für Ø 1 bis 6,5 mm, Wiederholgenauigkeit am bewegten Rohr (nicht am Normal), Einfluss von Auflage und Durchbiegung, Messgeschwindigkeit bei 3 m Länge und Messpunktabstand 2 mm. Quellen mit Seitenzahl angeben.

### 4.3 Messprinzip (Entscheidung für Janek)
Ob die Zylinderform aus mehreren Winkelmessungen (ThruBeam, Drehung) oder aus einem 2D-Bild kommt, hängt vom Sensor ab. Das ist eine fachliche Entscheidung. Du bereitest die Entscheidungsgrundlage vor (Vor- und Nachteile, Messzeit, Aufwand), entscheidest aber nicht.

### 4.4 Morphologischer Kasten (Spann- und Handhabungskonzept)
Stand: 13 Teilfunktionen und 3 Querschnittsfunktionen (`tools.json`, `morph`). Eigene Ideen fehlen bei den meisten Teilfunktionen (nur TF1, TF3 und TF4 sind von Janek). Gesamtvarianten fehlen. Erarbeiten: Lücken und Abhängigkeiten aufzeigen, Kriterien aus Anforderungen 2.5, 3.1, 3.2, 3.3 und 4.2 ableiten, Janek die Ideen überlassen. Keine Lösungen liefern.

### 4.5 Bewertungskriterien für die Variantenauswahl (11.12.)
Festanforderungen (F) als K.-o.-Kriterien, Mindestanforderungen (M) und Wünsche (W) als gewichtete Kriterien. Die Vorlage `tools.json`, Eintrag `eval`, ist leer und kann mit den Kriterien befüllt werden. Gewichtung und Bewertung macht Janek.

### 4.6 Herstellerfragen und Angebotsanfragen
Entwurf der Fragen an Micro-Epsilon, Keyence und RIFTEK, geordnet nach Anforderungen. Versand nur durch Janek. Angebote sind Ergebnis der Arbeit und fehlen komplett.

### 4.7 Dokumentation
Die Gliederung hat 9 Kapitel (Doku-Speicher). Kapitel 2 (Problemstellung) lässt sich aus dem PH sinngemäß entwickeln (Paraphrase, keine vertraulichen Daten zitieren). Die Umsetzung schreibt Janek. Recherche zu Normen und Messtechnik mit Quellen ist erlaubt und wird im KI-Logbuch vermerkt.

### 4.8 Offene Klärungen mit dem Betrieb
Siehe Abschnitt 5. Diese sollten vor der Sensorfreigabe und der Variantenauswahl geklärt werden.

---

## 5. Offene Fragen an den Betrieb (für Janek zusammengestellt)

1. **Toleranzwerte Zylinderform** NiTi und Edelstahl (PH 2.1 [?]). Zusätzlich: Toleranz je Werkstoff mit QM (Aufgabe, Frist 20.11., heute überschritten bzw. offen).
2. **%GRR-Grenze 10 %** bezogen auf welche Toleranzbreite, Herr Baidinger bestätigen (Anf. 2.4).
3. **Taktzeit pro Rohr** (Anf. 4.1, Richtwert offen).
4. **Platzbedarf** L × B (Anf. 5.1, offen).
5. **Zulässige Kontaktwerkstoffe** für Auflage und Führung (PH 3.2, Frist 04.12.).
6. **Bilder** Stents und Marker von Herrn Baidinger (Frist 27.11.).
7. **PH-Freigabe-Datum:** 27.11. laut PH V1.2 oder 04.12. laut Cockpit.
8. **Herstellerangaben** für Ø 1 bis 6,5 mm (Keyence hat die Angabe für Ø 40 mm gemacht).
9. **QM-Vorgaben** ISO 13485 für neues Prüfmittel im Wareneingang.
10. **Lieferprüfprotokolle:** Die Nachreichung bis zu zwei Wochen nach Lieferung (PH Problemstellung) betrifft die Messwerte für den Wareneingang. Klären, ob das Messsystem für die Abnahme gebraucht wird.
11. **Kostenrahmen** (PH 5.3, offen, wird nach dem Konzept erstellt).

---

## 6. Priorisierte Arbeitspakete

Priorität nach Wirkung auf den Abgabezustand. Janek entscheidet, was umgesetzt wird.

1. **Toleranzwerte und %GRR-Grenze klären (hoch).** Die Entscheidungsgrundlage aus 4.1 als Postfach-Entscheidung an Janek übergeben. Ohne diese Werte ist keine Sensorauswahl belastbar.
2. **Messprinzip vorbereiten (hoch).** Entscheidungsgrundlage aus 4.3.
3. **Sensor-Shortlist eingrenzen (hoch).** Vorprüfung 4.2 mit Quellen und Datenblatt-Auszügen. Offene Herstellerfragen als Liste.
4. **Morphologischer Kasten: Lücken aufzeigen (mittel).** Keine Lösungen, nur Lücken und Kriterien (4.4).
5. **Bewertungskriterien für die Variantenauswahl (mittel).** Entwurf nach 4.5, Gewichtung bleibt Janek.
6. **Cockpit an PH V1.2 angleichen (mittel).** Abschnitt 3.2 als Postfach-Vorschläge: Anforderung 2.1 auf Zylinderform, Entscheidung Zylinderform erledigt, PH-Freigabe-Datum, Platzbedarf, Dubletten.
7. **Herstellerfragen formulieren (mittel).** Entwurf, Versand durch Janek.
8. **Gliederung der Dokumentation prüfen (niedrig).** Abgleich mit dem PH-Aufbau, keine Texte schreiben.

**Nicht jetzt:** CAD-Konstruktion, Fertigungszeichnungen, Stückliste und Pläne. Sie hängen an der Variantenauswahl am 11.12.

---

## 7. Termine und Fristen (für die Planung)

- **27.11.2026:** PH-Freigabe laut PH V1.2 (Cockpit: 04.12.). Entscheidungen zu MS 1, Zylinderform, Datumsklärungen und Bilder.
- **04.12.2026:** Cockpit-Frist PH-Freigabe, Taktzeit, Kontaktwerkstoffe.
- **11.12.2026:** Variantenauswahl (PH und Cockpit). Bis dahin: Sensor-Shortlist, Messprinzip, Bewertungskriterien.
- **08.01.2027 (ca.):** gesetzliche Frist finale Aufgabenstellung.
- **15.01.2027:** Konstruktionsfreigabe (PH). Gleichzeitig MS 2 laut Cockpit.
- **19.03.2027:** MS 3 (Projektabschluss, Cockpit).
- **05.03.2027:** Übergabe und Projektabschluss im Betrieb.
- **05.04.2027, 10:00 Uhr:** Abgabe Dokumentation im Sekretariat.
- **17./18.06.2027:** Präsentationsprüfung (je 13 bis 15 Minuten plus Fragen).

---

## 8. Risiken

- **Toleranzen offen:** ohne Toleranzwerte keine belastbare Sensorauswahl und keine %GRR-Prüfung.
- **Messtechnik:** Nur Keyence betrachtet. Die Vorprüfung deutet auf Micro-Epsilon hin, ist aber nicht belegt.
- **Termine:** PH-Freigabe-Datum widersprüchlich. Variantenauswahl am 11.12. ist knapp, wenn die Messtechnik offen bleibt.
- **KI-Anteil:** Teile des Morphologischen Kastens und der Aufgabenstellung stammen von KI. Sie müssen im KI-Logbuch erfasst sein (`fach: true`) und in der Dokumentation ausgewiesen werden. Das Formatvorlage V10 erlaubt KI nur zur sprachlichen Optimierung.
- **Projektplan:** seit 16.10. nicht aktualisiert.
- **Dubletten im Cockpit:** erschweren den Überblick, Bereinigung steht aus.

---

## 9. Ergebnis dieser Sitzung

Am Ende: (a) Postfach-Einträge für alle Vorschläge und KI-Hilfen angelegt, (b) `build.py` ausgeführt, (c) Änderungen auf `main` committet und gepusht, (d) eine kurze Zusammenfassung für Janek im Chat mit den drei wichtigsten Punkten: Toleranzwerte, Messprinzip, Sensor-Shortlist.
