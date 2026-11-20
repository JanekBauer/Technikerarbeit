# Projektstand Technikerarbeit – Janek Bauer

*Stand: 20.11.2026, 13:00 Uhr – gemeinsame Wissensbasis für alle Chats. **Maßgeblich für Status, Termine und Listen ist seit 18.11. das GitHub-Cockpit (Repo `cockpit/daten/*.json`)**; dieses Dokument fasst zusammen. Eingearbeitet: Übergaben Chat 01/02 (bis 06.11.), Chat 05 (19.11.), **MS 1 (20.11.) mit PH V1.2 und AS V4.3 (TA-Allgemein)**.*

> **Hinweis für alle Chats (Stand 13./14.11.):** Für MS 1 gilt eine **neue Versionszählung**: **Bauer_TA_AS_V3.docx (13.11.)** und **Bauer_TA_PH_V1.docx (13.11.)** sind die finalen Fassungen (Entscheidung Janek). Die alte AS V3 vom 30.10. ist verworfen. Inhaltlich entsprechen sie AS V4.2 bzw. PH V8.7 final mit den Änderungen vom 13.11. (s. Sachstand). Die Projektdatei `claude/Aufgabenstellung_Bauer_TA_V4.md` trägt noch den alten Namen ❗.

## Eckdaten
- **Titel (AS V3/V4, gilt laut Entscheidung Janek 30.10.2026, 99 Zeichen):** Konzeption und Konstruktion einer automatisierten Messanlage zur Prüfung von Rohren im Wareneingang
  - Von der FSL festgelegt ist noch AS V2 („Konstruktion und Prozessentwicklung einer automatisierten Messanlage für Nitinol-Rohre“). Wesentliche Änderung → mit Hr. Graudejus de Olio/FSL klären (W5)
