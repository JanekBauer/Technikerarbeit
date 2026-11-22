# Mess-Systeme und Anwendungen für die berührungslose Prüfung von Präzisions- und Medizinrohren (Ø ca. 1–6,5 mm, bis 3 m)

Stand der Recherche: 22.11.2026. Erstellt von KI (Claude Code, Recherche-Subagent).

**Wichtiger Hinweis zur Quellenlage:** In dieser Sitzung ließ sich keine Herstellerseite öffnen. Gesperrt waren laserlinc.com, metrology.news, keyence.com und nordson.com, laut Auftrag außerdem mitutoyo.com, marposs.com, res.cloudinary.com und pdf.directindustry.com. **Alle Werte unten stammen daher aus Suchergebnissen (Snippets bzw. Zusammenfassungen der Suchmaschine).** Sie sind durchgehend als „Suchergebnis, nicht eingesehen“ gekennzeichnet. Kein Wert wurde geschätzt. Vor einer Verwendung in der Technikerarbeit sollte jeder Wert im Original-Datenblatt geprüft werden.

Kennzeichnung je Wert: **[S]** = Suchergebnis, nicht eingesehen. **[D]** = Dokument gelesen (kam in dieser Recherche nicht vor).

## Welche Systeme gibt es für die Offline- und Inline-Prüfung von Medizin- und Präzisionsrohren?

### Takeaway
Fertige Offline-Prüfplätze für lange, dünne Medizinteile gibt es am Markt. Am deutlichsten passt LaserLinc Metron / BenchLinc: 3-Achs-Lasermikrometer, motorischer Schlitten und optionale 360°-Drehung, laut Treffer für Teile bis 1,8 m. Für 3 m ist kein fertiges System belegt. Inline-Messköpfe für Ovalität mit 3 oder 4 Achsen bieten Zumbach (ODAC TRIO), Sikora (LASER 2000 T), NDC/Beta LaserMike (AccuScan 6012) und LaserLinc (Triton) an. Für Wellen und Rohrabschnitte kommen optische Wellenmessmaschinen mit Drehachse hinzu, etwa Mahr MarShaft SCOPE plus und Vicivision. Sie sind aber auf kurze Längen (≤ 2 m) ausgelegt.

### Cited Findings

**Übersichtstabelle Systeme (alle Werte [S] = Suchergebnis, nicht eingesehen)**

