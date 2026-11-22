# Entwürfe 001 bis 005 (KI-Vorschlag)

Stand 22.11.2026 · KI (Claude Code) · **Vorschlag für die Dokumentation, keine Festlegung.** Die Varianten bestehen nur aus Ideen, die im Morphologischen Kasten stehen (Repo, `cockpit/daten/tools.json`, Eintrag `morph`). Es wurden keine neuen Lösungen erfunden. Der KI-Anteil ist für die Technikerarbeit zu kennzeichnen (KI-Logbuch, Formatvorlage).

## 1. Festanforderungen (Prüfung je Variante)

✓ erfüllt · ? offen bzw. vom Sensor abhängig · ✗ nicht erfüllt. Ein ✗ schließt die Variante aus.

| Festanforderung | 001 | 002 | 003 | 004 | 005 |
|---|---|---|---|---|---|
| 1.1 Werkstoff NiTi / Edelstahl | ✓ | ✓ | ✓ | ✓ | ✓ |
| 1.2 Rohrlänge 1000–3000 mm | ✓ | ✓ | ✓ | ✓ | ✓ |
| 1.3 Außendurchmesser 1–6,5 mm | ✓ | ? | ✓ | ✓ | ✓ |
| 1.4 Wandstärke n. a. | ✓ | ✓ | ✓ | ✓ | ✓ |
| 2.1 Zylinderform erfassbar | ✓ | ✓ | ? | ✓ | ✓ |
| 2.2 Ø ±13 µm erfassbar | ✓ | ✓ | ✓ | ? | ? |
| 2.5 Je Messpunkt, keine Mittelwerte | ? | ? | ? | ? | ? |
| 3.1 Keine plastische Verformung | ✓ | ✓ | ✓ | ✓ | ? |
| 3.2 Keine Beschädigung, sauber | ✓ | ? | ? | ✓ | ✓ |
| 3.3 Durchbiegung und Lage ohne Einfluss | ✓ | ? | ✓ | ? | ? |
| 4.2 Manuell einlegen, automatisch messen | ✓ | ✓ | ✓ | ✓ | ✓ |
| Taktzeit über 5 min je Rohr (Regel Janek) | ✗ | ✗ | ? | ✗ | ? |

Taktzeit: Die Regel aus der Sensorbewertung (über 5 min je Rohr entfällt) ist nach der Modellrechnung für alle 1D-Sensoren erfüllt nicht. Die Sensoren der Varianten 003 und 005 sind nicht im Sensorvergleich geprüft.

## 2. Teilfunktionen je Variante

