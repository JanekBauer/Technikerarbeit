# Chat-Menü Technikerarbeit – Janek Bauer

*Stand: 07.11.2026 (Abschnitt A und Dateipfade auf AS V4 / PH V8.7 aktualisiert; erste Fassung 19.10.2026) · Prompt-Bibliothek für alle Abschnitts-Chats im Projekt „Technikerarbeit“*

> Archiv-Hinweis (20.11.2026): Prompt-Bibliothek aus dem claude.ai-Projekt. Termine und Fassungen in Abschnitt A sind überholt (siehe `cockpit/daten/deadlines.json`, AS V4.3, PH V1.2). Bei Weiterverwendung die Pfade `claude/…` durch `projekt/claude-projekt/…` ersetzen.

So funktioniert es:
1. Für jeden Abschnitt einen **neuen Chat im Projekt „Technikerarbeit“** öffnen und den passenden Prompt (Codeblock) komplett hineinkopieren. Bestehende Chats 00–11 weiterverwenden – der Startblock sorgt dafür, dass sie den aktuellen Stand lesen.
2. Jeder Chat liest zuerst die Projekt-Dokumente (`claude/Projektstand_TA_Bauer.md`, `claude/Aufgabenstellung_Bauer_TA_V4.md`, `claude/Unterstuetzungsprogramm_UP0-UP7_Kompendium.md`, dieses Menü). Gibt es eine neuere AS-Datei (`claude/Aufgabenstellung_Bauer_TA_V*.md`), gilt immer die höchste Versionsnummer.
3. Jeder Chat endet mit einem **Übergabeblock** (festes Format, siehe unten).
4. Den Übergabeblock kopierst du in den **Chat 00 „Cockpit“**. Das Cockpit aktualisiert daraus `claude/Projektstand_TA_Bauer.md` und das TA-Cockpit-Artefakt → der nächste Chat startet auf dem neuesten Stand.
5. Jede Datei (AS, PH, Protokolle …) wird nach `claude/TA_Ablage-Regel.md` im Cockpit-Archiv und im PC-Ordner abgelegt.

---

## A. Projektdaten (Wissensbasis für alle Chats, Stand 07.11.2026)

Maßgeblich für Details ist immer `claude/Projektstand_TA_Bauer.md` (aktueller als dieses Menü).

### A.1 Eckdaten
| | |
|---|---|
| Titel (AS V4.2, Entwurf; FSL-Prüfung offen) | Konzeption und Konstruktion einer automatisierten Messanlage zur Prüfung von Rohren im Wareneingang |
| Von der FSL festgelegt (AS V2, nur Archiv) | Konstruktion und Prozessentwicklung einer automatisierten Messanlage für Nitinol-Rohre |
| Titel Ausschreibung (02.07.2026) | Konzeption und Konstruktion einer Messvorrichtung zur Prüfung von Nitinol-Rohren im Wareneingang |
| Betrieb | BD Gamer Lasertechnik GmbH, Vichystraße 10, 76646 Bruchsal (Stents aus Nitinol und Edelstahl, Marker aus Tantal) |
| Betrieblicher Betreuer | Paul Baidinger, Technischer Leiter (möchte keine Gesprächsprotokolle) |
| Schulischer Betreuer | Björn Graudejus de Olio (Kommunikation per privatem Teams-Chat) |
| Klasse | FTM25 (Vollzeit), Abschlussjahrgang 2027, Carl-Benz-Schule Karlsruhe |
| Projekttag | freitags im Betrieb (bestätigt 30.10.) |
| CAD | SolidWorks |
| Physischer Bau | entfällt (Konzeption, CAD, Messprozess, Unterlagen, Doku) |
| Sperrvermerk | nein – Rohrspezifikationen und interne Dokumente nicht beifügen/zeigen, nur sinngemäß verwenden |
| Cockpit | TA-Cockpit-Artefakt https://claude.ai/artifact/LZiNTP2ktcUetHv3DgQAVK (offene Punkte, Fragen, Termine, Anforderungen, Widersprüche, KI-Logbuch, Archiv) |

### A.2 Aufgabenstellung V4.2 (Datei `claude/Aufgabenstellung_Bauer_TA_V4.md`)
- **Problem:** Im Wareneingang nur Sichtprüfung; Rundheit/Maßhaltigkeit werden aus Lieferantendokumenten übernommen, die die Geometrie nur an einzelnen Stellen erfassen → Abweichungen fallen meist erst beim Laserschneiden auf.
- **Ziel:** fertigungsreife Konstruktion einer Messanlage für Nitinol- und Edelstahl-Rohre (1–3 m, Ø 1,0–6,5 mm), manuell einlegen, automatisch und berührungslos auf Außen-Ø und Ovalität prüfen; Tantal wünschenswert. Erreicht, wenn die F- und M-Anforderungen des freigegebenen PH nachweislich erfüllt sind.
- **Übergabe:** SolidWorks-3D-Modell, Fertigungszeichnungen, Stückliste, Pneumatik- und Elektronikplan, Beschreibung des Messprozesses inkl. Sensorkonzept, Funktionsbeschreibung, Angebote für Kaufteile, technische Dokumentation.
- ⚠️ Titel, Problemstellung und Ziel von V3/V4 wurden von der KI formuliert (KI-Logbuch) → selbst prüfen/überarbeiten.

