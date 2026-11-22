# Messstrategien (Kinematik und Sensoranordnung) für Außen-Ø und Formabweichung eines dünnen Rohrs, Taktzeit < 60 s

## 1. Strategievergleich: Geschwindigkeiten, Raten, Sensorzahl, Zeit für 1500 Querschnitte

### Takeaway
Stop-and-go mit Drehung (a) ist mit einem Kopf um den Faktor 15–20 zu langsam; unter 60 s kommen nur kontinuierliche Verfahren: feste Mehrachsköpfe mit Vorschub (c), Helixscan mit rotierendem Kopf oder rotierendem Rohr (b, d) und eine Silhouetten-Kamera mit langem Messfeld bei langsamer Rohrdrehung (f). Volle Umfangserfassung je 2 mm in < 60 s ist kinematisch plausibel, wenn das Rohr nur langsam (≈ 30–60 U/min) dreht und das Messfeld axial lang ist (f), oder wenn ein Kopf mit einigen hundert U/min um das Rohr rotiert (d). Bei (f) ist die Bedingung der Zielkonflikt Messfeldlänge gegen Genauigkeit: ein langes Feld (40 mm) hat laut Herstellerangabe ±1,2 µm, ein genaues Feld (Ø 6 mm) ist zu kurz für < 60 s und zu klein für Ø 6,5 mm. Ob (f) reicht, hängt an der noch offenen Toleranz für Ø max − Ø min.