| Nr | Teilfunktion | 001 | 002 | 003 | 004 | 005 |
|---|---|---|---|---|---|---|
| TF1 | Rohr einlegen | Von oben in offene Auflagen legen | Auf Ladeleiste legen, die das Rohr in die Messlage absenkt | Von oben in offene Auflagen legen | Von oben in offene Auflagen legen | Auf Ladeleiste legen, die das Rohr in die Messlage absenkt |
| TF2 | Durchbiegung begrenzen | Viele feste Stützstellen im berechneten Abstand | Durchgehende Rinne mit Messfenstern oder Längsschlitz | Viele feste Stützstellen im berechneten Abstand | Durchgehende Rinne mit Messfenstern oder Längsschlitz | Viele feste Stützstellen im berechneten Abstand |
| TF3 | Auflager und Ausrichtung | Rollenpaar aus Kunststoff oder Keramik | Luftlager-Prisma, Rohr schwebt auf ölfreier Druckluft [F? 3.2, ruhige Lage bei Ø 1 mm unsicher] | Zentrisch schließende Dreipunkt-Auflage (Lünette) | Wechseleinsätze oder höhenverstellbare Auflage je Ø-Bereich | Rollenpaar aus Kunststoff oder Keramik |
| TF4 | Gegen Bewegung sichern | Federnde Niederhalterrollen aus Kunststoff | Nur Eigengewicht und Endanschlag | Federnde Niederhalterrollen aus Kunststoff | Federnde Niederhalterrollen aus Kunststoff | Vakuum-Prisma (Saugnut hält das Rohr) |
| TF5 | Rohrtyp und Sollwerte | Auswahl am Bedienpanel (Rezept je Rohrtyp) | Barcode/DataMatrix vom Begleitpapier scannen | Kodierte Wechseleinsätze melden den Ø-Bereich | Nenn-Ø aus erster Messung erkennen, Werkstoff manuell wählen | Barcode/DataMatrix vom Begleitpapier scannen |
| TF6 | Rohranfang/-ende erkennen | Fester Endanschlag ist der Nullpunkt | Messsensor erkennt die Rohrkante am Signalsprung | Eigene Gabellichtschranke am Schlitten | Messsensor erkennt die Rohrkante am Signalsprung | Messsensor erkennt die Rohrkante am Signalsprung |
| TF7 | Durchmesser berührungslos erfassen | Schattenmikrometer LED + Zeilenkamera, einachsig (z. B. Keyence LS, Micro-Epsilon optoCONTROL) [F? W10 Streuung, W7 Messbereich] | Laser-Scan-Mikrometer mit rotierendem Spiegel [F? W10] | Mehrachs-Messkopf mit 2 oder 3 Achsen (z. B. Zumbach, Sikora, LaserLinc, Aeroel – ungeprüft) [F? W10] | Zwei gegenüberliegende Abstandssensoren (konfokal oder Triangulation), Ø aus Differenz [F? W10] | Telezentrische Kamera mit Bildauswertung [F? W10] |
| TF8 | Querschnitt in Winkellagen erfassen | Rohr dreht an jedem Messpunkt 360° | Messkopf schwenkt um das stehende Rohr (180° reichen) | Mehrere feste Messachsen, nichts dreht sich [F? 2.1 Ø max/min zwischen den Achsen] | Rohr dreht an jedem Messpunkt 360° | Rohr dreht an jedem Messpunkt 360° |
| TF9 | Messposition entlang der Länge | Sensor fährt Rohrlänge ab, Rohr gehalten | Sensor fährt Rohrlänge ab, Rohr gehalten | Sensor ist stationär und das Rohr wird durch den Messbereich geführt | Sensor fährt Rohrlänge ab, Rohr gehalten | Sensor fährt Rohrlänge ab, Rohr gehalten |
| TF10 | Position erfassen und zuordnen | Geber im Antriebsmotor (Servo oder Schrittmotor) | Direktes Längenmesssystem am Schlitten (Magnetband oder Glasmaßstab) | Messung positionsgesteuert alle 2 mm auslösen | Direktes Längenmesssystem am Schlitten (Magnetband oder Glasmaßstab) | Messung positionsgesteuert alle 2 mm auslösen |
| TF11 | Messwerte auswerten | Sensor-Controller mit Grenzwerten und Signalleuchte | Industrie-PC mit Messprotokoll je Rohr | SPS mit Bedienpanel | Industrie-PC mit Messprotokoll je Rohr | Industrie-PC mit Messprotokoll je Rohr |
| TF12 | Rohr entnehmen und zuordnen | Manuell in zwei gekennzeichnete Ablagen (i.O./n.i.O.) | Pneumatischer Auswerfer kippt in i.O.- oder n.i.O.-Rinne | Entnahme erst nach Quittierung, bei n.i.O. gibt nur die Sperrablage frei | n.i.O.-Rohr bekommt Anhänger/Etikett an der Schutzhülle | Pneumatischer Auswerfer kippt in i.O.- oder n.i.O.-Rinne |
| TF13 | Messsystem prüfen und einstellen | Kalibrierter Prüfstift fest am Anfang des Fahrwegs, wird bei jedem Rohr mitgemessen | Stufendorn mit mehreren Ø zwischen 1,0 und 6,5 mm | Kalibrierter Prüfstift fest am Anfang des Fahrwegs, wird bei jedem Rohr mitgemessen | Referenzrohr als Meisterteil | Einstellmeister wird täglich manuell eingelegt |
| TF14 | Querschnitt: sauber und ölfrei | Kontaktflächen nur Kunststoff (z. B. PEEK, POM, PE-UHMW) oder Keramik | Antriebe und Führungen unterhalb des Rohrs oder gekapselt | Kontaktflächen nur Kunststoff (z. B. PEEK, POM, PE-UHMW) oder Keramik | Glatte, abwischbare Wechselauflagen | Druckluft über Öl- und Partikelfilter |
| TF15 | Querschnitt: Störeinflüsse | Steifes Maschinenbett (Aluprofil, Stahl-Schweißkonstruktion oder Hartgestein) | Haube gegen Staub, Zugluft und Fremdlicht | Schwingungsdämpfende Maschinenfüße | Steifes Maschinenbett (Aluprofil, Stahl-Schweißkonstruktion oder Hartgestein) | Haube gegen Staub, Zugluft und Fremdlicht |
| TF16 | Querschnitt: Bediener schützen | Lichtgitter vor dem Einlegebereich | Haube mit Sicherheitsschalter | Lichtgitter vor dem Einlegebereich | Langsame, kraftbegrenzte Achsen | Haube mit Sicherheitsschalter |

