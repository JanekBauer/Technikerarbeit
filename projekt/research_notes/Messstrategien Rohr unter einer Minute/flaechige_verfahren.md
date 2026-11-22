# Flächige und bereichsweise berührungslose Messverfahren für ein langes dünnes Metallrohr (Ø 1–6,5 mm, bis 3 m, Querschnitt alle 2 mm, Ziel < 1 min)

Vorbemerkung zur Quellenlage: Viele Herstellerseiten (keyence.co.in, qualitrol.com, arxiv.org, pmc.ncbi.nlm.nih.gov, micro-epsilon.com) waren im Netz dieser Sitzung gesperrt. Werte daraus stammen aus Suchergebnis-Auszügen und sind als „Suchergebnis, nicht eingesehen“ gekennzeichnet. Eigene Rechnungen sind als „eigene Rechnung“ markiert.

**Bezugsgröße (eigene Rechnung):** %GRR = 6·σ_GRR / T · 100 %. Bei Durchmessertoleranz ±13 µm (T = 26 µm) und %GRR ≤ 10 % folgt σ_GRR ≤ 26 µm · 0,1 / 6 ≈ **0,43 µm** (mit 5,15σ statt 6σ: ≈ 0,50 µm). Für eine Formtoleranz von ca. 10 µm folgt σ ≤ 10 µm · 0,1 / 6 ≈ **0,17 µm**. Gefragt ist also eine Wiederholpräzision im Bereich einiger Zehntel Mikrometer, auf dem echten Bauteil (glänzendes, rundes, dünnes Rohr), nicht auf einem Herstellernormal.

## 1. Laserprofilsensoren (2D/3D-Lasertriangulation: Keyence LJ-X8000, Micro-Epsilon scanCONTROL, LMI Gocator)

### Takeaway
Die feinsten Profilsensoren geben auf ihrem Normal eine Wiederholpräzision von 0,2–0,3 µm bei nur 7–14,5 mm Profilbreite an; auf einem glänzenden Ø-1-mm-Rohr sind diese Werte nicht zu erwarten (Spiegelreflex, Speckle-Fehler bis ±20 µm in der Literatur). Für ±13 µm mit %GRR ≤ 10 % sind sie nach Datenlage **nicht geeignet**, bestenfalls für eine grobe Vorprüfung oder für Geradheit/Krümmung.

