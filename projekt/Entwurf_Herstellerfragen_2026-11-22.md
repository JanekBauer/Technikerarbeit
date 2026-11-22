# Entwurf: Fragen an Sensorhersteller (Arbeitspaket 7)

Stand 22.11.2026 · Entwurf der KI (Claude Code) · **nicht versendet**. Versand nur durch Janek, Inhalt und Formulierung prüft Janek. Keine vertraulichen Daten aus den Rohrspezifikationen enthalten: Toleranzen sind nur als Größenordnung angegeben, nachdem der Betrieb sie freigegeben hat.

Empfänger: Micro-Epsilon (optoCONTROL 2700), Keyence (LS-9030 / LS-9030D), RIFTEK (RF656.2D / RF657.2D). Nach Download der Datenblätter auch Mitutoyo (LSM-501S/503S) und Aeroel/Marposs (XLS13XY).

## Anschreiben (Kurzfassung)

Im Rahmen einer Technikerarbeit wird eine Messanlage für den Wareneingang konzipiert. Sie soll dünnwandige Metallrohre (Ø 1 bis 6,5 mm, Länge 1 bis 3 m) berührungslos messen. Erfasst werden der Außendurchmesser und die Zylinderform (Ø max − Ø min) an Messpunkten im Abstand von 2 mm über die gesamte Länge. Für die Konzeptauswahl bitten wir um folgende Angaben sowie um ein unverbindliches Angebot.

## Fragen, geordnet nach Anforderungen (PH V1.2)

**Messbereich (Anf. 1.3)**
1. Gelten die Angaben zu Wiederholgenauigkeit und Linearität auch für Objekte mit Ø 1,0 mm, oder nur für das im Datenblatt genannte Normal (Keyence Ø 10 mm, Micro-Epsilon 2-mm-Prüfstift)? Gibt es Werte für Ø 1 / 3 / 6,5 mm?

**Wiederholgenauigkeit ohne bzw. mit wenig Mittelung (Anf. 2.4, 2.5)**
2. Wie groß ist die Wiederholgenauigkeit (Angabe als σ oder ±2σ) bei **einer einzelnen Abtastung** und bei 8, 32, 128 Mittelungen?
3. Micro-Epsilon: Fn. 6 im Katalog nennt „Mittelung von 1024 Werten über einen Zeitraum von 5 Minuten“. Was genau bedeutet das? Ist der Wert ±-Halbbreite oder Gesamtbreite des 95-%-Intervalls?
4. Gibt es Angaben zur Wiederholgenauigkeit an einem **bewegten** bzw. **rotierenden** Objekt (Vorschub bis ca. 30 mm/s)?

**Lage im Messfeld (Anf. 2.2, 3.3)**
5. Wie ändern sich Messabweichung und Wiederholgenauigkeit, wenn das Objekt in Strahlrichtung (Z) und quer dazu von der Messfeldmitte abweicht (z. B. ±0,5 / ±1 / ±2 mm)?
6. Einfluss einer Schrägstellung des Objekts zur optischen Achse (Neigung von wenigen Zehntel Grad durch Durchbiegung)? Gibt es eine Neigungskorrektur (Micro-Epsilon nennt „Durchmesser inkl. Neigungskorrektur“, Katalog S. 13)?

**Zylinderform (Anf. 2.1)**
7. Kann das Gerät bzw. die Steuerung Ø max und Ø min über mehrere Winkellagen selbst auswerten, wenn das Objekt rotiert (Micro-Epsilon S. 12: „Rundlaufmessungen von rotierenden Teilen“)? Mit welchem Winkelgeber-Eingang und welcher Winkelauflösung?
8. RIFTEK: Wie groß ist die Wiederholgenauigkeit der Durchmessermessung (im Handbuch Kap. 6.1 nicht angegeben)? In welcher Richtung liegt das Messfeld zum Objekt, z. B. 15 × 20 mm, und wie viele Längenpositionen lassen sich aus einem Bild auswerten?

**Positionszuordnung (Anf. 2.3, 2.5)**
9. Kann die Messung über einen Encoder-Eingang **positionsgesteuert** (alle 2 mm) ausgelöst werden? Welche Verzögerung (Latenz) liegt zwischen Trigger und Messwert?

**Umgebung und Werkstoff (Anf. 3.2, Rahmenbedingungen)**
10. Einfluss glänzender Metalloberflächen (Nitinol, Edelstahl, Tantal) und von Fremdlicht im Wareneingang auf die Kantenerkennung?
11. Temperaturdrift je K und erforderliche Warmlaufzeit?

**Angebot (PH Kap. 3: Angebote für Kaufteile)**
12. Unverbindliches Angebot für Messkopf, Steuerung, Kabel, Software und gegebenenfalls Kalibriernormal; Lieferzeit.
13. Gibt es ein Kalibrierzertifikat (DAkkS bzw. rückführbar) für das Gerät und das Normal? Hintergrund: Prüfmittel im QM-System nach ISO 13485.