## 3. Beschreibung der Varianten

### Entwurf 001

**Kern:** Kunststoff-Rollen als Auflage, Niederhalterrollen, 1D-Schattenmikrometer, Rohr dreht bei jedem Messpunkt 360°, Sensor fährt die Länge ab

**K.-o.-Status:** Taktzeit ✗ (1D-Schattenmikrometer, Rohr dreht je Punkt: ca. 37,5 min)

**Gewählte Lösungen:**
- TF1 Rohr einlegen: Von oben in offene Auflagen legen
- TF2 Durchbiegung begrenzen: Viele feste Stützstellen im berechneten Abstand
- TF3 Auflager und Ausrichtung: Rollenpaar aus Kunststoff oder Keramik
- TF4 Gegen Bewegung sichern: Federnde Niederhalterrollen aus Kunststoff
- TF5 Rohrtyp und Sollwerte: Auswahl am Bedienpanel (Rezept je Rohrtyp)
- TF6 Rohranfang/-ende erkennen: Fester Endanschlag ist der Nullpunkt
- TF7 Durchmesser berührungslos erfassen: Schattenmikrometer LED + Zeilenkamera, einachsig (z. B. Keyence LS, Micro-Epsilon optoCONTROL) [F? W10 Streuung, W7 Messbereich]
- TF8 Querschnitt in Winkellagen erfassen: Rohr dreht an jedem Messpunkt 360°
- TF9 Messposition entlang der Länge: Sensor fährt Rohrlänge ab, Rohr gehalten
- TF10 Position erfassen und zuordnen: Geber im Antriebsmotor (Servo oder Schrittmotor)
- TF11 Messwerte auswerten: Sensor-Controller mit Grenzwerten und Signalleuchte
- TF12 Rohr entnehmen und zuordnen: Manuell in zwei gekennzeichnete Ablagen (i.O./n.i.O.)
- TF13 Messsystem prüfen und einstellen: Kalibrierter Prüfstift fest am Anfang des Fahrwegs, wird bei jedem Rohr mitgemessen
- TF14 Querschnitt: sauber und ölfrei: Kontaktflächen nur Kunststoff (z. B. PEEK, POM, PE-UHMW) oder Keramik
- TF15 Querschnitt: Störeinflüsse: Steifes Maschinenbett (Aluprofil, Stahl-Schweißkonstruktion oder Hartgestein)
- TF16 Querschnitt: Bediener schützen: Lichtgitter vor dem Einlegebereich

