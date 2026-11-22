# Schatten-Mikrometer (LED/Laser + Zeilen- oder Flächensensor, Durchlicht) für Rohre Ø 1–6,5 mm

Stand der Recherche: 22.11.2026. Quellenlage: Herstellerseiten und PDFs im Netz waren in dieser Sitzung **nicht abrufbar**. WebFetch wurde abgelehnt für micro-epsilon.de, keyence.com, keyence.eu, ia.omron.com, scigate.com.sg und willrich.com; curl bekam vom Proxy 403. Für das Abrufen müssen diese Hosts freigegeben werden. Deshalb gibt es zwei Arten von Quellen:

- **[DB]** = Datenblatt eingesehen, lokale Kopie im Repo unter `docs/archiv/6 Recherche Messtechnik/…`, mit Seitenangabe. Die Seitenzahlen sind PDF-Seiten. Beim ME-Katalog stimmen sie mit den gedruckten Seitenzahlen überein.
- **[SE]** = Suchergebnis, Datenblatt nicht eingesehen. Das Such-Tool liefert zusammengefasste Auszüge, keine Rohtexte. Diese Werte sind deshalb vorläufig. Wo ein lokales Datenblatt vorliegt, gilt der [DB]-Wert.

Unbekannte Felder bleiben leer („–“). Es gibt keine Schätzungen.

## Welche Modelle gibt es über die bekannten hinaus (Keyence LS-9006/9030/9120, ME ODC2700/2520/1200)?

### Takeaway
Neu und für Ø 1–6,5 mm brauchbar sind vor allem der **Micro-Epsilon ODC2600-40** (LED, 40 mm, 2,3 kHz), der **Keyence LS-7030M** (Vorgänger des LS-9030, 2400/s) und die zweiachsigen Köpfe **Keyence LS-9006D** und **LS-9030D**. Grenzfälle, die nur bis 6 mm oder weniger reichen, sind LS-7010M, TM-X5006, Sikora LASER 2005 XY und Aeroel XLS13XY /B und /F. Omron ZX-GT, Panasonic HG-T und Keyence IG sind Lichtband-Sensoren der 1–10-µm-Klasse und für die geforderte µm-Genauigkeit eher ungeeignet. Bei Banner, SICK, Baumer, Wenglor, Takex und Vicivision wurde kein Schatten-Mikrometer der µm-Klasse gefunden.