- **Betrieb:** BD Gamer Lasertechnik GmbH, Vichystraße 10, 76646 Bruchsal (Stents aus Nitinol und Edelstahl, Marker aus Tantal)
- **Betrieblicher Betreuer:** Paul Baidinger, Technischer Leiter (Paul.Baidinger@bd.com)
- **Schulischer Betreuer:** Björn Graudejus de Olio (Namensänderung nach Heirat, Stand 06.11.2026; privater Teams-Chat)
- **Schule:** Carl-Benz-Schule Karlsruhe, FTM25 (Vollzeit), Abschlussjahrgang 2027
- **Projekttag:** Freitag (bestätigt 30.10.) · **CAD:** SolidWorks (30.10.)
- **Unterlagen lokal:** `C:\_Janek_Bauer\Cloude\Technikerarbeit\`
- **Projekt-Dokumente:** `claude/Aufgabenstellung_Bauer_TA_V4.md` · `claude/TA_Ablage-Regel.md` · Kompendium UP0–UP7 · Chat-Menü · `PH_Aenderungsdoku_und_Fragenliste.md` · `Wochenstatus_TA.md`
- **Ablage:** jede Datei ins TA-Cockpit-Archiv (https://claude.ai/artifact/LZiNTP2ktcUetHv3DgQAVK) + `…\Technikerarbeit\Archiv\` (Regel: `claude/TA_Ablage-Regel.md`); zusätzlich GitHub-Cockpit (seit 17./18.11., Abgleich Repo ↔ Artefakt)
- **Aktuelle Dateien (20.11.):** **AS V4.3** (Bauer_TA_AS_V4.3.docx; gelb offen: Zylinderform) · **PH V1.2** (Bauer_TA_PH_V1.docx; gelb offen: Bild, Toleranzen je Werkstoff, Platzbedarf) · **Projektplan V1 (18.11.)** (Projektplan_Janek_Bauer_V1.pdf + Projektplan.rpj) · MS-1-Fassungen AS V3/PH V1 (13.11.) und V1.1/V3.1 mit Janeks Kommentaren unter `_Versionen` · Sensorvergleich_Datenblaetter_V1.xlsx + 10 Datenblätter (13.11.) · Morpho-Kasten V2 / V2 Janek (12./13.11.) · ältere Fassungen AS V4.2, PH V8.7 final (06.11.) im Archiv · 7 Fotos Rohrspezifikationen (vertraulich, nur im Cockpit-Archiv) · Protokoll_Ersttermin_Baidinger_2026-10-23.docx · Checkliste_MS1_Bauer.docx
  - PC-Archiv am 17.11. vollständig abgeglichen · `claude/PH_Aenderungsdoku_und_Fragenliste.md` nur bis V7 – maßgeblich ist Kap. 6 im PH

## Aktueller Sachstand (PH V8.7 final 06.11. = Basis von PH V1, 13.11.2026)
- **Änderungen PH V1 (13.11.) gegenüber V8.7:** „Rundheit“ → „Ovalität“ (5×), PH-Freigabe 27.11.2026, „Messmaschine“ → „Messanlage“, Anf. 5.1 Platzbedarf F → W; AS V3 (13.11.): „Rundheit“ → „Ovalität“ (2×) (Quelle: Cockpit-Archiv)
- **Anforderungen:** 1.1 F Werkstoff Nitinol/Edelstahl · **1.2 W Tantal** · 1.3 F Länge 1000–3000 mm (Spez. bis 3500 mm) · 1.4 F Ø 1–6,5 mm · 1.5 F Wandstärke n. a. · **2.1 F Ovalität (Ø max − Ø min): NiTi ≤ 0,010 mm, Edelstahl ≤ 0,025 mm** · **2.2 F Außen-Ø ± 13 µm** · 2.3 M Messpunktabstand 2 mm · **2.4 M Reproduzierbarkeit %GRR ≤ 10 %** (AIAG MSA; 10–30 % bedingt) · 2.5 F Auswertung je Messpunkt, keine Mittelwerte · 2.6 W Rauheit · 2.7 W Beschädigung/Kontamination · 3.1 F keine plastische Verformung (σ < 380 MPa NiTi / 690 MPa Edelstahl) · 3.2 F sauber/ölfrei · 3.3 F Durchbiegung verfälscht Messung nicht · 4.1 W Taktzeit (ohne Wert) · 4.2 F manuell einlegen, Messen/Auswerten automatisch · 5.1 W Platzbedarf · berührungslos (Auflage/Führung zulässig) · 230 V + Druckluft (Druck später) · Kostenrahmen später
- **Aus den Rohrspezifikationen (vertraulich, nur sinngemäß verwenden):** Lieferant misst Ø bei NiTi nur an einem Rohrende (4 Punkte à 90°), Edelstahl an ≥ 4 Punkten; Ovalität Edelstahl weder Stichprobe noch COA → Begründung für Messung über die Länge · Werkstoffe: NiTi superelastisch bei RT (Af ≤ 0–5 °C, oberes Plateau ≥ 380 MPa), Edelstahl Rp ≥ 690 MPa · Normen: NiTi ASTM F2633/F2063, Edelstahl ASTM F138, Tantal ASTM F560-22
- **Abgrenzung:** automatisches Zuführen/Einlegen · Programmierung Steuerung/Auswertesoftware · Messmittelfähigkeit am realen System · IT-/QM-Anbindung · **Bestellung/Beschaffung** (Angebote einholen gehört dazu) · Bau/Fertigung/Montage · Inbetriebnahme · Prüfung von Wandstärke, Konzentrizität und Geradheit
- **Umfang:** Konzeption + Konstruktion der Messanlage **und Messprozessentwicklung inkl. Sensorintegration** (Entscheidung 30.10.)
- **Ergebnisse:** SolidWorks-3D-Modell, Fertigungszeichnungen, Stückliste, Pneumatik- und **Elektronikplan**, **Beschreibung des Messprozesses**, **Angebote für Kaufteile**, technische Doku · kein physischer Bau
- **Ist-Zustand (Rundgang 23.10.):** 100-%-Sichtprüfung im WE durch QM; Maßhaltigkeit nur über Lieferantendokumente; Rohrfehler fallen meist erst beim Laserschneiden auf
- **Organisation:** Laptop vom Betrieb, Sicherheitsunterweisung Laser; Ansprechpartner Hr. Baidinger + Team · **Sperrvermerk: nein** · Spezifikationen/interne Dokumente dürfen weder beigefügt noch gezeigt werden, Einzeldaten paraphrasiert (06.11.)
- **Messtechnik (Übergabe Chat 05, 19.11.; Datenstand 07./12.11.):**
  - 19 Geräte aus der Websuche (s01–s19); **maßgeblich ist der Sensorvergleich im Cockpit aus den Datenblättern (26 Sensoren, 17./18.11.; Entscheidung e23)**
  - Shortlist Messprinzipien: **A** Laser-Scan-Mikrometer 2 Achsen (Sikora 6020/2010 XY, Mitutoyo LSM-501S) · **B** LED-Schattenwurf (Micro-Epsilon ODC 2700-10, Keyence LS-9030M/D) · **C** Profilprojektor (Keyence TM-X5040) · **D** schwenkender Messkopf, Rohr ruht (Zumbach DVO 2 + ODAC, Daten offen) · **E** Mehrachs-Sensor, Rohr steht (Nordson AccuScan 6012) · **F** vertikal mit 360°-Drehung (Konzeptvorbild LaserLinc Metron, Zumbach QC 2) · **G** konfokal-chromatisch (zweitrangig) · **H** Wirbelstrom (nur Fehler, Anf. 2.7)
  - Vorläufiger Abgleich nach **Annahme** Messunsicherheit ≤ 1/10 Toleranz (Ø ≤ 2,6 µm, Ovalität NiTi ≤ 1 µm) – nicht vom Betrieb bestätigt, KI-Bewertung; eigene Bewertung in Chat 07
  - Neue Erkenntnisse: Herstellerwerte zur Wiederholbarkeit sind fast immer gemittelt (1024/2048-fach) → Konflikt mit 2.5 „keine Mittelwerte“ (q16) · bei 2 Messachsen kann Ovalität unter 45° unentdeckt bleiben (q17) · Taktzeit 3 m ÷ 2 mm ≈ 1500 Querschnitte, bei Annahme 1,5 s ≈ 37 min/Rohr → Helix-Frage (q02)

## MS 1 (20.11.2026) – Ergebnisse (Notizen Janek, umgesetzt in PH V1.2 / AS V4.3)
- „Ovalität“ → **„Zylinderform“** (PH 8×, AS 3×); Messgröße/Definition offen – Formel Ø max − Ø min passt nicht mehr (q17)
- Toleranzen je Werkstoff, i.O./n.i.O. je Messpunkt, **mit dem QM erarbeiten** (t-toleranzen-qm) · **Tantal ohne Toleranz** · **Rohrlänge 1–3 m endgültig** · **CE-normgerechte Konstruktion** · Platzbedarf offen · Taktzeit-Reduzierung erwünscht · Laserschneide-Satz entfernt · Problemstellung mit Bildern (Stents/Marker von Hr. Baidinger)
- Helix-Abtastung (q02): „nein“ (Janek, 20.11.)
- ⚠️ Formulierungen in PH V1.2/AS V4.3 hat die KI nach Janeks Vorgaben eingesetzt (KI-Logbuch, fachlich) – selbst prüfen
- ❗ Versionsnummern: AS V3 (13.11.) → V3.1 → **V4.3** – Zählung vor der finalen Unterschrift vereinheitlichen

## ⚠️ Widersprüche (Stand 19.11.; Pflege im TA-Cockpit, Sammlung „conflicts“)
- ✅ geklärt: W0–W3 · W14, W15, W16 (19.11., Janek) · W4 (18.11., Janek) · W6 · W7 (18.11.: Sensorvergleich deckt 6,5 mm ab; LS-9006/TM-X5006 ausgeschlossen) · W8 (18.11., Janek) · W13 (18.11., Janek)
- **W5** AS bei FSL nicht bestätigt (festgelegt ist V2) → MS 1 am 20.11.
- **W10** %GRR ≤ 10 % bei Ovalität 0,010 mm ⇒ Streuung (6σ) ≲ 1 µm; Wert aus KI-Websuche → Betrieb bestätigen (q03)
- **W11** %GRR vs. abgegrenzte Messmittelfähigkeit → rechnerischer Nachweis (t-grr-abschaetzung)
- **W12** 3.1/3.3 F-Anforderungen ohne Auslegungsberechnungen
- **W14** kein Sperrvermerk vs. vertrauliche Werte
- **W15** Tantal-Spezifikation Rundheit max. 0,005 mm, im PH kein Wert
- **W16** Prüfanweisung Edelstahl ab 700 mm, PH ab 1000 mm
- **Regel (Janek, 19.11., e23):** Bei Abweichungen zwischen Chat-Übergaben und Cockpit gelten die Cockpit-Daten → keine neuen W-Einträge. Daraus folgt: maßgeblich sind der Sensorvergleich im Cockpit (26 Sensoren) und die Termine laut PH V1. Die Mittelung bei 2.5 wird als Frage geklärt (q16).

## Termine
| Termin | Datum | Status |
|---|---|---|
| Kick-off Betrieb | 23.10.2026 | ✅ |
| Klärungsgespräch Hr. Baidinger | 30.10.2026 | ✅ |
| **MS 1 – Planung/Vorbereitung** | **Fr. 20.11.2026, 9:30–10:30 Uhr** | ✅ stattgefunden |
| **Betrieblich: PH-Freigabe + Unterschrift** | **Fr. 27.11.2026** (Entscheidung Janek 13.11., steht im PH V1) | geplant |
| Finale AS (unterschrieben, PDF + DOCX an FSL) | ca. 30.11.2026 (2 Wo. nach MS 1 → prüfen); gesetzl. Frist 08.01.2027 | offen |
| Betrieblich: Variantenauswahl | **Fr. 11.12.2026** (festgelegt 18.11.) | Bestätigung Baidinger mit PH-Unterschrift |
| Betrieblich: Konstruktionsfreigabe | **Fr. 15.01.2027** (festgelegt 18.11.) | Bestätigung Baidinger mit PH-Unterschrift |
| MS 2 – Durchführung | **15.01.2027** (festgelegt 18.11.) | schriftlich sichern |
| Betrieblich: Übergabe/Projektabschluss | **05.03.2027** (festgelegt 18.11.) | |
| MS 3 – Abschluss | **19.03.2027** (festgelegt 18.11.) | |
| **Abgabe Dokumentation** | **Mo. 05.04.2027, 10:00 Uhr** | |
| Präsentationsprüfung | Do./Fr. 17./18.06.2027 | |

## Stand der Arbeitspakete
| AP | Ampel | Stand |
|---|---|---|
| Aufgabenstellung | 🟡 | AS V3 (MS 1 final, 13.11.); offen: FSL-Prüfung (W5), Unterschriften |
| Pflichtenheft | 🟡 | PH V1 (MS 1 final, 13.11.); offen: Freigabe 27.11., Rest-Formfehler, W10–W12, W14–W16, Präzisierung 2.5 |
| Projektplan (Rillsoft) | 🟡 | 13.11. aktualisiert; weicht vom PH V1 ab → anpassen (gilt: PH, e19); neuer Vorgang „Angebote Sensorik“ |
| Lösungsansätze (PDF) | 🟡 | Shortlist A–H aus Chat 05 als Grundlage; PDF für MS 1 nicht belegt |
| MS-1-Termin | 🟢 | Fr. 20.11., 9:30 Uhr fest |
| Messtechnik-Recherche (05) | 🟡 | Übergabe 19.11.: Recherche weitgehend erledigt; offen: Datenblätter gegenprüfen, Zumbach, Angebote, %GRR-Abschätzung; maßgeblich ist der Sensorvergleich im Cockpit |
| Spann-/Handhabung (06) | 🟡 | Morpho-Kasten V2 / V2 Janek; Gesamtvarianten fehlen; Kernfrage aus Chat 05: Rohr dreht oder Sensor schwenkt |
| Bewertung (07) | ⬜ | Shortlist bewerten bis 04.12. |
| Messprozess/Sensorintegration (09 Teil A) | ⬜ | nach Variantenwahl |
| Dokumentation (10) | ⬜ | Gliederungsentwurf 19.10.; Doku-Speicher nicht belegt |

## Entscheidungen (Datum – Entscheidung – Quelle)
| Datum | Entscheidung | Quelle |
|---|---|---|
| bis 29.10. | MS 1 → ca. Mitte Nov., MS 2 → ca. Mitte Feb. (MS finden statt, vorher absprechen) | Hr. Graudejus (mündl./Teams) – schriftlich sichern |
| 30.10. | Projekttag Freitag; CAD SolidWorks | Gespräch Hr. Baidinger |
| 30.10. | Automatisierungsgrad: manuell einlegen, Messen + Auswerten automatisch; Zuführung nicht Bestandteil | Gespräch Hr. Baidinger |
| 30.10. | Werkstoffe Nitinol/Edelstahl/Tantal; Länge 1–3 m; Ø 1,0–6,5 mm; berührungslos; Messpunkte max. 2 mm | Gespräch Hr. Baidinger |
| 30.10. | Abgrenzung bestätigt (Software/Steuerung, Messmittelfähigkeit, IT/QM, Bau, Inbetriebnahme) | Gespräch Hr. Baidinger |
| 30.10. | Titel AS V3 gilt, auch im PH | Janek (Cockpit) – FSL/Graudejus informieren |
| 30.10. | Angebote für Kaufteile = Ergebnis; Bestellung/Beschaffung = Abgrenzung | Janek (Cockpit), deckt sich mit Ausschreibung |
| 30.10. | **Messprozessentwicklung inkl. Sensorintegration gehört zum Umfang** | Janek (Cockpit) |
| 30.10. | Kein physischer Bau | AS |
| 30.10. | Schulische MS aus dem PH entfernt; betriebliche MS bleiben im PH | Chat 02 (UP0) |
| 30.10. | Auslegungsberechnungen als Ergebnis gestrichen | Janek, PH V5 – ❗ prüfen (W12) |
| 03.11. | Hr. Baidinger möchte keine Gesprächsprotokolle | Janek |
| 05.11. | PH-Änderungsdoku (Kap. 6) beginnt mit V7; interne Historie V1–V7 in `claude/PH_Aenderungsdoku_und_Fragenliste.md` | Janek (Chat 02) |
| 06.11. | Betriebl. MS: Variantenauswahl 04.12. · Konstruktionsfreigabe 22.01. · Übergabe 26.02. | Janek (Chat 02) |
| 06.11. | Anforderungen aus Rohrspezifikationen: Ovalität, Ø ± 13 µm, keine Mittelwerte, Tantal nur W; Wandstärke/Konzentrizität/Geradheit abgegrenzt | Chat 02 / Rohrspezifikationen / Janek |
| 06.11. | %GRR ≤ 10 % als Reproduzierbarkeit | Janek (Wert aus Websuche AIAG MSA) – ❗ Betrieb bestätigen |
| 06.11. | Elektronikplan = Schaltplan Pneumatik + E-Plan, keine Programmierung | Janek (Cockpit) |
| 06.11. | Folge/Kosten der Rohrfehler nicht mehr nötig | Janek (Cockpit) |
| 06.11. | Kein Sperrvermerk; Spezifikationen nicht beifügen/zeigen, nur paraphrasieren | Janek/Betrieb |
| 12.11. | **Annahme** Abgleich-Maßstab Messgeräte: Messunsicherheit ≤ 1/10 Toleranz (e22) | Janek/Claude (Chat 05) – nicht vom Betrieb |
| 13.11. | PH-Freigabe + Unterschrift auf **27.11.** verschoben | Janek (PH V1) |
| 19.11. | Bei Abweichungen Chat-Übergabe ↔ Cockpit gelten die Cockpit-Daten (e23) | Janek (Chat 00) |
| 13.11. | Neue Versionszählung: AS V3 + PH V1 sind die finalen MS-1-Fassungen; PH Kap. 6 auf Stand 0 | Janek |
| 14.11. | Alte AS V3 (30.10.) verworfen; AS V3 vom 13.11. ist die Originalfassung | Janek (e20) |
| 14.11. | Bei Terminabweichungen gelten die Daten aus dem PH V1; Projektplan wird angepasst | Janek (e19) |
| 14.11. | MS 1 am Fr. 20.11.2026, 9:30–10:30 Uhr | Janek / Hr. Graudejus de Olio (e21) |

## Offene Punkte (wer – bis wann, Stand 19.11.; identisch mit Cockpit)
| # | Punkt | Wer | Bis |
|---|---|---|---|
| 1 | **MS 1 vorbereiten:** AS V3, PH V1, Projektplan (an PH angepasst), Lösungsansätze (Shortlist A–H) als PDF, KI-Logbuch | Janek (Chat 04/05/03) | **Do. 19.11.** |
| 2 | **MS 1:** FSL-Prüfung AS V3 (W5), KI-Anteil offenlegen, MS-Verschiebung schriftlich, MS 3 Mitte März? | Janek ↔ Graudejus de Olio | **Fr. 20.11., 9:30** |
| 3 | Fragen an Hr. Baidinger (Prio 1): 2 mm/Helix (q02), %GRR ≤ 10 % (q03), **Mittelung 2.5 (q16)**, **Ovalitätsdefinition (q17)** | Janek → Baidinger | Fr. 20.11. |
| 4 | Projektplan Rillsoft an PH V1 anpassen + Vorgang „Angebote Sensorik“ → PDF (t15) | Janek (Chat 03) | Fr. 20.11. |
| 5 | PH-Freigabe + Unterschrift; dabei bestätigen: Spezifikationswerte, betriebl. MS, Vertraulichkeit (W14); Taktzeit-Richtwert (q04) | Janek/Baidinger | **Fr. 27.11.** |
| 6 | PH vorher: Rest-Formfehler, Inhaltsverzeichnis, W11, W12, W15, W16, ggf. 2.5 präzisieren | Janek (Chat 02) | 27.11. |
| 7 | Originaldatenblätter Shortlist gegenprüfen + Quellenverzeichnis ins Archiv | Janek (Chat 05) | 27.11. |
| 8 | Zumbach anfragen (ODAC-Köpfe für DVO 2) · Angebote Sensorik anfragen | Janek (Chat 05) | 27.11. |
| 9 | Kontaktstellen/Kontaktwerkstoffe klären | Janek/Baidinger (Chat 06) | 27.11. |
| 10 | %GRR/Messunsicherheit rechnerisch abschätzen (W11) | Janek (Chat 05/07) | 04.12. |
| 11 | Shortlist bewerten → Variantenauswahl im Betrieb | Janek (Chat 06/07) | 04.12. |
| 12 | Finale AS V3 unterschreiben → PDF + DOCX an FSL | Janek | ca. 30.11. (gesetzl. Frist 08.01.2027) |
| 13 | Druckluftdruck (q11), Kostenrahmen | Baidinger | 15.01.2027 |

*Erledigt 07.–19.11.: Chat-Menü Abschnitt A (07.11.) · MS-1-Termin vereinbart (14.11.) · PH-Freigabetermin im PH (13.11.) · AS/PH „Ovalität“ vereinheitlicht · Projektplan 13.11. exportiert · Tantal-Spezifikation (q12) · PC-Abgleich (17.11.) · W4, W7, W8, W13 (18.11.) · Übergabe Chat 05 (19.11.).*

## Aufgaben laut Ausschreibung (Betrieb, 02.07.2026)
1. Analyse der Prüfanforderungen · 2. Messmerkmale und Randbedingungen · 3. Recherche Messverfahren/-prinzipien · 4. Technische Bewertung der Konzeptvarianten · 5. CAD-Konstruktion · 6. Handhabungs- und Spannkonzept · 7. Technische Doku inkl. Funktionsbeschreibung und Konstruktionsunterlagen

## KI-Nutzungs-Logbuch
| Datum | Chat | Zweck | Art der Hilfe |
|---|---|---|---|
| 16.10. | – | Projektplan, Pflichtenheft | Feedback Projektplan; PH-Gerüst aus Schulvorlage (Inhalte aus AS, offene Punkte markiert) |
| 19.10. | Allgemein/00 | Organisation | Kompendium UP0–UP7, Chat-Menü, Projektstand, Status-Übersicht |
| 20.10. | 00 | Vorbereitung Betrieb | Checkliste/Fragensammlung Ersttermin |
| 22.10. | 00 | Vorbereitung Betrieb | Word-Vorlage Gesprächsprotokoll |
| 24.10. | 02 | Pflichtenheft Kap. 2 | Prüfung PH-Entwurf (Feedback); Einarbeitung Janeks Angaben zum Ist-Zustand; Änderungsdoku + Fragenliste |
| 30.10. | 02 | Anforderungsliste | Fragenkatalog (Excel) nach Hauptmerkmalliste Pahl/Beitz |
| 30.10. | 02 | PH V3–V6 | Einarbeitung von Janeks Notizen/Entscheidungen, Konsistenzprüfung, sprachliche Überarbeitung eines Absatzes, Kap. 6 aus bestehender Liste |
| 30.10. | 01 | Aufgabenstellung | Kritik AS V2; ⚠️ **Ausformulierung von Titel, Problemstellung und Ziel der AS V3 durch KI** auf Basis von Janeks Notizen und PH V5 |
| 30.10. | 01 | Aufgabenstellung | Übertragung in die Word-Vorlage, Formatierung, Logo |
| 30.10. | 05 | Messtechnik | Normbegriffe (ISO 1101/12181/14405/10579); Abgleich Lösungsidee mit PH V5 und Keyence-Katalogen; Denkfragen |
| 30.10. | 00 | Projektsteuerung | Checkliste MS 1 (Word); Statusabgleich; Prompts für AS V3/PH V6 |
| 05.11. | 02 | PH V7 | ⚠️ **Vorschlag der Termine für zwei betriebliche MS (KI-Vorschlag, gekennzeichnet)**; Umsetzung von Janeks Entscheidungen |
| 05.11. | 00 | Projektsteuerung | Prüfung Übergabe Chat 02; Widerspruchsprüfung, Einträge im TA-Cockpit |
| 06.11. | 02 | Rohrspezifikationen / PH V8–V8.7 | Auswertung der Spezifikationen; Eintragen von Daten und Entscheidungen, **sprachliche Formulierung einzelner Anforderungen** |
| 06.11. | 02 | Anf. 2.4 | ⚠️ **Websuche Standardwerte MSA (AIAG %GRR) – Wert stammt aus KI-Recherche** |
| 05./06.11. | 01 | AS V3.1/V4 | ⚠️ **AS V4 von der KI aus PH V8.7 abgeleitet und formuliert** (auf Anweisung) |
| 06.11. | 00 | Projektsteuerung | Projektabgleiche inkl. Status aller Cockpit-Sammlungen |
| 07.11. | 00 | Chat-Menü | Abschnitt A + Pfade aktualisiert (Organisation) |
| 07.11. | 05 | Messtechnik | ⚠️ Hersteller- und Produktrecherche per Websuche, Auswertung von Datenblättern/Katalogen (19 Geräte) |
| 07./12.11. | 06 | Morpho-Kasten V1/V2 | ⚠️ **Lösungsideen je Teilfunktion als „KI-Vorschlag“** (auf Janeks Wunsch, gekennzeichnet) |
| 12.11. | 05 | Abgleich Messgeräte ↔ PH | ⚠️ **Vergleich und vorläufige Bewertung durch die KI nach Faustregel (Annahme 1/10 Toleranz)** – eigene Bewertung in Chat 07 |
| 13.11. | 05/06 | Sensorvergleich V1 | ⚠️ Werte aus Janeks Datenblättern von der KI abgelesen – am Original prüfen |
| 17./18.11. | 00 | Cockpit/GitHub | Sensorliste aus Datenblättern übertragen (ohne Bewertung), GitHub-Cockpit, Abgleich-Skripte (Organisation) |
| 17.11. | 00 | Projektsteuerung | Projektabgleich, PC-Abgleich Archiv |
| 19.11. | 05/00 | Übergabe Chat 05 | Strukturierung des Übergabeblocks; Einarbeitung ins Cockpit und in den Projektstand |
| 20.11. | Allgemein | PH V1.2 / AS V4.3 | ⚠️ MS-1-Notizen und Kommentare nach Janeks Vorgaben ins PH/die AS eingearbeitet (Formulierungen KI) |
| 20.11. | 00 | Projektsteuerung | Projektabgleich, PC-Ablage, Nachtrag ins GitHub-Cockpit |