### Entwurf 002

**Kern:** Ladeleiste, Luftlager-Prisma, Laser-Scan mit rotierendem Spiegel, Messkopf schwenkt um das stehende Rohr, direktes Längenmesssystem

**K.-o.-Status:** Taktzeit ✗ (1D-Laser-Scan, Drehung je Punkt: ca. 37,5 min); Luftlager bei Ø 1 mm ?

**Gewählte Lösungen:**
- TF1 Rohr einlegen: Auf Ladeleiste legen, die das Rohr in die Messlage absenkt
- TF2 Durchbiegung begrenzen: Durchgehende Rinne mit Messfenstern oder Längsschlitz
- TF3 Auflager und Ausrichtung: Luftlager-Prisma, Rohr schwebt auf ölfreier Druckluft [F? 3.2, ruhige Lage bei Ø 1 mm unsicher]
- TF4 Gegen Bewegung sichern: Nur Eigengewicht und Endanschlag
- TF5 Rohrtyp und Sollwerte: Barcode/DataMatrix vom Begleitpapier scannen
- TF6 Rohranfang/-ende erkennen: Messsensor erkennt die Rohrkante am Signalsprung
- TF7 Durchmesser berührungslos erfassen: Laser-Scan-Mikrometer mit rotierendem Spiegel [F? W10]
- TF8 Querschnitt in Winkellagen erfassen: Messkopf schwenkt um das stehende Rohr (180° reichen)
- TF9 Messposition entlang der Länge: Sensor fährt Rohrlänge ab, Rohr gehalten
- TF10 Position erfassen und zuordnen: Direktes Längenmesssystem am Schlitten (Magnetband oder Glasmaßstab)
- TF11 Messwerte auswerten: Industrie-PC mit Messprotokoll je Rohr
- TF12 Rohr entnehmen und zuordnen: Pneumatischer Auswerfer kippt in i.O.- oder n.i.O.-Rinne
- TF13 Messsystem prüfen und einstellen: Stufendorn mit mehreren Ø zwischen 1,0 und 6,5 mm
- TF14 Querschnitt: sauber und ölfrei: Antriebe und Führungen unterhalb des Rohrs oder gekapselt
- TF15 Querschnitt: Störeinflüsse: Haube gegen Staub, Zugluft und Fremdlicht
- TF16 Querschnitt: Bediener schützen: Haube mit Sicherheitsschalter

### Entwurf 003

**Kern:** Dreipunkt-Lünette, Mehrachs-Messkopf mit festen Achsen (kein Drehen), Auslösung positionsgesteuert alle 2 mm, SPS

**K.-o.-Status:** Sensor offen ? (ohne Drehung: mit Aeroel XLS ca. 26–38 min ✗, mit anderem Sensor offen)

**Gewählte Lösungen:**
- TF1 Rohr einlegen: Von oben in offene Auflagen legen
- TF2 Durchbiegung begrenzen: Viele feste Stützstellen im berechneten Abstand
- TF3 Auflager und Ausrichtung: Zentrisch schließende Dreipunkt-Auflage (Lünette)
- TF4 Gegen Bewegung sichern: Federnde Niederhalterrollen aus Kunststoff
- TF5 Rohrtyp und Sollwerte: Kodierte Wechseleinsätze melden den Ø-Bereich
- TF6 Rohranfang/-ende erkennen: Eigene Gabellichtschranke am Schlitten
- TF7 Durchmesser berührungslos erfassen: Mehrachs-Messkopf mit 2 oder 3 Achsen (z. B. Zumbach, Sikora, LaserLinc, Aeroel – ungeprüft) [F? W10]
- TF8 Querschnitt in Winkellagen erfassen: Mehrere feste Messachsen, nichts dreht sich [F? 2.1 Ø max/min zwischen den Achsen]
- TF9 Messposition entlang der Länge: Sensor ist stationär und das Rohr wird durch den Messbereich geführt
- TF10 Position erfassen und zuordnen: Messung positionsgesteuert alle 2 mm auslösen
- TF11 Messwerte auswerten: SPS mit Bedienpanel
- TF12 Rohr entnehmen und zuordnen: Entnahme erst nach Quittierung, bei n.i.O. gibt nur die Sperrablage frei
- TF13 Messsystem prüfen und einstellen: Kalibrierter Prüfstift fest am Anfang des Fahrwegs, wird bei jedem Rohr mitgemessen
- TF14 Querschnitt: sauber und ölfrei: Kontaktflächen nur Kunststoff (z. B. PEEK, POM, PE-UHMW) oder Keramik
- TF15 Querschnitt: Störeinflüsse: Schwingungsdämpfende Maschinenfüße
- TF16 Querschnitt: Bediener schützen: Lichtgitter vor dem Einlegebereich

