### ÜBERGABE – Chat 06 Spann- & Handhabungskonzept (Morphologischer Kasten) – 20.11.2026

Quelle: Übergabe-Text, den Janek am 20.11.2026 in den Chat gegeben hat. Abgleich mit dem Repo: Teilfunktionen,
Morpho-Kasten (tools.json „morph“), Sensorvergleich und die Archivdateien sind im Repo; die offenen Punkte
sind im Cockpit ergänzt worden (siehe Commit). Maßgeblich ist das Cockpit (`cockpit/daten`).
Die Claude-Doc-/Artefakt-Links der Übergabe sind nicht Teil des Repos; die Fassungen liegen im Archiv
unter `docs/archiv/10 Konzept & Lösungsfindung/`.

**Erledigt / Entscheidungen:**
- Teilfunktionen festgelegt: TF1–TF13 + Q1–Q3 (sauber/ölfrei, Störeinflüsse, Bediener schützen). Liste ist KI-Vorschlag, von Janek in seiner Fassung V2 übernommen (13.11.).
- Morphologischer Kasten V2: 4–5 Ideen je Zeile, grober F-Check, Abhängigkeiten (TF7/TF8/TF9 bestimmen den Rest).
- Janek verwirft 5 Ideen; sie bleiben für die Schul-Doku sichtbar (13.11.): 1.5/2.4 vertikal hängen („zu unhandlich“), 3.3 Luftlager („zu ungenau“), 4.5 Vakuum-Prisma, 5.4 kodierte Wechseleinsätze (Begründung 4.5/5.4 fehlt).
- Janek: KI-Kennzeichnung im Morpho-Dokument entfernt, „geht so klar“ (13.11.); KI-Logbuch im Cockpit bleibt.
- Sensorvergleich aus Datenblättern erstellt: 15 Sensoren, je 9 Kriterien.
- NICHT erledigt: Blackbox, Durchbiegungsmodell/Stützabstände, 2–4 Gesamtvarianten.

**Neue Fakten (Quelle: Keyence-/Micro-Epsilon-/Riftek-Datenblätter, Stand 13.11.2026):**
- LS-9006/-M/-D und TM-X5006: Messbereich max. 6 mm → Ø 6,5 mm nicht abgedeckt, W7 bestätigt.
- LS-9030/-M/-D: 0,3–30 mm, Wiederholbarkeit ±0,1 µm (±2σ, ruhendes Normal, 2048-fach gemittelt), Genauigkeit ±2 µm, 16 000/s; LS-9030D 2-achsig, ca. 9 kg.
- optoCONTROL 2700-10: 10 mm, Wiederholpräzision ≤ 0,03 µm, Linearität ≤ 0,5 µm, 15 kHz, Encoder-/Trigger-Eingänge; 2700-40: ≤ 0,1 µm / ≤ 1 µm.
- optoCONTROL 2520-46 (≤ 5 µm) und 1200 (≥ 40 µm) zu grob für 10 µm Ovalität.
- Riftek RF657.2D-15x20: Messfehler ±0,8 µm, nur 24 Messungen/s, keine Wiederholgenauigkeit angegeben.
- Wiederholangaben nur unter Laborbedingungen und nicht direkt vergleichbar (Keyence ±2σ, Micro-Epsilon 95 %-Konfidenz).

**Geänderte Werte / Anforderungen:** keine

**Offene Punkte + Verantwortlicher + Termin:**
- Gesamtvarianten (2–4 Pfade, TF7/8/9 zuerst) – Janek – vor Variantenauswahl 04.12.
- Durchbiegungsmodell + Stützabstände (W12) – Janek, KI prüft – vor 04.12.
- Blackbox (Ein-/Ausgangs-/Störgrößen) – Janek – vor 04.12.
- Begründung 4.5 und 5.4 ergänzen; Begründung Luftlager („zu ungenau“) fachlich prüfen – Janek – vor 04.12.
- Sensorwerte am Original gegenprüfen, in OneNote übertragen – Janek – offen (Cockpit: t-datenblaetter-pruefen)
- Cockpit „Morph. Kasten“ an Janeks Fassung V2 angleichen (Verworfen-Markierungen fehlen dort) – Cockpit
- Fragen an Hrn. Baidinger: Schraubenlinie zulässig (8.2)? Raumhöhe/Platz Wareneingang (2.4, 9.2)? Zulässige Kontaktwerkstoffe (Q1.1, Cockpit: t-kontaktstellen)? %GRR ≤ 10 % (W10, Cockpit: q03) – Janek – 27.11. (PH-Freigabe)
- OneNote: .docx-Anhänge lassen sich nicht öffnen; Test mit .doc/.rtf und fremder Word-Datei – Ergebnis offen – Janek
- PC-Ablage der Dateien – Janek („PC-Ordner abgleichen“; laut Cockpit erledigt 09.11., Stand jetzt erneut prüfen)
- ⚠️ Widerspruch W8 verschärft: Ideen im Morpho-Kasten stammen größtenteils von der KI, Kennzeichnung entfernt ↔ KI-Regel Formatvorlage V10 – Janek mit Hrn. Graudejus de Olio klären

**Erstellte/geänderte Dateien:**
- Claude Doc „Chat 06 – Morphologischer Kasten V2“ (V2) und V1: Fassungen im Archiv unter `10 Konzept & Lösungsfindung`
- Cockpit-Archiv › 10 Konzept & Lösungsfindung: Morpho-Kasten V1/V2 (md, docx, pdf, Janek-Fassung)
- Cockpit-Archiv › 6 Recherche Messtechnik: Sensorvergleich V1 (xlsx) + Datenblätter/Kataloge
- Cockpit: tools/morph (16 Zeilen), KI-Logbuch-Einträge
- Nur Test, nicht archiviert: Morpho-Kasten_V2_Test.doc/.rtf

**Auswirkung auf Projektplan:** Variantenauswahl 04.12. (laut Cockpit 11.12.) gefährdet: Gesamtvarianten, Durchbiegung und Messunsicherheitsabschätzung fehlen noch; Vorgang „Sensorvergleich“ begonnen.

**Nächster Chat / nächster Schritt:** Chat 05: Sensorwerte prüfen, %GRR-Abschätzung für LS-9030(D) und optoCONTROL 2700, Shortlist. Danach zurück in Chat 06: Gesamtvarianten + Durchbiegung → Chat 07 (Bewertung).

**KI-Nutzung (für Logbuch/Anhang):** siehe `kilog.json` (Chat 06, Einträge 07.11.–13.11.)
