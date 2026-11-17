# Chat 06 – Morphologischer Kasten V2: Teilfunktionen & Ideenfindung

Stand 12.11.2026 · Janek Bauer · Live-Dokument (vollständig, inkl. F-Check und Abhängigkeiten): https://claude.ai/artifact/S52wDerR9Cn5mYmaUhY316

Alle Einträge sind KI-Vorschläge, solange nicht „(Janek)“ dahinter steht. Grundlage: PH V8.7 final. „[F]“ = berührt eine Festanforderung (siehe F-Check im Live-Dokument). Herstellernamen ungeprüft.

## Teilfunktionen

TF1 Rohr aufnehmen · TF2 Durchbiegung begrenzen · TF3 Rohr auflagern und zur Messachse ausrichten (neu) · TF4 Rohr gegen ungewollte Bewegung sichern · TF5 Rohrtyp und Sollwerte vorgeben (neu) · TF6 Rohranfang und Rohrende erkennen · TF7 Durchmesser berührungslos erfassen · TF8 Querschnitt in mehreren Winkellagen erfassen · TF9 Messposition entlang der Länge ändern · TF10 Position erfassen und dem Messwert zuordnen (neu) · TF11 Messwerte auswerten und Ergebnis ausgeben · TF12 Rohr entnehmen und zuordnen · TF13 Messsystem prüfen und einstellen (neu) · Q1 Sauber und ölfrei halten · Q2 Störeinflüsse fernhalten (neu) · Q3 Bediener schützen (neu)

## Morphologischer Kasten