### Cited Findings
- Keyence LJ-X8000: X-Punktabstand je nach Kopf 2,5 µm (min. ca. 2 µm) bis 225 µm, 3200 Punkte je Profil (Suchergebnis, nicht eingesehen) — [Keyence LJ-X8000 Specs](https://keyence.com/products/measure/laser-2d/lj-x8000/specs)
- Keyence LJ-X8020: Referenzabstand 7,5 mm, X-Messbreite 7 mm (Nahbereich; Pressemitteilung nennt max. 8 mm), Wiederholpräzision Z und X je 0,3 µm; Bedingung laut Fußnote: Mittelwert der Höhe im Standard-Messbereich, Keyence-Standardtarget, Standardeinstellungen (Suchergebnis, nicht eingesehen) — [Keyence LJ-X8020](https://www.keyence.com/products/measure/laser-2d/lj-x8000/models/lj-x8020)
- Keyence LJ-X8030: X-Punktabstand 5 µm (min. 3 µm); LJ-X8060: X-Wiederholpräzision 0,5 µm (Suchergebnis, nicht eingesehen) — [Keyence LJ-X8030](https://www.keyence.com/products/measure/laser-2d/lj-x8000/models/lj-x8030/), [Keyence LJ-X8060](https://www.keyence.com/products/measure/laser-2d/lj-x8000/models/lj-x8060/)
- LMI Gocator 2510: X-Auflösung bis 8 µm, Z-Wiederholpräzision 0,2 µm, Sichtfeld 13–14,5 mm (nur diffus; 2512 auch spiegelnd) — [LMI Gocator 2500](https://lmi3d.com/series/gocator-2500-series/), [Basler Gocator 2510](https://www.baslerweb.com/en-sg/shop/lmi-sensor-gocator-2510/)
- Micro-Epsilon scanCONTROL 30xx: 1024 bzw. 2048 Punkte je Profil, Profilfrequenz bis 10 kHz; kleinste Messbereiche der Familie ab ca. 10 × 8 mm (Suchergebnis, nicht eingesehen) — [Micro-Epsilon scanCONTROL Katalog](https://www.micro-epsilon.com/download/products/cat--scanCONTROL--en.pdf)
- Speckle erzeugt bei Triangulationssensoren einen systematischen, wiederholbaren Fehler, im Versuch auf Stahl-Endmaß bis ca. ±20 µm — [Uni Hiroshima, Speckle-Einfluss](https://mecdes.hiroshima-u.ac.jp/~ibaraki.h0523/research/research_meas_kitagawa.html)
- Spiegelnde Oberflächen können verhindern, dass der Sensor den reflektierten Strahl erfasst; Untersuchungen setzen deshalb nicht spiegelnde Flächen voraus — [PMC12158334, Speckle-Kompensation Profilsensoren](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12158334/)
- Speckle-bedingte Unsicherheit ließ sich mit einem Diffusor um bis zu 63 % senken — [Csencsics et al. 2022, TU Wien](https://www.acin.tuwien.ac.at/file/publications/iat/pre_post_print/csencsics_2022_TIM.pdf)

### Inferences
- **Profil längs zur Rohrachse, Rohr dreht sich (eigene Rechnung):** Ein LJ-X8020 erfasst ca. 7 mm Rohrlänge je Profil, also ca. 3–4 Querschnitte im 2-mm-Raster gleichzeitig (bei 2,5 µm Punktabstand sogar sehr viele Stützstellen längs). Für 3 m sind ca. 430 Abschnitte nötig (Gocator 2510 mit 14 mm: ca. 215). Bei z. B. 360 Profilen je Umdrehung und 1 kHz dauert eine Umdrehung 0,36 s; mit ca. 0,3 s Verfahren je Abschnitt ergibt das ca. 430 × 0,66 s ≈ 280 s, also deutlich über 1 min. Erst mit ca. 5 Sensoren parallel oder einer Helix-Bahn (Rohr dreht, Sensor fährt kontinuierlich) käme man rechnerisch unter 1 min. Die Profilrate ist nicht der Engpass, die Mechanik schon.
- Ein einzelner Profilsensor sieht nur die ihm zugewandte Seite. Der Durchmesser ergibt sich dann aus Radius zur Drehachse; Rundlauf, Durchbiegung und Lagerspiel des 3 m langen, dünnen Rohrs gehen voll in den Messwert ein. Ein Ø-1-mm-Rohr mit 3 m Länge biegt sich ohne enge Stützung stark durch; jede Auflage-/Drehbewegung ist ein Fehlerbeitrag im µm-Bereich (Schätzung, nicht belegt).
- Quer zur Achse liegt auf Ø 1 mm nur ein Bogen von < 1 mm im Profil, also bei 2,5–8 µm Punktabstand nur ca. 100–400 Punkte, und an den Flanken mit steilem Einfallswinkel. Das verschlechtert eine Kreisanpassung zusätzlich.
- Die Herstellerwerte (0,2–0,3 µm) gelten für Mittelwerte über eine Fläche auf einem Standardtarget. Für ein glänzendes Metallrohr ist mit Werten eine Größenordnung schlechter zu rechnen (Schluss aus Speckle- und Spiegelreflex-Befunden). σ ≤ 0,43 µm auf dem Rohr ist daher unwahrscheinlich.

### Gaps
- Keine Herstellerangabe oder Anwendungsnotiz gefunden, die eine Durchmesser-Messunsicherheit von Laserprofilsensoren auf Ø 1–6,5 mm Metallrohr nennt.
- Die Datenblätter von Keyence und Micro-Epsilon konnten nicht direkt eingesehen werden (Hosts gesperrt); Linearitätswerte fehlen.

## 2. 360°-Ringprofilsensoren (mehrere Profilsensoren rund um Stab/Rohr, Extrusions-/Stabprüfung)

### Takeaway
Es gibt kommerzielle 360°-Systeme aus Laserlinien-Triangulation (LaserLinc FlawSense, Starrett Profile360/Surface360) für Rohr, Schlauch, Draht und Profile; belastbare Genauigkeitswerte im µm-Bereich wurden nicht gefunden. Sie sind für die Inline-Überwachung von Extrusion gebaut, nicht für Sub-µm-Wiederholpräzision.

### Cited Findings
- LaserLinc FlawSense: Laserlinien-Triangulation für 360°-Inline-Prüfung von Rohr, Schlauch, Draht und Kabel, unabhängig von der Lage; Hersteller behauptet genauere Durchmesser-/Ovalitätswerte als Lasermikrometer und Kamerasysteme (Herstelleraussage, nicht unabhängig geprüft) — [Production Machining/PTOnline, Surface-Flaw Detection](https://ptonline.com/products/surface-flaw-detection-for-pipe-tubing)
- Starrett Profile360 digitalisiert das Profil mit Linienlasersensoren und vergleicht mit CAD-Vorgabe; Surface360 misst die Oberflächengeometrie inline in Echtzeit — [Starrett Profile360](https://www.starrett.com/products/laser-measurement-systems/profile-measurement-systems/profile360)
- Ein Einachs-Durchmessermessgerät misst je Scan nur einen Querschnitt; volle Profilabdeckung braucht mehrere Sensoren oder Drehung von Sensor oder Stab — [Ranjan 2019, Stahlstab-Profilmessung](https://yadda.icm.edu.pl/baztech/element/bwmeta1.element.baztech-deb2219d-f39e-4004-a653-5bba3b563df4/c/saurabh_ranjan_real_4_2019.pdf)

### Inferences
- Ein Ring aus 3–4 Profilsensoren misst je Profil-Takt einen vollen Querschnitt ohne Rohrdrehung. Bei 1–10 kHz Profilrate und 2 mm Raster wäre die Zeit rechnerisch kein Problem (eigene Rechnung: 1500 Querschnitte für 3 m; bei 1 kHz 1,5 s, Vorschub dann 2 m/s; realistisch begrenzt durch Mechanik und Rohrführung, also eher 10–30 s bei 0,1–0,3 m/s).
- Die Genauigkeit ist aber durch die Einzelsensoren begrenzt (siehe Abschnitt 1) und zusätzlich durch die Registrierung der Sensoren zueinander. Für Ø 1 mm passen typische Ringsysteme vom Messbereich her schlecht (für größere Profile ausgelegt).

### Gaps
- Keine Datenblattwerte (Auflösung, Wiederholpräzision, kleinster Durchmesser) für FlawSense oder Profile360 gefunden.

## 3. Telezentrische Kamerasysteme, Kamera-Arrays längs des Rohrs, Zeilenkameras

### Takeaway
Telezentrische Durchlicht-(Schatten-)Messung ist das einzige flächige Verfahren in dieser Recherche, das σ im Bereich 0,03–0,2 µm (Hersteller, Normal) bzw. ca. 1 µm Unsicherheit (Literatur) erreicht, und sie misst beide Kanten gleichzeitig, also unabhängig von Durchbiegung und Rundlauf. Die Messfelder sind aber nur wenige mm bis cm groß; 3 m müssen gescannt oder mit sehr vielen Kameras abgedeckt werden. Mit wenigen gescannten Köpfen ist < 1 min rechnerisch erreichbar.

### Cited Findings
- Keyence TM-X5000: Wiederholpräzision ±0,03 µm (TM-X5006), ±0,08 µm (TM-X5040), ±0,1 µm (TM-X5065), ±0,2 µm (TM-X5120) (Suchergebnis, nicht eingesehen) — [Keyence TM-X5000 Specs](https://keyence.com/products/measure/micrometer/tm-x5000/specs)
- TM-X5065: Messbereich Ø 65 mm, Hochgenauigkeitsbereich Ø 40 mm, Positionsgenauigkeit ±1,2 µm (Hochgenauigkeitsbereich) bzw. ±2,2 µm (ganzer Bereich) (Suchergebnis, nicht eingesehen) — [Keyence UK TM-X5065](https://www.keyence.co.uk/products/measure/micrometer/tm-x5000/models/tm-x5065/)
- Definition der TM-X-Wiederholpräzision: Mittel der ±2σ-Werte bei 16-maliger Messung eines Glas-Kalibriermaßstabs in der Mitte des Messfelds (Suchergebnis, nicht eingesehen) — [Keyence Handbuch Kap. 6](https://keyence.com/support/manual/measure/tm-x5000/TM-X_UM_06.jsp)
- Telezentrische Subpixel-Zählung für Ringdurchmesser: Empfindlichkeit ca. 1/20 Pixel, mittlere Unsicherheit ca. 1 µm (Suchergebnis, nicht eingesehen) — [Poyraz et al., Uludağ Univ.](https://acikerisim.uludag.edu.tr/entities/publication/ecbc4675-8682-422d-89ab-6908c4adafb9/full)
- Vergleich von drei Subpixel-Kantenverfahren (Partial Area, Canny/Devernay, Subpixel-Zählung) mit telezentrischer Optik: alle zeigen eine Durchmesserabhängigkeit des Fehlers, die dem Abbildungssystem zugeschrieben wird; Korrektur über Referenznormale (Suchergebnis, nicht eingesehen) — [arXiv 2508.03721](https://arxiv.org/pdf/2508.03721)
- Telezentrische Kamera mit Zernike-Momenten-Kantenerkennung für Mikroteile: Vergrößerungsfehler 0,7 %, max. mittlerer Absolutfehler 0,84 µm über 2,1 mm Messbereich (Suchergebnis, nicht eingesehen) — [HIT Scholar, Mikroteile](https://scholar.hit.edu.cn/en/publications/method-for-measuring-geometric-dimensions-of-micro-parts-based-on/)
- Lian et al. (IEEE TIM 2025): Kalibrierung von Vergrößerung und Kantenlage mit Kugel und Lehrdorn reduzierte Durchmesserfehler um ca. 0,03–0,04 mm; unkorrigierter Kantenbias kann das Budget dominieren (Suchergebnis, nicht eingesehen) — [HIT Scholar, telezentrische Messung rotationssymmetrischer Teile](https://scholar.hit.edu.cn/en/publications/telecentric-imaging-based-dimensional-measurement-for-rotational-/)
- Doppel-Telezentrik-System für große Wellen: mittlerer Fehler ca. 5 µm, keine Messzeitangabe — [MDPI Sensors 22(11) 3982](https://mdpi.com/1424-8220/22/11/3982)
- Optische Wellenmessmaschinen (Jenoptik Opticline C): Wiederholbarkeit/GRR „ab 1 µm“, Längen bis 900 mm (C908/C914); Gebrauchtangebot C314 nennt Durchmesser-Wiederholpräzision 0,3 µm und Genauigkeit 1,0 + D/200 µm (Händlerangabe, nicht Datenblatt) — [Jenoptik Opticline Katalog 2020](https://www.jenoptik.us/-/media/hommel-etamic-documents/metrology/neu/opticline/opticline-general-catalogue-2020-04-en.pdf), [Machineseeker C314](https://www.machineseeker.ie/jenoptik+optical+systems+gmbh-opticline+c314/i-20355855); MPE < 2 µm typisch — [Quality Magazine](https://www.qualitymag.com/articles/92898-jenoptik-optical-shaft-measuring-devices)

### Inferences
- **Gescannter telezentrischer Kopf (eigene Rechnung):** Bei ca. 6 mm Sichtfeld längs der Achse (Annahme aus dem Modellnamen TM-X5006, nicht belegt) sind für 3 m ca. 500 Positionen nötig; bei 0,1 s je Bild/Position etwa 50 s. Mit 2–4 Köpfen parallel oder größerem Kopf (TM-X5040, 40 mm Hochgenauigkeitsfeld: 75 Positionen) rechnerisch 10–25 s. Jeder Bildausschnitt liefert alle Querschnitte im 2-mm-Raster gleichzeitig.
- Eine Ansicht liefert nur eine Schattenbreite je Querschnitt. Für Ovalität/Form sind mehrere Blickrichtungen nötig (z. B. 3 Köpfe unter 60° oder Rohr in Schritten drehen); die Messzeit steigt entsprechend.
- **Starres Kamera-Array über 3 m (eigene Rechnung):** Bei 5 µm Pixel im Objektraum und 1/20 Pixel Subpixel-Auflösung (≈ 0,25 µm) braucht man 3000 mm / 5 µm = 600 000 Pixel längs. Das sind ca. 37 Zeilenkameras mit 16k Pixeln oder ca. 120 Flächenkameras mit 5000 Pixeln Breite, jede mit eigener telezentrischer Optik (Telezentrik-Objektive sind so groß wie ihr Sichtfeld). Technisch denkbar, aber Kalibrieraufwand und Kosten sehr hoch; jede Kamera ist ein eigenes Messmittel für die MSA.
- **Zeilenkamera mit Vorschub:** Eine Zeile quer zur Achse plus Rohrvorschub erzeugt ein Bild der ganzen Länge; bei 2 mm Raster und z. B. 0,1 m/s Vorschub wären es 30 s (eigene Rechnung). Die Genauigkeit hängt dann zusätzlich an der Führung (Rohr darf sich nicht im Schärfebereich bewegen).
- σ ≤ 0,43 µm für den Durchmesser liegt im Bereich der Herstellerangaben (±0,03–0,2 µm als ±2σ), aber diese gelten am Glasmaßstab in Feldmitte. Literaturwerte auf realen Teilen liegen bei ca. 0,8–1 µm Unsicherheit. Erreichbar erscheint das Ziel nur mit: Durchlicht mit kollimierter Beleuchtung, Kalibrierung gegen Lehrdorne/Ringe ähnlichen Durchmessers (Durchmesserabhängigkeit des Kantenbias), Temperaturführung, sauberer Oberfläche und Mittelung mehrerer Bilder. Die Formtoleranz von 10 µm mit σ ≤ 0,17 µm ist deutlich schwieriger.

### Gaps
- Bildfeldgröße und Messrate der TM-X5006 konnten nicht belegt werden (Host gesperrt).
- Keine veröffentlichte Messzeit für ein gescanntes Telezentrik-System über mehrere Meter gefunden.
- Kein Volltext der Subpixel-Studien eingesehen; Pixelgröße und Vergrößerung der Versuchsaufbauten unbekannt.

## 4. Industrielle Computertomographie (CT) für lange, dünne Metallrohre

### Takeaway
CT scheidet für 3 m und < 1 min klar aus: kleine Voxel bedeuten kleines Sichtfeld, 3 m passen in keine bekannte Mess-CT, und die angegebenen Längenmessabweichungen liegen bei einigen µm (nicht σ < 0,5 µm).

### Cited Findings
- Werth TomoScope XL: Längenmessabweichung bis 4,5 µm, Werkstücke bis 725 mm Länge, abhängig vom Seitenverhältnis — [Werth TomoScope XL](https://www.werth.de/en/products/machines/d/computed-tomography/device/tomoscoper-xl.html)
- Helix-CT (Werkstück fährt während der Drehung längs der Drehachse) verkürzt bei großem Längen-/Durchmesserverhältnis die Messzeit gegenüber Raster-Tomographie und vermeidet Kegelstrahlartefakte — [Werth, Genauigkeit erhöht](https://werth.de/en/current/d/accuracy-increased.html)
- Skalierungsfehler wachsen linear mit der Nennlänge; MPE wird als lineare Funktion der Länge angegeben — [J. Sens. Sens. Syst. 11, 171–186, 2022](https://jsss.copernicus.org/articles/11/171/2022/jsss-11-171-2022.pdf)
- Ein Hersteller-MPE (9 + L/50) µm wird genannt — [IMEKO WC 2015 TC14](https://imeko.org/publications/wc-2015/IMEKO-WC-2015-TC14-281.pdf)
- VDI/VDE 2630-2.1 ist die wichtigste CT-spezifische Richtlinie, deckt nur Außengeometrien ab; das Verfahren mit kalibriertem Werkstück ist aufwendig — [PTB 2025, Hausotte](https://conferences.ptb.de/event/12/attachments/123/352/2025-12-03_13-30_Hausotte.pdf)
- Voxelgrößen-Kalibrierung an kalibrierter Länge: ca. ±1 µm auf einem 55-mm-Stab — [Lifton 2022, Univ. Southampton](https://eprints.soton.ac.uk/498002/1/1-s2.0-S0141635922002276-main.pdf)
- Kleinere effektive Pixelgröße bedeutet kleineres Sichtfeld; Stitching kostet Messzeit, Rechenzeit und erzeugt Artefakte — [Thermo Fisher, Helical microCT Whitepaper](https://assets.thermofisher.com/TFS-Assets/MSD/Reference-Materials/microct-helical-whitepaper-wp0020.pdf)

### Inferences
- **Eigene Rechnung:** Ein Detektor mit ca. 3000 Pixeln deckt bei 5 µm Voxel nur ca. 15 mm Länge ab, also ca. 200 Segmente für 3 m. Selbst bei optimistischen 1 min je Segment wären es über 3 h. Umgekehrt ergäbe 3 m auf 3000 Pixel 1 mm Voxel, viel zu grob für Ø 1 mm.
- Unabhängig von der Zeit liegt die Unsicherheit (MPE einige µm) über dem nötigen σ von ca. 0,4 µm.
- Sinnvoll nur als Referenz für kurze Rohrabschnitte (z. B. Wanddicke, Innenkontur) im Labor.

### Gaps
- Keine CT-Anlage für 3 m lange Teile mit µm-Voxeln gefunden; keine Werte zu Helix-CT-Messzeiten für dünne Metallrohre.

## 5. Streifenprojektion (Structured Light), Photogrammetrie, optische Kohärenztomographie (OCT)

### Takeaway
Alle drei Verfahren liegen bei der Genauigkeit eine bis zwei Größenordnungen über dem Bedarf oder sind für Metall/Außendurchmesser nicht geeignet. Keines erreicht σ < 0,5 µm auf einem Ø-1–6,5-mm-Rohr über 3 m.

### Cited Findings
- Streifenprojektion mit hoher Genauigkeit ist auf kleines Sichtfeld und kleine Schärfentiefe beschränkt; bei Defokus steigt die Tiefenunsicherheit stark — [DLR, Optics Express 33(1) 983](https://elib.dlr.de/217075/1/as%20downloaded%20article%20oe-33-1-983.pdf)
- Echtzeit-Streifenprojektion: Genauigkeit im Bereich zehn µm bei Sichtfeld um 1 m² (Suchergebnis, nicht eingesehen) — [NSF PAR, High-speed fringe projection](https://par.nsf.gov/servlets/purl/10392052)
- Streifenprojektion kann ungenauer als taktile Verfahren sein; geschätzte Unsicherheit erklärte die Abweichungen zu taktilen Referenzen nicht vollständig — [Univ. Nottingham, Dissertation](https://eprints.nottingham.ac.uk/73409/1/Thesis%20MK2.pdf)
- OCT: Dickenmessung wegen Lichtabschwächung auf nicht opake Materialien beschränkt; Zwei-Seiten-OCT erreicht ca. 3 µm auf opaken (flachen) Proben — [Optics Letters 45, 832 (2020)](https://ui.adsabs.harvard.edu/abs/2020OptL...45..832W/abstract)
- Industrielle OCT erreicht in der Praxis zuverlässig ca. 10 µm Auflösung an realen Proben — [Fraunhofer ITWM, OCT](https://www.itwm.fraunhofer.de/en/departments/mc/products-and-services/non-destructive-material-testing-oct.html)

### Inferences
- Für ein Metallrohr sieht OCT nur die Außenfläche (wie ein Abstandssensor) und bietet gegenüber konfokalen oder Triangulationssensoren keinen Vorteil.
- Glänzende, gekrümmte Oberflächen sind für Streifenprojektion und Photogrammetrie ungünstig (Glanzlichter); meist wäre Mattierungsspray nötig, das selbst einige µm aufträgt (Schluss, nicht belegt).

### Gaps
- Keine belastbare Quelle zur Photogrammetrie an dünnen Metallrohren mit µm-Genauigkeit gefunden.

## 6. Veröffentlichte Systeme, die lange dünne Stäbe/Rohre/Drähte „in einem Schuss“ messen

### Takeaway
Gefunden wurden nur Inline-Systeme für Extrusion/Draht (Laserscan-Mikrometer, 360°-Triangulation), die einen Querschnitt pro Scan messen und das Rohr durchlaufen lassen, sowie optische Wellenmessmaschinen bis 900 mm. Ein System, das 3 m mit Sub-µm-Wiederholpräzision in einem Schuss erfasst, wurde nicht gefunden.

### Cited Findings
- Nordson AccuScan Pro (Einachs-Durchmessermessgerät): Auflösung 0,00001 mm, 1200 Scans/s — [Nordson AccuScan Pro](https://www.nordson.com/en/products/measurement-and-control-products/accuscan-pro)
- Draht wird mit 10–20 m/s extrudiert; ältere Scanner kamen über ca. 10 m/s nicht mit (Patent) — [US-Patent 4659937](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4659937)
- Jenoptik Opticline C: max. Länge 900 mm, GRR „ab 1 µm“ — [Jenoptik Opticline Katalog 2020](https://www.jenoptik.us/-/media/hommel-etamic-documents/metrology/neu/opticline/opticline-general-catalogue-2020-04-en.pdf)

### Inferences
- Die Auflösung eines Durchlauf-Mikrometers (0,01 µm) ist nicht seine Wiederholpräzision; für die MSA zählt σ am Bauteil.
- Für < 1 min bei 3 m und 2-mm-Raster sind 1500 Querschnitte zu messen. Gesamtbewertung (eigene Bewertung): Nur Durchlicht-/Schattenverfahren (telezentrische Kamera, Laserscan-Mikrometer, ggf. mehrere Köpfe unter verschiedenen Winkeln) mit Vorschub längs der Achse kommen nach Datenlage in Reichweite von σ ≈ 0,1–0,5 µm. Laserprofil, Ringprofil, Streifenprojektion, Photogrammetrie, OCT und CT verfehlen die Genauigkeit, CT zusätzlich die Zeit.

### Gaps
- Keine unabhängigen GRR-Studien für eines der Verfahren an Rohren Ø 1–6,5 mm gefunden; die Eignung muss durch eine eigene MSA (Verfahren 1 und 2) am realen Rohr nachgewiesen werden.