### A.3 Ausschreibung des Betriebs (02.07.2026)
- Rohre Ø 1,0–6,5 mm, max. 3,0 m · Aufgaben: (1) Prüfanforderungen analysieren · (2) Messmerkmale und Randbedingungen · (3) Messverfahren/-prinzipien recherchieren · (4) Konzeptvarianten technisch bewerten · (5) CAD-Konstruktion · (6) Handhabungs- und Spannkonzept · (7) technische Doku inkl. Funktionsbeschreibung und Konstruktionsunterlagen · Ergebnisse: Fertigungszeichnungen, Stückliste, Angebote

### A.4 Pflichtenheft V8.7 final (für MS 1, 06.11.2026)
- **Anforderungsliste:** 1.1 F Werkstoff Nitinol/Edelstahl · 1.2 W Tantal · 1.3 F Länge 1000–3000 mm · 1.4 F Ø 1–6,5 mm · 1.5 F Wandstärke n. a. · 2.1 F Ovalität (Ø max − Ø min) NiTi ≤ 0,010 mm / Edelstahl ≤ 0,025 mm · 2.2 F Außen-Ø ± 13 µm · 2.3 M Messpunktabstand 2 mm · 2.4 M Reproduzierbarkeit %GRR ≤ 10 % (Bestätigung Betrieb offen) · 2.5 F Auswertung je Messpunkt, keine Mittelwerte · 2.6 W Rauheit · 2.7 W Beschädigung/Kontamination feststellen · 3.1 F keine plastische Verformung (σ < 380 MPa NiTi / 690 MPa Edelstahl) · 3.2 F sauber/ölfrei · 3.3 F Durchbiegung verfälscht die Messung nicht · 4.1 W Taktzeit (ohne Wert) · 4.2 F manuell einlegen, Messen/Auswerten automatisch · 5.1 Platzbedarf
- **Abgrenzung:** automatisches Zuführen · Programmierung Steuerung/Auswertesoftware · Messmittelfähigkeit am realen System · IT-/QM-Anbindung · Bestellung/Beschaffung (Angebote einholen gehört dazu) · Bau, Montage, Inbetriebnahme · Prüfung von Wandstärke, Konzentrizität, Geradheit
- **Rahmen:** berührungslos (Auflage/Führung zulässig) · 230 V + Druckluft (Druck später) · Kostenrahmen später · QM-Vorgaben ISO 13485 im Projektverlauf
- **Änderungsdoku:** Kap. 6 im PH (ab V8.4); interne Historie bis V7 in `claude/PH_Aenderungsdoku_und_Fragenliste.md`

### A.5 Termine (Projektplan Rillsoft noch auf Stand 16.10. – muss angepasst werden)
| Termin | Datum |
|---|---|
| MS 1 – Planung/Vorbereitung (Terminanfrage bis 09.11.) | ca. Mo. 16.11.2026 |
| Betrieblich: PH-Freigabe + Unterschrift | Fr. 20.11.2026 |
| Finale AS unterschrieben an FSL | ca. 30.11.2026 (gesetzl. Frist 08.01.2027) |
| Betrieblich: Variantenauswahl | Fr. 04.12.2026 |
| Betrieblich: Konstruktionsfreigabe | Fr. 22.01.2027 |
| MS 2 – Durchführung | ca. Mitte Feb. 2027 (verschoben, mit s. B. abgesprochen) |
| Betrieblich: Übergabe/Projektabschluss | Fr. 26.02.2027 |
| MS 3 – Abschluss | Mitte März 2027 |
| **Abgabe Dokumentation** | **Mo. 05.04.2027, 10:00 Uhr** |
| Präsentationsprüfung | Do./Fr. 17./18.06.2027 |

### A.6 Offene Widersprüche (Stand 07.11., Pflege im Cockpit)
W4 „fertigungsreif“ im PH-Ziel? · W5 AS V4 bei FSL nicht bestätigt · W6 betriebl. MS in Rillsoft fehlen · W7/W10 Messbereich und %GRR ≤ 10 % (Streuung < 1 µm) – Machbarkeit · W8 Selbstständigkeitserklärung (V10: KI nur sprachlich) vs. KI-formulierte AS · W11 %GRR vs. abgegrenzte Messmittelfähigkeit · W12 3.1/3.3 ohne Auslegungsberechnungen · W13 Rohre > 3 m · W14 kein Sperrvermerk vs. vertrauliche Werte

---

## B. Spielregeln, die in jedem Prompt stecken