### Cited Findings
**Prinzip „Schatten + Zeilensensor“ (1D), passend zur Fragestellung**
- Keyence LS-9000: ein „speziell entwickelter CMOS-Zeilensensor“ mit 16 kHz Abtastfrequenz und grüner InGaN-LED als Lichtquelle — [DB] `Keyence LS-9000 Produktbroschüre/Original_LS-9000 Produktbroschüre (DE).pdf`, PDF-S. 4
- Keyence LS-7000 (LS-7010/7030): GaN-LED mit „high-speed linear CCD“, 2400 Abtastungen/s — [SE] [thomasnet](https://news.thomasnet.com/fullstory/optical-micrometer-system-uses-gan-led-and-linear-ccd-457373/), [automation.com](https://www.automation.com/article/keyence-new-precision-optical-micrometer-uses-gan)
- Micro-Epsilon ODC2700: LED türkis 508 nm, „kein Laser, LED nach DIN EN 62471“, 15 kHz — [DB] `Micro-Epsilon optoCONTROL – Katalog/Original_cat--optoCONTROL-ODC--de.pdf`, S. 13
- Micro-Epsilon ODC2600: im Lieferantentitel als „LED micrometer“ geführt; 40-mm-Kopf, 2,3 kHz — [SE] [ME-Datenblatt ODC2600-40](https://www.micro-epsilon.com/download/products/dat--optoCONTROL-2600-40-Option-209-210--en.pdf), [industrysearch.com.au](https://industrysearch.com.au/micro-epsilon-led-micrometer-micro-epsilon-germany-optocontrol-2600-by-bestech-australia/p/41347). Das ODC2600 steht nicht im lokalen ME-Katalog, dort gibt es nur ODC1200/1201/1202, ODC2520 und ODC2700 [DB].
- Sikora LASER Series 2000 (z. B. LASER 2005 XY): „fächerförmiger Laserstrahl auf hochauflösende CCD-Zeile“, Durchmesser per Beugungsanalyse aus dem Schattenbild — [SE] [Sikora LASER Series 2000 (PDF)](https://sikora.net/wp-content/uploads/LASER_Series_2000_wc.pdf)

**Prinzip „Schatten + Flächensensor“ (2D, telezentrisch)**
- Keyence TM-X5000: grüne InGaN-LED, Bildaufnahme mit einstellbarer Belichtung — [DB] `Keyence TM-X5006 – Datenblatt/Original_TM-X5006_Datasheet.pdf`, S. 1
- Riftek RF65x.2D: LED kollimiert, Schattenbild auf „2D CMOS sensor“ („shadow principle“) — [DB] `Riftek RF65x.2D – Handbuch 2D Optical Micrometers/Original_2D_Optical_Micrometers_eng.pdf`, S. 4–5

**Lichtband-Sensoren (Durchlicht, geringere Genauigkeit; Detektortyp nur angegeben, wo die Quelle ihn nennt)**
- Omron ZX-GT: Laser 650 nm, Klasse 1, CCD; Messbreite 28 mm — [SE] [Omron Spezifikation](https://www.ia.omron.com/products/family/1918/specification.html)
- Keyence IG-010/IG-028: „CCD Laser Micrometer“, Laser 660 nm Klasse 1 — [SE] [Keyence IG Specs](https://www.keyence.com/products/measure/micrometer/ig/specs/)
- Panasonic HG-T1010: Durchlicht-Laser-Wegsensor („thru-beam type digital displacement sensor“), Messbreite 10 mm — [SE] [Panasonic HG-T](https://industry.panasonic.com/global/en/products/fasys/measurement/measurement/hg-t)
- Zumbach: Die Baureihe MSD ist als „LED measuring device … based on CCD technology with several point-source LEDs“ beschrieben, ohne Zahlen. ODAC-Köpfe arbeiten mit Laserdiode — [SE] [directindustry MSD](https://directindustry.com/prod/zumbach-electronic-ag/product-15879-1806247.html)

**Anderes Prinzip, nur zum Vergleich (kein Schatten-Zeilensensor)**
- Aeroel XLS13XY ist ein **Laser-Scan-Mikrometer**: „Scanning Motor ohne Kugellagerung“ und „Abtastgeschwindigkeit (m/s) 156/163“ — [DB] `Aeroel XLS13XY XLS35XY – Datenblatt/Original_AEROEL_xls_xy_de.pdf`, S. 3–4
- Mitutoyo LSM ist ebenfalls ein Laser-Scan-Mikrometer. Das Bulletin 2101 liegt lokal vor (`Mitutoyo Laser Scan Micrometer – Bulletin 2101/`), wurde hier aber nicht ausgewertet.

### Inferences
- Für eine Taktzeitrechnung „1D-Zeile, hohe Rate“ bleiben im Bereich Ø 1–6,5 mm mit vollem Bereich: ODC2700-10/-40 (15 kHz), LS-9030/LS-9030D (16 kHz), ODC2600-40 (2,3 kHz, [SE]) und LS-7030M (2,4 kHz, [SE]).
- Die 2D-Systeme (TM-X, Riftek) liefern nur 4 bis ca. 330 Messungen/s, also ein bis zwei Größenordnungen weniger. Dafür erfassen sie ein Bildfeld statt einer Linie.

### Gaps
- Banner, SICK, Baumer, Wenglor, Takex: Die Suche fand kein Durchlicht-Mikrometer der µm-Klasse. Gefunden wurden nur Lichtgitter und Lichtbänder ohne µm-Angabe, z. B. ein Balluff-Lichtband mit IO-Link ([Balluff](https://www.balluff.com/en-th/news/compact-laser-light-band-with-io-link)). Ob es solche Geräte nicht gibt oder ob die Suche sie nur nicht fand, bleibt offen.
- Vicivision, Mitutoyo: nicht gesucht bzw. nicht ausgewertet. Vicivision baut Wellenmessmaschinen, keinen Inline-Sensor; das ist ungeprüft.
- „optoCONTROL CLS“: Kein Micrometer-Modell dieses Namens gefunden.
- Zumbach MSD und Sikora: keine Wiederholgenauigkeit gefunden.

## Datenblattwerte je Modell (Messbereich, Wiederholgenauigkeit mit Bedingung, Linearität, Rate, Ein-/Ausgänge, Lichtquelle)

### Takeaway
Die Wiederholgenauigkeiten der Schatten-Mikrometer gelten **durchweg mit starker Mittelung am ruhenden Normal**: Keyence LS-9000 2048-fach, Micro-Epsilon ODC2700 1024 Werte, Keyence TM-X 16 Messungen. Die Abtastraten reichen von 2,3 kHz (ODC2600) bis 16 kHz (LS-9000). Bei Keyence hängt die Rate von der Zahl der OUTs und von der Störunterdrückung ab.

### Cited Findings

#### Tabelle A – Messdaten

| Modell | Prinzip / Achsen | Messbereich; kleinstes Objekt | Deckt Ø 1–6,5 mm? | Wiederholgenauigkeit + Bedingung | Linearität/Genauigkeit + Bedingung | Abtastrate / Ausgaberate; Belichtung | Lichtquelle, Klasse | Lage im Messfeld / Abstand | Quelle |
|---|---|---|---|---|---|---|---|---|---|
| **ME ODC2700-10** | LED-Schatten, 1 Achse | 10 mm; 0,05 mm (0,03 mm in Mitte) | ja | ≤ 0,03 µm; 95-%-Konfidenz, Durchmesser, Mittelung 1024 Werte „über einen Zeitraum von 5 Minuten“, temperaturstabilisiert, 45 min Warmlauf (Fn. 6) | ≤ 0,5 µm in Messfeld 1 (Z = ±0,5 mm), ≤ 1 µm (Z = ±1,5 mm), ≤ 2,5 µm (Z = ±2,5 mm), mit 2-mm-Prüfstift (Fn. 7) | Abtastrate 15 kHz („durchgeführte Messungen je Sekunde“), Messrate 15 kHz („Messwerte an der Schnittstelle“); Belichtung 8,5 µs, mit Videomittelung 3 × 8,5 µs | LED türkis 508 nm, RG 1 nach DIN EN 62471 | Messabstand Objekt–Empfänger 150 ± 2,5 mm; Sender–Empfänger 300 mm | [DB] ME-Katalog S. 13 |
| **ME ODC2700-40** | LED-Schatten, 1 Achse | 40 mm; 0,3 mm (0,1 mm in Mitte) | ja | ≤ 0,1 µm; wie oben (Fn. 6) | ≤ 1 µm bei Z = ±2,5 mm; ≤ 3 µm bei Z = ±10 mm, 2-mm-Prüfstift, 95 % (Fn. 8) | wie oben, 15 kHz / 15 kHz; 8,5 µs | LED 508 nm, RG 0 | 150 ± 10 mm (Option 002: 200 ± 10 mm) | [DB] ME-Katalog S. 13 |
| **ME ODC2600-40** (neu) | LED-Schatten, 1 Achse | 40 mm; 0,3 mm | ja | ±1 µm (Grundmodell), ±1,5 µm (Option 209/210); Fußnoten 1) und 3) nicht gesehen | < ±3 µm; „3 sigma; Kantenmessung ohne Mittelung“, Arbeitsabstand 150 ± 5 mm | Messrate 2,3 kHz; Belichtung – | LED (nur Lieferantentitel); RG – | 150 ± 5 mm; Option 209/210: 200 ± 5 mm | [SE] [ME dat ODC2600-40](https://www.micro-epsilon.com/download/products/dat--optoCONTROL-2600-40-Option-209-210--en.pdf), [ME dax ODC2600](https://micro-epsilon.com/fileadmin/download/excerpts/dax--optoCONTROL-2600--en-us.pdf) |
| ME ODC2520-46 | Laser-Schatten, 1 Achse | 46 mm; typ. ≥ 0,5 mm | ja (knapp bei 1 mm) | Reproduzierbarkeit ≤ 5 µm (-46) / ≤ 6 µm (-95), gemessen bei einem gleitenden Mittel über 32 Werte (Fn. 4) | < ±12/±15/±20 µm (je nach Abstand), 3 Sigma (Fn. 3) | 2,5 kHz | Halbleiterlaser 670 nm, Klasse 1M | Objekt–Empfänger 20–2000 mm, optimal 20/50/100/150 mm | [DB] ME-Katalog S. 17 |
| ME ODC1200 (2/5/10 mm) | Laser-Lichtband, 1 Achse, analog | 2/5/10/16 mm; ≥ 0,03/0,05/0,1/0,15 mm | 5-/10-mm-Variante ja | Werte bei ±2 Sigma (Fn. 4), statisches Rauschen in der Mitte über 3 min (Fn. 5); Zahlen hier nicht ausgelesen | – | 100 kHz (−3 dB) | Laser 670 nm, Klasse 1 | Objekt–Empfänger 20 mm, Sender–Empfänger 150 mm (Fn. 2) | [DB] ME-Katalog S. 23 |
| **Keyence LS-9006** | LED-Schatten, CMOS-Zeile, 1 Achse | 0,04 (0,01) – 6 mm | **Grenzfall, bis 6 mm** | ±0,03 µm; ±2σ, Normal Ø 1,0 mm, Mitte, 2048-fache Mittelung (*2) | ±0,5 µm, bewegtes Normal Ø 1,0 mm im Bereich 2 × 4 mm (*3) | 16 000/s; „wird durch die Anzahl der verwendeten OUTs und durch … gegenseitige Störunterdrückung beeinflusst“ (*4); Positionserkennung 4000/s | grüne InGaN-LED | Sender–Empfänger 60 ± 5 mm; Erkennungsbereich 4 × 5 mm | [DB] `Keyence LS-9006 – Datenblatt/…pdf` S. 1 |
| **Keyence LS-9006D** | wie oben, **2 Achsen** | Ø 0,04–6 mm | **Grenzfall, bis 6 mm** | ±0,03 µm (*1, wie LS-9006) | ±0,5 µm (*2) | 16 000/s (*3) | grüne InGaN-LED | – | [DB] `Keyence LS-9006D – Datenblatt/…pdf` S. 1 |
| **Keyence LS-9030** (auch -M, -D) | LED-Schatten, CMOS-Zeile, 1 Achse (D: 2 Achsen) | 0,3 (0,08) – 30 mm | ja | ±0,1 µm; ±2σ, Normal Ø 10 mm, Mitte, 2048-fach (*2) | ±2 µm, bewegtes Normal Ø 10 mm im Bereich 10 × 20 mm (*3) | 16 000/s (*4, wie oben) | grüne InGaN-LED | Sender–Empfänger 160 ± 40 mm; Erkennungsbereich 20 × 24 mm | [DB] `Keyence LS-9030 – Datenblatt/…pdf` S. 1 |
| Keyence LS-9120M | LED-Schatten, 1 Achse | 0,8–120 mm | nein (Ø 1 mm knapp, zu ungenau) | ±0,3 µm; Ø 40 mm, 2048-fach (*1) | ±8 µm (*2) | 16 000/s | grüne InGaN-LED | 400 ± 100 mm | [DB] `Keyence LS-9120M – Datenblatt/…pdf` S. 1 |
| **Keyence LS-7010M** (neu, Vorgänger) | GaN-LED, lineare CCD, 1 Achse | 0,04–6 mm; 0,04 mm | **Grenzfall, bis 6 mm** | ±0,06 µm; Fußnote laut Suche „±2σ, 20-mm-Stab, Mitte, 512-fach“. **Bedingung unklar**, die Fußnote gehört vermutlich zum LS-7030M (ein 6-mm-Kopf kann keinen 20-mm-Stab messen) | ±0,5 µm | 2400/s | GaN-LED | Sender–Empfänger 60 ± 5 mm | [SE] [plc-direct LS-7010M](https://plc-direct.com/products/ls-7010m), [Keyence LS-7000 Specs](https://www.keyence.eu/products/measure/micrometer/ls-7000/specs/) |
| **Keyence LS-7030M** (neu) | wie oben | 0,3–30 mm | ja | ±0,15 µm | ±2 µm | 2400/s | GaN-LED | 160 ± 40 mm | [SE] [Keyence LS-7030M](https://www.keyence.com:443/products/measure/micrometer/ls-7000/models/ls-7030m/) |
| **Keyence TM-X5006** (neu) | LED, telezentrisch, 2D-Bild | Bildfeld Ø 6 mm (hochpräzise Ø 4 mm); Tiefenschärfe 4 mm (hochpräzise 2 mm) | **Grenzfall, bis 6 mm; hochpräzise nur 4 mm** | ±0,03 µm; „Mittelwert von ±2σ bei 16-maliger Messung der Breite eines KEYENCE-Standardobjekts (Glaskalibriermaßstab) in der Mitte“ (*2) | ±0,2 µm (hochpräziser Bereich), ±0,3 µm (Messbereich), Glaskalibriermaßstab (*1) | Aufnahmezeit/Triggerintervall ca. 24 ms (voller Bereich), ca. 3 ms (Bereich „4/16“); Belichtung 25/50/100 µs | grüne InGaN-LED | Sender–Empfänger 60 mm | [DB] `Keyence TM-X5006 – Datenblatt/…pdf` S. 1 |
| Keyence TM-X5040 / TM-X5065 | wie oben | Ø 40 mm (hochpräzise Ø 26) / Ø 65 mm (hochpräzise Ø 40) | ja, aber großes Feld | ±0,08 µm / ±0,1 µm; 16 Messungen, wie oben | TM-X5065: ±1,2 µm (hochpräzise), ±2,2 µm | TM-X5065: ca. 24 ms (voll), ca. 3 ms („4/16“); TM-X5040: – | grüne LED | 180 mm / 270 mm | [SE] [Keyence TM-X5065](https://www.keyence.com/products/measure/micrometer/tm-x5000/models/tm-x5065/), [TM-X Specs](https://keyence.com/products/measure/micrometer/tm-x5000/specs) |
| Riftek RF656.2D-8x10 | LED, 2D-CMOS | 8 × 10 mm; 0,07 mm | ja | **keine Angabe** | Messfehler ±1,5 µm im Bereich ±1 mm entlang der Achse | „up to 65“ Messungen/s; Belichtung 100 µs | LED 630 nm, „safe“ nach EN 62471 | – | [DB] Riftek-Handbuch S. 4–5 |
| Riftek RF657.2D-15x20 | LED, 2D-CMOS | 15 × 20 mm; 0,13 mm | ja | keine Angabe | ±0,8 µm im Bereich ±5 mm | 24 Messungen/s; 15 µs | LED 525 nm | – | [DB] Riftek-Handbuch S. 6 |
| Sikora LASER 2005 XY | Laser-Fächer + CCD-Zeile, **2 Achsen** | 0,05–5 mm | **nein, bis 5 mm** | – | ±0,5 µm („accuracy“) | 1200 Messungen/s/Achse (Serie: 500); Belichtung 0,2 µs | Laser | – | [SE] [Sikora LASER Series 2000](https://sikora.net/wp-content/uploads/LASER_Series_2000_wc.pdf) |
| Omron ZX-GT28 | Laser + CCD, Lichtband | Messbreite 28 mm | Bereich ja, Genauigkeit fraglich | – (nicht gefunden) | ±0,1 % F.S. (Sender–Empfänger 100 mm, Abschattung 50 mm vor Empfänger); „10 µm“ steht teils als Auflösung (16-fach gemittelt), teils als Genauigkeit → **Konflikt** | 1,5 ms Standard / 0,5 ms Highspeed (= 2000/s); Mittelung 1–4096 in Zweierpotenzen | Laser 650 nm, Klasse 1 | – | [SE] [Omron Spezifikation](https://www.ia.omron.com/products/family/1918/specification.html), [Omron JP-Katalog](https://www.fa.omron.co.jp/data_pdf/cat/zx-gt_ds_j_1_20.pdf) |
| Panasonic HG-T1010 | Laser-Durchlicht | Messbreite 10 mm; kleinstes Objekt Ø 0,5 mm (bei 500 mm Abstand) | Bereich ja, Genauigkeit fraglich | 1 µm, „P-P-Wert … bei halber Abschattung in der Mitte“; einmal auf 20 mm bezogen (100 mm: 2,5 µm, 500 mm: 5 µm), laut Anleitung bei 100 mm → **Konflikt** | ±0,12 % F.S. (20 mm), ±0,28 % F.S. (100 mm) | Abtastzyklus 1 ms Standard / 0,5 ms Highspeed | Laser | Montageabstand 0–500 mm | [SE] [Panasonic HG-T](https://industry.panasonic.com/global/en/products/fasys/measurement/measurement/hg-t), [HG-T1010-Anleitung](https://fs-ep-eu-p-industry-pim.wd.pisceu.panasonic.eu/storage/download-files/import/mn_hgt1010_instruction_pid_en.pdf) |
| Keyence IG-010 / IG-028 | CCD-Laser, Lichtband | 10 mm / 28 mm | Bereich ja, Genauigkeit fraglich | IG-010: 5 µm bei 100 mm, 10 µm bei 500 mm Abstand | ±0,1 % | 980 µs, 490 µs bei Mittelung „high speed“ | Laser 660 nm, Klasse 1 | – | [SE] [Keyence IG Specs](https://www.keyence.com/products/measure/micrometer/ig/specs/) |
| *Aeroel XLS13XY /A* (Vergleich, Laser-Scan) | Laser-Scan, **2 Achsen** | Feld 13 × 13 mm; Ø 0,1–10 mm (10 mm nur zentriert, Fn. 5) | ja | ±0,15 µm (/480) bzw. ±0,04 µm (/1500); Bedingung (Fn. 11–13) teils unlesbar; „T = 1 s, ±2σ“ nur [SE]. **Einzelabtastung** siehe unten | ±0,5 µm, Objekt zentriert (Fn. 6/7); ±1,5 µm im ganzen Feld; ±1 µm im beschränkten Feld 5 × 5 mm | 480 Hz bzw. 1500 Hz je Achse (X + Y) | sichtbare Laserdiode (Text verstümmelt), EN 60825-1:2014 | Feld 13 × 13 mm für Ø ≥ 0,3 mm | [DB] `Aeroel XLS13XY XLS35XY – Datenblatt/Original_AEROEL_xls_xy_de.pdf` S. 4 |
| *Aeroel XLS13XY /B, /F* | wie oben | Feld 4 × 4 mm; Ø 0,03–3 mm (/B), 0,02–3 mm (/F) | **nein, bis 3 mm** | ±0,03 µm (/480), ±0,02 µm (/1500) | ±1 µm im ganzen Feld; ±0,5 µm im beschränkten Feld 2 × 2 mm | wie oben | wie oben | – | [DB] Aeroel S. 4 |

#### Tabelle B – Ein-/Ausgänge, Trigger, Encoder

| Modell | Trigger / Sync / Encoder | Mittelung einstellbar | Quelle |
|---|---|---|---|
| ME ODC2700 | „3x Eingänge wahlweise für Encoder, Nullpunkt, Reset, Trigger; Light on/off“; Digitalausgang Synchronisation; Ethernet, RS422, EtherCAT, EtherNet/IP, PROFINET | „frei wählbare Mittelungen“ | [DB] ME-Katalog S. 13 |
| ME ODC2520 | TrigIn / SyncIn (über RS422-Pegel) | – | [DB] ME-Katalog S. 17 |
| ME ODC2600 | – (Handbuch Kap. 6.3.7.6 „Averaging“ existiert, Inhalt nicht gesehen) | ja (laut Handbuch-Inhaltsverzeichnis) | [SE] [ME Handbuch ODC2600](https://www.micro-epsilon.com/download/manuals/man--optoCONTROL-2600--en.pdf) |
| Keyence LS-9000 (Controller LS-9500/9501) | Encodereingang (NPN/PNP, Spannung 5/12/24 V, Leitungstreiber); Synchroneingang 1, 2; Auto-Zero-, Reset-, Speicher-Trigger-, Speicher-Start-Eingang | ja („über Mittelwertbildung“) | [DB] LS-9000-Broschüre PDF-S. 13 (Ein-/Ausgänge), PDF-S. 4 |
| Keyence TM-X5000 | Triggerintervall s. Tabelle A; weitere E/A nicht gesehen | – | [DB] TM-X5006 S. 1 |
| Riftek RF65x.2D | 1 Synchronisationseingang; 2 Logikausgänge (1 als Strobe der aktiven Belichtung); Ethernet 1 Gbit/s; OPC UA, Modbus TCP, Siemens S7, UDP | – | [DB] Riftek-Handbuch S. 5–6 |
| Aeroel XLS13XY | 2 opto-isolierte Digitaleingänge 10–30 VDC, programmierbar für Start/Stop, Pulszähler und **Quadraturencoder** („synchronisieren die Lasermessung mit der gemessenen Position“); RS232, RS485, Ethernet; Modi Free-Running, On-Command Single-Shot, On-Command Continuous, Auto-Sync | „einfache Mittelung von n Abtastungen, für programmierbares n ≥ 1“; Extremwerte über k Werte | [DB] Aeroel S. 2–3 |
| Omron ZX-GT | – | 1–4096 (Zweierpotenzen); Ansprechzeit erstes Ergebnis ca. Messzyklus × (Mittelung + 1) + max. 1 ms | [SE] [Omron EU](https://industrial.omron.eu/en/products/zx-gt) |

### Inferences
- Für die Taktzeit sind beim LS-9000 die 16 000/s nur eine Obergrenze. Laut Fußnote *4 sinkt die Rate mit der Zahl der aktiven OUTs und mit der Störunterdrückung; um wie viel, steht im Datenblatt nicht.
- Beim ODC2700 sind Abtastrate (gemessen) und Messrate (ausgegeben) beide 15 kHz. Eine 1024-fache Mittelung entspricht damit ca. 68 ms (1024 / 15 000 s⁻¹). Das ist eine Rechnung aus den Datenblattwerten. Die Fußnote spricht aber von „über einen Zeitraum von 5 Minuten“; was damit gemeint ist, bleibt offen.
- TM-X5006 und Riftek messen das ganze Bildfeld in einem Bild. Ihre Rate (≈ 3–24 ms bzw. 15–65 Messungen/s) ist deshalb nicht direkt mit den kHz-Raten der Zeilensensoren vergleichbar.

### Gaps
- ODC2600: Fußnoten zur Wiederholgenauigkeit (Mittelung), Belichtung, Ein-/Ausgänge und Risikogruppe nicht gesehen. Benötigte Quelle: `dat--optoCONTROL-2600-40-Option-209-210--de.pdf` (micro-epsilon.de, Host gesperrt).
- LS-7000: Fußnotenzuordnung (Ø Normal, Mittelungszahl) unklar; Controller-E/A nicht gefunden.
- TM-X5040: Triggerintervall nicht gefunden.
- Omron ZX-GT: Wiederholgenauigkeit nicht gefunden.
- Sikora 2005 XY: Wiederholgenauigkeit nicht gefunden.
- Zumbach: kein Datenblatt für einen LED/CCD-Kopf im Bereich 1–6,5 mm gefunden. Ein Suchergebnis nennt den ODAC 60J (Ø 0,25–5 mm, ±0,25 µm, 1000/s, Option 2000/s), aber mit Laserdiode und nur bis 5 mm ([thomasnet](https://news.thomasnet.com/fullstory/laser-gauge-measures-at-scanning-rate-of-1-000-sec-6285)); [SE], ungeprüft.
- Für Ø 1 mm gibt außer Keyence LS-9006 (Normal Ø 1,0 mm) kein Hersteller die Wiederholgenauigkeit an.

## Gibt es veröffentlichte Wiederholgenauigkeit ohne Mittelung (Einzelabtastung) oder mit kurzer Mittelung?

### Takeaway
Für einen **Schatten-Zeilensensor** veröffentlicht kein gefundener Hersteller eine Wiederholgenauigkeit der Einzelabtastung. Den einzigen belastbaren Einzelabtastwert liefert der **Laser-Scan-Mikrometer Aeroel XLS13XY**: ±0,75 µm bis ±1,5 µm (±2σ). Das sind etwa 20- bis 40-mal größere Werte als die gemittelten Angaben. Kurze Mittelung (32 Werte) nennt nur Micro-Epsilon beim ODC2520.

### Cited Findings
- **Aeroel XLS13XY, Einzelabtastung [DB]:** Fußnote (11): „Die Wiederholbarkeit ist für beide Achsen gleich und wird für den Mittelwert spezifiziert (X+Y)/2. Die Wiederholbarkeit bei einzelner Abtastung (± 2σ) ist ± 1 μm (XLS13XY/480), ± 0.75 μm (XLS13XY/1500 für Ø ≤ 3 mm), ± 1.5 μm (XLS13XY/1500 für Ø > 3 mm), ± 3.5 μm (XLS35XY/480) und ± 2.5 μm (XLS35XY/1500).“ Die Zeichen ≤, > und σ sind im PDF als verstümmelte Glyphen dargestellt und aus dem Zusammenhang gelesen. Die Zeilenüberschrift und die Fußnoten 12, 13 und 15 sind unlesbar. Auf S. 1 wird außerdem „Ausgezeichnete Wiederholbarkeit bei einzelner Abtastung“ beworben — `Aeroel XLS13XY XLS35XY – Datenblatt/Original_AEROEL_xls_xy_de.pdf`, S. 1 und 4
- Aeroel, Mittelungszeit des gemittelten Werts: „Repeatability (T=1s, ±2σ)“ — [SE] [directindustry/Marposs XLS XY](https://pdf.directindustry.com/pdf/marposs/xls-xy-plus/7365-1095766.html), im lokalen PDF nicht lesbar
- **ME ODC2520, kurze Mittelung [DB]:** „Reproduzierbarkeit [4] … Gemessen bei einem gleitenden Mittel über 32 Werte“, Wert ≤ 5 µm (ODC2520-46) bzw. ≤ 6 µm (ODC2520-95) — ME-Katalog S. 17
- **ME ODC2600, ohne Mittelung, aber nur Linearität [SE]:** Linearität < ±3 µm, „measured with 3 sigma; edge measurement without averaging“. Das ist **Linearität, keine Wiederholgenauigkeit** — [SE] [ME dat ODC2600-40](https://www.micro-epsilon.com/download/products/dat--optoCONTROL-2600-40-Option-209-210--en.pdf)
- **Zum Vergleich, starke Mittelung [DB]:**
  - Keyence LS-9006/9030/9120: 2048-fache Mittelung, ±2σ — Datenblätter S. 1; Broschüre PDF-S. 7 (Kurven mit 512 Mittelwerten)
  - ME ODC2700: 1024 Werte „über einen Zeitraum von 5 Minuten“, 95 %, 45 min Warmlauf — ME-Katalog S. 13, Fn. 6
  - Keyence TM-X5006: Mittelwert von ±2σ aus 16 Messungen — Datenblatt S. 1, Fn. *2
  - ME ODC1200: ±2σ, statisches Rauschen über 3 min — ME-Katalog S. 23, Fn. 4/5
- Omron ZX-GT: Auflösung „10 µm (number of process values to average: 16)“ — [SE] [Omron](https://www.ia.omron.com/products/family/1918/specification.html)
- Panasonic HG-T: Wiederholgenauigkeit 1 µm als P-P-Wert; ob und wie stark gemittelt wird, geht aus dem Suchergebnis nicht hervor — [SE] [Panasonic HG-T](https://industry.panasonic.com/global/en/products/fasys/measurement/measurement/hg-t)

### Inferences
- Der Aeroel-Wert zeigt die Größenordnung: Die Einzelabtastung streut bei diesem Gerät etwa 20- bis 40-mal stärker als der gemittelte Wert (±0,75 µm gegenüber ±0,04 µm bei /1500). Unter der Annahme rein zufälligen Rauschens (σ ~ 1/√n) passt das zu einer Mittelung über einige hundert bis tausend Abtastungen. Bei 1500 Hz und T = 1 s ([SE]) wären es 1500 Abtastungen. Das ist eine Plausibilitätsrechnung, keine Herstellerangabe.
- Auf Schatten-Zeilensensoren (Keyence, Micro-Epsilon) lässt sich das nicht direkt übertragen: anderes Prinzip, anderes Rauschen. Den Einzelabtastwert muss der Hersteller nennen (→ Herstellerfrage).

### Gaps
- Keyence LS-9000/LS-7000/TM-X, Micro-Epsilon ODC2700/2600, Sikora, Zumbach: keine veröffentlichte Wiederholgenauigkeit für Einzelabtastung oder kurze Mittelung (≤ 32) gefunden.
- Aeroel: Fußnoten 12/13/15 und die Zeilenüberschrift im lokalen PDF sind wegen der Schriftkodierung unlesbar. Eine saubere Kopie (marposs.com, gesperrt) würde helfen.