### Entwurf 004

**Kern:** Kunststoff-Niederhalterrollen, Wechseleinsätze je Ø, zwei gegenüberliegende Abstandssensoren, Rohr dreht je Punkt

**K.-o.-Status:** Taktzeit wahrscheinlich ✗ (zwei Abstandssensoren, 1D, Drehung je Punkt); Datenblatt fehlt

**Gewählte Lösungen:**
- TF1 Rohr einlegen: Von oben in offene Auflagen legen
- TF2 Durchbiegung begrenzen: Durchgehende Rinne mit Messfenstern oder Längsschlitz
- TF3 Auflager und Ausrichtung: Wechseleinsätze oder höhenverstellbare Auflage je Ø-Bereich
- TF4 Gegen Bewegung sichern: Federnde Niederhalterrollen aus Kunststoff
- TF5 Rohrtyp und Sollwerte: Nenn-Ø aus erster Messung erkennen, Werkstoff manuell wählen
- TF6 Rohranfang/-ende erkennen: Messsensor erkennt die Rohrkante am Signalsprung
- TF7 Durchmesser berührungslos erfassen: Zwei gegenüberliegende Abstandssensoren (konfokal oder Triangulation), Ø aus Differenz [F? W10]
- TF8 Querschnitt in Winkellagen erfassen: Rohr dreht an jedem Messpunkt 360°
- TF9 Messposition entlang der Länge: Sensor fährt Rohrlänge ab, Rohr gehalten
- TF10 Position erfassen und zuordnen: Direktes Längenmesssystem am Schlitten (Magnetband oder Glasmaßstab)
- TF11 Messwerte auswerten: Industrie-PC mit Messprotokoll je Rohr
- TF12 Rohr entnehmen und zuordnen: n.i.O.-Rohr bekommt Anhänger/Etikett an der Schutzhülle
- TF13 Messsystem prüfen und einstellen: Referenzrohr als Meisterteil
- TF14 Querschnitt: sauber und ölfrei: Glatte, abwischbare Wechselauflagen
- TF15 Querschnitt: Störeinflüsse: Steifes Maschinenbett (Aluprofil, Stahl-Schweißkonstruktion oder Hartgestein)
- TF16 Querschnitt: Bediener schützen: Langsame, kraftbegrenzte Achsen

### Entwurf 005

**Kern:** Rollenpaar, Vakuum-Prisma, telezentrische Kamera mit Bildauswertung, Rohr dreht je Punkt, Auslösung alle 2 mm

**K.-o.-Status:** Sensor offen ? (telezentrische Kamera, kein Datenblatt); Vakuum auf Nitinol (3.1) ?