**Startblock** (ist in jedem Prompt enthalten):
- Lies zuerst `claude/Projektstand_TA_Bauer.md`, `claude/Aufgabenstellung_Bauer_TA_V4.md` (bzw. die neueste `claude/Aufgabenstellung_Bauer_TA_V*.md`), `claude/Unterstuetzungsprogramm_UP0-UP7_Kompendium.md` und `claude/TA_Chat-Menue_Prompts.md` (Abschnitt A).
- Fasse mir in 3–5 Zeilen zusammen, was für diesen Abschnitt schon feststeht und was offen ist, bevor du loslegst.
- Arbeite als sokratischer Mentor: Fragen stellen, Feedback geben, mich selbst denken lassen. Fachliche Inhalte der Dokumentation schreibe ich selbst.
- Wenn du einen Widerspruch zu früheren Festlegungen siehst, sag es sofort.

**Übergabeblock** (jeder Chat endet damit, auf mein Kommando „Übergabe“):
```
### ÜBERGABE – Chat [Nr. Name] – [Datum]
**Erledigt / Entscheidungen:** …
**Neue Fakten (Quelle: wer hat es gesagt / Dokument):** …
**Geänderte Werte / Anforderungen:** …
**Offene Punkte + Verantwortlicher + Termin:** …
**Erstellte/geänderte Dateien:** …
**Auswirkung auf Projektplan:** …
**Nächster Chat / nächster Schritt:** …
**KI-Nutzung (für Logbuch/Anhang):** Datum – Zweck – Art der Hilfe
```

---

## C. Die Chats (Prompts zum Kopieren)

Reihenfolge = Projektablauf. Chat 00 läuft dauerhaft daneben, Chat 10 (Doku) läuft prozessbegleitend.

| Nr. | Chat | Phase / UP | Wann |
|---|---|---|---|
| 00 | Cockpit – Projektsteuerung | alle | dauerhaft |
| 01 | Klärung mit dem Betrieb & finale Aufgabenstellung | Phase 1 / UP1 | bis finale AS (ca. 30.11.) |
| 02 | Pflichtenheft & Anforderungsliste | Phase 1 / UP3 | bis PH-Freigabe 20.11., danach bei Änderungen |
| 03 | Projektplan Rillsoft | UP2 | jetzt (bis 09.11.), danach zu jedem MS |
| 04 | Meilenstein-Vorbereitung (M1, M2, M3) | schulisch | vor jedem MS (MS 1 ca. 16.11.) |
| 05 | Messtechnik-Recherche & Messprinzipien | Phase 2 / UP4 | Nov. |
| 06 | Spann- & Handhabungskonzept | Phase 2 / UP4 | Nov. |
| 07 | Konzeptbewertung & Variantenauswahl | Phase 2 / UP4 | bis 04.12. |
| 08 | CAD-Konstruktion & Auslegungsberechnungen | Phase 3 / UP4 | Dez. – 22.01. |
| 09 | Messprozess, Sensorintegration & technische Unterlagen | Phase 3 + 5 / UP4 + UP6 | Jan. – 26.02. |
| 10 | TA-Dokumentation (prozessbegleitend) | UP5 | ab jetzt bis 05.04. |
| 11 | Präsentationsprüfung | UP7 | Mai–Juni |

---

### Chat 00 – Cockpit / Projektsteuerung
```
Chat 00 – COCKPIT meiner Technikerarbeit.

Lies zuerst: claude/Projektstand_TA_Bauer.md, claude/Aufgabenstellung_Bauer_TA_V4.md (bzw. die neueste AS-Datei), claude/Unterstuetzungsprogramm_UP0-UP7_Kompendium.md, claude/TA_Ablage-Regel.md und claude/TA_Chat-Menue_Prompts.md (Abschnitt A + B). Das TA-Cockpit-Artefakt (https://claude.ai/artifact/LZiNTP2ktcUetHv3DgQAVK) pflegst du mit.

Deine Rolle: Projektleitungs-Coach und „Gedächtnis“ meines Projekts. Alle anderen Chats (01–11) liefern dir Übergabeblöcke.

Deine Aufgaben:
1. Wenn ich einen Übergabeblock einfüge: prüfe ihn auf Widersprüche zu bisherigen Festlegungen (AS, Pflichtenheft, Projektplan, Ausschreibung), frag nach, wenn etwas unklar ist, und aktualisiere dann Projektstand_TA_Bauer.md und das Cockpit.
2. Führe eine Liste: offene Punkte (wer, bis wann), Entscheidungen mit Datum und Quelle, Termine (schulisch + betrieblich), KI-Nutzungs-Logbuch.
3. Sag mir bei jedem Kontakt, welche Frist als Nächstes kommt (Termine laut Projektstand) und welcher Chat jetzt dran ist.
4. Wenn ich „Status“ schreibe: Ampelübersicht aller Arbeitspakete + die drei wichtigsten nächsten Schritte. Für einen vollständigen Abgleich gibt es den Skill /ta-projektabgleich.
5. Achte auf die Bewertungskriterien (Vorgehen 40 %, Ausarbeitung 30 %, Projektverlauf 30 %) und weise mich darauf hin, wo ich Punkte verliere (z. B. Selbstständigkeit, Meilensteine, Pflichtenheft als Werkzeug).

Starte mit einer Status-Übersicht auf Basis der Dokumente.
```