### Cited Findings
- Scanrate eines Vierachs-Schattenwurfmessgeräts: 2400 Scans/s je Achse, 9600 Scans/s gesamt (AccuScan 6012/6000) — [Nordson AccuScan 6000](https://www.nordson.com/en/Products/Measurement-and-Control-Products/AccuScan-6000) (Suchergebnis, nicht eingesehen); gleiche Angabe in der Pressemitteilung zum 6012 — [plasticsmachinerymanufacturing.com, AccuScan 6012 medical tubing](https://www.plasticsmachinerymanufacturing.com/thermoforming/article/13000341/ndc-accuscan-6012-gauge-zeros-in-on-medical-tubing) (Suchergebnis, nicht eingesehen).
- Optisches Mikrometer mit 16 000 Messungen/s (Keyence LS-9000) — [Keyence LS-9000](https://www.keyence.com/products/measure/micrometer/ls-9000/) (Suchergebnis, nicht eingesehen); unabhängig bestätigt — [machinery.co.uk](https://www.machinery.co.uk/content/product-launches/keyence-offers-16-000-hz-sampling-rate-ls-9000-optical-micromet) (Suchergebnis, nicht eingesehen).
- Telezentrisches Bildmesssystem (Keyence TM-X5000) mit Messfeld-Ø 6, 40, 65 bzw. 124 mm (Produktseite nennt 120 mm für das breiteste Modell, Spezifikationsseite 124 mm – Widerspruch), Schärfentiefe ± 20 mm — [Keyence TM-X5000 Specs](https://keyence.co.in/products/measure/micrometer/tm-x5000/specs); [Keyence TM-X5000](https://keyence.com/products/measure/micrometer/tm-x5000) (Suchergebnis, nicht eingesehen).
- Zumbach baut aus bis zu 6 ODAC-Scannern Messeinheiten SMS (statisch), SMO (oszillierend) und SMR (rotierend) — [Zumbach Katalog via directindustry](https://pdf.directindustry.com/pdf/zumbach-electronic-ag/zumbach-electronic-ag-general/15879-830759.html) (Suchergebnis, nicht eingesehen).
- Zumbach DVO 2: mechanische Oszilliervorrichtung, die den ODAC-Messkopf auf einer Scheibe kontinuierlich um das Produkt schwenkt, Winkel einstellbar −50° bis +50°, 1 bis 3 Messachsen — [Zumbach DVO 2 via directindustry](https://pdf.directindustry.com/pdf/zumbach-electronic-ag/dvo-2/15879-1024559.html) (Suchergebnis, nicht eingesehen).
- Patent US6862099 „Tubular ovality testing“: rotierender Kopf mit Laser(n), der um das durchlaufende Rohr dreht und eine Spiralbahn beschreibt; Laser zielen dort auf einen berührenden Messschuh — [US6862099 (USPTO)](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6862099) (Suchergebnis, nicht eingesehen; berührend, nicht direkt übertragbar).
- Starrett Profile360: Laser-System für Rohr-Außen-Ø und Unrundheit, erfasst einen vollen Querschnitt in einem Zyklus, aber für Rohr 6"–24" — [Starrett Profile360](https://starrett.com/products/laser-measurement-systems/profile-measurement-systems/360pipe) (Suchergebnis, nicht eingesehen).
- Industrie-CT: Helix-CT für Gussteile mit Scans von „wenigen Sekunden“ (Herstellerangabe) — [foundrymag, Baker Hughes](https://www.foundrymag.com/new-products/article/21119902/fast-automated-ct-scanning-baker-hughes-inspection-technologies); Inline-CT XCTube: Gesamtprüfung eines Fahrwerksteils < 30 s, Voxelgröße 120–400 µm — [foundrymag, XCTube](https://www.foundrymag.com/new-products/article/21926976/highspeed-inline-product-inspection) (beide Suchergebnis, nicht eingesehen).
- Industrie-CT-Scans großer/dichter Teile dauern wegen begrenzter Röhrenleistung deutlich länger als medizinische; lange Scanzeiten begrenzen den Durchsatz — [US9188549](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9188549); [US9476845](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9476845) (Suchergebnis, nicht eingesehen).

### Inferences (alles eigene Rechnung, Annahmen offen genannt)

Randbedingungen (aus Auftrag): Rohr Ø 1–6,5 mm, Länge bis 3 m, Nitinol/Edelstahl/Tantal; je 2 mm ein Querschnitt (≈ 1500 Querschnitte); Kennwerte Ø und Ø max − Ø min über den Umfang; berührungslos, Führen/Stützen erlaubt. Laut `cockpit/daten/reqs.json` gilt außerdem r10 (Anf. 2.5): „Auswertung je Messpunkt, Mittelwerte unzulässig“; die Toleranz für Ø max − Ø min (r06, Anf. 2.1) ist offen, frühere Werte 0,010 / 0,025 mm (NiTi / Edelstahl) gelten als nicht gesichert.

Gemeinsame Rechenbasis (eigene Rechnung):
- 3000 mm in 60 s ⇒ mittlere Axialgeschwindigkeit v = 50 mm/s, wenn die ganze Minute gemessen wird. Mit realistischem Handling (Einlegen, Zentrieren, Auswerfen, z. B. 10–15 s) bleiben 45–50 s ⇒ v ≈ 60–67 mm/s.
- Abtastabstand pro Messwert in Axialrichtung: Δz = v / f (f = Messrate je Achse). Bei f = 2400 Hz und v = 67 mm/s ⇒ Δz ≈ 0,028 mm. Die 2-mm-Forderung ist für die Axialrichtung damit kein Engpass; der Engpass ist die Abdeckung des Umfangs.
- Eine Durchmessermessung (Schattenwurf-Mikrometer, Zweipunktmessung) bei Winkel φ deckt die Richtungen φ und φ+180° gleichzeitig ab. Für alle Durchmesserrichtungen reicht daher eine **halbe Umdrehung (180°)**, mit M gleichmäßig verteilten Achsen reichen 180°/M.

**(a) Stop-and-go je Querschnitt mit Rotation**
- Ablauf je Querschnitt: 2 mm verfahren + Ausschwingen + 180° drehen (Schattenwurf-Achse) + Messen.
- Annahme: Verfahren 2 mm + Beruhigen 0,15 s, Drehung 180° bei 1 U/s = 0,5 s ⇒ ≈ 0,65 s/Querschnitt ⇒ 1500 × 0,65 s ≈ 975 s ≈ 16 min.
- Für 60 s wären 40 ms je Querschnitt nötig (inkl. Start/Stopp eines 3-m-Rohrs) – mechanisch nicht plausibel. Mit K parallelen Köpfen (Strategie e) sinkt die Zeit auf ≈ 16 min / K; für < 60 s wären K ≈ 16–20 Köpfe nötig.
- Sensorrate unkritisch (z. B. 2400 Hz ⇒ ≈ 1200 Werte je halbe Umdrehung), Datenrate klein.
- Fazit: nicht < 60 s; geeignet als Referenz-/Kalibrierverfahren oder Stichprobe.

**(b) Kontinuierliche Rohrdrehung + Vorschub (Helixscan, Rohr dreht)**
- Bedingung für „volle Durchmesserabdeckung je 2 mm“: Während das Rohr 2 mm vorrückt, müssen 180°/M Drehung stattfinden (M = Zahl der Schattenwurf-Achsen).
- Drehzahl n ≥ v / (2 · M · 2 mm). Bei v = 60 mm/s: M = 1 ⇒ n ≥ 15 U/s = 900 U/min; M = 2 ⇒ 450 U/min; M = 4 ⇒ 225 U/min.
- Ganghöhe der Helix je volle Umdrehung p = v/n; mit M = 1 und n = 15 U/s ⇒ p = 4 mm je Umdrehung = 2 mm je halber Umdrehung. Die 2-mm-Forderung bedeutet also: **Ganghöhe je 180°/M ≤ 2 mm**, nicht je 360°.
- Winkelauflösung: Δφ = 360°·n/f; bei n = 15 U/s, f = 2400 Hz ⇒ 2,25° je Messwert (80 Werte je 180°); bei f = 16 000 Hz ⇒ 0,34°.
- Problem: Ein 3 m langes Rohr mit Ø 1 mm bei mehreren hundert U/min zu drehen erzeugt Schlag und Schwingen (Rohr ist biegeweich); Antrieb über die Länge und Führung nötig. Rohrdrehung ist bei 1–6,5 mm Ø und 3 m Länge nur bei niedriger Drehzahl realistisch (siehe f).
- Torsion und Ruckgleiten: Wird das 3-m-Rohr nur an einem Ende gedreht, kann der Drehwinkel an der Messstelle durch Torsion und Reibung in den Stützen hinter dem Spannfutterwinkel zurückbleiben oder ruckeln. 180° am Futter garantieren dann keine 180° am Sensor. Abhilfe: Antrieb oder Mitnahme nahe der Messstelle, Winkelmessung am Rohr selbst oder Drehwinkel-Reserve über 180° einplanen. Gilt genauso für (f).
- Zeit: ≈ 50 s Messen + Handling – kinematisch < 60 s möglich, mechanisch kritisch.

**(c) Feste Mehrachsköpfe, nur Vorschub, keine Drehung**
- v = 50–67 mm/s, Messrate 2400 Hz/Achse ⇒ Δz ≈ 0,02–0,03 mm; je 2-mm-Abschnitt ≈ 70–100 Messungen je Achse (Mittelung möglich).
- Zeit: reine Messzeit = Durchlaufzeit ≈ 45–60 s; < 60 s plausibel. Datenrate: M × 2400 Werte/s, z. B. 4 × 2400 × 8 Byte ≈ 77 kB/s – unkritisch.
- Grenze: Formabweichung wird nur in M Richtungen erfasst ⇒ systematische Unterschätzung (siehe Abschnitt 3). Kein Teil des Rohrs muss drehen – mechanisch am einfachsten.

**(d) Rotierender (oder oszillierender) Messkopf um das laufende Rohr**
- Gleiche Formel wie (b), aber der Kopf dreht statt des Rohrs: n ≥ v/(4 mm · M). Bei v = 60 mm/s, M = 2 Achsen (90°) ⇒ n ≥ 7,5 U/s = 450 U/min; M = 3 ⇒ 300 U/min.
- Oszillierend (wie Zumbach DVO 2, ±50°): Zwei Achsen um 90° versetzt, die ±45° schwenken, überstreichen 180°. Pro Schwenk (einfache Richtung) muss das Rohr < 2 mm weiterlaufen ⇒ Schwenkfrequenz ≥ v/2 mm = 30 Hub/s bei 60 mm/s – für eine Mechanik mit Messkopf auf Scheibe vermutlich zu schnell (keine Herstellerangabe zur Schwenkfrequenz gefunden). Dauerdrehung mit Schleifring/Funk (Prinzip aus US6931748, siehe Gaps) ist für hohe Drehzahl geeigneter.
- Vorteil gegenüber (b): Rohr läuft nur axial, kein Rohrschlag; Kopf ist kompakt und kann ausgewuchtet werden.
- Zeit: wie (c) ≈ 45–60 s; < 60 s plausibel, wenn Kopf 300–900 U/min schafft.

**(e) Mehrere Messköpfe parallel entlang der Länge**
- K Köpfe teilen das Rohr in K Abschnitte von 3000/K mm; jeder Kopf fährt nur 3000/K mm (oder das Rohr nur 3000/K mm).
- Für (a): Zeit ≈ 975 s / K ⇒ K ≈ 20 für 50 s. Für (b)/(d): v sinkt auf 60/K mm/s, Drehzahl sinkt um Faktor K (z. B. K = 4, M = 1 ⇒ 225 U/min).
- Aufwand: K komplette Messstellen, Abgleich der Köpfe untereinander, Übergabestellen an den Abschnittsgrenzen.

**(f) Silhouetten-Kamera / Profil über ein Längenstück, Rohr dreht langsam**
- Ein telezentrisches Bild mit Messfeldlänge L liefert für alle Querschnitte im Feld gleichzeitig den Ø in einer Richtung.
- Kontinuierlich (Drehung + Vorschub): Ein Querschnitt bleibt L/v Sekunden im Feld; in dieser Zeit muss das Rohr 180° drehen ⇒ n ≥ v/(2L). Mit L = 60 mm (Feld Ø 65 mm, s. Findings) und v = 60 mm/s ⇒ n ≥ 0,5 U/s = 30 U/min. Mit L = 35 mm (Feld Ø 40 mm) ⇒ ≈ 52 U/min.
- Bildrate für A Winkelstellungen je Querschnitt: f_Bild ≥ A·v/L; für A = 18 (10°-Raster) und L = 60 mm ⇒ 18 Bilder/s; für A = 36 ⇒ 36 Bilder/s. Bildrate des TM-X5000 nicht eingesehen (Gap).
- Datenmenge: 50 s × 18–36 Bilder/s ≈ 900–1800 Bilder je Rohr; Auswertung ist Kantendetektion je Pixelspalte – rechnerisch machbar, aber Bildrate und Auswertezeit des konkreten Systems ungeklärt.
- Diese Strategie entkoppelt Drehzahl und Vorschub am stärksten: niedrige Drehzahl, trotzdem volle Umfangsabdeckung je 2 mm. Rohrschlag verfälscht den Ø nicht, solange das Rohr im telezentrischen Feld bleibt (Schärfentiefe ±20 mm laut Findings).
- **Entscheidende Bedingung: Messfeldlänge gegen Genauigkeit.** Werte aus der Nachbar-Recherche `research_notes/Berührungslose Sensoren für drehende Rohre/bild_telezentrisch_2d.md` (dort als Suchergebnis [S] markiert): TM-X5006 Messbereich Ø 6 mm, Positionsgenauigkeit ±0,2–0,3 µm; TM-X5040 Hochgenauigkeitsbereich Ø 26 mm, ±1 µm (±2 µm im ganzen Feld); TM-X5065 Hochgenauigkeitsbereich Ø 40 mm, ±1,2 µm (±2,2 µm im ganzen Feld); Bildaufnahme ca. 24 ms bei vollem Feld, ca. 3 ms bei verkleinertem Bereich.
  - Langes Feld, z. B. TM-X5065 mit L = 40 mm: n ≥ 60/(2·40) = 0,75 U/s = 45 U/min; bei ≈ 41 Bildern/s (24 ms) ⇒ A = 41·40/60 ≈ 27 Winkelstellungen je Querschnitt (≈ 6,7°). Kinematisch < 60 s, aber Genauigkeit ±1,2 µm.
  - Genaues Feld, TM-X5006 mit L ≈ 4–6 mm: n ≥ 60/(2·5) = 6 U/s = 360 U/min, A = 41·5/60 ≈ 3–4 Winkel bei vollem Feld – zu wenig; im 3-ms-Modus (≈ 330 Bilder/s) ≈ 27 Winkel, aber mit verkleinertem Bereich. Zudem passt Ø 6,5 mm nicht in ein Ø-6-mm-Feld.
  - Bewertung: Bei einer Toleranz von z. B. 10 µm (früherer, nicht gesicherter NiTi-Wert) und %GRR ≤ 10 % (reqs.json) sind ±1–2 µm Genauigkeit grenzwertig bis zu grob. Ob (f) mit langem Feld reicht, lässt sich erst mit der gesicherten Toleranz entscheiden; sonst nur mit mehreren genauen Kameras parallel (Kombination mit e).
- Zeit: ≈ 45–60 s; **< 60 s kinematisch plausibel**, messtechnisch nur, wenn die Genauigkeit bei Messfeldlänge L zur Toleranz passt.
- Variante Zeilen-/Linientriangulationssensoren: misst nur die zugewandte Seite (Radius, nicht Ø) ⇒ zwei gegenüberliegende Sensoren und eine Mittelpunktreferenz nötig; sonst gleiche Kinematik.

**(g) Vollfeld-Verfahren (3D-Scan, CT, Photogrammetrie, viele Kameras)**
- Viele Kameras über 3 m: bei L ≈ 60 mm je Kamera ⇒ ≈ 50 Kameras je Blickrichtung; für Formabweichung mehrere Richtungen (z. B. 3–4) ⇒ 150–200 Kameras – unwirtschaftlich. Alternativ ≈ 50 Kameras und Rohr 180° drehen ⇒ Messzeit wenige Sekunden, aber sehr hoher Aufwand.
- CT: veröffentlichte Inline-CT-Werte gelten für kompakte Gussteile (Voxel 120–400 µm) und sind für µm-Toleranzen an Ø 1–6,5 mm viel zu grob; ein 3 m langes Teil passt nicht in übliche Messräume; Tantal ist für Röntgen stark absorbierend (allgemeines Wissen, nicht quellenbelegt). Für < 60 s und µm-Genauigkeit nicht plausibel.
- 3D-Streifenprojektion/Photogrammetrie: keine Quelle zu Genauigkeit an Ø 1 mm über 3 m gefunden (Gap).

**Übersicht (eigene Rechnung, v = 60 mm/s, ein Messplatz, falls nicht anders genannt)**

| Strategie | Drehung nötig | Sensoren | Messzeit 1500 QS | Umfang voll? | < 60 s? |
|---|---|---|---|---|---|
| (a) Stop-and-go | 180° je QS | 1 Achse | ≈ 16 min | ja | nein (erst mit ≈ 20 Köpfen) |
| (b) Helix, Rohr dreht | 900/M U/min | M Achsen | ≈ 50 s | ja (Fenster 2 mm) | kinematisch ja, mechanisch kritisch |
| (c) Mehrachskopf fest | keine | 2–8 Achsen | ≈ 50 s | max − min: worst case −25 % (3 Achsen) bis −29 % (4 Achsen); mit Ellipsenanpassung exakt, wenn die Form elliptisch ist, sonst N ≥ k + 1 nötig | ja |
| (d) Kopf rotiert | 900/M U/min (Kopf) | M Achsen | ≈ 50 s | ja (Fenster 2 mm) | ja, wenn Kopf schnell dreht |
| (e) K Köpfe parallel | je nach Basis /K | K × Basis | Basis / K | wie Basis | erleichtert a, b, d |
| (f) Kamera, L = 40 mm | ≈ 45 U/min | 1 Kamera | ≈ 50 s | ja (≈ 27 Winkel je QS) | kinematisch ja; Genauigkeit ±1,2 µm, Eignung hängt an Toleranz |
| (g) Vollfeld | – | 50–200 Kameras / CT | s bis min | ja | Aufwand/Genauigkeit unplausibel |

### Gaps
- Hinweis zur Quellenlage: Fast alle Herstellerseiten (keyence.com, nordson.com, laserlinc.com, zumbach.com, sikora.net) sowie directindustry.com, patents.google.com, findlight.net und matterhackers.com waren in dieser Sitzung nicht abrufbar (DNS/Proxy-Sperre). Alle Herstellerwerte stammen daher aus Suchergebnis-Zusammenfassungen und sind als „Suchergebnis, nicht eingesehen“ markiert. Alle Taktzeiten und Fehlerwerte ohne Quelle sind „eigene Rechnung“; das Rechenskript liegt nicht im Repo (Scratchpad), die Formeln stehen hier.
- Keine Herstellerangabe zu Drehzahlen rotierender Ø-Messköpfe (Zumbach SMR) oder zur Schwenkfrequenz des DVO 2 gefunden.
- Bildrate, Auswertezeit und Genauigkeit telezentrischer Kameras (TM-X5000 u. a.) nicht eingesehen; für (f) entscheidend.
- Keine Quelle für CT oder Streifenprojektion an 3 m langen dünnen Rohren; keine Quelle zur Röntgenabsorption von Tantal in dieser Sitzung geprüft.
- Handlingzeit (Einlegen, Ausrichten, Spannen eines 3-m-Rohrs) ist eine Annahme (10–15 s).


## 2. Wie misst die Industrie Ovalität inline, und wie ist „Ovalität“ dort definiert?

### Takeaway
Inline (Draht, Kabel, Schlauch, Medizinschlauch) wird Ovalität mit 2-, 3- oder 4-Achs-Schattenwurfköpfen ohne Drehung gemessen und als Differenz der größten und kleinsten Achsmessung (max − min der M Achsen) ausgewiesen; eine volle Umfangserfassung gibt es nur mit oszillierenden/rotierenden Köpfen oder offline. Die Hersteller räumen selbst ein, dass die Achszahl die Genauigkeit begrenzt.

### Cited Findings
- LaserLinc Triton: drei koplanare Messachsen, je 60° versetzt, Messebene senkrecht zum Produkt; liefert mittleren Ø und Ovalität („roundness or eccentricity“); Anwendungen u. a. Draht, Kabel, Schlauch, Rohr — [LaserLinc Triple-Axis](https://laserlinc.com/triple-axis_laser_micrometers.html); [LaserLinc Triton](https://www.laserlinc.com/products/triton) (Suchergebnis, nicht eingesehen).
- Ein Laser-Mikrometer-Hersteller (LaserLinc, Seite „DualAxis5-Ovality“): Bei einem Zweiachsgerät ist die Ovalität nur richtig, wenn Haupt- und Nebenachse des Produkts auf den Messachsen liegen; um 45° gedreht zeigen beide Achsen gleiche Werte ⇒ Ovalität null, „100 % Fehler“ — [LaserLinc DualAxis5-Ovality](https://test.laserlinc.com/measurement_types/DualAxis5-Ovality.html) (Suchergebnis, nicht eingesehen; Host nicht erreichbar).
- Nordson/NDC AccuScan 6000/6012: Vierachsgerät; „42 % improvement in detecting true ovality over three-axis gauges“ bzw. „42 % improvement in ovality error over three-axis gauges“; 100 % Ovalitätsgenauigkeit nur, wenn das Produkt auf den Messachsen ausgerichtet ist; Dreiachsgeräte erreichen „nie 100 %“ — [Nordson AccuScan 6000](https://www.nordson.com/en/Products/Measurement-and-Control-Products/AccuScan-6000); [plasticsmachinerymanufacturing.com 6012](https://www.plasticsmachinerymanufacturing.com/thermoforming/article/13000341/ndc-accuscan-6012-gauge-zeros-in-on-medical-tubing); [NDC 6000 Katalog via directindustry](https://pdf.directindustry.com/pdf/ndc-technologies/accuscan-6000-series-industry-s-only-four-axis-diameter-ovality-gaugesfor-products-up-to-50-mm/26204-907573.html) (Suchergebnis, nicht eingesehen; Herstellerangaben eines Wettbewerbers).
- Beta LaserMike (Vierachsgerät): Zwei- und Dreiachsgeräte liefern Ovalität nur mit begrenzter Genauigkeit, exakt nur bei ausgerichtetem elliptischem Produkt — [tic.co.th Datenblatt](https://www.tic.co.th/storages/products/attachments/file_1170_5955.pdf) (Suchergebnis, nicht eingesehen).
- Zumbach ODAC 33TRIO/63TRIO: drei synchronisierte Messachsen in einer Ebene für Ø und Ovalität; QC 2 als Offline-Messplatz für Ø und Ovalität von Draht-, Kabel- und Rohrproben — [Zumbach ODAC 63TRIO via directindustry](https://pdf.directindustry.com/pdf/zumbach-electronic-ag/odac-63trio/15879-1087409.html); [Zumbach QC 2](https://pdf.directindustry.com/pdf/zumbach-electronic-ag/qc-2-piece-measurement/15879-1119901.html) (Suchergebnis, nicht eingesehen).
- Ovalitätsdefinition in einem Patent: (große Achse − kleine Achse) / mittlerer Ø, Ellipse als Näherung der Rohrform — [US6272762 Ovality measurement method](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6272762) (Suchergebnis, nicht eingesehen).
- Filament-Industrie (3D-Druck), Faustregel: Zahl der Achsen × 2 = Eckenzahl der „schlimmstmöglichen“ unerkannten Form; bei 3 Achsen ein Sechseck — [MatterHackers, Importance of Ovality](https://www.matterhackers.com/articles/digital-fabrication-anatomy-the-importance-of-ovality) (Suchergebnis, nicht eingesehen; populärtechnische Quelle).

### Inferences
- Industrie-„Ovalität“ = max − min über M diskrete Richtungen (M = 2–4), also eine **Untergrenze** der echten Ø-max − Ø-min über den Umfang. Für ein Pflichtenheft mit „über den Umfang“ muss klar sein, ob die Achsmethode akzeptiert wird oder ein Korrekturmodell/volle Abtastung gefordert ist.
- Die Herstellerformulierungen „100 % bei Ausrichtung“ meinen den günstigsten Fall; für ein Prüfmittel zählt der ungünstigste Fall (Abschnitt 3).

### Gaps
- Konkrete Inline-Liniengeschwindigkeiten (m/s) aus Draht-/Kabel-/Faserlinien wurden in dieser Sitzung nicht belegt; Herstellerseiten gesperrt.
- Kein Beleg gefunden, wie Medizinrohr-Hersteller (Nitinol/Edelstahl, Ø 1–6,5 mm) die Formabweichung bei der Endprüfung definieren (Achsen vs. voller Umfang).
- Wie Sikora für Rohre Ovalität misst, ließ sich nicht klären (Suche zu „CENTERWAVE“ lieferte nur fachfremde Treffer).


## 3. Mathematischer Fehler bei N festen Achsen statt voller Drehung

### Takeaway
Für eine Ellipse (2. Harmonische) liefert ein Gerät mit N gleichmäßig verteilten Achsen im ungünstigsten Lagewinkel: N = 2 ⇒ 0 % der echten Ovalität (100 % Fehler), N = 3 ⇒ 75 % (−25 %), N = 4 ⇒ 70,7 % (−29,3 %), N = 6 ⇒ 86,6 % (−13,4 %), N = 8 ⇒ 92,4 % (−7,6 %). Gemittelt über alle Lagewinkel unterschätzen 3 Achsen um 17,3 %, 4 Achsen um 10,0 % – das ergibt genau die von Nordson genannte „42 % Verbesserung“ (eigene Rechnung). Ungerade Harmonische (Gleichdick-Formen) sieht keine Durchmessermessung, egal mit wie vielen Achsen.

### Cited Findings
- Zweiachsgerät: um 45° verdrehte Ellipse ⇒ Ovalität 0, „100 % Fehler“ — [LaserLinc DualAxis5-Ovality](https://test.laserlinc.com/measurement_types/DualAxis5-Ovality.html) (Suchergebnis, nicht eingesehen).
- Vierachsgerät: „42 % improvement in ovality error over three-axis gauges“; Dreiachsgeräte „never 100 %“ auch bei Ausrichtung — [Nordson AccuScan 6000](https://www.nordson.com/en/Products/Measurement-and-Control-Products/AccuScan-6000) (Suchergebnis, nicht eingesehen).
- Mehrsonden-Rundheitsmessung (Fehlertrennung, rotierendes Werkstück): bestimmte Harmonische werden je nach Sondenwinkeln unterdrückt; maßgeblich ist der größte gemeinsame Teiler der Winkel mit 180°; Kato et al. schlagen 0°/38°/67° vor; mehr als vier Sonden verbessern das Ergebnis laut einer Simulationsstudie kaum; Konditionszahl der Gleichungsmatrix korreliert mit der Unsicherheit der Harmonischen — [Tiainen & Viitala, Robust optimization of multi-probe measurement (Aalto)](https://acris.aalto.fi/ws/portalfiles/portal/44872505/ENG_Tiainen_et_al_Robust_optimization_of_multi_probe_Measurement.pdf); [Tiainen et al., Effect of positional errors, MSSP (Aalto)](https://acris.aalto.fi/ws/portalfiles/portal/42549885/ENG_Tiainen_et_al_Effect_of_positional_Mechanical_Systems_and_Signal_Processing.pdf); [Springer, Nanomanufacturing and Metrology s41871-021-00120-8](https://link.springer.com/article/10.1007/s41871-021-00120-8) (Suchergebnis, nicht eingesehen). Achtung: Diese Verfahren betreffen Abstandssonden an einem **drehenden** Teil (Trennung Form/Spindelfehler), nicht feste Achsen ohne Drehung.
- Keine unabhängige Studie gefunden, die den Unterschätzungsfehler je Achszahl beziffert (Ergebnis der Suche).

### Inferences (eigene Rechnung)
**Modell:** Breitenfunktion (Ø in Richtung φ) einer leicht ovalen Kontur: w(φ) = D + (Δ/2)·cos(2(φ − φ0)), Δ = Ø max − Ø min. Ein Gerät mit N Achsen im Abstand 180°/N misst w an N Stellen; die angezeigte Ovalität ist max − min dieser N Werte. Numerisch über alle Lagewinkel φ0 ausgewertet (zusätzlich mit exakter Ellipse a = 1,03, b = 0,97 geprüft, gleiche Werte bis auf < 1 %):

| Achsen N | Anzeige/echt, ungünstigster Fall | Fehler worst case | Anzeige/echt, Mittel | Fehler Mittel |
|---|---|---|---|---|
| 2 | 0 % | −100 % | 63,7 % | −36,3 % |
| 3 | 75,0 % | −25,0 % | 82,7 % | −17,3 % |
| 4 | 70,7 % | −29,3 % | 90,0 % | −10,0 % |
| 6 | 86,6 % | −13,4 % | 95,5 % | −4,5 % |
| 8 | 92,4 % | −7,6 % | 97,5 % | −2,6 % |
| 12 | 96,6 % | −3,4 % | 98,9 % | −1,1 % |
| 18 | 98,5 % | −1,5 % | 99,5 % | −0,5 % |
| 36 | 99,6 % | −0,4 % | 99,9 % | −0,1 % |

- Geschlossene Formeln für den ungünstigsten Fall (Ellipse, kleine Ovalität): N gerade ⇒ Anzeige/echt = cos(180°/N) (N = 4: cos 45° = 0,707; N = 8: cos 22,5° = 0,924); N ungerade ⇒ (1 + cos(180°/N))/2 (N = 3: 0,75).
- Bemerkenswert: Im **ungünstigsten** Fall ist ein Dreiachsgerät (−25 %) besser als ein Vierachsgerät (−29,3 %). Das Dreiachsgerät liegt immer zwischen 75 % und 86,6 %, das Vierachsgerät zwischen 70,7 % und 100 %. Nordsons Aussagen („4 Achsen 100 % bei Ausrichtung, 3 Achsen nie 100 %“) beschreiben den günstigsten Fall.
- Nordsons „42 %“: mittlerer Fehler 3 Achsen 17,3 %, 4 Achsen 10,0 % ⇒ (17,3 − 10,0)/17,3 = 42 %. Die Zahl passt exakt zum **lagegemittelten** Fehler, nicht zum worst case (eigene Rechnung; dass Nordson so rechnet, ist nicht belegt).
- **Rekonstruktion statt max − min:** Eine reine Ellipse hat 3 Unbekannte (D, Δ, φ0). Mit 3 oder mehr nicht redundanten Achsen kann man eine Sinusfunktion cos 2φ anpassen und Δ exakt bestimmen (bei 4 Achsen überbestimmt, Ausgleichsrechnung). Damit verschwindet die Unterschätzung für reine Ovalität; höhere gerade Harmonische (4., 6. …) verfälschen aber die Anpassung (Aliasing), wenn N zu klein ist. Die N Achsen tasten w(φ) mit N Punkten über 180° ab; damit lassen sich gerade Harmonische bis zur Ordnung k nur eindeutig bestimmen, wenn N ≥ k + 1 (Ellipse k = 2 ⇒ N ≥ 3; zusätzlich 4. Harmonische ⇒ N ≥ 5); die Konturform der realen Rohre (nur Ellipse oder auch höhere Formfehler) muss daher bekannt sein.
- **Gleichdick-Problem:** Für jede Durchmesser-(Zweipunkt-)Messung gilt w(φ) = r(φ) + r(φ + 180°); ungerade Harmonische (3-, 5-Bogen-Form) heben sich auf. Eine solche Form zeigt in **jeder** Richtung gleichen Ø, auch bei voller Drehung. Für die Kenngröße „Ø max − Ø min“ ist das konsistent (die Ø-Spanne ist tatsächlich null), für Rundheit (Radiusabweichung) nicht. Das Pflichtenheft fordert Ø max − Ø min – also genügt Zweipunktmessung, solange niemand Rundheit nach ISO 1101 erwartet.
- Folgerung für (c): Bei Toleranz T für Ø max − Ø min müsste ein Gerät mit N Achsen den Grenzwert auf T × (Anzeige/echt, worst case) absenken, z. B. 3 Achsen ⇒ 0,75 T, 8 Achsen ⇒ 0,92 T, oder die Ellipsenanpassung nutzen.

### Gaps
- Keine Primärquelle (Paper/Norm) gefunden, die genau diese Tabelle (N Achsen ohne Drehung, worst case) veröffentlicht; die Werte sind eigene Rechnung und sollten durch Simulation im Projekt nachvollzogen werden.
- Welche Harmonischen die realen gezogenen Rohre (Nitinol, Edelstahl, Tantal) zeigen, ist unbekannt; nötig für die Wahl von N.


## 4. Verletzt ein Helixscan „jeder Querschnitt in Toleranz“? Wie wird punktweise ausgewertet?

### Takeaway
Ein Helixscan misst keinen echten ebenen Querschnitt, sondern setzt einen „Querschnitt“ aus Messwerten zusammen, die über ein Axialfenster verteilt sind (Fenster = Vorschub je 180°/M Drehung). Das ist zulässig, wenn das Fenster ≤ 2 mm ist und sich die Form innerhalb dieses Fensters nicht nennenswert ändert; die Industrie (Patente) arbeitet so, eine Norm dazu wurde nicht gefunden.

### Cited Findings
- Patent: Helixabtastung durch Drehen der Messeinrichtung um die Messachse, während das Rohr nur axial vorgeschoben wird — [USRE30088 (USPTO)](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/RE30088) (Suchergebnis, nicht eingesehen; Zuordnung des Zitats zu diesem Patent laut Suchzusammenfassung, nicht geprüft).
- Patent (aus derselben Trefferliste, Nummer nicht eindeutig zugeordnet): Rohr läuft vor und dreht, die Ø-Messpunkte bilden Helices; zwei senkrechte Ø-Messungen in einer Ebene ergeben vier Umfangspunkte, der Umfang wird durch vier Helices abgedeckt — [Trefferliste u. a. US6956661](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6956661) (Suchergebnis, nicht eingesehen, Zuordnung unsicher).
- Rotierender Kopf beschreibt eine Spiralbahn um das durchlaufende Rohr und ermittelt Ovalität und deren Verlauf — [US6862099](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6862099) (Suchergebnis, nicht eingesehen).
- Ein Verfahren nach US12366310 nutzt einen kommerziellen Laserscanner, der mittleren Außen-Ø und Unrundheit mit axialer und Umfangs-Position ausgibt, nachdem das Rohr durch den Scanner indexiert wurde — [US12366310](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12366310) (Suchergebnis, nicht eingesehen).
- Patent zu rotierendem Messkopf mit Prozessoren und Funksender auf dem Kopf (Datenübertragung) — [US6931748](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6931748) (Suchergebnis, nicht eingesehen).

### Inferences (eigene Rechnung / Bewertung)
- Fensterlänge: Δz_F = v / (2·M·n) (Vorschub während 180°/M). Bedingung für die Forderung „alle 2 mm“: Δz_F ≤ 2 mm. Bei (f) gilt analog: jeder Querschnitt wird in allen Winkeln an **derselben** axialen Stelle gemessen (Kamera sieht den ganzen Abschnitt), d. h. kein Fensterfehler – nur die Zeitpunkte unterscheiden sich. Das ist ein Vorteil von (f) gegenüber (b)/(d).
- Fehler durch das Fenster: Ändert sich der Ø entlang z mit Steigung dD/dz (Konizität), erzeugt das Fenster eine Scheinovalität ≈ |dD/dz|·Δz_F. Beispiel: 1 µm Ø-Änderung je 10 mm und Δz_F = 2 mm ⇒ ≈ 0,2 µm Scheinovalität – vernachlässigbar. Lokale Fehler kürzer als das Fenster (Dellen, Knicke) werden nur in einem Teil der Winkel gesehen.
- Anforderung r10 „Auswertung je Messpunkt, Mittelwerte unzulässig“: Ein Fenster, das Werte aus verschiedenen Winkeln zu einem Querschnitt zusammensetzt, ist keine Mittelung (max − min bleibt erhalten). Mehrfachmessungen gleicher Richtung zu mitteln (z. B. 70–100 Scans je 2 mm bei Strategie c) oder eine Ellipsenanpassung wären aber mit dem Betrieb abzustimmen, ob das unter „Mittelwerte unzulässig“ fällt.
- Auswertung „punktweise“: Praktikabel ist ein gleitendes Fenster: für jede Position z_i (alle 2 mm) alle Messwerte aus [z_i − Δz_F/2, z_i + Δz_F/2] nehmen, nach Winkel sortieren, Ø max − Ø min bilden (oder Ellipse anpassen). So entsteht je 2 mm ein Wert; die Fenster überlappen oder stoßen aneinander, Lücken entstehen nicht, solange Δz_F ≥ Abstand der Auswertepositionen.
- Ob „jeder Querschnitt“ im Pflichtenheft eine ebene Schnittfläche oder ein Abschnitt von 2 mm meint, muss mit dem Betrieb geklärt werden; bei „Abschnitt von 2 mm“ ist der Helixscan mit Δz_F ≤ 2 mm normgerecht im Sinne der Forderung.
- Schlag/Mittelpunktwanderung: Für Schattenwurf-Mikrometer unkritisch (Ø ist lageunabhängig im Messfeld); für Triangulationssensoren (Radius) muss der Mittelpunkt aus gegenüberliegenden Sensoren bestimmt werden, sonst wird Schlag als Formfehler gemessen.

### Gaps
- Keine Norm oder Herstellernotiz gefunden, die festlegt, wie Helixdaten zu „Querschnitten“ zusammengefasst werden; die Methode des gleitenden Fensters ist eigene Herleitung.
- Patentinhalte konnten nicht eingesehen werden (patents.google.com gesperrt, USPTO-PDFs nur als Suchtreffer).
