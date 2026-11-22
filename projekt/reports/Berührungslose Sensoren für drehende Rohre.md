# Achsstopp und Mittelung bestimmen die Taktzeit, nicht der Sensor

Stand 22.11.2026 · KI-Recherche und eigene Rechnung (Claude Code) · keine Messung, keine Auswahl. Janek entscheidet.

**Kein Sensor erreicht unter dem vorgegebenen Modell eine grüne Taktzeit (unter 1 min) je 3-m-Rohr. Bei einem Achsstopp von t_s = 0,5 s ist jeder Sensor rot, der an allen 1501 Prüfstellen anhält: 1D-Mikrometer, Mehrachsköpfe und paarweise Punktsensoren.** Allein die Stopps kosten 1501 × 0,5 s = 12,5 min, auch bei unendlich schneller Messung. Gelb (1–5 min) erreichen bei 0,5 s nur 2D-Bildsensoren mit großem Feld: **Keyence TM-X5065 (1,7 min) und TM-X5040 (2,8 min)**, beide nur als Suchergebnis belegt, sowie **RIFTEK RF656.2D-40x50 / -25x35 / -15x20 (1,9 / 2,8 / 4,8 min)** und **RF657.2D-60x80 / -40x50 (2,2 / 3,5 min)**, die im Datenblatt im Repo stehen. Sinkt t_s auf 0,1 s oder 0,05 s, werden fast alle 1D- und Punktsensoren rechnerisch gelb (2,5–3,5 min bzw. 1,3–2,5 min). Das gilt aber nur für einen Einzelscan ohne Mittelung. Dafür veröffentlichen nur Aeroel (±0,75–1,5 µm, Datenblatt), Nordson AccuScan 6012 (±1 µm ±0,025 %) und LaserLinc Triton312 (±2,5 µm) einen Wert. Außerdem müsste sich das 3-m-Rohr dafür mit 400 bis über 10.000 1/min drehen. Die sehr guten Wiederholgenauigkeiten der Datenblätter (±0,03–0,1 µm) gelten nur mit 512- bis 2048-facher Mittelung am ruhenden Normal. Winkelsynchron gemittelt kosten sie 2 bis 39 Stunden je Rohr. Fast alle Herstellerseiten waren in dieser Sitzung gesperrt. Nur die Werte für Keyence LS-9000/TM-X5006, Micro-Epsilon ODC, RIFTEK, Aeroel und Mitutoyo sind am Datenblatt geprüft, alle anderen sind vorläufig.

Kennzeichnung: **[DB]** Datenblatt eingesehen (lokale Kopie unter `docs/archiv/6 Recherche Messtechnik/…`, mit Seite) · **[SE]** nur Suchergebnis, Datenblatt nicht eingesehen · **[R]** eigene Rechnung (KI). Unbekannte Felder stehen als „–“.

---

## 1. Kurzfassung: Ampel je Sensor

Grundlage: Achsstopp t_s = 0,5 s (Grundwert), 1501 Prüfstellen, 5°-Schritt = 72 Messwerte je Umdrehung. Die Rechenart folgt der Sensorklasse aus dem Auftrag. Bei Mehrachsköpfen ist „ohne Drehung“ die Hauptrechnung. Die Spalte „Rep im Rechenmodus“ zeigt, ob der Hersteller die Wiederholgenauigkeit für genau die gerechnete Betriebsart nennt.

| Sensor | Familie | Rechenart | Taktzeit 0,5 s | Ampel 0,5 s | bestes Ergebnis (0,05 s) | Rep im Rechenmodus | Beleg |
|---|---|---|---|---|---|---|---|
| Keyence TM-X5065 | 2D telezentrisch | 47 Stationen | 1,7 min | **gelb** | 1,4 min gelb | ±0,1 µm nur mit 16-fach-Mittelung | [SE] |
| RIFTEK RF656.2D-40x50 | 2D Schattenbild | 60 Stationen (optimistisch) | 1,9 min | **gelb** | 1,5 min gelb | keine Angabe (nur Messfehler ±4,5 µm) | [DB] |
| RIFTEK RF657.2D-60x80 | 2D Schattenbild | 38 Stationen (optimistisch) | 2,2 min | **gelb** | 1,9 min gelb | keine Angabe (Messfehler ±3 µm) | [DB] |
| RIFTEK RF656.2D-25x35 | 2D | 86 Stationen | 2,8 min | **gelb** | 2,1 min gelb | keine Angabe (±2,5 µm) | [DB] |
| Keyence TM-X5040 | 2D telezentrisch | 75 Stationen | 2,8 min | **gelb** | 2,2 min gelb | ±0,08 µm nur mit 16-fach | [SE], Triggerintervall nur Serienwert |
| RIFTEK RF657.2D-40x50 | 2D | 60 Stationen | 3,5 min | **gelb** | 3,0 min gelb | keine Angabe (±2 µm) | [DB] |
| RIFTEK RF656.2D-15x20 | 2D | 150 Stationen | 4,8 min | **gelb (knapp)** | 3,7 min gelb | keine Angabe (±2 µm) | [DB] |
| RIFTEK RF657.2D-25x35 | 2D | 86 Stationen | 5,0 min | rot (knapp) | 4,4 min gelb | keine Angabe (±1,2 µm) | [DB] |
| RIFTEK RF656.2D-8x10, RF657.2D-15x20, RF657R.2D (alle) | 2D | 30–300 Stationen | 7,7–37 min | rot | 7,5–36 min rot | keine Angabe | [DB] |
| Keyence TM-X5006 | 2D telezentrisch | 500 Stationen | 18,6 min | rot | 14,8 min rot | ±0,03 µm mit 16-fach | [DB] |
| Micro-Epsilon ODC2700-10/-40 | 1D Schatten (LED) | Drehung je Prüfstelle | 14,2 min | rot | 3,0 min gelb (mit Mittelung) | ja, nur mit 1024-fach (≤ 0,03 / 0,1 µm) | [DB] |
| Keyence LS-9030 / -M | 1D Schatten (LED) | Drehung je Prüfstelle | 15,7 min | rot | 4,5 min gelb (mit Mittelung) | ja, nur mit 2048-fach (±0,1 µm) | [DB] |
| Keyence LS-9006 / -D | 1D/2-Achs Schatten | Drehung | 15,7 min | rot | 4,5 min gelb | ±0,03 µm 2048-fach, **nur bis Ø 6 mm** | [DB] |
| Mitutoyo LSM-501S / -503S | 1D Laser-Scan | Drehung | 20,5 min | rot | 9,3 min rot (mit Mittelung) | ja, nur mit 512-fach (±0,04 / ±0,11 µm) | [DB] |
| Mitutoyo LSM-6902H/6900 | 1D Laser-Scan | Drehung | 44,5 min | rot | 33,3 min rot | ja, nur mit 1024-fach (±0,03 µm) | [DB] |
| Aeroel XLS13XY/1500 | 2-Achs Laser-Scan | ohne Drehung (2 Achsen) | 12,5 min | rot | 1,3 min gelb | ja: Einzelscan ±0,75 µm (Ø ≤ 3 mm) / ±1,5 µm (Ø > 3 mm) | [DB] |
| Aeroel XLS13XY/1500 | 2-Achs Laser-Scan | mit Drehung, Einzelscan [R, Zusatz] | 13,7 min | rot | 2,5 min gelb | ja, wie oben | [DB] |
| Nordson AccuScan 6012 | 4-Achs Laser-Scan | ohne Drehung | 12,5 min | rot | 1,3 min gelb | ja: Einzelscan ±1 µm ±0,025 % | [SE] |
| LaserLinc Triton312 | 3-Achs Laser-Scan | ohne Drehung, Einzelscan | 12,6 min | rot | 1,3 min gelb | ja: ungemittelt ±2,5 µm | [SE] |
| Zumbach ODAC 13TRIO | 3-Achs Laser-Scan | ohne Drehung, 0,1 s | 15,0 min | rot | 3,8 min gelb | ja, 0,12 µm (3σ, 0,1 s) | [SE] |
| Zumbach ODAC 14XY Standard | 2-Achs Laser-Scan | ohne Drehung, 0,1 s | 15,0 min | rot | 3,8 min gelb | ja, 0,16 µm (3σ, 0,1 s) | [SE] |
| Sikora LASER PRO 13 XY | 2-Achs Laser/CCD | ohne Drehung, Einzelmessung | 12,5 min | rot | 1,3 min gelb | unbekannt (±0,1 µm ohne Bedingung) | [SE] |
| Sikora LASER 2010 XY (abgekündigt) | 2-Achs Laser/CCD | ohne Drehung, 1 s | 37,5 min | rot | 26,3 min rot | ja, ±0,1 µm (±3σ, 1 s) | [SE] |
| Konfokal: ME IFC2466+IFS2406, IFD2415, Precitec CHRocodile 2 S, Keyence CL-3000, STIL CCS | Punkt, paarweise | Drehung je Prüfstelle | 12,5–13,4 min | rot | 1,3–2,2 min gelb | unbekannt für Durchmesser, Einzelwert | [SE] |
| Triangulation/Interferometer: Keyence LK-G5000, ME ILD2300/1900, Keyence SI-F, ME IMS5400 | Punkt, paarweise | Drehung | 12,5–12,9 min | rot | 1,3–1,6 min gelb | ILD2300: 0,03 µm „ohne Mittelung“ (Abstand), sonst unbekannt | [SE] |
| ME ODC2520, ODC1200, Omron ZX-GT, Panasonic HG-T, Keyence IG | 1D Laser/Lichtband | Drehung | 12,5–13,4 min | rot | 1,3–2,2 min gelb | Rep 1–140 µm, für µm-Toleranz zu grob | [DB]/[SE] |