### Chat 01 – Klärung mit dem Betrieb & finale Aufgabenstellung
```
Chat 01 – KLÄRUNG MIT DEM BETRIEB & FINALE AUFGABENSTELLUNG (Phase 1, UP1).

Startblock: Lies claude/Projektstand_TA_Bauer.md, claude/Aufgabenstellung_Bauer_TA_V4.md (bzw. die neueste AS-Datei), claude/Unterstuetzungsprogramm_UP0-UP7_Kompendium.md (Kap. 2 + 5.2 Phase 1) und claude/TA_Chat-Menue_Prompts.md (Abschnitt A). Fasse den Stand kurz zusammen.

Kontext: Festgelegt ist bei der FSL noch AS V2. Mein aktueller Entwurf ist AS V4.2 (an PH V8.7 angeglichen). Die finale AS muss ca. bis 30.11. unterschrieben (b. B. + Firmenstempel, s. B., ich) als PDF + DOCX an die FSL; gesetzliche Frist 08.01.2027.

Ziel dieses Chats:
1. Prüfe mit mir, ob Titel (max. 100 Zeichen, Substantivierung einer Tätigkeit), Problemstellung (Umfeld + wie macht sich das Problem bemerkbar, KEINE Lösungen/Ziele) und Ziel (Kriterien der Zielerreichung + Form der Übergabe, KEINE Handlungen) den UP1-Regeln entsprechen. Gib Feedback, formuliere nicht für mich um – ich überarbeite die Texte selbst (KI-Regel der Formatvorlage V10).
2. Achte auf Übereinstimmung mit dem aktuellen Pflichtenheft (Begriffe, Werkstoffe, Ergebnisse).
3. Kläre mit mir, ob die Änderungen gegenüber V2 eine erneute Prüfung durch die FSL brauchen, und was ich Herrn Graudejus de Olio dazu schreibe.

Beende den Chat auf mein Kommando „Übergabe“ mit dem Übergabeblock aus Abschnitt B.
```

### Chat 02 – Pflichtenheft & Anforderungsliste
```
Chat 02 – PFLICHTENHEFT & ANFORDERUNGSLISTE (Phase 1, UP3).

Startblock: Lies claude/Projektstand_TA_Bauer.md, claude/Aufgabenstellung_Bauer_TA_V4.md (bzw. die neueste AS-Datei), claude/Unterstuetzungsprogramm_UP0-UP7_Kompendium.md (Kap. 4 und 5.4 Pahl/Beitz 6.2) und claude/TA_Chat-Menue_Prompts.md (Abschnitt A.4 = Stand PH V8.7). Fasse den Stand zusammen und übernimm alle Ergebnisse aus den letzten Übergaben.

Ziel: Pflichtenheft für die betriebliche PH-Freigabe mit Unterschrift (20.11.2026) und als gepflegtes Werkzeug bis zum Projektende.

Arbeitsweise:
1. Gehe die Kapitel der Schulvorlage durch (Abkürzungen, Problemstellung/Ist-Zustand, Ziel/Soll-Zustand, Anforderungsliste, Abgrenzung, Rahmenbedingungen 5.1–5.4, Kap. 6 Änderungsdoku). Pro Kapitel: Was fehlt, was ist unklar, was widerspricht AS/Ausschreibung?
2. Anforderungsliste: Prüfe jede Zeile auf richtige Art (F/M/W), Messbarkeit, Einheit und Quelle. Festanforderungen eignen sich später nicht für die Nutzwertanalyse.
3. Abgrenzung „wasserdicht“ halten.
4. Keine Lösungsansätze im PH; vertiefte Analysen gehören in die Doku.
5. Jede Änderung in Kap. 6 (Version, Datum, Änderung, Grund, wer hat entschieden).

Werte, die nur der Betrieb kennen kann, erfindest du nicht. Du markierst sie als offen und nimmst sie in meine Fragenliste (Cockpit „Fragen Betrieb“) auf.
Ende auf „Übergabe“ mit dem Übergabeblock aus Abschnitt B.
```

