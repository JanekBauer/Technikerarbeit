# Physikalische und mechanische Grenzen beim Drehen und Verfahren dünner Rohre (Ø 1–6,5 mm, bis 3 m)

Stand der Recherche: 22.11.2026. Mehrere Hosts waren im Netz gesperrt (dovermotion.com, sikora.net, web.mit.edu, rbb.union.edu). Inhalte von dort stammen nur aus Suchergebnis-Auszügen und sind als „Suchergebnis, nicht eingesehen“ markiert. Alle Zahlenbeispiele für Rohre sind **eigene Rechnung** (Python-Skript, Formeln jeweils angegeben); keine Messwerte.

Verwendete Werkstoffdaten:

| Werkstoff | E-Modul | Dichte | Quelle |
|---|---|---|---|
| Nitinol superelastisch | 41–75 GPa (temperatur- und dehnungsabhängig); andere Angaben: Austenit ca. 75–83 GPa, Martensit 28–40 GPa | 6,45–6,5 g/cm³ | [Confluent Medical Datenblatt](https://confluentmedical.com/wp-content/uploads/2026/06/Material-Data-Sheet-Superelastic-2026-V6.pdf), [Johnson Matthey](https://matthey.com/products-and-services/medical-components/resource-library/nitinol-technical-properties), [JAS Tech Sheet](https://www.jacques-allemann.com/media/cms/Legierungen%20/%20Tech-Sheets/JAS%20-%20Tech%20Sheet%20/%20Werkstoffe/jas-036-tech-sheet-nitinol.pdf) (alle: Suchergebnis, nicht eingesehen) |
| 316L | 193 GPa (Bandbreite 190–215 GPa je Quelle) | 7,99 g/cm³ | [Alloys International 316L](https://alloysintl.com/inventory/stainless-steel/stainless_steel316/), [Rolled Alloys Datenblatt](https://www.rolledalloys.com/wp-content/uploads/316_316L_Stainless_DataSheet_RolledAlloys.pdf), [Total Materia](https://www.totalmateria.com/en-us/material/1250289) (Suchergebnis, nicht eingesehen) |
| Tantal | 186 GPa | 16,6–16,69 g/cm³ | [Princeton MAE Glossar Tantal](https://www.princeton.edu/~maelabs/mae324/glos324/tantalum.htm), [Goodfellow Tantal](https://www.goodfellow.com/material/metals/tantalum) (Suchergebnis, nicht eingesehen) |

Für die Rechnung: NiTi E = 40 und 75 GPa, ρ = 6450 kg/m³; 316L E = 193 GPa, ρ = 7990 kg/m³; Ta E = 186 GPa, ρ = 16650 kg/m³.

Wichtig: Der Nitinol-E-Modul ist im superelastischen Bereich nicht konstant (Austenit/Martensit, Mischungsregel nach [Abaqus-Doku Superelastizität](https://docs.software.vt.edu/abaqusv2024/English/SIMACAEMATRefMap/simamat-c-superelasticity.htm), Suchergebnis, nicht eingesehen). Bei den kleinen Biegedehnungen durch Eigengewicht bleibt das Rohr im Austenit-Ast; dort ist der obere Wert realistischer, der untere Wert ist der ungünstige Fall.

## 1. Kritische Drehzahl (Biegekritische / Whirling) eines gelagerten dünnwandigen Rohrs

### Takeaway
Die erste biegekritische Drehzahl hängt fast nur vom Stützabstand L (mit 1/L²), vom Durchmesser und von E/ρ ab, kaum von der Wandstärke. Bei 300 mm Stützabstand liegt sie für ein Ø-1-mm-Rohr nur bei etwa 700–1650 1/min, bei 1000 mm Stützabstand bei 66–150 1/min (eigene Rechnung). Ein Ø-1-mm-Rohr frei zwischen den Enden über 3 m zu drehen ist praktisch unmöglich (kritisch < 20 1/min, Durchhang meterweise). Drehen geht nur mit engen Stützen (≤ 100–150 mm) oder mit Drehung im Bereich weniger Umdrehungen pro Sekunde und kurzem freiem Abschnitt.

### Cited Findings
- Biegeeigenfrequenz eines beidseitig gelenkig gelagerten, gleichförmigen Balkens: ω₁ = (π/L)²·√(EI/(ρA)); die biegekritische Drehzahl entspricht der Biegeeigenfrequenz (Resonanz, wenn Drehfrequenz = Eigenfrequenz) — [Transverse vibration of beams, Cooper Union](https://engfac.cooper.edu/pages/tzavelis/uploads/Transverse%20vibration%20of%20beams.pdf); [Scribd: Transverse vibration of a thin uniform beam](https://www.scribd.com/doc/292460898/A) (Suchergebnis, nicht eingesehen)
- Rayleigh-Näherung für Wellen mit Einzelmassen: ω = √(g·Σmᵢyᵢ / Σmᵢyᵢ²) — [Union College MER419 Critical Frequency](https://rbb.union.edu/courses/mer419/content/data/Lectures/MER419%20L06%20Critical%20Frequency.pdf) (Host gesperrt; Suchergebnis, nicht eingesehen)
- Lagerungsfaktoren aus der Kugelgewindetrieb-Praxis (gleiche Physik, schlanke Welle): fest-frei 0,25; gelenkig-gelenkig 1,00; fest-gelenkig 2,00; fest-fest 4,00 (relativ zur Drehzahl gelenkig-gelenkig, nach vereinfachten Herstellerformeln) — [AutomationDirect Ball Screw Calculations](https://cdn.automationdirect.com/static/manuals/rbs/ballscrewcalculations.pdf); [Machine Design: Importance of ballscrew end fixity](https://www.machinedesign.com/linear-motion/importance-ballscrew-end-fixity) (Suchergebnis, nicht eingesehen)
- Steinmeyer gibt Lagerfaktoren k = 25,5 (fest–fest), 11,5 (gestützt–gestützt), 3,9 (fest–frei) an und empfiehlt Betrieb nur bis ca. 80 % der kritischen Drehzahl — [Steinmeyer Critical Speed](https://steinmeyer.com/en/technology/speed-limits/critical-speed) (Suchergebnis, nicht eingesehen)
- Hinweis: Die exakte Eigenwertlösung für beidseitig eingespannt ergibt (4,730/π)² ≈ 2,27-fache Frequenz gegenüber gelenkig (Standard-Eigenwert βL = 4,730 für eingespannt-eingespannt). Die „4,00“ der Kugelgewinde-Kataloge ist eine Vereinfachung — Eigenwert aus Lehrbuchwissen (z. B. Blevins, Formulas for Natural Frequency and Mode Shape); nicht online eingesehen.

### Inferences (eigene Rechnung)
Formel: f₁ = (π / (2L²))·√(E·I/(ρ·A)), mit I = π(D⁴−d⁴)/64, A = π(D²−d²)/4, also I/A = (D²+d²)/16. n_k = 60·f₁. Gelenkige Lagerung je Feld (ungünstiger Fall; Einspannung erhöht um Faktor ≈ 2,27).

Für einen Durchlaufträger mit vielen gleich weiten Feldern und gelenkigen Stützen existiert eine Eigenform mit Knoten an jeder Stütze; deren Frequenz ist gleich der des Einzelfelds. Der Stützabstand L ist daher die maßgebliche Größe, nicht die Rohrlänge (eigene Herleitung; Lehrbuchergebnis, nicht online belegt).

Erste biegekritische Drehzahl n_k in 1/min (eigene Rechnung, gelenkig, Werte gerundet):

| Rohr | Werkstoff | L = 100 mm | L = 300 mm | L = 1000 mm | L = 3000 mm |
|---|---|---|---|---|---|
| Ø 1 × 0,1 mm | NiTi E=40 | 7 500 | 835 | 75 | 8 |
| Ø 1 × 0,1 mm | NiTi E=75 | 10 300 | 1 140 | 103 | 11 |
| Ø 1 × 0,1 mm | 316L | 14 800 | 1 650 | 148 | 16 |
| Ø 1 × 0,1 mm | Ta | 10 100 | 1 120 | 101 | 11 |
| Ø 1 × 0,25 mm | 316L | 12 900 | 1 440 | 129 | 14 |
| Ø 6,5 × 0,5 mm | NiTi E=40 | 50 000 | 5 550 | 500 | 56 |
| Ø 6,5 × 0,5 mm | NiTi E=75 | 68 400 | 7 600 | 684 | 76 |
| Ø 6,5 × 0,5 mm | 316L | 98 600 | 11 000 | 986 | 110 |
| Ø 6,5 × 0,5 mm | Ta | 67 000 | 7 450 | 671 | 75 |
| Ø 6,5 × 0,1 mm | 316L | 105 000 | 11 650 | 1 048 | 116 |

Entsprechende Eigenfrequenzen f₁ (Beispiele): Ø 1 × 0,1 mm, 316L: 247 Hz (100 mm), 27,5 Hz (300 mm), 2,5 Hz (1000 mm), 0,3 Hz (3000 mm). Ø 6,5 × 0,5 mm, 316L: 1 643 Hz, 183 Hz, 16,4 Hz, 1,8 Hz.

Weitere Schlussfolgerungen:
- Wandstärke spielt kaum eine Rolle (I/A ≈ D²/8 bei dünner Wand). Tantal ist trotz hohem E wegen seiner Dichte etwa so „weich“ wie Nitinol mit E = 75 GPa (E/ρ fast gleich).
- Mit 80-%-Regel (Steinmeyer) wäre die zulässige Drehzahl für Ø 1 mm bei 100 mm Stützabstand etwa 6 000–12 000 1/min, bei 300 mm nur etwa 670–1 300 1/min.
- Unwuchtverstärkung (Einmassenschwinger, Lehrbuchformel r/e = (Ω/ω)²/(1−(Ω/ω)²)): bei Ω/ω = 0,2 → 4 % der Exzentrizität, 0,5 → 33 %, 0,7 → 96 %, 0,8 → 178 % (eigene Rechnung). Für Messung sinnvoll: Drehfrequenz unter ca. 20–30 % der ersten Eigenfrequenz, sonst bildet die Messung die dynamische Durchbiegung mit ab.
- Bei Drehung auf Rollen oder in V-Stützen ist das Rohr praktisch an jeder Stütze geführt; die Grenze setzt dort eher Reibung, Rollenrundlauf und Geradheit (siehe Abschnitt 5) als die biegekritische Drehzahl.

### Gaps
- Kein frei zugänglicher Lehrbuchauszug (Dubbel, Roloff/Matek) eingesehen; Formeln sind Standard, aber nur über Suchergebnisse belegt.
- Keine veröffentlichten Messungen der kritischen Drehzahl speziell an Nitinol-Kanülen oder Hypotubes gefunden.
- Gyroskopische Effekte und Lagersteifigkeit von Rollen/V-Prismen nicht berücksichtigt (bei so schlanken Rohren vernachlässigbar bzw. unbekannt).

## 2. Durchhang unter Eigengewicht und nötiger Stützabstand

### Takeaway
Für Durchhang < 0,1 mm darf der Stützabstand bei Ø 1 mm nur etwa 140–210 mm betragen (gelenkig) bzw. 210–310 mm (eingespannt); bei Ø 6,5 mm etwa 390–560 mm (gelenkig) bzw. 580–830 mm (eingespannt) (eigene Rechnung). Ein 3-m-Rohr mit Ø 1 mm braucht also mindestens 15–20 Stützstellen, wenn es auf 0,1 mm gerade liegen soll.

### Cited Findings
- Maximaler Durchhang Zweifeldträger, gleichmäßige Last: δ_max ≈ wL⁴/(185EI) — [Firgelli Continuous Beam Calculator](https://www.firgelliauto.com/blogs/engineering-calculators/continuous-beam-calculator-two-equal-spans) (Suchergebnis, nicht eingesehen; Seite laut Suchauszug in ihrem Rechenbeispiel inkonsistent); gleicher Wert in [Eng-Tips Forum](https://eng-tips.com/threads/deflection-equation-for-continuous-beam-with-unequal-spans.449843) (Suchergebnis, nicht eingesehen)
- Standardformeln Einfeldträger: gelenkig δ = 5qL⁴/(384EI), beidseitig eingespannt δ = qL⁴/(384EI) — Standard-Balkentabellen, z. B. [MIT 3.11 Beam Displacements](https://web.mit.edu/course/3/3.11/www/modules/bdisp.pdf), [Engineering Toolbox Beams](https://www.engineeringtoolbox.com/beam-stress-deflection-d_1312.html) (Host gesperrt bzw. Suchergebnis, nicht eingesehen)

### Inferences (eigene Rechnung)
Formel: q = ρ·g·A; δ_gelenkig = 5qL⁴/(384EI) = 5·ρ·g·L⁴·16 / (384·E·(D²+d²)). Eingespannt: 1/5 davon. Erforderlicher Abstand: L = (δ_zul·384·E·I/(5q))^¼.

Durchhang δ (gelenkig) in mm:

| Rohr / Werkstoff | L = 100 mm | L = 300 mm | L = 1000 mm | L = 3000 mm |
|---|---|---|---|---|
| Ø 1 × 0,1 NiTi E=40 | 0,020 | 1,63 | 201 | (16 m, sinnlos) |
| Ø 1 × 0,1 NiTi E=75 | 0,011 | 0,87 | 107 | — |
| Ø 1 × 0,1 316L | 0,005 | 0,42 | 52 | — |
| Ø 1 × 0,1 Ta | 0,011 | 0,90 | 112 | — |
| Ø 6,5 × 0,5 NiTi E=40 | 0,0005 | 0,037 | 4,5 | 368 |
| Ø 6,5 × 0,5 316L | 0,0001 | 0,009 | 1,17 | 95 |
| Ø 6,5 × 0,5 Ta | 0,0003 | 0,020 | 2,5 | 204 |

(Hinweis: Bei Durchhang im Bereich der Rohrlänge gilt die lineare Balkentheorie nicht mehr; die Werte zeigen nur, dass das Rohr nicht selbsttragend ist.)

Maximal zulässiger Stützabstand in mm für Durchhang 0,01 / 0,1 / 1 mm:

| Rohr / Werkstoff | gelenkig | eingespannt |
|---|---|---|
| Ø 1 × 0,1 NiTi E=40 | 84 / 149 / 266 | 126 / 223 / 397 |
| Ø 1 × 0,1 NiTi E=75 | 98 / 175 / 311 | 147 / 261 / 465 |
| Ø 1 × 0,1 316L | 118 / 210 / 373 | 176 / 314 / 558 |
| Ø 1 × 0,1 Ta | 97 / 173 / 308 | 146 / 259 / 460 |
| Ø 1 × 0,25 316L | 110 / 196 / 349 | 165 / 293 / 521 |
| Ø 6,5 × 0,5 NiTi E=40 | 217 / 385 / 685 | 324 / 576 / 1024 |
| Ø 6,5 × 0,5 NiTi E=75 | 253 / 451 / 801 | 379 / 674 / 1198 |
| Ø 6,5 × 0,5 316L | 304 / 541 / 962 | 455 / 809 / 1439 |
| Ø 6,5 × 0,5 Ta | 251 / 446 / 793 | 375 / 667 / 1186 |

- Zusammenhang Durchhang ↔ Eigenfrequenz (gelenkig, eigene Rechnung aus beiden Formeln): f₁ ≈ 0,56/√δ (δ in m), z. B. δ = 0,1 mm → f₁ ≈ 56 Hz. Wer den Durchhang klein hält, bekommt automatisch eine hohe Eigenfrequenz und kurze Ausschwingzeit.
- Zweifeld- und Durchlaufträger liegen zwischen gelenkig und eingespannt (1/185 statt 5/384 ≈ 1/77), d. h. etwa 2,4-mal weniger Durchhang als das gelenkige Einzelfeld.
- Der Durchhang selbst stört eine Durchmessermessung quer zur Achse kaum, solange das Rohr innerhalb des Messfelds und der Schärfentiefe bleibt; er verschiebt aber die Lage und kippt das Rohr leicht (Schräglage → scheinbar größerer Durchmesser um Faktor 1/cos α, bei kleinen Winkeln vernachlässigbar).

### Gaps
- Kein frei eingesehener Beleg für die Koeffizienten von Durchlaufträgern mit mehr als zwei Feldern.
- Einfluss der Vorkrümmung (Geradheit) ist meist größer als der Durchhang zwischen engen Stützen; siehe Abschnitt 5.

## 3. Ausschwingzeit nach Stop-and-Go und wie kontinuierliche Bewegung sie vermeidet

### Takeaway
Servo-Linearachsen brauchen nach einem Punkt-zu-Punkt-Hub typischerweise einige bis einige zehn Millisekunden zum Einschwingen, je nach Toleranzfenster. Das Rohr selbst schwingt bei geringer Dämpfung und großem Stützabstand deutlich länger (Sekunden), weil seine Eigenfrequenz niedrig ist. Kontinuierliche Bewegung ohne Halt (Messung „on the fly“) vermeidet diese Zeiten fast ganz; dann zählt nur die einmalige Beschleunigung am Anfang.

### Cited Findings
- Einschwingzeit ist nur mit Toleranzfenster sinnvoll; je enger das Fenster, desto länger. Servotische brauchen oft „several tens of milliseconds“ — [Dover Motion: Move and Settle Time](https://dovermotion.com/resources/motion-control-handbook/move-and-settle-time) (Host gesperrt; Suchergebnis, nicht eingesehen)
- Beispielanforderung: 1 mm Hub, Einschwingen auf ±3 µm in < 40 ms; Einschwingen kann 1,5- bis 2-mal so lang dauern wie die eigentliche Bewegung; Unterbau, Verankerung und Material beeinflussen das Einschwingen — [Machine Design: Settling stage](https://www.machinedesign.com/mechanical-drives/settling-stage) (Suchergebnis, nicht eingesehen)
- Messfall: 100 µm XY-Hub mit ALIO-Linearservos, Einschwingen < 1 ms auf ±150 nm; höhere Reglertakte (bis 16 kHz) brachten keinen merklichen Gewinn — [Galil Application Note](https://www.galil.com/node/10871) (Suchergebnis, nicht eingesehen)
- Hochpräzision: 0,1 µm Schritt, Einschwingen auf ±7 nm in 3 ms — [Novanta technical papers](https://novanta.com/precision-medicine/?p=1944) (Suchergebnis, nicht eingesehen)
- Einschwingen ist der Teil der Bewegungszeit, den die Firmware nicht direkt vorgibt; Reglerabstimmung beeinflusst ihn — [ASI Imaging: Stage accuracy and settling time](https://asiimaging.com/docs/stage_accuracy_settling_time_for_asi_stage) (Suchergebnis, nicht eingesehen)
- Höhere Dämpfung → schnelleres Abklingen freier Schwingungen; Dämpfung hängt bei Edelstahl-Rohren von der Dehnungsamplitude ab (NASA-Daten zu AISI-321-Rohrleitungen) — [NASA NTRS 19690022112](https://ntrs.nasa.gov/api/citations/19690022112/downloads/19690022112.pdf), [Manchester Structural Concepts](https://www.sites.se.manchester.ac.uk/structural-concepts/?p=576) (Suchergebnis, nicht eingesehen)

### Inferences (eigene Rechnung)
Abklingzeit des Rohrs auf 2 % der Anfangsamplitude: t ≈ 4/(ζ·ω₁), ω₁ = 2π·f₁ (Standardnäherung, ln 50 ≈ 3,9). Dämpfungsgrade ζ sind **Annahmen**, kein Messwert: 0,1 % (freies Metallrohr, Materialdämpfung), 0,5 %, 2 % und 5 % (Reibung in V-Stützen/Rollen, Kunststoffauflagen).

| f₁ des Rohrs | ζ = 0,1 % | ζ = 0,5 % | ζ = 2 % | ζ = 5 % |
|---|---|---|---|---|
| 5 Hz | 127 s | 25 s | 6,4 s | 2,5 s |
| 20 Hz | 32 s | 6,4 s | 1,6 s | 0,64 s |
| 50 Hz | 12,7 s | 2,5 s | 0,64 s | 0,25 s |
| 200 Hz | 3,2 s | 0,64 s | 0,16 s | 0,06 s |

- Zuordnung: Ø 1 mm bei 300 mm Stützabstand → f₁ ≈ 14–28 Hz; bei 100 mm → 125–250 Hz (Abschnitt 1). Mit wenig Dämpfung kann ein angestoßenes Rohr bei 300 mm Stützabstand also Sekunden nachschwingen. Bei 100 mm Stützabstand und etwas Reibung an den Auflagen sind es Zehntelsekunden.
- Ob das Nachschwingen stört, hängt von der Amplitude ab: Eine axiale Beschleunigung regt die Querbiegung nur indirekt an (Reibung/Stick-Slip an Auflagen, Mitnahme an einem Ende). Bei kleiner Anregung und einem Messfeld mit ausreichender Tiefe wird die Durchmessermessung durch kleine Querschwingungen kaum verfälscht. Sikora wirbt mit sehr kurzer Belichtungszeit (0,2 µs) gerade, um Messwerte trotz Probenvibration zu erhalten — [Sikora: Precise diameter values despite vibrations](https://sikora.net/en/?p=61165), [Sikora LASER Series 6000](https://sikora.net/produkt/laser6000/) (Host gesperrt; Suchergebnis, nicht eingesehen).
- Grobe Taktrechnung (eigene Rechnung, Annahme 30 ms Einschwingen der Achse je Halt, Werte aus Dover/Machine Design): 30 Messpositionen im Stop-and-Go → ca. 0,9 s nur Einschwingen der Achse; plus Rohr-Nachschwingen, wenn das Rohr frei hängt. Bei kontinuierlicher Fahrt entfällt beides bis auf Anfahren/Abbremsen.
- Kontinuierliche Bewegung: Positionsbezogenes Auslösen der Messung (Encoder-Trigger) statt Halt; die Messrate begrenzt dann den Punktabstand (Abschnitt 4).

### Gaps
- Keine zugänglichen Hersteller-Daten für Einschwingzeit speziell bei 2 mm bzw. 20–50 mm Hub; nur die oben genannten Beispiele (1 mm/40 ms, 100 µm/<1 ms).
- Kein Messwert für die Dämpfung dünner NiTi-/316L-/Ta-Rohre in V-Auflagen gefunden. Nitinol hat im superelastischen Bereich Hysterese (höhere Dämpfung), aber bei kleinen elastischen Amplituden ist das nicht belegt.

## 4. Axiale Vorschubgeschwindigkeiten bei Inline-Durchmessermessung (Draht, Schlauch, Rohr)

### Takeaway
Inline-Lasermikrometer messen mit 500 bis 5 000 Messungen je Sekunde und Achse; das reicht für Liniengeschwindigkeiten von Metern pro Sekunde. Feindraht wird bis zu 25–50 m/s gezogen. Für ein 3-m-Rohr ist die axiale Geschwindigkeit messtechnisch kaum die Grenze; die Grenze setzen Führung, Beschleunigung und gewünschter Punktabstand.

### Cited Findings
- Sikora LASER Series 6000: 2 500 Messungen/s je Achse (optional 5 000 bei LASER 6020 XY), Durchmesserbereich 0,2–18 mm, Belichtungszeit 0,2 µs — [Sikora LASER 6000](https://sikora.net/produkt/laser6000/) (Suchergebnis, nicht eingesehen)
- Sikora LASER PRO: bis 5 000 Messungen/s je Achse — [Sikora Flyer LASER PRO](https://sikora.net/wp-content/uploads/Flyer_LASER_PRO_wc.pdf) (Suchergebnis, nicht eingesehen)
- Ältere Sikora LASER Series 2000: 500 Messungen/s/Achse, 1 000 bzw. 1 200 bei Sondermodellen — [Sikora LASER Series 2000](https://sikora.net/wp-content/uploads/LASER_Series_2000_wc.pdf) (Suchergebnis, nicht eingesehen)
- Zumbach ODAC 18XY: Scanrate Standard 2 × 1 200/s, Version F 2 × 2 500/s; ODAC 14XY speziell für Fein- und Feinstdraht — [Zumbach ODAC 18XY](https://pdf.directindustry.com/pdf/zumbach-electronic-ag/odac-18xy/15879-1024587.html), [Zumbach ODAC 14XY](https://pdf.directindustry.com/pdf/zumbach-electronic-ag/odac-14xy/15879-1024584.html) (Suchergebnis, nicht eingesehen)
- Marktübliche Scanraten 100 bis ca. 2 800 Scans/s je Achse; LaserLinc wirbt mit 4 000 Hz je Achse. Scanrate ≠ Messrate: Ein Gerät mit 1 000 Scans/s liefert ggf. nur 10 Messwerte/s, weil je 100 Scans gemittelt werden — [MD+DI: Advances in OD/ID Systems](https://mddionline.com/ivd/advances-in-od-id-systems-benefit-medical-tubing-extrusion), [LaserLinc dual axis](https://test.laserlinc.com/dual-axis_laser_micrometers.html) (Suchergebnis, nicht eingesehen)
- LaserLinc-Beispiel: bei 20 in/s (≈ 30 m/min) und 1 200 Hz ein Messwert alle 0,017 in (≈ 0,43 mm) — [Medical Design and Outsourcing / LaserLinc](https://www.medicaldesignandoutsourcing.com/laserlinc-real-time-ultrasonic-measurement-tubing-precision/) (Suchergebnis, nicht eingesehen)
- Je kleiner der Außendurchmesser, desto schneller überstreicht der Strahl das Produkt, sodass die Produktbewegung die Messung nicht beeinflusst — [MD+DI: Profiling – the missing link](https://www.mddionline.com/new-technologies/profiling-the-missing-link-in-measurement-technology) (Suchergebnis, nicht eingesehen)
- Marposs EXTRULINE: Durchmesser und Ovalität 0,1–149 mm, ein- oder zweiachsig — [DirectIndustry Marposs EXTRULINE](https://www.directindustry.com/prod/marposs/product-7365-2744595.html) (Suchergebnis, nicht eingesehen)
- Feindrahtziehen bis ca. 50 m/s; moderne Mehrfachziehmaschinen > 25 m/s; Studie mit Kupfer-Feindraht 1–21 m/s; ein Patent nennt historisch ca. 75 m/min als Grenze für 0,09 mm — [Wikipedia Wire drawing](https://www.wikipedia.org/wiki/Wire_drawing), [Springer s00170-021-08172-2](https://link.springer.com/content/pdf/10.1007/s00170-021-08172-2.pdf), [US-Patent 5282377](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5282377) (Suchergebnis, nicht eingesehen)

### Inferences (eigene Rechnung)
Punktabstand Δx = v / Messrate:

| v | v in mm/s | 100 /s | 1 000 /s | 2 500 /s | 5 000 /s |
|---|---|---|---|---|---|
| 1 m/min | 16,7 | 0,17 mm | 0,017 mm | 0,007 mm | 0,003 mm |
| 5 m/min | 83 | 0,83 mm | 0,083 mm | 0,033 mm | 0,017 mm |
| 10 m/min | 167 | 1,7 mm | 0,17 mm | 0,067 mm | 0,033 mm |
| 60 m/min | 1 000 | 10 mm | 1,0 mm | 0,4 mm | 0,2 mm |
| 100 m/min | 1 667 | 17 mm | 1,7 mm | 0,67 mm | 0,33 mm |

- 3 m Rohr bei 10 m/min → 18 s Durchlaufzeit; bei 30 m/min → 6 s (eigene Rechnung). Messtechnisch wären bei 2 500 Messungen/s auch dann noch Punktabstände < 0,2 mm möglich.
- Wenn gemittelt werden muss (MD+DI: z. B. 100 Scans pro Messwert für die Wiederholgenauigkeit), sinkt die effektive Messrate stark; dann ist der Punktabstand das Kriterium für die zulässige Geschwindigkeit.

### Gaps
- Keine belastbare m/min-Angabe für Extrusionslinien von Medizinschläuchen oder für Metall-Hypotubes gefunden (Sikora/Zumbach-Datenblätter gesperrt).
- Keine Angabe, mit welcher Geschwindigkeit Hersteller von Nitinol-/316L-Kanülen ihre Rohre offline axial durch Messköpfe fahren.

## 5. Einfluss der Drehung auf die Messung: Rundlauf, Geradheit, Exzentrizität, Fliehkraft, Verschleiß

### Takeaway
Bei so schlanken Rohren dominiert die Geradheit: Herstellertoleranzen von z. B. 0,030 in/ft (≈ 2,5 mm/m) sind viel größer als jeder Durchhang zwischen engen Stützen. Beim Drehen erzeugt eine Krümmung Rundlauf (Schlag), der das Rohr aus dem Messfeld wandern lässt; die Durchmessermessung im Schattenverfahren bleibt aber unabhängig von der Lage, solange das Rohr im Messfeld bleibt. Fliehkräfte sind vernachlässigbar.

### Cited Findings
- Geradheit Nitinol-Rohr (Viant): max. 0,030 in/ft — [Viant Nitinol Tubing](https://viantmedical.com/wp-content/uploads/2025/02/Viant-Nitinol-Tubing-CB.pdf) (Suchergebnis, nicht eingesehen); umgerechnet 2,5 mm/m (eigene Rechnung)
- Johnson Matthey veröffentlicht Spezifikationsrichtlinien für Nitinol-Komponenten — [JM Nitinol specification guidelines](https://matthey.com/products-and-services/medical-components/resource-library/nitinol-specification-guidelines) (Suchergebnis, nicht eingesehen; Inhalt zur Geradheit nicht geprüft)
- Drehende Rohrprüfung: NOVACAM TUBEINSPECT dreht das Rohr auf einem Drehtisch und erfasst Durchmesser, Geradheit, Zylindrizität, Konzentrizität, Ovalität, Konizität und Rundlauf — [Novacam Tube ID and OD measurement](https://www.novacam.com/applications/tube-id-and-od-measurement/) (Suchergebnis, nicht eingesehen)
- Nordson BenchMike Pro: Laser auf V-Block-Aufnahme, Probe wird in Winkelschritten gedreht, Grafik zeigt Abweichung über Drehwinkel — [Nordson BenchMike Pro](https://www.nordson.com/en/Products/Measurement-and-Control-Products/BenchMike-Pro) (Suchergebnis, nicht eingesehen)
- Keyence: Außendurchmesser einachsig, mehrachsig oder flächig messen, um Ovalität und Min/Max zu erfassen; Werkstück drehen für Rundheit und Exzentrizität; berührungslos vermeidet Verformungsfehler bei dünnwandigen Teilen — [Keyence inner and outer diameter measurement](https://www.keyence.com/products/measure/applications/dimension-measurement/inner-and-outer-diameter-measurement.jsp?ad_local=cbgt) (Suchergebnis, nicht eingesehen)
- Bei Kugelgewindetrieben mit drehender Mutter kann die kritische Drehzahl überschritten werden, wenn der Rundlauf eng toleriert ist — [Machine Design: Ball screw speed basics](https://www.machinedesign.com/motion-control/ball-screw-speed-basics) (Suchergebnis, nicht eingesehen)

### Inferences (eigene Rechnung / Schlussfolgerung)
- **Geradheit vs. Rundlauf:** Bei 2,5 mm/m und einem gleichmäßigen Bogen hat ein 3-m-Rohr bis zu 7,5 mm Pfeilhöhe (lineare Hochrechnung der Herstellerangabe je Fuß; tatsächliche Form unbekannt). Liegt es auf mehreren Stützen und wird gedreht, muss der Bogen sich bei jeder Umdrehung elastisch „durchwalken“ oder das Rohr schlägt zwischen den Stützen aus. Bei Ø 1 mm reicht schon ein kurzer Bogen, um das Rohr aus einem Messfeld von wenigen mm zu bewegen.
- **Exzentrisches Spannen:** Eine Exzentrizität e am Spannfutter erzeugt Rundlauf 2e am Spannort, der mit dem Abstand zur nächsten Stütze abklingt. Bei Schattenmessung (Lasermikrometer) ändert die Lage den gemessenen Durchmesser nicht, solange das Rohr in Messfeld und Schärfentiefe bleibt; bei Abstands-/Triangulationssensoren geht der Schlag dagegen voll in den Messwert ein.
- **Fliehkraft:** Umfangsspannung im dünnen Ring σ = ρ·ω²·r². Für 316L Ø 6,5 mm bei 3 000 1/min: ca. 8 kPa; bei 10 000 1/min: ca. 93 kPa; Tantal Ø 6,5 mm bei 10 000 1/min: ca. 0,19 MPa (eigene Rechnung). Das ist gegenüber Streckgrenzen von Hunderten MPa vernachlässigbar; Aufweitung durch Fliehkraft spielt messtechnisch keine Rolle. Fliehkraft wirkt sich nur über Unwucht/Vorkrümmung aus (Abschnitt 1, Verstärkungsfaktor).
- **Verschleiß/Kratzer an Auflagen:** Drehung in V-Stützen bedeutet Gleitreibung an zwei Linien je Stütze; bei Medizinrohren mit polierter Oberfläche ist das ein Kratzrisiko. Rollen (Abrollen statt Gleiten) oder Kunststoff-/Keramik-Auflagen verringern es; dafür bringen Rollen eigenen Rundlauf ein. Belastbare Verschleißdaten nicht gefunden.
- **Praktische Folgerung für schnelle Messung (< 1 min):** Drehen eines 3-m-Rohrs als Ganzes ist mechanisch heikel (Geradheit, viele Stützen, Reibung). Günstiger: Rohr steht still, Sensoren drehen sich um das Rohr oder mehrere Achsen messen gleichzeitig (XY-Mikrometer); oder Rohr wird nur axial durchgezogen (kontinuierlich) und nur ein kurzer Abschnitt nahe dem Messkopf ist eng geführt.

### Gaps
- Keine veröffentlichten Werte zur typischen Geradheit von 316L- und Tantal-Präzisionsrohren gefunden (nur Viant für Nitinol).
- Keine Daten zur Oberflächenbeschädigung von Nitinol/316L beim Drehen in V-Auflagen gefunden.
- Keine Norm (ASTM/ISO) für die Rundlaufmessung dünner Medizinrohre eingesehen.