| Teilfunktion | Idee 1 | Idee 2 | Idee 3 | Idee 4 | Idee 5 | Ideen Janek |
| --- | --- | --- | --- | --- | --- | --- |
| TF1 Rohr aufnehmen | 1.1 Von oben in offene Auflagen legen (Janek: manuell) | 1.2 Von vorn in seitlich offene Auflagen | 1.3 Axial durch Trichter einschieben [F] | 1.4 Ladeleiste senkt Rohr in Messlage ab | 1.5 Vertikal einhängen [F] | |
| TF2 Durchbiegung begrenzen | 2.1 Viele feste Stützstellen im berechneten Abstand | 2.2 Durchgehende Rinne mit Messfenstern/Längsschlitz | 2.3 Stütze fährt mit dem Sensor mit | 2.4 Rohr hängt vertikal [F] | 2.5 Leichte Zugvorspannung [F] | |
| TF3 Auflagern und ausrichten | 3.1 Festes V-Prisma aus Kunststoff | 3.2 Rollenpaar aus Kunststoff/Keramik | 3.3 Luftlager-Prisma (ölfreie Druckluft) | 3.4 Zentrisch schließende Dreipunkt-Auflage | 3.5 Wechseleinsätze/höhenverstellbar je Ø-Bereich | |
| TF4 Gegen Bewegung sichern | 4.1 Eigengewicht und Endanschlag | 4.2 Spannzange/Futter mit Kunststoffeinsatz an einem Ende [F] | 4.3 Beide Enden gefasst [F] | 4.4 Federnde Niederhalterrollen | 4.5 Vakuum-Prisma | |
| TF5 Rohrtyp und Sollwerte | 5.1 Auswahl am Bedienpanel (Rezept) | 5.2 Barcode/DataMatrix vom Begleitpapier | 5.3 Nenn-Ø aus erster Messung, Werkstoff manuell | 5.4 Kodierte Wechseleinsätze | | |
| TF6 Anfang und Ende erkennen | 6.1 Fester Endanschlag = Nullpunkt | 6.2 Messsensor erkennt Rohrkante | 6.3 Gabellichtschranke am Schlitten | 6.4 Länge aus Rezept, nur Anfang erkannt | | |
| TF7 Durchmesser erfassen | 7.1 Schattenmikrometer LED + Zeilenkamera, einachsig (z. B. Keyence LS, Micro-Epsilon optoCONTROL) | 7.2 Laser-Scan-Mikrometer | 7.3 Mehrachs-Messkopf 2/3 Achsen (z. B. Zumbach, Sikora, LaserLinc, Aeroel) | 7.4 Zwei gegenüberliegende Abstandssensoren (konfokal/Triangulation) | 7.5 Telezentrische Kamera | |
| TF8 Mehrere Winkellagen | 8.1 Rohr dreht schrittweise 360° je Messpunkt (Janek) | 8.2 Rohr dreht durchgehend, Schraubenlinie (Janek) [F] | 8.3 Messkopf schwenkt 180° um stehendes Rohr | 8.4 Mehrere feste Messachsen [F] | 8.5 Mehrachs-Kopf plus kleiner Schwenk | |
| TF9 Messposition ändern | 9.1 Rohr steht, Sensor fährt (Janek, Chat 05) | 9.2 Sensor steht, Treibrollen schieben Rohr [F] | 9.3 Sensor steht, Rohr auf fahrendem Träger | 9.4 Zwei Sensoren teilen die Strecke | | |
| TF10 Position zuordnen | 10.1 Geber im Antriebsmotor | 10.2 Direktes Längenmesssystem am Schlitten | 10.3 Positionsgesteuert alle 2 mm auslösen | 10.4 Zeitgesteuert bei konstanter Geschwindigkeit | 10.5 Drehgeber für den Winkel | |
| TF11 Auswerten und ausgeben | 11.1 Sensor-Controller mit Grenzwerten und Signalleuchte | 11.2 Industrie-PC mit Messprotokoll | 11.3 SPS mit Bedienpanel | 11.4 Verlauf über die Länge mit markierter Fehlstelle | | |
| TF12 Entnehmen und zuordnen | 12.1 Manuell in zwei gekennzeichnete Ablagen | 12.2 Entnahme nach Quittierung, n.i.O. nur Sperrablage | 12.3 Pneumatischer Auswerfer in i.O.-/n.i.O.-Rinne | 12.4 Anhänger/Etikett an der Schutzhülle | | |
| TF13 Messsystem prüfen | 13.1 Prüfstift fest am Fahrweganfang, wird je Rohr mitgemessen | 13.2 Einstellmeister täglich manuell | 13.3 Stufendorn mit mehreren Ø | 13.4 Referenzrohr als Meisterteil | | |
| Q1 Sauber und ölfrei | Q1.1 Kontaktflächen Kunststoff (PEEK, POM, PE-UHMW) oder Keramik | Q1.2 Antriebe/Führungen unterhalb oder gekapselt | Q1.3 Schmierfreie Führungen | Q1.4 Öl- und Partikelfilter für Druckluft | Q1.5 Abwischbare Wechselauflagen | |
| Q2 Störeinflüsse fernhalten | Q2.1 Steifes Maschinenbett | Q2.2 Schwingungsdämpfende Füße | Q2.3 Haube gegen Staub, Zugluft, Fremdlicht | Q2.4 Sperrluft vor der Optik | Q2.5 Temperaturausgleich/Temperatur erfassen | |
| Q3 Bediener schützen | Q3.1 Haube mit Sicherheitsschalter | Q3.2 Lichtgitter | Q3.3 Langsame, kraftbegrenzte Achsen | Q3.4 Start-Taster außerhalb des Fahrbereichs | | |

Verworfen: magnetisches Halten, taktiles Messen, pneumatische Messringe.

## KI-Logbuch

| Datum | Chat | Zweck | Art der Hilfe |
| --- | --- | --- | --- |
| 12.11.2026 | 06 | Morphologischer Kasten V2 | Teilfunktionen von der KI überarbeitet und ergänzt (TF3, TF5, TF10, TF13, Q2, Q3); Ideenfindung durch die KI (4 bis 5 Ideen je Zeile); grober F-Check und Abhängigkeiten als Hinweise. Auswahl, eigene Ideen, Gesamtvarianten: Janek |