### Chat 03 – Projektplan Rillsoft
```
Chat 03 – PROJEKTPLAN IN RILLSOFT (UP2).

Startblock: Lies claude/Projektstand_TA_Bauer.md, claude/Unterstuetzungsprogramm_UP0-UP7_Kompendium.md (Kap. 3) und claude/TA_Chat-Menue_Prompts.md (Abschnitt A.5 = aktuelle Termine). Übernimm die Ergebnisse der letzten Übergaben.

Ziel: ein dynamischer, MS-tauglicher Terminplan (nur Terminplanung, keine Ressourcen) mit den Teilprojekten „TA (Schule)“ und „Betrieblicher Auftrag“, Ende-Anfang-Verknüpfungen, Meilensteinen ohne Dauer und sichtbarem kritischem Pfad. Export als PDF (DIN A3, farbig). Nach MS 1 einen Basisplan für den Soll-Ist-Vergleich anlegen.

Bekannte Baustellen (Plan noch auf Stand 16.10.): neue Termine laut A.5 (MS 1 ca. 16.11., PH-Freigabe 20.11., Variantenauswahl 04.12., Konstruktionsfreigabe 22.01., MS 2 ca. Mitte Feb., Übergabe 26.02., MS 3 Mitte März) · fehlende Vorgänge: Messprinzip-Recherche/-Bewertung, Lösungsansätze vor MS 1, Messunsicherheitsabschätzung, Auslegungsberechnungen, Messprozessentwicklung, Pneumatik-/Elektronikplan, Angebote einholen, Abschlussmeeting, Puffer · Dokumentation prozessbegleitend · Feiertage/Ferien und Freitags-Projekttage prüfen.

Arbeitsweise: Du baust den Plan nicht für mich. Du fragst mich nach Vorgängen, Dauern und Vorgängern, prüfst meine Logik (Vorgänger/Nachfolger, Fixierungen vs. Verknüpfungen) und erklärst mir Rillsoft-Funktionen, wenn ich nicht weiterkomme. Vor jedem Meilenstein machen wir hier einen Soll-Ist-Abgleich: Abweichungen, Gründe, Gegenmaßnahmen, Risiken.

Ende auf „Übergabe“ mit dem Übergabeblock aus Abschnitt B (inkl. aller geänderten Termine).
```

### Chat 04 – Meilenstein-Vorbereitung
```
Chat 04 – VORBEREITUNG SCHULISCHER MEILENSTEIN [M1 / M2 / M3 – bitte eintragen].

Startblock: Lies claude/Projektstand_TA_Bauer.md, claude/Unterstuetzungsprogramm_UP0-UP7_Kompendium.md (Kap. 1.4 Meilensteine + Protokollinhalte, Kap. 1.5 Bewertung) und claude/TA_Chat-Menue_Prompts.md (Abschnitt A). Übernimm die letzten Übergaben.

Schulischer Betreuer: Björn Graudejus de Olio (privater Teams-Chat). Den Termin vereinbare ich auf eigene Initiative, mindestens ein Vor-Ort-Termin im Betrieb.

Deine Aufgaben:
1. Checkliste der Pflichtunterlagen für diesen Meilenstein (M1: AS, Pflichtenheft, Projektplan aus der Software, Lösungsansätze als PDF · M2: aktualisiertes PH mit Änderungen, bisherige Ergebnisse, Projektplan Soll/Ist + kritischer Pfad, Ausblick · M3: letzte PH-Fassung, Ergebnisse + Bewertung, Übergabe, Reflexion des Plans, Stand der Doku) und Abgleich mit dem, was ich habe.
2. Geh mit mir die Punkte des Protokolls durch, die der Betreuer abhakt, und stelle mir die Fragen, die er stellen könnte (Probegespräch).
3. Hilf mir, eine kurze Nachricht zur Terminanfrage zu formulieren (inkl. Vorschlag für den Vor-Ort-Termin bei BD Gamer und offenen Klärungspunkten wie FSL-Prüfung der AS und KI-Regel).
4. Nach dem Termin: Wir werten das Gespräch aus (Vereinbarungen, Nacharbeiten, Fristen).

Ende auf „Übergabe“ mit dem Übergabeblock aus Abschnitt B.
```

### Chat 05 – Messtechnik-Recherche & Messprinzipien
```
Chat 05 – MESSTECHNIK-RECHERCHE & MESSPRINZIPIEN (Phase 2, Ausschreibung Aufgaben 1–3).

Startblock: Lies claude/Projektstand_TA_Bauer.md, claude/Aufgabenstellung_Bauer_TA_V4.md (bzw. die neueste AS-Datei), claude/TA_Chat-Menue_Prompts.md (Abschnitt A) und claude/Unterstuetzungsprogramm_UP0-UP7_Kompendium.md (Kap. 5). Übernimm die aktuelle Anforderungsliste (PH V8.7, A.4).

Messaufgabe: Außendurchmesser (± 13 µm) und Ovalität (Ø max − Ø min, NiTi ≤ 0,010 mm, Edelstahl ≤ 0,025 mm) von Rohren aus Nitinol und Edelstahl (Tantal wünschenswert), Ø 1,0–6,5 mm, 1–3 m lang, dünnwandig und labil, im Wareneingang eines Medizintechnik-Herstellers. Messpunktabstand 2 mm über die Länge, Auswertung je Messpunkt, berührungslos, Reproduzierbarkeit %GRR ≤ 10 %, Oberfläche darf nicht beschädigt oder kontaminiert werden.

Ziel:
1. Messmerkmale sauber definieren (Ovalität vs. Rundheit nach DIN EN ISO 1101/12181, Zweipunktmaß nach ISO 14405-1, nicht-starre Teile ISO 10579), abgeleitet aus den Anforderungen.
2. Systematischer Überblick über geeignete berührungslose Messprinzipien (z. B. Laser-Scan-Mikrometer/Schattenwurf, optische Mikrometer/Kameras, konfokal-chromatisch, Triangulation, Luftmessung) mit Funktionsprinzip, Messbereich (bis 6,5 mm!), Wiederholgenauigkeit, Einfluss von Durchbiegung/Rotation, Kosten-Größenordnung – mit mehreren Herstellern (nicht nur Keyence).
3. Was heißt das für Rotation/Handhabung (Schnittstelle zu Chat 06) und für die Taktzeit (2 mm über 3 m)?
4. Messunsicherheit grob einordnen: Ist %GRR ≤ 10 % bei 0,010 mm Toleranz realistisch? (Messmittelfähigkeit am realen System ist abgegrenzt → rechnerische Abschätzung.)

Bitte mit Quellen (Hersteller, Normen, Fachliteratur). Kennzeichne Unsicheres. Ich entscheide, du lieferst Fragen und Struktur.
Ende auf „Übergabe“ mit dem Übergabeblock aus Abschnitt B (inkl. Shortlist der Messprinzipien + Quellenliste).
```

