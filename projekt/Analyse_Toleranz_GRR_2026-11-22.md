# Analyse: Toleranzwerte Zylinderform und %GRR-Grenze (Arbeitspaket 1)

Stand 22.11.2026 · erstellt von KI (Claude Code) als Entscheidungsgrundlage · **keine Festlegung**. Janek und der Betrieb entscheiden.

Kennzeichnung: **[H]** Herstellerangabe · **[PH]** Pflichtenheft · **[R]** eigene Rechnung (KI) · **[S]** Schätzung (KI) · **[Q?]** Quelle nicht eindeutig

## 1. Ausgangslage im Pflichtenheft

Maßgeblich ist das Pflichtenheft V1.2 (Janek nennt es V0.2), Datei `docs/archiv/3 Pflichtenheft/Pflichtenheft/V1.2_Bauer_TA_PH_V1.docx`, Stand 20.11.2026.

- Anf. 2.1 (F): Zylinderform (Ø max − Ø min), Toleranz je Rohrtyp: **NiTi [?], Edelstahl [?]**, Einheit mm. [PH, Kap. 3 Anforderungsliste]
- Anf. 2.2 (F): Außendurchmesser, **ΔD ± 13 µm** lt. Rohrspezifikation. [PH]
- Anf. 2.4 (M): %GRR bezogen auf die Toleranz, **max. 10 %**. [PH]
- Anf. 2.5 (F): Auswertung je Messpunkt, Mittelwerte unzulässig. [PH]
- Anf. 3.3 (F): Einfluss von Durchbiegung und Lage ist in 2.4 enthalten. [PH]
- Rahmenbedingungen: „Zylinderform = Ø max − Ø min“. [PH, Kap. 5.3]

Die früheren Cockpit-Werte NiTi 0,010 mm / Edelstahl 0,025 mm (`reqs.json`, r06) gelten seit PH V1.2 nicht mehr als gesichert. Sie dienen hier nur als **Platzhalter**.

## 2. Formel

Bei %GRR bezogen auf die Toleranz verwendet die AIAG-MSA (4. Auflage) die 6-σ-Spannweite:

  %GRR = 6 · σ_GRR / T · 100 %  →  σ_GRR,max = 0,10 · T / 6

Quelle: AIAG, Measurement Systems Analysis, 4. Aufl. 2010. Die Grenzen < 10 % (annehmbar), 10–30 % (bedingt annehmbar) und > 30 % (nicht annehmbar) stehen in Tab. II-D 1 „GRR Criteria“, S. 78. **[Q?]** Die Seitenangabe stammt nur aus einer Sekundärquelle. Das Original lag nicht vor: SPC for Excel, „Acceptance Criteria for Measurement Systems Analysis“, https://www.spcforexcel.com/knowledge/measurement-systems-analysis/acceptance-criteria-for-MSA, Suchergebnis vom 22.11.2026. Laut dieser Quelle ersetzt die 4. Auflage den früheren Faktor 5,15 durch 6. Janek sollte S. 78 im Original prüfen, z. B. über das QM.

## 3. Drei Szenarien [R]

| Szenario | Toleranz T | Grundlage | σ_GRR,max = 0,1·T/6 |
|---|---|---|---|
| A | 26 µm (± 13 µm) | Anf. 2.2 Außendurchmesser [PH] | **0,43 µm** |
| B | 10 µm | früherer Wert NiTi (Platzhalter) | **0,17 µm** |
| C | 25 µm | früherer Wert Edelstahl (Platzhalter) | **0,42 µm** |

Rechenweg A: 0,1 · 26 µm / 6 = 0,433 µm. B: 0,1 · 10 / 6 = 0,167 µm. C: 0,1 · 25 / 6 = 0,417 µm.

## 4. Punkte, die die Rechnung verschieben (Fragen für den Betrieb)

1. **Toleranzbreite bei einseitiger Toleranz [Q?].** Die Zylinderform hat nur eine Obergrenze, denn Ø max − Ø min ≥ 0. Offen ist, ob T = Obergrenze − 0 gilt (wie in Szenario B/C) oder ob das QM eine andere Bezugsgröße nutzt. Das muss das QM festlegen; die KI legt es nicht fest.
2. **Differenz aus zwei Messwerten [R, Annahme].** Die Zylinderform ist eine Differenz zweier Durchmesserwerte. Sind beide Werte unabhängig und gleich gestreut, gilt σ_Diff = √2 · σ_Einzel. Für Szenario B wäre die Grenze je Einzelwert dann 0,17 / √2 ≈ **0,12 µm**. Das ist eine Annahme und kein Herstellerwert.
3. **Extremwertbildung [S, qualitativ].** Ø max und Ø min werden aus vielen Winkellagen gewählt. Rauschen vergrößert Ø max − Ø min systematisch. Je mehr Winkellagen es gibt, desto größer ist dieser Effekt. Ohne Messdaten lässt er sich nicht beziffern.
4. **Was %GRR enthält.** %GRR umfasst Wiederholbarkeit (Gerät) und Vergleichbarkeit (Bediener bzw. Einlegen). Nach Anf. 3.3 gehören auch Durchbiegung und Lage dazu. Die Sensor-Wiederholgenauigkeit ist nur **ein** Anteil, das Budget für Mechanik und Einlegen kommt hinzu.
5. **Linearität ist nicht %GRR.** Linearität bzw. Messabweichung ist ein systematischer Fehler (Bias). Sie betrifft vor allem die absolute Ø-Prüfung nach 2.2, nicht die %GRR-Grenze. Der Statusbericht vom 22.11. (Abschnitt 4.2) hat die Linearität von ±2 µm mit der σ-Grenze verglichen. **Das war fachlich nicht sauber und wird hiermit korrigiert.**
6. **Abgrenzung.** Eine MFU am realen System ist abgegrenzt (PH Kap. 4). Der Nachweis von 2.4 kann in der TA also nur rechnerisch erfolgen, zum Beispiel als Messunsicherheitsbudget. So steht es schon im früheren Widerspruch w11 im Postfach. Wie der Nachweis aussehen soll, entscheidet Janek mit dem Betrieb.

## 5. Was Janek entscheiden bzw. klären muss

- Toleranzwerte NiTi und Edelstahl (QM, Hr. Baidinger), Anf. 2.1.
- Bezugsgröße T für %GRR bei der Zylinderform (einseitig) und beim Durchmesser (± 13 µm).
- Welches Szenario bis zur Klärung als Arbeitsannahme für die Sensorauswahl gilt.

Eintrag im Postfach: `pv-ent-toleranz-grr` (Entscheidung).