**Grün ist in keinem Szenario erreichbar.** Für grün dürfte ein 1D-Sensor höchstens 60 s ÷ 1501 = 0,04 s je Prüfstelle brauchen, Stopp eingeschlossen. Ein 2D-Sensor bräuchte bei t_s = 0,05 s ein Feld von rund 90 mm (TM-X-Rate), 75 mm (RF656.2D, 50/s) bzw. 150 mm (RF657.2D, 24/s) [R].

---

## 2. Die Sensorfamilien im Einzelnen

### 2.1 Laser-Scan-Mikrometer mit Polygonspiegel: nur Aeroel nennt den Einzelscan im eigenen Datenblatt

Für Ø 1–6,5 mm kommen mehrere Laser-Scan-Köpfe in Frage. Die Wiederholgenauigkeiten sind aber nicht vergleichbar. Zumbach nennt 3σ bei 0,1 s, Sikora ±3σ bei 1 s, Mitutoyo ±2σ bei 0,32 s bzw. 1,28 s, Aeroel ±2σ bei 1 s und zusätzlich im Einzelscan. Nordson und LaserLinc nennen den Einzelscan bzw. den ungemittelten Wert. **Aeroel nennt als einziger Hersteller in einem Datenblatt im Repo einen Einzelscan-Wert: ±1 µm (/480), ±0,75 µm (/1500, Ø ≤ 3 mm) und ±1,5 µm (/1500, Ø > 3 mm).** Das ist rund 20- bis 40-mal mehr als der gemittelte Wert. Der Aeroel-Kopf hat außerdem zwei Digitaleingänge, die sich als Quadraturencoder programmieren lassen. Damit lässt sich jeder Scan einem Drehwinkel zuordnen ([DB] `Aeroel XLS13XY XLS35XY – Datenblatt/Original_AEROEL_xls_xy_de.pdf`, S. 2–4).

Mitutoyo-Werte aus dem lokalen Bulletin 2101 habe ich selbst gelesen. Die 3200 Scans/s und die 650-nm-Laserdiode (Klasse 2) gelten für alle Köpfe. Der externe Triggereingang „B5 RUN“ steuert die Einzel- oder Dauermessung ([DB] `Mitutoyo Laser Scan Micrometer – Bulletin 2101/Original_2101_Laser-Scan-Mic.pdf`, S. 8, 12, 14, Anschlussbelegung B5).