### Chat 06 – Spann- & Handhabungskonzept
```
Chat 06 – SPANN- & HANDHABUNGSKONZEPT FÜR LANGE ROHRE (Phase 2, Ausschreibung Aufgabe 6).

Startblock: Lies claude/Projektstand_TA_Bauer.md, claude/TA_Chat-Menue_Prompts.md (Abschnitt A) und claude/Unterstuetzungsprogramm_UP0-UP7_Kompendium.md (Kap. 5.2 Phase 2, 5.3 Morphologischer Kasten, 5.4 Gestaltungsprinzipien). Übernimm die letzten Übergaben von Chat 02 (Anforderungen) und Chat 05 (Messprinzip-Shortlist).

Problem: Rohre Ø 1,0–6,5 mm, 1–3 m, dünnwandig, superelastisches Nitinol und Edelstahl, biegen unter Eigengewicht durch. Keine plastische Verformung (σ < 380/690 MPa), sauber/ölfrei, Durchbiegung darf die Messung nicht verfälschen. Rohr wird manuell eingelegt; Messung braucht definierte Lage, evtl. Rotation und Vorschub. Zulässige Kontaktstellen/-werkstoffe mit Hr. Baidinger klären (bis 27.11.).

Ziel (Variantenauswahl im Betrieb am 04.12.2026):
1. Gesamtfunktion → Teilfunktionen (einlegen, auflagern/stützen, ausrichten, spannen, drehen, axial verfahren, Messkopf positionieren, entnehmen). Blackbox mit Ein-/Ausgangsgrößen und Störgrößen.
2. Morphologischer Kasten mit mehreren Ideen je Teilfunktion; Abhängigkeiten kennzeichnen.
3. Durchbiegung abschätzen: Hilf mir, das Modell aufzustellen (Balken auf zwei oder mehr Stützen, Streckenlast aus Eigengewicht, I für Kreisring, E-Modul mit Quelle). Die Rechnung mache ich selbst, du prüfst.
4. Gestaltungsregeln eindeutig, einfach, sicher sowie fehlerarm und montagegerecht berücksichtigen.

Ende auf „Übergabe“ mit dem Übergabeblock aus Abschnitt B (inkl. ausgefülltem Morpho-Kasten und 2–4 Gesamtvarianten).
```

### Chat 07 – Konzeptbewertung & Variantenauswahl
```
Chat 07 – KONZEPTBEWERTUNG & VARIANTENAUSWAHL (Phase 2, Ausschreibung Aufgabe 4).

Startblock: Lies claude/Projektstand_TA_Bauer.md, claude/TA_Chat-Menue_Prompts.md (Abschnitt A) und claude/Unterstuetzungsprogramm_UP0-UP7_Kompendium.md (Kap. 5.2 Fehlerquellen, 5.4 Pahl/Beitz 6.4). Übernimm die Varianten aus Chat 05 und 06 und die aktuelle Anforderungsliste.

Ziel: eine nachvollziehbare, dokumentierte Entscheidung für den betrieblichen Meilenstein „Variantenauswahl“ (04.12.2026), die der Auftraggeber trifft.

Vorgehen:
1. Vorauswahl: Varianten, die eine Festanforderung verletzen, scheiden aus. Festanforderungen werden NICHT gewichtet.
2. Bewertungskriterien aus Mindest-/Wunschanforderungen und Qualitätsanforderungen ableiten (z. B. %GRR/Messunsicherheit, Taktzeit, Oberflächenschonung, Platzbedarf, Kosten, Wartung/Kalibrierung, Komplexität, Tantal-Eignung).
3. Gewichtung per paarweisem Vergleich. Danach Nutzwertanalyse oder technisch-wirtschaftliche Bewertung nach VDI 2225. Erkläre mir den Unterschied, ich wähle die Methode und begründe sie.
4. Sensitivitätsprüfung: Kippt das Ergebnis, wenn sich Gewichte leicht ändern?
5. Hilf mir, die Entscheidungsvorlage für Herrn Baidinger vorzubereiten. Da er keine Protokolle will: kurze schriftliche Zusammenfassung der Entscheidung zur Bestätigung.

Prüfe meine Tabellen auf Methodenfehler (falsche Abhängigkeiten, F-Anforderungen in der Wertung, Doppelzählungen).
Ende auf „Übergabe“ mit dem Übergabeblock aus Abschnitt B (inkl. gewählter Variante, Begründung, Bestätigung).
```