**Gewählte Lösungen:**
- TF1 Rohr einlegen: Auf Ladeleiste legen, die das Rohr in die Messlage absenkt
- TF2 Durchbiegung begrenzen: Viele feste Stützstellen im berechneten Abstand
- TF3 Auflager und Ausrichtung: Rollenpaar aus Kunststoff oder Keramik
- TF4 Gegen Bewegung sichern: Vakuum-Prisma (Saugnut hält das Rohr)
- TF5 Rohrtyp und Sollwerte: Barcode/DataMatrix vom Begleitpapier scannen
- TF6 Rohranfang/-ende erkennen: Messsensor erkennt die Rohrkante am Signalsprung
- TF7 Durchmesser berührungslos erfassen: Telezentrische Kamera mit Bildauswertung [F? W10]
- TF8 Querschnitt in Winkellagen erfassen: Rohr dreht an jedem Messpunkt 360°
- TF9 Messposition entlang der Länge: Sensor fährt Rohrlänge ab, Rohr gehalten
- TF10 Position erfassen und zuordnen: Messung positionsgesteuert alle 2 mm auslösen
- TF11 Messwerte auswerten: Industrie-PC mit Messprotokoll je Rohr
- TF12 Rohr entnehmen und zuordnen: Pneumatischer Auswerfer kippt in i.O.- oder n.i.O.-Rinne
- TF13 Messsystem prüfen und einstellen: Einstellmeister wird täglich manuell eingelegt
- TF14 Querschnitt: sauber und ölfrei: Druckluft über Öl- und Partikelfilter
- TF15 Querschnitt: Störeinflüsse: Haube gegen Staub, Zugluft und Fremdlicht
- TF16 Querschnitt: Bediener schützen: Haube mit Sicherheitsschalter

## 4. Bewertung (Punkte 0–4, Gewichte aus Cockpit-Screenshot 22.11.)

| Kriterium (Gewicht) | 001 | 002 | 003 | 004 | 005 |
|---|---|---|---|---|---|
| K1 1.5 Werkstoff Tantal (10 %) | 3 | 4 | 2 | 3 | 2 |
| K2 2.4 %GRR-Reserve (33,3 %) | 2 | 3 | 3 | 1 | 1 |
| K3 2.6 Rauheit messen (10 %) | 0 | 0 | 0 | 0 | 0 |
| K4 2.7 Beschädigung feststellen (16,7 %) | 1 | 1 | 0 | 0 | 2 |
| K5 4.1 Taktzeit (26,7 %) | 0 | 0 | 1 | 0 | 1 |
| K6 5.1 Platzbedarf (3,3 %) | 2 | 2 | 3 | 2 | 3 |
| **Erfüllung (gewichtet)** | **30.0 %** | **40.8 %** | **39.1 %** | **17.5 %** | **30.8 %** |

Begründungen der Punkte stehen in `projekt/Analyse_Bewertung_Konzepte_2026-11-22.md` (für die Konzepte A bis D). Für 001 bis 005 gilt: K1 nach Werkstoffkontakt (Kunststoff und Luftlager schonen Tantal); K2 nach Sensorart (Laser-Scan und Mehrachs-Messkopf mit kleiner Wiederholgenauigkeit, 1D-Schattenmikrometer mit Unsicherheit); K3 Rauheit ist in keiner Variante vorgesehen; K4 Beschädigung nur mit Kamera-Auswertung (005); K5 Taktzeit ist bei 1D-Sensoren (001, 002, 004) bereits K.-o.; K6 nach Anzahl der Achsen und Köpfe.

Schätzung, keine Messung. Die Punkte sind nicht gegen Herstellerdatenblätter geprüft; die Festanforderungen 2.5 und 3.1 sind ungeklärt (Mittelung, Vakuum).

## 5. Lücke im Morphologischen Kasten (Hinweis, kein Vorschlag im Entwurf)

Die 2D-Schattenbild-Messung (RIFTEK RF656.2D, Taktzeit unter 5 min bei 40×50 mm Feld) ist im Morphologischen Kasten nicht als Idee enthalten. Sie ist der einzige geprüfte Sensor, der die Taktzeitregel erfüllt. Ob sie als Idee aufgenommen wird, entscheidet Janek. Wenn ja, müsste ein Entwurf neu gebildet werden.