| Hersteller | Modell | Prinzip | Messbereich | kleinstes Objekt | Wiederholgenauigkeit (Bedingung) | Linearität / Genauigkeit | Rate | Achsen | Trigger / Encoder | Lichtquelle | Quelle | Beleg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aeroel / Marposs | XLS13XY/480 und /1500 (/A) | Laser-Scan | Ø 0,1–10 mm, Feld 13 × 13 mm (10 mm nur zentriert) | 0,1 mm | gemittelt ±0,15 µm (/480), ±0,04 µm (/1500); Bedingung „T = 1 s, ±2σ“ nur [SE]. Einzelscan ±2σ: ±1 µm (/480), ±0,75 µm (/1500, Ø ≤ 3 mm), ±1,5 µm (/1500, Ø > 3 mm) | ±0,5 µm zentriert; ±1,5 µm im ganzen Feld; ±1 µm im Feld 5 × 5 mm | 480 bzw. 1500 Hz je Achse | 2 (X+Y) | 2 Eingänge: Start/Stop, Pulszähler, **Quadraturencoder**; Modi Free-Running, Single-Shot, Auto-Sync | sichtbare Laserdiode | lokal S. 2–4; [Marposs XLS XY](https://www.marposs.com/media/9655/d-1/t-file/AEROEL_xls_xy_en.pdf) | [DB] |
| Aeroel | XLS13XY /B, /F | Laser-Scan | Ø 0,03 bzw. 0,02–3 mm (Feld 4 × 4 mm) | 0,03 / 0,02 mm | ±0,03 µm (/480), ±0,02 µm (/1500) | ±1 µm im Feld | wie oben | 2 | wie oben | wie oben | lokal S. 4 | [DB], **nur bis Ø 3 mm** |
| Mitutoyo | LSM-501S | Laser-Scan | 0,05–10 mm (Feld 4 × 10 mm) | 0,05 mm | ±0,04 µm; ±2σ, Ø 10 mm, „0.32 sec. interval (512-time average)“ | ±0,5 µm (ganzer Bereich); Lagefehler ±0,5 µm | 3200 Scans/s | 1 | ext. Trigger B5 RUN (Anzeige LSM-6200/6900/9506) | 650 nm, Klasse 2 | Bulletin 2101 S. 12 | [DB] |
| Mitutoyo | LSM-503S | Laser-Scan | 0,3–30 mm (Feld 10 × 30 mm) | 0,3 mm | ±0,11 µm; wie oben, 0,32 s / 512-fach | ±1,0 µm; Lagefehler ±1,5 µm | 3200 Scans/s | 1 | wie oben | 650 nm, Klasse 2 | Bulletin 2101 S. 14 | [DB] |
| Mitutoyo | LSM-6902H/6900 | Laser-Scan | 0,1–25 mm (Feld ±1,5 × 25 mm) | 0,1 mm | ±0,03 µm (Ø 10 mm), ±0,045 µm (Ø 25 mm); ±2σ, 1,28 s / 1024-fach | ±0,5 µm; Lagefehler ±0,5 µm | 3200/s | 1 | wie oben; Mittelung 2–2048 einstellbar | 650 nm, Klasse 2 | Bulletin 2101 S. 8 | [DB] |
| Mitutoyo | „LSM-902“ (Händlerangabe) | Laser-Scan | 0,1–25 mm | 0,1 mm | ±0,05 µm (Bedingung –) | – | 800 Scans/s | 1 | – | – | [ATEC](https://www.atecorp.com/products/mitutoyo/lsm-902) | [SE]; vermutlich identisch mit LSM-6902H, Werte widersprechen [DB] |
| Zumbach | ODAC 14XY Standard | Laser-Scan | 0,06–16 mm | 0,06 mm | 0,16 µm (3σ, Mittelung 0,1 s); zweiter Wert 0,07 µm, Bedingung abgeschnitten | – | 2 × 500 Scans/s; Ausgabe bis 125 Datenpakete/s | 2 | – | Laserdiode | [Zumbach ODAC 14XY](https://zumbach.com/app/uploads/odac14xy-odac.007.2014.en-.pdf), [Extrusion 5-2016](https://www.extrusion-info.com/upload/magazines/extrusion/5-2016/files/assets/basic-html/page-68.html) | [SE] |
| Zumbach | ODAC 14XY Micro | Laser-Scan | 0,015–3 mm | 0,015 mm | Zuordnung unklar | – | 2 × 500/s | 2 | – | Laserdiode | wie oben | [SE], **nur bis 3 mm** |
| Zumbach | ODAC 13TRIO (Standard/F/FF) | Laser-Scan | max. 13 mm empfohlen | 0,06 mm | 0,12 µm (3σ, 0,1 s; Standard und F) | – | 3 × 600 / 1500 / 3000 Scans/s; Ausgabe bis 200 Pakete/s | 3 | – | Laserdiode | [Zumbach 13TRIO](https://zumbach.com/app/uploads/odac13trio-odac.007.0313.en-.pdf), [ODAC](https://zumbach.com/products/odac/) | [SE] |
| Nordson / Beta LaserMike | AccuScan 6012 | Laser-Scan | 0,1–12 mm | 0,1 mm | ±1 µm ±0,025 % (Einzelscan) | ±0,5 µm | 2400 Scans/s je Achse | 4 | – | – | [tic.co.th Datenblatt](https://www.tic.co.th/storages/products/attachments/file_1170_5955.pdf), [DirectIndustry](https://pdf.directindustry.com/pdf/ndc-technologies/accuscan-6012/26204-593251.html) | [SE] |
| Nordson | AccuScan 5012 | Laser-Scan | – | – | Zeile „Single Scan“ vorhanden, Wert abgeschnitten | – | 2400/s je Achse | 2 | – | – | [Nordson AccuScan 5000](https://www.nordson.com/en/products/measurement-and-control-products/accuscan-5000) | [SE] |
| LaserLinc | Triton312 | Laser-Scan | 0,102–11,4 mm | 0,102 mm | ±2,5 µm ungemittelt; ±0,125 µm bei 2 s (Teile ≤ 10,2 mm) | – | 600 Hz je Achse | 3 | – | – | [Triton312 Specs](https://test.laserlinc.com/specs/Triton312_specs.html), [Findlight](https://www.findlight.net/uploads/products/datasheet/Triton312-Triple-Axis-Scanning-Laser-Micrometers.pdf) | [SE], Stand evtl. 2011 |
| Takikawa | LDM-303H | Laser-Scan | 0,3–30 mm | 0,3 mm | ±0,3 µm (Bedingung –) | ±2 µm | 400 Scans/s (Hochgeschwindigkeitsserie 2000/s) | 1 | – | – | [TJ Solution](https://www.tjsolution.com/Products/Takikawa/Specification_laser%20micrometer%20head.html), [Gaging.com](https://store.gaging.com/ldm-303h-takikawa-engineering-laser-scan-micrometer-with-30mm-beam) | [SE] |
| Takikawa | LDM-301H / 302H | Laser-Scan | 0,02–1 / 0,05–5 mm | 0,02 / 0,05 mm | 302H: 0,3 bzw. 0,25 µm (widersprüchlich) | ±1 µm | 400/s | 1 | – | – | [Scigate](https://scigate.com.sg/products/42-takikawa/7357-ldm-series-specifications) | [SE], **zu klein** |
| Proton Products | InteliSENS SL | Laser-Scan | bis 30 mm | – | ≤ ±0,02 % | ≤ ±0,05 % | – | – | – | – | [Proton Katalog 2026](https://protonproducts.com/wp-content/uploads/2026/08/proton-catalogue-wire-cable-2026-english.pdf) | [SE], keine Absolutwerte |

### 2.2 Schatten-Mikrometer mit Zeile (LED oder Laser): hohe Raten, Rep nur mit starker Mittelung

Die Schatten-Mikrometer haben die höchsten Raten (Keyence LS-9000 16 kHz, Micro-Epsilon ODC2700 15 kHz). **Ihre Wiederholgenauigkeiten gelten aber durchweg mit 1024- bis 2048-facher Mittelung am ruhenden Normal. Einen Einzelwert veröffentlicht keiner dieser Hersteller.** Bei Keyence sinken die 16.000/s außerdem mit der Zahl der aktiven OUTs und mit der Störunterdrückung. Um wie viel, steht nicht im Datenblatt (Fußnote *4). Beide Controller haben Encodereingänge: ODC2700 „3x Eingänge wahlweise für Encoder, Nullpunkt, Reset, Trigger“, LS-9500/9501 einen Encodereingang und zwei Synchroneingänge ([DB] ME-Katalog S. 13; LS-9000-Broschüre PDF-S. 13).

| Hersteller | Modell | Prinzip | Messbereich | kleinstes Objekt | Wiederholgenauigkeit (Bedingung) | Linearität (Bedingung) | Rate | Achsen | Trigger / Encoder | Lichtquelle | Quelle | Beleg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Micro-Epsilon | ODC2700-10 | LED-Schatten, Zeile | 10 mm | 0,05 mm (0,03 mm in Mitte) | ≤ 0,03 µm; 95 %, Mittelung 1024 Werte „über einen Zeitraum von 5 Minuten“, temperaturstabilisiert, 45 min Warmlauf | ≤ 0,5 µm (Z = ±0,5 mm), ≤ 1 µm (±1,5 mm), ≤ 2,5 µm (±2,5 mm), 2-mm-Prüfstift | 15 kHz Abtast- und Ausgaberate; Belichtung 8,5 µs | 1 | 3 Eingänge Encoder/Nullpunkt/Reset/Trigger; Sync-Ausgang | LED 508 nm, RG 1 | `Micro-Epsilon optoCONTROL – Katalog/…de.pdf` S. 13 | [DB] |
| Micro-Epsilon | ODC2700-40 | wie oben | 40 mm | 0,3 mm (0,1 mm in Mitte) | ≤ 0,1 µm; wie oben | ≤ 1 µm (Z = ±2,5 mm), ≤ 3 µm (±10 mm) | 15 kHz | 1 | wie oben | LED 508 nm, RG 0 | ME-Katalog S. 13 | [DB] |
| Micro-Epsilon | ODC2600-40 | LED-Schatten | 40 mm | 0,3 mm | ±1 µm (Option 209/210: ±1,5 µm); Fußnote nicht gesehen | < ±3 µm, „3 sigma; Kantenmessung ohne Mittelung“ | 2,3 kHz | 1 | – | LED | [ME dat ODC2600-40](https://www.micro-epsilon.com/download/products/dat--optoCONTROL-2600-40-Option-209-210--en.pdf) | [SE] |
| Micro-Epsilon | ODC2520-46 | Laser-Schatten | 46 mm | typ. ≥ 0,5 mm | ≤ 5 µm; gleitendes Mittel 32 Werte | < ±12 bis ±20 µm (3σ, je Abstand) | 2,5 kHz | 1 | TrigIn / SyncIn | Laser 670 nm, Kl. 1M | ME-Katalog S. 17 | [DB] |
| Micro-Epsilon | ODC1200 (5/10 mm) | Laser-Lichtband, analog | 5 / 10 mm | 0,05 / 0,1 mm | 40–140 µm (±2σ, statisches Rauschen über 3 min), Wert laut Repo-Analyse | – | 100 kHz (−3 dB) | 1 | – | Laser 670 nm, Kl. 1 | ME-Katalog S. 23 | [DB] |
| Keyence | LS-9030 / -M | LED-Schatten, CMOS-Zeile | 0,3–30 mm | 0,08 mm | ±0,1 µm; ±2σ, Normal Ø 10 mm, Mitte, 2048-fach | ±2 µm, bewegtes Normal Ø 10 mm im Bereich 10 × 20 mm | 16.000/s (sinkt mit Zahl der OUTs); Lageerkennung 4000/s | 1 | Encodereingang, Sync 1/2, Trigger (LS-9500/9501) | grüne InGaN-LED | `Keyence LS-9030 – Datenblatt` S. 1; Broschüre PDF-S. 4, 13 | [DB] |
| Keyence | LS-9030D | wie oben | 0,3–30 mm | 0,08 mm | ±0,1 µm (wie oben) | ±2 µm | 16.000/s | 2 | wie oben | grüne LED | `Keyence LS-9030D – Datenblatt` | [DB] |
| Keyence | LS-9006 / -D | LED-Schatten | 0,04–6 mm | 0,01 mm | ±0,03 µm; ±2σ, Normal **Ø 1,0 mm**, 2048-fach | ±0,5 µm, bewegtes Normal Ø 1 mm im Bereich 2 × 4 mm | 16.000/s | 1 / 2 | wie oben | grüne LED | `Keyence LS-9006(D) – Datenblatt` S. 1 | [DB], **nur bis Ø 6 mm** |
| Keyence | LS-9120M | LED-Schatten | 0,8–120 mm | – | ±0,3 µm (Ø 40 mm, 2048-fach) | ±8 µm | 16.000/s | 1 | wie oben | grüne LED | `Keyence LS-9120M – Datenblatt` S. 1 | [DB], zu grob |
| Keyence | LS-7030M | GaN-LED, CCD-Zeile | 0,3–30 mm | – | ±0,15 µm (Bedingung unklar) | ±2 µm | 2400/s | 1 | – | GaN-LED | [Keyence LS-7030M](https://www.keyence.com:443/products/measure/micrometer/ls-7000/models/ls-7030m/) | [SE], Vorgänger |
| Keyence | LS-7010M | wie oben | 0,04–6 mm | 0,04 mm | ±0,06 µm (Fußnotenzuordnung unklar) | ±0,5 µm | 2400/s | 1 | – | GaN-LED | [plc-direct](https://plc-direct.com/products/ls-7010m) | [SE], nur bis 6 mm |
| Sikora | LASER PRO 13 XY | Laser, Zeile | 0,1–13 mm | 0,1 mm | ±0,1 µm (Bedingung –) | ±0,5 µm (Faser-Katalog) | 5000 Messwerte/s je Achse | 2 | – | Laser | [Flyer LASER PRO](https://sikora.net/wp-content/uploads/Flyer_LASER_PRO_wc.pdf), [Catalog Optical Fibers](https://sikora.net/wp-content/uploads/Catalog_Optical_Fibers.pdf) | [SE] |
| Sikora | LASER 2010 XY | Laser-Fächer, CCD-Zeile, Beugung | 0,2–10 mm | 0,2 mm | ±0,1 µm, ±3σ über 1 s | ±0,5 µm | 500/s je Achse | 2 | – | Laser | [Sikora LASER Series 2000](https://sikora.net/wp-content/uploads/LASER_Series_2000_wc.pdf), [Radwell](https://www.radwell.com/Buy/SIKORA/SIKORA/LASER%202010%20XY) | [SE], abgekündigt |
| Sikora | LASER 2005 XY | wie oben | 0,05–5 mm | 0,05 mm | – | ±0,5 µm | 1200/s je Achse (Serie: 500) | 2 | – | Laser | wie oben | [SE], **nur bis 5 mm** |
| Omron | ZX-GT28 | Laser-Lichtband, CCD | 28 mm Breite | – | – | ±0,1 % v. E.; „10 µm“ teils Auflösung, teils Genauigkeit | 2000/s (Highspeed) | 1 | – | Laser 650 nm, Kl. 1 | [Omron](https://www.ia.omron.com/products/family/1918/specification.html) | [SE], zu grob |
| Panasonic | HG-T1010 | Laser-Durchlicht | 10 mm | Ø 0,5 mm | 1 µm P-P (Abstand widersprüchlich) | ±0,12 % v. E. | 0,5 ms Zyklus | 1 | – | Laser | [Panasonic HG-T](https://industry.panasonic.com/global/en/products/fasys/measurement/measurement/hg-t) | [SE], zu grob |
| Keyence | IG-010 / IG-028 | CCD-Laser, Lichtband | 10 / 28 mm | – | 5 µm (100 mm Abstand) | ±0,1 % | 490 µs | 1 | – | Laser 660 nm, Kl. 1 | [Keyence IG](https://www.keyence.com/products/measure/micrometer/ig/specs/) | [SE], zu grob |

### 2.3 2D-Bildsensoren: langsame Bildrate, aber viele Prüfstellen je Bild

Ein 2D-Schattenbild deckt mehrere Millimeter Rohr gleichzeitig ab. Dadurch braucht es nur 38 bis 150 statt 1501 Achsstopps. Das gleicht die 20- bis 300-mal niedrigere Rate aus. Die nötige Drehzahl ist mit 20–42 1/min auch für ein dünnes 3-m-Rohr realistisch. Der Nachteil: **RIFTEK nennt keine Wiederholgenauigkeit, nur einen Messfehler von ±0,8 bis ±4,5 µm, der nur in einem begrenzten Bereich entlang der optischen Achse gilt.** Die TM-X-Werte gelten mit 16-facher Mittelung. Welche Feldseite bei RIFTEK in Rohrrichtung liegt, ist nicht geprüft. Die Rechnung nimmt optimistisch die längere Seite.

| Hersteller | Modell | Prinzip | Feld (Messbereich) | kleinstes Objekt | Wiederholgenauigkeit (Bedingung) | Genauigkeit / Messfehler | Bild-/Messrate | Achsen | Trigger / Encoder | Lichtquelle | Quelle | Beleg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RIFTEK | RF656.2D-8x10 / -15x20 / -25x35 / -40x50 | LED-Schattenbild auf 2D-CMOS | 8 × 10 / 15 × 20 / 25 × 35 / 40 × 50 mm | 0,07 / 0,2 / 0,2 / 0,35 mm | keine Angabe | ±1,5 / ±2 / ±2,5 / ±4,5 µm, gültig bis ±1 / ±2 / ±3 / ±4 mm entlang der Achse | Sensor bis 65/s; mit Controller SuM 50/s; Belichtung 100 µs | 2D | 1 Synchronisationseingang; 2 Logikausgänge (1 als Belichtungs-Strobe) | LED 630 nm, EN 62471 sicher | `Riftek RF65x.2D – Handbuch…/Original_2D_Optical_Micrometers_eng.pdf` PDF-S. 4–7 | [DB] |
| RIFTEK | RF657.2D-15x20 / -25x35 / -40x50 / -60x80 | wie oben | 15 × 20 / 25 × 35 / 40 × 50 / 60 × 80 mm | 0,13 / 0,13 / 0,2 / 0,3 mm | keine Angabe | ±0,8 / ±1,2 / ±2 / ±3 µm, gültig bis ±5 / ±10 / ±15 / ±20 mm | 24/s (Sensor und SuM); Belichtung 15 µs | 2D | wie oben | LED 525 nm | Handbuch PDF-S. 6–7 | [DB] |
| RIFTEK | RF657R.2D-25 / -45 / -70 / -100 | wie oben, rundes Feld | Ø 25 / 45 / 70 / 100 mm | 0,1 / 0,13 / 0,2 / 0,3 mm | keine Angabe | ±0,8 / ±1,2 / ±2 / ±3 µm | 4/s; 15 µs | 2D | wie oben | LED 525 nm | Handbuch PDF-S. 6 | [DB] |
| Keyence | TM-X5006 | LED, telezentrisch, 2D | Ø 6 mm (Hochgenauigkeit Ø 4 mm); Tiefenschärfe 4 mm | – | ±0,03 µm; ±2σ, 16 Messungen, Glasmaßstab, Mitte | ±0,3 µm (Messbereich), ±0,2 µm (Hochgenauigkeit) | Triggerintervall ca. 24 ms (voll), ca. 3 ms („4/16“); Belichtung 25/50/100 µs | 2D | Triggerintervall bekannt, weitere E/A nicht gesehen | grüne InGaN-LED | `Keyence TM-X5006 – Datenblatt` S. 1 | [DB], **Ø 6,5 mm passt nicht ins Ø-6-mm-Feld** |
| Keyence | TM-X5040 | wie oben | Ø 40 mm (Hochgenauigkeit Ø 26 mm) | – | ±0,08 µm (16 Messungen) | ±1 µm (HG), ±2 µm | Serienwert 24 ms / 3 ms; Modellwert nicht gefunden | 2D | – | grüne LED | [Keyence TM-X5040](https://www.keyence.eu/products/measure/micrometer/tm-x5000/models/tm-x5040/), [Broschüre](https://movetec.fi/wp-content/uploads/2025/02/TM-X5000.pdf) | [SE] |
| Keyence | TM-X5065 | wie oben | Ø 65 mm (Hochgenauigkeit Ø 40 mm) | – | ±0,1 µm (16 Messungen) | ±1,2 µm (HG), ±2,2 µm | ca. 24 ms (voll), ca. 3 ms („4/16“) | 2D | – | grüne LED | [Keyence TM-X5065](https://www.keyence.com/products/measure/micrometer/tm-x5000/models/tm-x5065/) | [SE] |
| Keyence | TM-X5120 | wie oben | HG Ø 60 mm; Serie bis Ø 124 mm (Werbung: 120 mm) | – | – | – | Serienwert | 2D | – | grüne LED | [Keyence TM-X Specs](https://keyence.com/products/measure/micrometer/tm-x5000/specs) | [SE] |
| Opto Engineering | TC23-Reihe (Objektiv + eigene Kamera) | bi-telezentrisch | z. B. TC23036 ca. 29,3 × 22,1 mm, TC23048 38,75 × 28,97 mm, TC23072 58,44 × 43,69 mm | – | – (Systemwert hängt von Kamera und Software ab) | – | von der Kamera abhängig | 2D | Kamera | – | [TC23048](https://www.opto-e.com/en/products/tc-series/TC23048) | [SE] |

Zum Vergleich gibt es Wellenmessmaschinen mit Drehachse, nicht für 3 m ausgelegt. Sie taugen eher als Referenz. Mahr MarShaft SCOPE 250 plus misst 250 mm Länge mit MPE Ø ≤ (1,5 + d/40) µm und einer C-Achse von 0,2–60 1/min ([SE] [Mahr Datenblatt](https://metrology.mahr.com/en-us/products/datasheet/5361802-optische-wellenmessgeraete-marshaft-scope-250-plus.pdf)). Vicivision MTL X5/X10 erreicht (2 + D/100) µm bei bis zu 270 mm Teilelänge und 180 °/s ([SE] [MSI Viking](https://www.msi-viking.com/VICIVision-MTL-X5-Optical-Measuring-Machine)). Weitere Beispiele sind Jenoptik Opticline und Marposs Optoflash. Keyence LM-X und IM-X sind Tischgeräte.

### 2.4 Punktsensoren paarweise: schnell genug, aber ohne Durchmesser-Rep

Zwei gegenüberliegende Abstandssensoren sind die übliche Mindestanordnung. Der Durchmesser ergibt sich aus dem kalibrierten Kopfabstand minus beide Abstände. Eine Querverschiebung in Messrichtung hebt sich dabei auf ([SE] [Fischer, Uni Bremen 2018](https://media.suub.uni-bremen.de/bitstream/elib/8273/1/Fischer_Angular-Dependent%20Radius%20Measurements%20at%20Rotating%20Objects%20Using%20Underdetermined%20Sensor%20Systems_2018_accepted-version.pdf)). **Die Messraten (5–392 kHz) sind für die Taktzeit nie der Engpass. Für die Durchmessermessung an Ø 1–6,5 mm nennt aber keine Quelle eine Messunsicherheit.** Alle Werte sind Abstandswerte, meist mit starker Mittelung an Spiegel oder Glas. Der Zweikanal-Controller IFC2466 erfasst beide Kanäle synchron und hat einen Encoderanschluss. Für diese Anordnung passt er deshalb am besten ([SE] [Datenblatt IFC246x](https://www.micro-epsilon.com/fileadmin/download/excerpts/dax--confocalDT-IFC246x--en.pdf)).

| Hersteller | Modell | Prinzip | Messbereich | Messfleck (kleinstes Objekt) | Auflösung / Wiederholgenauigkeit (Bedingung) | Linearität | Rate | Achsen | Trigger / Encoder | Lichtquelle | Quelle | Beleg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Micro-Epsilon | IFS2406-3 an IFC2465/2466 | chrom. konfokal | 3 mm | 35 µm | statisch 50 nm, dynamisch 168 nm (Bedingungen nicht gesehen) | < ±1,5 µm | Controller 100 Hz–30 kHz; IFC2466 2 Kanäle synchron | 1 je Kopf | Encoder 15-pol. HD-Sub | – | [IFS2406](https://www.micro-epsilon.com/fileadmin/download/excerpts/dax--confocalDT-IFS2406--en.pdf), [IFC246x](https://www.micro-epsilon.com/fileadmin/download/excerpts/dax--confocalDT-IFC246x--en.pdf) | [SE] |
| Micro-Epsilon | IFS2407-0,1 | chrom. konfokal | 0,1 mm | 3 µm | – | – | über Controller | 1 | über Controller | – | [IFS2407](https://www.micro-epsilon.de/fileadmin/download/excerpts/dax--confocalDT-IFS2407--de.pdf) | [SE], Messbereich für Schlag zu klein |
| Micro-Epsilon | IFD2415 (1/3/10 mm) | konfokal, Controller integriert | 1 / 3 / 10 mm | 8 / 9 / 16 µm | – | – | bis 25 kHz | 1 | – | – | [ME IFD2410/2415](https://www.micro-epsilon.com/distance-sensors/confocal-sensors/confocaldt-ifd2410-2415/?sLang=en) | [SE] |
| Precitec | CHRocodile 2 S / 2 SE | chrom. konfokal / interferometrisch | je Messkopf (–) | – | axial 1 nm | 0,2 µm | 70 kHz (Datenblatt 09/2024) bzw. 66 kHz | 1 | – | – | [Precitec Übersicht](https://precitec.com/fileadmin/products/3d-metrology/chr-2s/Overview_interferometric_sensors_probes_datasheet.pdf) | [SE] |
| Keyence | CL-3000 + CL-P070G/N | chrom. konfokal | – | Ø 50 µm | Auflösung 0,025 / 0,25 µm bei 16.384-fach (Spiegel); Rep nicht angegeben | ±1,9 / ±2,0 µm | bis 10 kHz | 1 | – | – | [CL-P070G](https://www.keyence.com/products/measure/laser-1d/cl-3000/models/cl-p070g/) | [SE] |
| Keyence | CL-3000 + CL-P015N | chrom. konfokal | 15 mm ±1,3 mm | – | – | ±0,49 µm | – | 1 | – | – | [CL-P015N](https://www.keyence.com/products/measure/laser-1d/cl-3000/models/cl-p015n/) | [SE] |
| STIL / Marposs | CCS Optima+ / CCS Prima | chrom. konfokal | je Kopf | CL-MG ca. 1,8–8,8 µm | – | – | bis 10 kHz / 100–2000 Hz | 1 | – | Weißlicht-LED | [MedicalExpo](https://www.medicalexpo.com/prod/marposs/product-300922-2808458.html) | [SE] |
| Keyence | LK-G5000 + LK-H008 | Laser-Triangulation | – | Ø 20 µm | 0,005 µm (Bedingung –); typ. 0,001 µm bei 65.536-fach, 200 µs | – | bis 392 kHz (Serie) | 1 | – | Laser | [LK-H008](https://www.keyence.com/products/measure/laser-1d/lk-g5000/models/lk-h008/) | [SE] |
| Micro-Epsilon | ILD2300-2 / -2DR | Laser-Triangulation | 2 mm | 70 × 70 µm Mitte (DR 8,5 × 11 µm); 255 × 350 µm am MB-Anfang | 0,03 µm, „mit 10 kHz, ohne Mittelung“ (Abstand) | ab 0,02 % MB | bis 49,14 kHz | 1 | – | Laser | [optoNCDT 2300](https://www.micro-epsilon.com/fileadmin/download/excerpts/dax--optoNCDT-2300--en.pdf) | [SE] |
| Micro-Epsilon | ILD1900 | Laser-Triangulation | – | – | 0,1 µm | ab 0,02 % | bis 10 kHz | 1 | – | Laser | [Katalog optoNCDT](https://www.micro-epsilon.com/download/products/cat--optoNCDT--en.pdf) | [SE] |
| Keyence | SI-F01 / SI-F10 | Spektralinterferenz | 0,05–1,1 / 11,3–12,35 mm | Ø 20 / 40 µm | Auflösung 0,001 µm (4096-fach, Glas) | – | 5 kHz | 1 | – | – | [SI-F01](https://www.keyence.com/products/measure/spectral/si-f/models/si-f01/) | [SE] |
| Micro-Epsilon | IMS5400-DS0.5 | Interferometer | 1,5 mm | ca. 10 µm | – (Messwinkel nur ±2°) | – | 100 Hz–6 kHz | 1 | – | – | [IMS5400-DS0.5](https://www.micro-epsilon.com/download/products/dat--interferoMETER-IMS5400-DS0-5-90-VAC--en.pdf) | [SE] |

Kapazitive Sensoren (capaNCDT) wurden ohne verwertbare Werte gefunden. Polytec und Lumetrics sind nicht recherchiert. Beim ILD2300 liegt der Messfleck am Messbereichsanfang (255 × 350 µm) in der Größe des Rohrradius bei Ø 1 mm. Das ist ungünstig. Die konfokalen Flecke (3–50 µm) mitteln die Krümmung kaum.

### 2.5 Fertige Prüfplätze: keiner für 3 m belegt

Am nächsten kommt LaserLinc Metron: 3-Achs-Mikrometer, motorischer Schlitten, optional 360°-Drehung, für Teile bis 1,8 m ([SE] [LaserLinc Metron](https://laserlinc.com/metron-an-automated-tubing-guidewire-inspection-solution)). BenchLinc und Nordson BenchMike Pro drehen die Probe in vorgegebene Winkel, BenchLinc mit bis zu 100 Messungen. Cerulean CD Express nimmt 100 Messungen je Umdrehung auf ([SE] [LaserLinc Offline-Broschüre](https://laserlinc.com/wp-content/uploads/2021/07/LaserLinc_Offline_Brochure-25th.pdf), [The Engineer](https://www.theengineer.co.uk/content/news/high-speed-laser-micrometer-measures-circumference-diameter-and-ovality-of-cylindrical-objects)). Taktzeiten oder Vorschübe veröffentlicht keiner dieser Anbieter.

---

## 3. Taktzeit-Rechnung [R]

### 3.1 Formeln

Alle Werte in diesem Abschnitt sind **eigene Rechnung (KI)** nach dem Modell aus dem Auftrag. Gerechnet wird mit N = 1501 Prüfstellen und 72 Werten je Umdrehung. Ampel: grün < 1 min, gelb 1–5 min, rot > 5 min.

- **1D-Sensor oder Punktpaar mit Drehung je Prüfstelle:** T = 1501 × (max(72 ÷ Rate; Mittelungszeit laut Rep-Bedingung) + t_s). Variante „Einzelscan“: T = 1501 × (72 ÷ Rate + t_s). Dann gilt nur die Einzelscan-Wiederholgenauigkeit, und die kennt man meist nicht.
- **Mehrachskopf ohne Drehung:** T = 1501 × (Messzeit je Punkt + t_s). **Ø max − Ø min wird nur zwischen den 2–4 Achsen erfasst, nicht über 72 Winkel.** Die Anforderung „Querschnitt über den Umfang“ ist damit nicht erfüllt.
- **2D-Bild mit Drehung je Station:** Stationen = ⌈3000 mm ÷ Feldlänge⌉; T = Stationen × (72 ÷ Bildrate + t_s).
- **Nötige Drehzahl:** n = 60 ÷ (Zeit je Umdrehung) [1/min], mit Zeit je Umdrehung = 72 ÷ Rate (bzw. die Mittelungszeit, wenn diese größer ist).
- **Winkelsynchron gemittelt (Zusatzrechnung):** Wenn die Rep-Bedingung des Datenblatts an jedem der 72 Winkel gelten soll, braucht jeder Winkel die volle Mittelung. Dann gilt T = 1501 × (72 × Mittelungszeit + t_s).

**Hinweis zur Mittelung:** Eine zeitliche Mittelung bei drehendem Rohr mittelt über den Winkel. Beim LS-9030 überstreichen 0,128 s Mittelung bei der Drehzahl der Variante A eine volle Umdrehung. Die Form ginge dabei verloren. Zulässig ist eine Mittelung nur winkelsynchron (encodergetriggert, über mehrere Umdrehungen am gleichen Winkel) oder bei stehendem Rohr. Variante A ist daher als Untergrenze zu lesen. Die ehrlichen Kosten der Datenblatt-Rep zeigt die Spalte „winkelsynchron“.

### 3.2 Taktzeit-Tabelle

A = mit Mittelung laut Rep-Bedingung, E = Einzelscan / Einzelmessung, OD = Mehrachskopf ohne Drehung. Zeiten in Minuten; Ampel in Klammern (g = grün, ge = gelb, r = rot).

| Sensor | Rate (Annahme) | Var. | Zeit je Umdr. / Punkt | Drehzahl n | t_s 0,5 s | t_s 0,1 s | t_s 0,05 s | winkelsynchron (0,5 s) | Rep in dieser Variante |
|---|---|---|---|---|---|---|---|---|---|
| Keyence LS-9030 / -M / -D, LS-9006 | 16.000/s (Obergrenze) | A (2048-fach) | 0,128 s | 469 1/min | 15,7 (r) | 5,7 (r) | 4,5 (ge) | 243 min | ±0,1 µm (LS-9006 ±0,03 µm), aber über den Winkel gemittelt |
| dto. | 16.000/s | E | 0,0045 s | 13.333 1/min | 12,6 (r) | 2,6 (ge) | 1,4 (ge) | – | unbekannt |
| Keyence LS-9030D | 16.000/s | OD (2 Achsen) | 0,128 s | – | 15,7 (r) | 5,7 (r) | 4,5 (ge) | – | ±0,1 µm, nur 2 Achsen |
| ME ODC2700-10 / -40 | 15.000/s | A (1024-fach) | 0,068 s | 878 1/min | 14,2 (r) | 4,2 (ge) | 3,0 (ge) | 135 min | ≤ 0,03 / 0,1 µm, über den Winkel gemittelt |
| dto. | 15.000/s | E | 0,0048 s | 12.500 1/min | 12,6 (r) | 2,6 (ge) | 1,4 (ge) | – | unbekannt |
| ME ODC2600-40 | 2300/s | E | 0,031 s | 1917 1/min | 13,3 (r) | 3,3 (ge) | 2,0 (ge) | – | ±1 µm, Bedingung unbekannt |
| Keyence LS-7030M | 2400/s | E | 0,030 s | 2000 1/min | 13,3 (r) | 3,3 (ge) | 2,0 (ge) | – | ±0,15 µm, Bedingung unklar |
| ME ODC2520-46 | 2500/s | A (32-fach) = E | 0,029 s | 2083 1/min | 13,2 (r) | 3,2 (ge) | 2,0 (ge) | 35,6 min | ≤ 5 µm (zu grob) |
| ME ODC1200 | 100 kHz | E | 0,0007 s | – | 12,5 (r) | 2,5 (ge) | 1,3 (ge) | – | 40–140 µm (zu grob) |
| Omron ZX-GT / Panasonic HG-T / Keyence IG | ca. 2000/s | E | 0,036 s | 1667 1/min | 13,4 (r) | 3,4 (ge) | 2,1–2,2 (ge) | – | 1–10 µm (zu grob) |
| Sikora LASER PRO 13 XY | 5000/s je Achse | E (gedreht) | 0,014 s | 4167 1/min | 12,9 (r) | 2,9 (ge) | 1,6 (ge) | – | ±0,1 µm ohne Bedingung |
| dto. | 5000/s | OD (2 Achsen) | 0,0002 s | – | 12,5 (r) | 2,5 (ge) | 1,3 (ge) | – | unbekannt, nur 2 Achsen |
| Sikora LASER 2010 XY | 500/s | OD, 1 s | 1 s | – | 37,5 (r) | 27,5 (r) | 26,3 (r) | – | ±0,1 µm (1 s), nur 2 Achsen |
| dto. | 500/s | E (gedreht) | 0,144 s | 417 1/min | 16,1 (r) | 6,1 (r) | 4,9 (ge) | – | unbekannt |
| Aeroel XLS13XY/1500 | 1500/s je Achse | OD, Einzelscan | 0,0007 s | – | 12,5 (r) | 2,5 (ge) | 1,3 (ge) | – | ±0,75 / ±1,5 µm, nur 2 Achsen |
| dto. | 1500/s | E (gedreht) | 0,048 s | 1250 1/min | 13,7 (r) | 3,7 (ge) | 2,5 (ge) | – | **±0,75 µm (Ø ≤ 3) / ±1,5 µm (Ø > 3) [DB]** |
| dto. | 1500/s | A (T = 1 s) | 1 s | 60 1/min | 37,5 (r) | 27,5 (r) | 26,3 (r) | 1814 min | ±0,04 µm (T = 1 s nur [SE]) |
| Aeroel XLS13XY/480 | 480/s | E (gedreht) | 0,150 s | 400 1/min | 16,3 (r) | 6,3 (r) | 5,0 (r, knapp) | – | ±1 µm [DB] |
| dto. | 480/s | OD, Einzelscan | 0,0021 s | – | 12,6 (r) | 2,6 (ge) | 1,3 (ge) | – | ±1 µm, nur 2 Achsen |
| Mitutoyo LSM-501S / -503S | 3200/s | A (0,32 s / 512-fach) | 0,32 s | 188 1/min | 20,5 (r) | 10,5 (r) | 9,3 (r) | 589 min | ±0,04 / ±0,11 µm, über den Winkel gemittelt |
| Mitutoyo LSM-6902H | 3200/s | A (1,28 s / 1024-fach) | 1,28 s | 47 1/min | 44,5 (r) | 34,5 (r) | 33,3 (r) | 2318 min | ±0,03 µm |
| Mitutoyo (alle) | 3200/s | E | 0,0225 s | 2667 1/min | 13,1 (r) | 3,1 (ge) | 1,8 (ge) | – | unbekannt |
| Takikawa LDM-303H | 400/s (HS 2000/s) | E | 0,18 s (0,036 s) | 333 (1667) 1/min | 17,0 (13,4) (r) | 7,0 (r) / 3,4 (ge) | 5,8 (r) / 2,2 (ge) | – | ±0,3 µm, Bedingung unbekannt |
| Zumbach ODAC 14XY Std | 500/s je Achse | OD, 0,1 s | 0,1 s | – | 15,0 (r) | 5,0 (r, knapp) | 3,8 (ge) | – | 0,16 µm (3σ, 0,1 s), nur 2 Achsen |
| dto. | 500/s (Ausgabe 125/s) | E (gedreht) | 0,144 s (0,576 s) | 417 (104) 1/min | 16,1 (26,9) (r) | 6,1 (16,9) (r) | 4,9 (ge) / 15,7 (r) | – | unbekannt |
| Zumbach ODAC 13TRIO | 600/s je Achse | OD, 0,1 s | 0,1 s | – | 15,0 (r) | 5,0 (r, knapp) | 3,8 (ge) | – | 0,12 µm (3σ, 0,1 s), nur 3 Achsen |
| dto. | 600/s | OD, Einzelscan | 0,0017 s | – | 12,6 (r) | 2,5 (ge) | 1,3 (ge) | – | unbekannt |
| Nordson AccuScan 6012 | 2400/s je Achse | OD, Einzelscan | 0,0004 s | – | 12,5 (r) | 2,5 (ge) | 1,3 (ge) | – | ±1 µm ±0,025 % (bei Ø 6,5 mm ≈ ±2,6 µm [R]), nur 4 Achsen |
| dto. | 2400/s | E (gedreht) | 0,030 s | 2000 1/min | 13,3 (r) | 3,3 (ge) | 2,0 (ge) | – | wie oben |
| LaserLinc Triton312 | 600/s je Achse | OD, 2 s | 2 s | – | 62,5 (r) | 52,5 (r) | 51,3 (r) | – | ±0,125 µm (2 s), nur 3 Achsen |
| dto. | 600/s | OD, ungemittelt | 0,0017 s | – | 12,6 (r) | 2,5 (ge) | 1,3 (ge) | – | ±2,5 µm |
| Konfokal ME IFC2466 / IFD2415 | 30 / 25 kHz | E | 0,0024–0,0029 s | 25.000 / 20.833 1/min | 12,6 (r) | 2,6 (ge) | 1,3 (ge) | – | unbekannt (Durchmesser) |
| Precitec CHRocodile 2 S | 66–70 kHz | E | 0,001 s | ca. 57.000 1/min | 12,5 (r) | 2,5 (ge) | 1,3 (ge) | – | unbekannt |
| Keyence CL-3000, STIL CCS Optima+ | 10 kHz | E | 0,0072 s | 8333 1/min | 12,7 (r) | 2,7 (ge) | 1,4 (ge) | – | unbekannt |
| STIL CCS Prima | 2 kHz | E | 0,036 s | 1667 1/min | 13,4 (r) | 3,4 (ge) | 2,2 (ge) | – | unbekannt |
| Keyence LK-G5000 | 392 kHz | E | 0,0002 s | – | 12,5 (r) | 2,5 (ge) | 1,3 (ge) | – | unbekannt (0,005 µm, Bedingung –) |
| ME ILD2300 | 10 kHz (Rep-Bedingung) | E | 0,0072 s | 8333 1/min | 12,7 (r) | 2,7 (ge) | 1,4 (ge) | – | 0,03 µm ohne Mittelung (Abstand, nicht Ø) |
| ME ILD1900 | 10 kHz | E | 0,0072 s | 8333 1/min | 12,7 (r) | 2,7 (ge) | 1,4 (ge) | – | 0,1 µm, Bedingung unbekannt |
| Keyence SI-F01 | 5 kHz | E | 0,0144 s | 4167 1/min | 12,9 (r) | 2,9 (ge) | 1,6 (ge) | – | unbekannt |
| ME IMS5400 | 6 kHz | E | 0,012 s | 5000 1/min | 12,8 (r) | 2,8 (ge) | 1,6 (ge) | – | unbekannt |

**2D-Bildsensoren** (Zeit je Station = 72 ÷ Bildrate + t_s):

| Sensor | Feldlänge in Rohrrichtung | Stationen | Bildrate | Zeit je Umdr. | n | t_s 0,5 s | t_s 0,1 s | t_s 0,05 s | Bemerkung |
|---|---|---|---|---|---|---|---|---|---|
| Keyence TM-X5065 | 65 mm (HG 40 mm) | 47 (75) | 41,7/s (24 ms) | 1,73 s | 35 1/min | **1,7 (ge)** / 2,8 (ge) | 1,4 (ge) | 1,4 (ge) | [SE]; Rep ±0,1 µm gilt mit 16 Bildern je Winkel |
| Keyence TM-X5040 | 40 mm (HG 26 mm) | 75 (116) | 41,7/s (Serienwert) | 1,73 s | 35 1/min | **2,8 (ge)** / 4,3 (ge) | 2,3 (ge) | 2,2 (ge) | [SE]; Triggerintervall des Modells nicht belegt |
| Keyence TM-X5006 | 6 mm (HG 4 mm) | 500 (750) | 41,7/s | 1,73 s | 35 1/min | 18,6 (r) / 27,9 (r) | 15,2 (r) | 14,8 (r) | [DB]; Ø 6,5 mm passt nicht |
| TM-X5006 im Modus „4/16“ | ≤ 6 mm (unbekannt) | ≥ 500 | 333/s (3 ms) | 0,22 s | 278 1/min | ≥ 6,0 (r) | ≥ 2,6 (ge) | ≥ 2,2 (ge) | **optimistisch**, Feld im 4/16-Modus unbekannt |
| RIFTEK RF656.2D-40x50 | 50 mm (optimistisch) | 60 | 50/s (SuM) | 1,44 s | 42 1/min | **1,9 (ge)** | 1,5 (ge) | 1,5 (ge) | [DB]; Messfehler ±4,5 µm |
| RIFTEK RF656.2D-25x35 | 35 mm | 86 | 50/s | 1,44 s | 42 1/min | **2,8 (ge)** | 2,2 (ge) | 2,1 (ge) | [DB]; ±2,5 µm |
| RIFTEK RF656.2D-15x20 | 20 mm | 150 | 50/s | 1,44 s | 42 1/min | **4,8 (ge)** | 3,9 (ge) | 3,7 (ge) | [DB]; ±2 µm |
| RIFTEK RF656.2D-8x10 | 10 mm | 300 | 50/s (Sensor allein bis 65/s) | 1,44 s (1,11 s) | 42 (54) 1/min | 9,7 (r) (8,0) | 7,7 (r) | 7,5 (r) | [DB]; ±1,5 µm |
| RIFTEK RF657.2D-60x80 | 80 mm | 38 | 24/s | 3,0 s | 20 1/min | **2,2 (ge)** | 2,0 (ge) | 1,9 (ge) | [DB]; ±3 µm |
| RIFTEK RF657.2D-40x50 | 50 mm | 60 | 24/s | 3,0 s | 20 1/min | **3,5 (ge)** | 3,1 (ge) | 3,0 (ge) | [DB]; ±2 µm |
| RIFTEK RF657.2D-25x35 | 35 mm | 86 | 24/s | 3,0 s | 20 1/min | 5,0 (r, knapp) | 4,4 (ge) | 4,4 (ge) | [DB]; ±1,2 µm |
| RIFTEK RF657.2D-15x20 | 20 mm | 150 | 24/s | 3,0 s | 20 1/min | 8,8 (r) | 7,8 (r) | 7,6 (r) | [DB]; ±0,8 µm |
| RIFTEK RF657R.2D-25 / -45 / -70 / -100 | 25 / 45 / 70 / 100 mm | 120 / 67 / 43 / 30 | 4/s | 18 s | 3,3 1/min | 37,0 / 20,7 / 13,3 / 9,3 (r) | 36,2 / 20,2 / 13,0 / 9,1 (r) | 36,1 / 20,2 / 12,9 / 9,0 (r) | [DB] |
| Eigenbau TC23036 / TC23048 / TC23072 + Kamera | 29,3 / 38,75 / 58,44 mm | 103 / 78 / 52 | frei | – | – | für < 5 min: ≥ 30 / 22 / 14 Bilder/s | ≥ 26 / 19 / 13 | ≥ 25 / 19 / 13 | Mindestrate [R]; Genauigkeit selbst nachzuweisen |

### 3.3 Was die Zahlen bedeuten

Vier Befunde ändern das Bild gegenüber einem reinen Vergleich der Messraten.

**Erstens setzt der Achsstopp die Untergrenze.** Bei t_s = 0,5 s kostet das Anhalten an 1501 Prüfstellen 12,5 min. Jeder Sensor mit einer Station je Prüfstelle ist damit rot, egal wie schnell er misst. Unter 5 min kommt man nur, wenn die Zeit je Umdrehung höchstens 300 s ÷ 1501 − t_s beträgt. Das sind 0,10 s bei t_s = 0,1 s und 0,15 s bei t_s = 0,05 s. Der Sensor braucht dann mindestens 721 bzw. 480 Werte/s. Das Rohr muss sich mit mindestens 600 bzw. 400 1/min drehen [R].

**Zweitens ist die Drehzahl in der Einzelscan-Variante unrealistisch hoch.** Ein LS-9030 oder ODC2700 setzt im Modell 12.500–13.300 1/min voraus, ein konfokaler Sensor 8.000–57.000 1/min. Das ist für ein 3 m langes Nitinol-Rohr mit Ø 1 mm nicht ernsthaft denkbar. In der Praxis begrenzt die zulässige Drehzahl des Rohrs die Taktzeit, nicht die Sensorrate. Bei 60 1/min (1 s je Umdrehung) kämen alle 1D- und Punktsensoren auf 1501 × 1,5 s = 37,5 min. Die Drehzahl steht nicht im Modell des Auftrags und gehört als Grenze an den Mechanikentwurf.

**Drittens ist die gute Wiederholgenauigkeit im Takt nicht zu haben.** Die Datenblattwerte von ±0,03–0,11 µm brauchen 0,07–1,28 s Mittelung. Winkelsynchron an 72 Winkeln dauert das 2,3 h (ODC2700) bis 39 h (LSM-6902H) je Rohr. Belastbare Einzelscan-Werte gibt es nur bei Aeroel XLS13XY (±0,75–1,5 µm [DB]), AccuScan 6012 (±1 µm ±0,025 % [SE]) und Triton312 (±2,5 µm [SE]). Die Rechnung im Repo hatte für den LS-9030 grob σ ≈ 2,3 µm je Einzelabtastung geschätzt (`projekt/Analyse_Sensorik_Messprinzip_2026-11-22.md`, Abschnitt 2.2). Die Werte passen in der Größenordnung zusammen.

**Viertens liefern 2D-Sensoren als einzige gelb bei 0,5 s, und das bei realistischen 20–42 1/min.** Der Preis ist eine Genauigkeit im Bereich ±0,8–4,5 µm (RIFTEK, ohne Rep-Angabe) oder ±1,2–2,2 µm (TM-X5065, [SE]). Je größer das Feld, desto kürzer der Takt und desto größer der Messfehler. Das ist der zentrale Zielkonflikt.

Wegen der Symmetrie des Durchmessers (Ø bei φ und φ + 180° sind gleich) würden 36 Werte über eine halbe Umdrehung genügen. Das halbiert die Messzeit je Station, nicht aber den Stopp. Das Modell des Auftrags rechnet mit 72 Werten und einer vollen Umdrehung; die Halbierung ist hier nicht eingerechnet.

---

## 4. Grenzen und Lücken

**Gesperrte Hosts.** Kein Datenblatt ließ sich in dieser Sitzung aus dem Netz öffnen. Gesperrt waren zumbach.com, sikora.net, nordson.com, laserlinc.com, gifa.de, tic.co.th, micro-epsilon.com/.de, keyence.com/.eu/.co.in, ia.omron.com, riftek.com, jenoptik.us, metrology.mahr.com, precitec.com, scigate.com.sg, willrich.com und metrology.news. Laut Auftrag außerdem mitutoyo.com, marposs.com, res.cloudinary.com und pdf.directindustry.com. [DB] gilt nur für die lokal abgelegten Datenblätter: Keyence LS-9006/-D/-M, LS-9030/-D/-M, LS-9120M, LS-9000-Broschüre, TM-X5006, Micro-Epsilon optoCONTROL-Katalog, RIFTEK-Handbuch RF65x.2D, Aeroel XLS13XY/XLS35XY (DE) und Mitutoyo Bulletin 2101.

**Fehlende Angaben.** Ein Encoder- oder Sync-Eingang ist belegt bei Aeroel, Micro-Epsilon ODC2700/2520, Keyence LS-9500, RIFTEK (1 Sync-Eingang) und Mitutoyo (Trigger B5 RUN). Bei IFC246x ist er nur als Suchergebnis belegt. Für Zumbach, Sikora, Nordson, LaserLinc, Takikawa, Precitec, STIL und Keyence TM-X/CL/LK fehlt die Angabe. Lichtquelle und Laserklasse fehlen bei den meisten Laser-Scan-Köpfen außer Aeroel und Mitutoyo. Folgende Werte fehlen ganz: das Triggerintervall des TM-X5040 und die Feldgröße im TM-X-Modus „4/16“, die Feldausrichtung bei RIFTEK, der Einzelscan-Wert der Schatten-Mikrometer, der Messbereich des AccuScan 5012 sowie jede Durchmesser-Messunsicherheit für paarweise Punktsensoren. Eine veröffentlichte %GRR-Studie an Rohren Ø 1–6,5 mm wurde nicht gefunden.

**Widersprüchliche Werte.** Wo ein Datenblatt [DB] vorliegt, gilt dessen Wert.

| Größe | Werte | Gilt |
|---|---|---|
| ODC2700 Rate und Lichtquelle | 5 kHz, „Laser-Lichtvorhang“ [SE] gegen 15 kHz, LED 508 nm [DB] | [DB] |
| LS-9000 Wiederholgenauigkeit | „nicht gefunden“ [SE] gegen ±0,1 µm, 2048-fach [DB] | [DB] |
| Aeroel XLS13XY gemittelt | ±0,01 / ±0,02 / ±0,2 µm [SE] gegen ±0,04 µm (/1500) [DB]; Rate 960/3000 Hz (ältere Broschüre) gegen 480/1500 Hz [DB] | [DB] |
| Mitutoyo LSM-902 / 6902H | 800 Scans/s, ±0,05 µm [SE] gegen 3200/s, ±0,03 µm [DB] | [DB] |
| Mitutoyo Mittelungszeit | 512 ÷ 3200/s = 0,16 s [R] gegen „0.32 sec. interval (512-time average)“ [DB]. Hier mit 0,32 s gerechnet. Die Repo-Analyse rechnete für LSM-501S effektiv mit 0,16 s (16,5 statt 20,5 min) | [DB] |
| RIFTEK RF656.2D Rate | bis 65/s (Sensor) gegen 50/s (Controller SuM) [DB]; ein Katalog nennt 130/50 Hz [SE] | 50/s mit SuM |
| RIFTEK Feldgrößen | Katalog 2024: 25 × 30, 30 × 40 mm [SE] gegen Handbuch 15 × 20, 25 × 35 mm [DB] | [DB] |
| Precitec CHRocodile 2 S | 66 kHz gegen 70 kHz [SE] | offen |
| Zumbach ODAC 13TRIO FF | 3 × 3000/s gegen „9000 measurements per second“ [SE]; vermutlich Summe der Achsen | offen |
| Sikora LASER 2005 XY | 1200/s gegen 500/s je Achse (Serie) [SE] | offen |
| Keyence TM-X5120 | Ø 124 mm gegen Ø 120 mm [SE] | offen |
| Keyence LS-7010M | Rep-Fußnote „20-mm-Stab“ passt nicht zu 6-mm-Kopf [SE] | offen |
| Panasonic HG-T1010 / Omron ZX-GT | Abstandsbezug der Rep bzw. „10 µm“ als Auflösung oder Genauigkeit [SE] | offen |

**Modellgrenzen.** Nicht enthalten sind Verfahrzeit zwischen den Stationen, Beschleunigung des Drehservos, Einlegen und Entnehmen sowie die höchste zulässige Drehzahl des Rohrs. Ebenso fehlen Schlag, Durchbiegung und Schwingung des drehenden Rohrs. Die Lage entlang der optischen Achse begrenzt bei allen Sensoren die Genauigkeit, etwa bei ODC2700 (±0,5–2,5 mm) und RIFTEK (±1–20 mm).

---

## 5. Empfehlung: Datenblätter und Herstellerfragen

**Datenblätter beschaffen (Priorität nach Ampel und Lücke).** An erster Stelle steht das Datenblatt **Keyence TM-X5040 und TM-X5065** mit Triggerintervall je Modell, Feldgröße im Modus „4/16“, Encoder- und Triggereingängen des Controllers und der Fußnote zur Wiederholgenauigkeit. Diese beiden sind die einzigen gelben Kandidaten mit Sub-µm-Angabe und stehen bisher nur als Suchergebnis da. Zweitens das **RIFTEK-Datenblatt bzw. Maßzeichnungen RF656.2D/RF657.2D**, damit klar ist, welche Feldseite in Rohrrichtung liegt. Davon hängt die Stationszahl ab. Drittens das Datenblatt **Nordson AccuScan 6012** (tic.co.th oder ingras.net) und **LaserLinc Triton312** in aktueller Fassung; beide nennen Einzelscan-Werte. Viertens **Zumbach ODAC 14XY und 13TRIO** (Bedingung des zweiten Rep-Werts, Ausgaberate, Trigger) sowie **Sikora LASER PRO 13 XY** (Rep-Bedingung). Fünftens **Micro-Epsilon ODC2600-40** (DE-Datenblatt mit Fußnoten) und **IFC2466/IFS2406** mit Handbuchkapitel „Encoder Inputs“. Für den Abruf müssen die oben genannten Hosts in den Netzeinstellungen der Sitzung freigegeben werden. Andernfalls legt Janek die PDFs selbst unter `docs/archiv/6 Recherche Messtechnik/` ab.

**Offene Herstellerfragen.**

| Hersteller | Frage |
|---|---|
| Keyence (LS-9000, TM-X) | Wiederholgenauigkeit bei Einzelmessung und bei 16-/64-/256-facher Mittelung, für Ø 1 mm und Ø 6,5 mm. Wie stark sinkt die 16-kHz-Rate je aktivem OUT? Lässt sich winkelsynchron über den Encodereingang mitteln? Triggerintervall und Feld des TM-X5040/5065 im Modus „4/16“. |
| Micro-Epsilon (ODC2700, ODC2600, IFC2466) | Rep ohne Mittelung bzw. mit 8–64 Werten. Bedeutung von „1024 Werte über einen Zeitraum von 5 Minuten“. Encoder-getriggerte Erfassung je Winkelschritt. Erreichbare Durchmesser-Unsicherheit mit zwei konfokalen Köpfen an Ø 1–6,5 mm, Metall blank. |
| RIFTEK | Wiederholgenauigkeit (±2σ, Einzelbild) je Feld. Feldorientierung. Höchste Bildrate über den Sync-Eingang mit SuM. Ist für Ø 1 mm eine Kantenauflösung im Sub-µm-Bereich erreichbar? |
| Aeroel / Marposs | Einzelscan-Rep für Ø 3–6,5 mm am /480 (bisher nur /1500 > 3 mm: ±1,5 µm). Bedingung „T = 1 s“ am Originaldatenblatt bestätigen. Höchste Ausgaberate je Scan bei Encoder-Sync. |
| Mitutoyo | Warum 0,32 s für 512 Mittelungen bei 3200 Scans/s? Rep im Einzelscan. Ausgaberate der Einzelscans über RS-232C/USB. |
| Nordson, LaserLinc, Zumbach, Sikora | Encoder-/Trigger-Eingang zur Winkelsynchronisation. Einzelscan-Rep bei Ø 1 mm. Datenrate je Scan an der Schnittstelle (Zumbach: 125 bzw. 200 Pakete/s begrenzen eine Drehmessung). |
| Betrieb (Postfach) | Welcher Achsstopp t_s ist mechanisch erreichbar? Welche Drehzahl verträgt ein 3-m-Rohr Ø 1 mm (Nitinol, Tantal)? Ist zeitliche Mittelung an einer Prüfstelle zulässig (Anf. 2.5)? Genügen 36 Winkel über 180°? |

## Fazit

Die Sensorwahl hängt weniger am Sensor als am Messablauf. Bei 1501 Stopps legt der Achsstopp die Taktzeit fest, und die realistisch fahrbare Rohrdrehzahl begrenzt sie zusätzlich. Die hohen Raten der Schatten- und Punktsensoren nutzen im Modell kaum etwas. Die besten Wiederholgenauigkeiten hängen an einer Mittelung, die bei drehendem Rohr nur winkelsynchron zulässig ist und dann Stunden kostet. Gelb bei 0,5 s erreichen nur 2D-Sensoren mit großem Feld. Mit ihnen tauscht man Taktzeit gegen Genauigkeit. Messbar machen lässt sich diese Abwägung erst, wenn zwei Werte vorliegen: eine Einzelbild-Wiederholgenauigkeit von RIFTEK oder Keyence TM-X und ein gemessener Achsstopp. Beide fehlen bisher.

Für die Arbeit bietet sich ein Abgleich gegen die Anforderungen an. Ein Weg mit 2D-Bild an 40–80 Stationen wäre gelb und mechanisch einfach. Er braucht aber einen Herstellerwert unter rund ±1 µm. Ein 1D- oder Mehrachskopf an 1501 Stationen erreicht gelb nur mit t_s ≤ 0,1 s, mit Einzelscan und mit mehreren hundert 1/min. Der Mehrachskopf erfüllt dabei zusätzlich die Umfangsdefinition nicht. Das spricht dafür, die Achsstopp-Zeit und die zulässige Drehzahl vor jeder Sensorentscheidung am Aufbau zu klären.