### Chat 08 – CAD-Konstruktion & Auslegungsberechnungen
```
Chat 08 – CAD-KONSTRUKTION & AUSLEGUNGSBERECHNUNGEN (Phase 3).

Startblock: Lies claude/Projektstand_TA_Bauer.md, claude/TA_Chat-Menue_Prompts.md (Abschnitt A) und claude/Unterstuetzungsprogramm_UP0-UP7_Kompendium.md (Kap. 5.2 Phase 3, 5.4 Teil III Gestaltung). Übernimm die gewählte Variante aus Chat 07 und die Anforderungsliste.

Rahmen: CAD-Konstruktion in SolidWorks ab Variantenauswahl (04.12.2026), Konstruktionsfreigabe im Betrieb am 22.01.2027, schulischer MS 2 ca. Mitte Feb. 2027. Kein physischer Bau.

Deine Rolle:
1. Mit mir eine Baugruppenstruktur festlegen (Grundgestell, Rohrauflage/Stützen, Dreh-/Spannachse, Linearachse, Sensorhalter, Einlegehilfe/Entnahme, Schutz/Abdeckung) und die Reihenfolge der Konstruktion planen (gestaltbestimmende Größen zuerst).
2. Konstruktionsentscheidungen kritisch hinterfragen: Kraftfluss, Steifigkeit, thermische Einflüsse auf die Messung, Justierbarkeit, Kalibrierung, Reinigbarkeit, fertigungs- und montagegerecht, Kaufteile vs. Eigenfertigung.
3. Auslegungsberechnungen strukturieren und meine Rechenwege prüfen (Durchbiegung Rohr und Gestell, Spannungen im Rohr gegen Anf. 3.1, Flächenpressung, Antriebe/Führungen, ggf. Eigenfrequenz). Nachvollziehbar mit Formeln, Annahmen und Quellen.
4. Vor der Konstruktionsfreigabe: Abgleich jeder Anforderung mit der Konstruktion (erfüllt/teilweise/nicht + Nachweis).

Ende auf „Übergabe“ mit dem Übergabeblock aus Abschnitt B (inkl. Anforderungs-Abgleich und Freigabestatus).
```

### Chat 09 – Messprozess, Sensorintegration & technische Unterlagen / Projektabschluss
```
Chat 09 – MESSPROZESS, SENSORINTEGRATION, TECHNISCHE UNTERLAGEN & BETRIEBLICHER PROJEKTABSCHLUSS (Phase 3 + 5, UP6).

Startblock: Lies claude/Projektstand_TA_Bauer.md, claude/TA_Chat-Menue_Prompts.md (Abschnitt A) und claude/Unterstuetzungsprogramm_UP0-UP7_Kompendium.md (Kap. 7 UP6). Übernimm die Übergaben aus Chat 05 (Messprinzip), 07 (Variante) und 08 (Konstruktion).

Teil A – Messprozessentwicklung: Hilf mir, den automatisierten Prüfablauf im Wareneingang zu beschreiben (Ablaufdiagramm: Rohr manuell einlegen, ausrichten, messen alle 2 mm über die Länge, Auswertung je Messpunkt gegen die Toleranz der Rohrspezifikation, i.O./n.i.O.-Entscheid, entnehmen), dazu Sensorintegration (Anordnung, Halterung, Justage, Schnittstellen, Kalibrierung/Referenznormal, Umgebungseinflüsse) und Taktzeitabschätzung. Software/Steuerung sind abgegrenzt: als Schnittstelle beschreiben.

Teil B – Technische Unterlagen für BD Gamer (bis 26.02.2027): Funktionsbeschreibung, Fertigungszeichnungen (normgerechte Bemaßung/Tolerierung), Stückliste (Eigenfertigung/Kaufteile), Pneumatik- und Elektronikplan (Schaltplan Pneumatik + E-Plan, keine Programmierung), Angebote für Kaufteile/Sensorik. Checklisten statt fertiger Texte.

Teil C – Projektabschluss (Übergabe 26.02.2027, schulischer MS 3 Mitte März): ehrlicher Soll-Ist-Vergleich gegen das Pflichtenheft, Übergabeliste und Ablageorte, Abschlussmeeting planen, Dank, Feedbackgespräch mit Herrn Baidinger. Checkliste Projektabschluss aus UP6 abarbeiten.

Ende auf „Übergabe“ mit dem Übergabeblock aus Abschnitt B.
```