| System / Hersteller | Art | Sensorprinzip | Messrate | Genauigkeit / Wiederholbarkeit | Messbereich / Teilelänge | Ovalitätsmethode | Quelle |
|---|---|---|---|---|---|---|---|
| LaserLinc **Metron** | Offline, automatisch, meist vertikal | 3-Achs-Lasermikrometer + motorischer vertikaler Scan-Schlitten; alternativ Laserlinien-Triangulation (FlawSense) oder Ultraschall | Laserlinie: „up to 10,000 times per second“ (Sensor, nicht Vorschub) | keine Angabe gefunden | Teile bis 1,8 m (72 in) Länge, bis 29,2 mm Ø | 3-Achs-Mikrometer; Option 360°-Teiledrehung | [S] [LaserLinc Metron](https://laserlinc.com/metron-an-automated-tubing-guidewire-inspection-solution), [FlawSense Metron](https://laserlinc.com/elementor-6767), [Laser Focus World](https://www.laserfocusworld.com/directory/fiber-optic-optoelectronic-components-equipment-systems/test-measurement-equipment/product/14294953/laserlinc-inc-metrontm-automated-dimensional-inspection) |
| LaserLinc **BenchLinc OD / BenchLinc V** | Offline-Tischgerät | Lasermikrometer | keine Angabe | keine Angabe | ganze Länge von Führungsdrähten/Kathetern (V) | Probe wird automatisch in mehrere Winkel gedreht; „up to 100 checks at a user-defined angle interval“; Ovalität = max − min Ø | [S] [LaserLinc Offline-Broschüre](https://laserlinc.com/wp-content/uploads/2021/07/LaserLinc_Offline_Brochure-25th.pdf), [LaserLinc Nitinol](https://test.laserlinc.com/nitinol_tubing.html) |
| LaserLinc **Triton312** | Messkopf (inline / Tisch) | 3-Achs-Scanning-Lasermikrometer | 600 Hz je Achse, 1.800 Hz gesamt (Standard) | Wiederholbarkeit ±2,5 µm ungemittelt, ±0,125 µm bei 2 s Mittelung (gilt für Teile ≤ 10,2 mm); Auflösung 0,025 µm | 0,102–11,4 mm, Gate 12 mm | 3 Achsen, Ovalität ohne Drehung der Probe | [S] [Triton312 Specs (Testseite)](https://test.laserlinc.com/specs/Triton312_specs.html), [Findlight-Datenblatt](https://www.findlight.net/uploads/products/datasheet/Triton312-Triple-Axis-Scanning-Laser-Micrometers.pdf), [Maßblatt](https://public.laserlinc.com/docs/Laser_Micrometers/Triton312/0312-0001-00_Triton312_Triple-Axis_Data_Micrometer/0312-0001-00%20Triton312%20Triple-Axis%20Data%20Micrometer%20Overall%20Mounting%20Dimensions.PDF) |
| NDC / Beta LaserMike **AccuScan 6012** | Inline-Messkopf | 4-Achs-Scanning-Laser | 2.400 Scans/s je Achse, 9.600 gesamt | Wiederholbarkeit ±1 µ ±0,025 % (Einzelscan); „single-scan repeatability down to 1 micron“ | bis 12 mm; Anwendungen u. a. Katheter, kleine Medizinschläuche | 4 Achsen; Hersteller wirbt mit „up to 100% ovality accuracy“ gegenüber 3-Achs-Geräten | [S] [Nordson AccuScan 6000](https://www.nordson.com/en/Products/Measurement-and-Control-Products/AccuScan-6000), [Plastics Machinery Mfg.](https://www.plasticsmachinerymanufacturing.com/thermoforming/article/13000341/ndc-accuscan-6012-gauge-zeros-in-on-medical-tubing) |
| NDC / Beta LaserMike **AccuScan 5000** | Inline-Messkopf | 2-Achs-Scanning-Laser | 2.400 Scans/s je Achse (4.800 gesamt) | Wiederholbarkeit nicht gefunden | bis 80 mm | 2 Achsen (XY) | [S] [Nordson AccuScan 5000](https://www.nordson.com/en/Products/Measurement-and-Control-Products/AccuScan-5000) |
| Nordson / Beta LaserMike **BenchMike Pro** | Offline-Tischgerät | Scanning-Laser | keine Angabe | keine Angabe | keine Angabe | dreht die Probe automatisch in vordefinierte Positionen; daraus Ovalität und Konzentrizität | [S] [Nordson BenchMike Pro](https://www.nordson.com/en/Products/Measurement-and-Control-Products/BenchMike-Pro) |
| Zumbach **ODAC TRIO** (13/33/63/113TRIO) | Inline-Messkopf | 3 synchronisierte Laserachsen in einer Ebene | 33TRIO: bis 9.000 Messungen/s (FF-Version) | nur qualitative Angaben; Werte im 113TRIO-Datenblatt nicht lesbar (pdf.directindustry.com gesperrt) | je nach Kopf | 3 Achsen; erkennt auch polygonale Unrundheit (Mehrfachkeule) | [S] [ODAC 33TRIO](https://pdf.directindustry.com/pdf/zumbach-electronic-ag/odac-33trio/15879-918150.html), [ODAC 113TRIO](https://pdf.directindustry.com/pdf/zumbach-electronic-ag/odac-113trio/15879-918153.html) |
| Zumbach **STEELMASTER SM** / **GaugePro** | Inline (Rohr, Draht) / Offline | Laser; GaugePro auch Wanddicke | keine Angabe | keine Angabe | keine Angabe | GaugePro: Ovalität, Exzentrizität, Wanddicke, ID, OD | [S] [Zumbach STEELMASTER](https://directindustry.com/prod/zumbach-electronic-ag/product-15879-1806625.html) |
| Sikora **LASER Series 2000 (XY / T)** | Inline-Messkopf, auch Metallrohr | Beugungsanalyse („intelligent diffraction analysis“), sehr kurze Belichtung | bis 5.000 Messungen/s je Achse | keine Zahl gefunden | Serie 0,05–300 mm (Broschüre); andere Seite: bis 500 mm | XY = 2 Achsen; 2010 T = 3 Achsen („six tangents“), liefert min/max Ovalität und Lage des Ovals | [S] [Sikora Ovalitätsmessung](https://sikora.net/en/ovality-measurement/), [The Fabricator](https://www.thefabricator.com/tubepipejournal/product/testingmeasuring/sikoras-laser-series-2000-measures-metal-tube-diameter-ovality), [Sikora Medizinschläuche](https://sikora.net/en/extra/medical-tubes-save-lives/) |
| Sikora **LASER PRO / Series 6000** | Inline | Laser | Flyer: 5.000 Messwerte je s und Achse, „500,000 measuring points“ | keine Angabe | keine Angabe | zusätzlich Knotenerkennung | [S] [Sikora LASER PRO Flyer](https://sikora.net/wp-content/uploads/Flyer_LASER_PRO_ht.pdf) |
| Keyence **LS-9000** | Messkopf | Hochgeschwindigkeits-Optikmikrometer (LED/CCD) | 16.000 Abtastungen/s | Wert nicht gefunden (keyence.com gesperrt) | keine Angabe | 1 Achse; Ovalität nur über Drehen oder 2 Köpfe | [S] [Keyence LS-9000](https://www.keyence.com/products/measure/micrometer/ls-9000/features/feature-04.jsp) |
| Keyence **TM-X5000** | Messkopf | telezentrisches 2D-Bild | keine Angabe | keine Angabe | keine Angabe | bis 100 Messbereiche gleichzeitig; Peak/Bottom-Extraktion; Keyence nennt „Catheter Outer Diameter Measurement“ als Anwendung | [S] [Keyence Innen-/Außendurchmesser](https://keyence.com/products/measure/applications/dimension-measurement/inner-and-outer-diameter-measurement.jsp) |
| Micro-Epsilon **optoCONTROL 2700** / **confocalDT 2400** | Sensor | Optikmikrometer (LED) / konfokal | optoCONTROL 2700 (10-mm-Modell): 5 kHz | keine Angabe | 10 mm und 40 mm Messbereich | Anwendung: Edelstahlrohr wird um 360° gedreht, Abstandsmessung an drei Positionen (Anfang, Mitte, Ende) | [S] [Micro-Epsilon Durchmesser](https://www.micro-epsilon.com/applications/areas/Durchmesser/), [Automation.com](https://www.automation.com/article/micro-epsilon-confocal-sensors-measure-diameter-of) |
| Mahr **MarShaft SCOPE 250 plus** | Offline-Wellenmessmaschine | Durchlicht-Kamera, über 120 Bilder/s | > 120 Bilder/s | MPE Ø ≤ (1,5 + d/40) µm; Länge MPE ≤ (3,0 + l/125) µm | bis 250 mm Länge, 40 mm Ø | Präzisions-Rundheitsachse C (0,2–60 1/min) | [S] [Mahr MarShaft SCOPE 250 plus](https://metrology.mahr.com/en-us/products/datasheet/5361802-optische-wellenmessgeraete-marshaft-scope-250-plus.pdf) |
| Vicivision **TECHNO** | Offline-Wellenmessmaschine | optisch (Schattenbild) | keine Angabe | keine Zahl gefunden | Ø 40–180 mm, Länge 300–2000 mm (eine andere Quelle: Ø 8–180 mm, 100–1250 mm) | Drehung des Teils | [S] [Quality Magazine](https://www.qualitymag.com/articles/95134-optical-shaft-metrology-a-new-generation-of-measuring-systems-provides-cutting-edge-precision-accuracy) |
| Marposs Aeroel **Barlinex** | Inline (Stangen/Rohre) | 1- oder 2-Achs-Lasermesskopf | keine Angabe | keine Angabe | keine Angabe | XY | [S] [The Fabricator](https://www.thefabricator.com/tubepipejournal/product/testingmeasuring/marposs-aeroel-barlinex-laser-system-measures-tube-ods) |
| Cerulean **CD Express** | Offline | Laser | 100 Einzelmessungen pro 360°-Umdrehung | keine Angabe | keine Angabe | Drehung | [S] [The Engineer](https://www.theengineer.co.uk/content/news/high-speed-laser-micrometer-measures-circumference-diameter-and-ovality-of-cylindrical-objects) |

**Weitere Befunde zu Rohrherstellern und Anwendungen**
- Bei Nitinolrohr kommen laut LaserLinc meist Lasermikrometer zum Einsatz, für die genaueste Ø- und Ovalitätsmessung die Triton-Serie. Wanddicke und Konzentrizität brauchen Ultraschall, z. B. UltraGauge+. [S] [LaserLinc Nitinol](https://test.laserlinc.com/nitinol_tubing.html), [MDDI](https://www.mddionline.com/manufacturing/why-od-monitoring-isn-t-enough-for-medical-tubing-production)
- Resonetics nennt für Nitinolrohr folgende OD-Toleranzen: „Precision“ ±0,0005" bis ±0,0008", „Premium“ ±0,2–0,8 %, Konzentrizität > 95 %. [S] [Resonetics Nitinol Tubing](https://resonetics.com/nitinol/nitinol-material/tube/)
- Viant gibt für Nitinolrohr eine Konzentrizität von max. 10 % an, gemessen nach ASTM F2633. [S] [Viant Nitinol Tubes](https://viantmedical.com/wp-content/uploads/2023/08/Viant-Nitinol-Tubes.pdf)
- Laut Snippet tauchen 2-Achs-Geräte bei dreizähliger Symmetrie (Gleichdick) als „rund“ auf. Das spricht für 3 oder mehr Achsen oder für Drehung. [S] [NDC Diameter & Ovality](https://ndc.com/cable-tube/measurements/diameter-ovality)

### Inferences
- Für 3 m lange Rohre mit Ø 1–6,5 mm ist **kein fertiges System belegt**. Das am nächsten liegende ist LaserLinc Metron (vertikal, bis 1,8 m). Für 3 m wäre wohl eine Sonderausführung oder ein Eigenbau nötig: Mehrachs-Messkopf plus Linearachse plus Drehachse.
- Am Markt gibt es zwei Wege zur Ovalität: (a) ein feststehender Messkopf mit 3 oder 4 Achsen (Triton, ODAC TRIO, Sikora 2000 T, AccuScan 6012) ohne Drehung oder (b) ein 1- oder 2-Achs-Mikrometer mit Drehen der Probe (BenchLinc, BenchMike Pro, Cerulean). Weg (b) ist langsamer, löst aber den Umfang feiner auf.
- Wellenmessmaschinen wie Mahr oder Vicivision sind sehr genau, für 3 m lange, biegeschlaffe Rohre aber zu kurz. Für die Arbeit taugen sie eher als Referenz (Vergleichsmessung).

### Gaps
- Keine Herstellerseite konnte geöffnet werden, alle Werte sind ungeprüfte Snippets. Gesperrte Hosts: laserlinc.com, metrology.news, keyence.com, nordson.com, dazu die laut Auftrag gesperrten. Für eine Prüfung müssten diese Hosts in den Netzwerkeinstellungen der Sitzung freigegeben werden.
- Kein Treffer zu Proton Products, Jenoptik (Rohr/Medizin) oder Qualitätsseiten von Confluent, Fort Wayne Metals, Johnson Matthey, Euroflex oder Memry mit Angaben zur Prüftechnik.
- Kein Hersteller nennt für Metron, BenchLinc oder BenchMike einen Vorschub in mm/s oder eine Taktzeit je Teil.
- Für ODAC TRIO, Sikora 2000 und Keyence LS-9000 fehlen die Wiederholbarkeitswerte, weil die Datenblätter nicht lesbar waren.

## Welche Sensortypen, Messraten, Genauigkeiten, Ovalitätsverfahren und Taktzeiten werden veröffentlicht?

### Takeaway
Fast alle Systeme nutzen **Schatten- bzw. Scanning-Lasermikrometer** (oder LED/CCD bzw. Beugung) mit **600–16.000 Messungen/s je Achse**. Die angegebene Einzelscan-Wiederholbarkeit liegt bei **±1 µm (AccuScan 6012)** bis **±2,5 µm (Triton312)**. Taktzeiten je Teil oder Vorschubgeschwindigkeiten offline sind **nicht veröffentlicht**.

### Cited Findings
- Scanning-Laser: Triton312 600 Hz je Achse / 1.800 Hz gesamt; AccuScan 5000/6012 2.400 Scans/s je Achse; ODAC 33TRIO bis 9.000/s. [S] Quellen siehe Tabelle.
- Beugung: Sikora LASER 2000 bis 5.000 Messungen/s je Achse. [S] [Sikora](https://sikora.net/en/ovality-measurement/)
- LED/CCD: Keyence LS-9000 16.000 Abtastungen/s. [S] [Keyence](https://www.keyence.com/products/measure/micrometer/ls-9000/features/feature-04.jsp)
- Laserlinien-Triangulation (Konturkarte, 360°): bis 10.000/s (FlawSense Metron). [S] [FlawSense Metron](https://laserlinc.com/elementor-6767)
- Konfokal (Abstand bei drehendem Rohr): Micro-Epsilon confocalDT 2400, gewählt wegen großer Apertur, großem Grundabstand und weil es auf vielen Oberflächen misst. [S] [Micro-Epsilon](https://www.micro-epsilon.com/applications/areas/Durchmesser/)
- Ovalität bei Drehung: Ovalität = größter minus kleinster gemessener Ø; BenchLinc bis 100 Messungen in frei wählbaren Winkelschritten. [S] [LaserLinc Nitinol](https://test.laserlinc.com/nitinol_tubing.html)
- Ovalität mit Mehrachskopf: Sikora 2000 T, 3 Achsen = 6 Tangenten, liefert min/max und Lage des Ovals. [S] [Sikora](https://sikora.net/en/ovality-measurement/)
- Bildverarbeitung: Mahr MarShaft > 120 Bilder/s, MPE Ø ≤ (1,5 + d/40) µm. [S] [Mahr](https://metrology.mahr.com/en-us/products/datasheet/5361802-optische-wellenmessgeraete-marshaft-scope-250-plus.pdf)

### Inferences
- **Eigene Rechnung, nicht aus Quellen, zur Einordnung der Taktzeit:** Ein Rohr von 3 m mit einer Messstelle alle 2 mm ergibt 1.500 Messstellen. Beim Durchfahren durch einen festen 3-Achs-Kopf (z. B. Triton312, 600 Hz je Achse) gilt: Punktabstand = Vorschub / Messrate. Bei 100 mm/s Vorschub wären das rund 0,17 mm je Messung, für 3 m etwa 30 s reine Fahrzeit. Begrenzt wird die Taktzeit dann eher durch Handling, Mittelung und Biegeschwingungen des Rohrs als durch den Sensor. Bei Ovalität durch Drehen (Anhalten, Drehen, Messen) multipliziert sich die Zeit: Messstellen × Winkelschritte × Drehzeit. Bei 1.500 Stellen und z. B. 1 s je Umdrehung wären das schon rund 25 min. Die Werte sind nur Beispiele, die Fahr- und Drehzeiten sind angenommen.
- Wichtig für die Taktzeit ist also die Wahl zwischen „Mehrachskopf ohne Drehen“ und „Drehen mit 1- oder 2-Achs-Sensor“. Möglich ist auch ein Mittelweg: Das Rohr dreht kontinuierlich und fährt gleichzeitig axial (Wendelbahn).

### Gaps
- Keine veröffentlichten Taktzeiten oder Vorschübe für Offline-Prüfplätze (Metron, BenchLinc, BenchMike).
- Keine Zumbach-Genauigkeitswerte für kleine Durchmesser lesbar.

## Gibt es veröffentlichte Wiederholbarkeits- oder %GRR-Ergebnisse für kleine Rohre?

### Takeaway
Es fanden sich **keine veröffentlichten %GRR-Studien** für diese Systeme an kleinen Rohren. Es gibt nur Wiederholbarkeitsangaben aus Datenblättern.

### Cited Findings
- AccuScan 6012: Einzelscan-Wiederholbarkeit ±1 µ ±0,025 %. [S] [Nordson](https://www.nordson.com/en/Products/Measurement-and-Control-Products/AccuScan-6000)
- Triton312: ±2,5 µm ungemittelt, ±0,125 µm bei 2 s Mittelung, für Teile ≤ 10,2 mm. Die Werte stammen teils von einer Testseite bzw. aus einem Maßblatt von 2011 und sind möglicherweise veraltet. [S] [Triton312](https://test.laserlinc.com/specs/Triton312_specs.html)
- Ein Jenoptik-bezogener Treffer nennt „repeatable results of .5 µm“ für Durchmesser an einem Schattenbildsystem. Quelle und Kontext sind unklar. [S] [Quality Magazine](https://www.qualitymag.com/articles/95134-optical-shaft-metrology-a-new-generation-of-measuring-systems-provides-cutting-edge-precision-accuracy)
- SPIE 1997: Triangulationssystem für Rohrenden mit ±10 µm Genauigkeit; ohne GRR, älter. [S] [SPIE](https://spiedigitallibrary.org/conference-proceedings-of-spie/3100/0000/Fast-inspection-of-radius-wall-thickness-eccentricity-and-ovality-at/10.1117/12.287761.full)

### Inferences
- Eine GRR-Studie (z. B. nach AIAG MSA oder VDA 5) müsste die Arbeit selbst durchführen. Datenblattwerte zur Wiederholbarkeit gelten meist für den statischen, gut geführten Prüfling, nicht für ein 3 m langes, durchhängendes und drehendes Rohr.

### Gaps
- Keine %GRR- oder Cg/Cgk-Ergebnisse von Herstellern oder Rohrherstellern gefunden.

## Messen bei Drehung, Synchronisation mit Encoder und kleinster Punktabstand

### Takeaway
Messen bei Drehung ist in Offline-Geräten üblich: BenchLinc, BenchMike Pro, Cerulean (100 Messungen je Umdrehung), Metron mit 360°-Option, die Micro-Epsilon-Anwendung und die C-Achse bei Mahr. Eine **Encoder-Synchronisation mit festem Punktabstand in mm** wird in den Treffern **nicht ausdrücklich beschrieben**.

### Cited Findings
- Metron: servogetriebene, wiederholgenaue Teileindexierung, Option 360°-Teiledrehung. [S] [LaserLinc Metron](https://laserlinc.com/metron-an-automated-tubing-guidewire-inspection-solution)
- BenchMike Pro dreht die Probe automatisch in vordefinierte Positionen. [S] [Nordson BenchMike Pro](https://www.nordson.com/en/Products/Measurement-and-Control-Products/BenchMike-Pro)
- Cerulean CD Express: 100 Einzelmessungen pro 360°-Umdrehung. [S] [The Engineer](https://www.theengineer.co.uk/content/news/high-speed-laser-micrometer-measures-circumference-diameter-and-ovality-of-cylindrical-objects)
- Micro-Epsilon: Rohr wird um 360° gedreht, Messung an drei axialen Positionen. [S] [Micro-Epsilon](https://www.micro-epsilon.com/applications/areas/Durchmesser/)
- Mahr MarShaft SCOPE 250 plus: C-Achse 0,2–60 1/min. [S] [Mahr](https://metrology.mahr.com/en-us/products/datasheet/5361802-optische-wellenmessgeraete-marshaft-scope-250-plus.pdf)

### Inferences
- Bei Inline-Mehrachsköpfen wird die Position meist über die Liniengeschwindigkeit zugeordnet. Für einen Offline-Prüfplatz mit festem Punktabstand (z. B. alle 2 mm) liegt ein Trigger über den Encoder der Linear- bzw. Drehachse nahe. Dafür fehlt hier ein Beleg aus der Recherche.

### Gaps
- Kein Beleg für Encoder-getriggerte Messung mit festem mm-Abstand und kein veröffentlichter kleinster Punktabstand bei einem Rohr-Prüfplatz.
- Keine Herstellerangaben zur Messung während kontinuierlicher Drehung (Wendelbahn) an langen Rohren.