### Chat 10 – TA-Dokumentation (prozessbegleitend)
```
Chat 10 – DOKUMENTATION DER TECHNIKERARBEIT (UP5), prozessbegleitend bis zur Abgabe am Mo. 05.04.2027, 10:00 Uhr.

Startblock: Lies claude/Projektstand_TA_Bauer.md, claude/TA_Chat-Menue_Prompts.md (Abschnitt A) und claude/Unterstuetzungsprogramm_UP0-UP7_Kompendium.md (Kap. 6 vollständig + Kap. 1.5 Bewertungskriterien). Übernimm alle bisherigen Übergaben. Doku-Speicher und KI-Logbuch liegen im TA-Cockpit.

WICHTIG: Die Doku ist Prüfungsleistung. Laut Erklärung der Formatvorlage V10 darf KI nur zur sprachlichen Optimierung genutzt werden, nicht zum Erzeugen fachlicher Inhalte. Du schreibst daher KEINE fachlichen Textabschnitte für mich. Du gibst Struktur, Fragen, Feedback und Sprachkorrektur und protokollierst jede Hilfe für das KI-Logbuch.

Aufgaben:
1. Sachlogische Gliederung (nicht chronologisch): Einleitung → Ist-Zustand/Problemanalyse und Anforderungen → Teilprobleme (Messprinzip, Spann-/Handhabung, Messprozess …) → Lösungsfindung und Bewertung → ausgearbeitete Gesamtlösung → Schlussbetrachtung und Ausblick. Mit Herrn Graudejus de Olio abstimmen (spätestens zu MS 3).
2. Zu jedem Projektabschnitt sofort Notizen und Abbildungen im Doku-Speicher sammeln.
3. Feedback auf meine Entwürfe nach den Regeln: Präsens, unpersönlich, Fachsprache auf Technikerniveau, Zahlen bis zwölf ausschreiben, keine Nacherzählung, kritischer Abgleich Problem ↔ Lösung, 30–60 Seiten.
4. Formalia prüfen: Arial 11 / TNR 12, 1,5-zeilig, Seitenzählung, Kapitelnummerierung, Beschriftungen, Quellen [n, S. x], Verzeichnisse, Anhang, AS wortgetreu, Selbstständigkeitserklärung. Kein Sperrvermerk: vertrauliche Spezifikationen nur sinngemäß, nicht beifügen.
5. Abstract erst ganz am Ende (max. 1 Seite, Präsens).
6. Abgabe-Checkliste: 2 Papierexemplare (einseitig, gebunden), Unterschriften + Firmenstempel, Datenträger in jedem Exemplar, digitale Abgabe.

Ende jeder Sitzung auf „Übergabe“ mit dem Übergabeblock aus Abschnitt B (inkl. Seiten-/Kapitelstand).
```

### Chat 11 – Präsentationsprüfung
```
Chat 11 – PRÄSENTATIONSPRÜFUNG (UP7) am 17./18.06.2027.

Startblock: Lies claude/Projektstand_TA_Bauer.md, claude/TA_Chat-Menue_Prompts.md (Abschnitt A) und claude/Unterstuetzungsprogramm_UP0-UP7_Kompendium.md (Kap. 8 + 1.5). Übernimm alle Übergaben, vor allem die finale Doku-Gliederung aus Chat 10.

Rahmen: 13–15 Minuten + Fragen vor dem Fachausschuss (Herr Graudejus de Olio + 2 Lehrkräfte), 1/3 der Endnote. Fachpublikum und Herr Baidinger dürfen zuhören; kein Sperrvermerk, aber vertrauliche Spezifikationen nicht zeigen. Räume R124/R014, PowerPoint 2019, 16:9, Referentenansicht; Videos lokal speichern; vorher im Raum testen.

Aufgaben:
1. Roter Faden und Zeitplan pro Folie (Problem → Ziel → Vorgehen → Lösung → Bewertung/Ergebnis → Ausblick). Die Kernbotschaft in einem Satz.
2. Auswahl der Inhalte: Was muss rein, was bleibt für die Fragerunde? Anschauungsmaterial (CAD-Animation/Explosionsdarstellung, Rohrmuster, Messprinzip-Skizze).
3. Feedback auf meine Folien (Lesbarkeit, Bild statt Text, Konsistenz mit der Doku).
4. Probeprüfung: kritische Fragen wie vom Fachausschuss (Methodenwahl, Messunsicherheit/%GRR, Durchbiegungsrechnung, Variantenbewertung, was ich anders machen würde).
5. Auftreten: Sprechtempo, Gestik, Umgang mit Fragen, Plan B bei Technikproblemen.

Ende auf „Übergabe“ mit dem Übergabeblock aus Abschnitt B.
```

---

## D. Pflege dieses Menüs
- Ändern sich Eckdaten (Titel, Werte, Termine, Dateipfade), lässt du im Cockpit (Chat 00) Abschnitt A dieses Menüs **und** den Projektstand aktualisieren (oder per Skill /ta-projektabgleich).
- Die Prompts verweisen auf `claude/Aufgabenstellung_Bauer_TA_V4.md` bzw. „die neueste AS-Datei“ – bei einer AS V5 muss nur Abschnitt A angepasst werden.
- Alte Fassungen (AS V2/V3, PH bis V8.6) gelten nur noch als Archiv (Cockpit-Archiv).
