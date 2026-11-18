# Chat 06 – Morphologischer Kasten: Teilfunktionen & Ideen

Stand 07.11.2026 · Janek Bauer · Live-Dokument: https://claude.ai/artifact/EDcdsL8eiMY3wcpuoPtQMM

## Hinweise

Arbeitsstand für den Morphologischen Kasten (Phase 2, Lösungsfindung), Grundlage ist Pflichtenheft V8.7 final.

- **KI-Vorschlag** = Anstoß von Claude, nicht übernommen. **Janek** = eigene Idee oder Entscheidung von Janek.
- Die Liste der Teilfunktionen ist selbst ein KI-Vorschlag. Janek legt die endgültigen Teilfunktionen fest.
- **F-Check** = grober Hinweis auf einen möglichen Konflikt mit einer Festanforderung (F). Bewertet und gewichtet wird erst in Chat 07.
- Größtes Risiko (W10): Ovalität ≤ 0,010 mm bei %GRR ≤ 10 % verlangt ca. 1 µm Streuung des Messsystems. Lagefehler aus Durchbiegung, Rundlauf und Vibration gehen direkt in den Ovalitätswert ein.

## Teilfunktionen mit Ideen

| Teilfunktion (KI-Vorschlag) | KI-Vorschlag Lösung | F-Check | Denkfrage | Ideen Janek |
| --- | --- | --- | --- | --- |
| TF1 Rohr aufnehmen (manuell, fest – Janek) | Einlegemulde über die ganze Länge mit Endanschlag | – | Wie verhinderst du, dass ein 3-m-Rohr beim Einlegen anstößt oder knickt? | |
| TF2 Rohr in Messlage halten (gegen Durchbiegung) | Mehrere V-Prismen aus Kunststoff (z. B. PEEK) im berechneten Stützabstand | – | Was passiert, wenn der Sensor genau an einer Stütze vorbeifahren muss? | |
| TF3 Querschnitt in mehreren Winkellagen erfassen | Rohr auf Rollenpaaren, ein angetriebenes Rollenpaar dreht es über Reibung | Achtung 3.3: Rundlauf, Schlupf, Torsion über 3 m fraglich; Reibung betrifft 2.7 (W) | Geht es ohne Drehen, mit mehreren Messrichtungen? Wie viele Winkellagen, damit Ø max/Ø min nicht dazwischen fallen? | |
| TF4 Messposition entlang der Länge ändern | Rohr steht, Sensor fährt auf Linearachse (Spindel oder Zahnriemen) | – | Was bewegt sich leichter und wiederholgenauer: 3-m-Rohr oder Messkopf? | |
| TF5 Rohr gegen ungewollte Bewegung sichern | Spannzange mit Kunststoffeinsatz an einem Rohrende | Achtung 3.1: Spannkraft bei dünnwandigem Rohr prüfen (Ovalisieren) | Braucht es Spannkraft, oder reicht ein Anschlag? | |
| TF6 Lage referenzieren (Messpunkt 0, Rohrende) | Messsensor erkennt Rohrkante selbst am Signalsprung | – | Wie genau muss Messpunkt 0 sein bei 2 mm Raster? | |
| TF7 Durchmesser und Ovalität erfassen (Messprinzip, Chat 05) | Optisches Laser-Scan-Mikrometer (Schattenprinzip); Keyence LS eine Option, weitere Hersteller dazu | Achtung W10: ca. 1 µm Streuung unsicher – in Chat 05 prüfen | Welche weiteren berührungslosen Prinzipien gibt es (kapazitiv, Wirbelstrom, Kamera)? | |
| TF8 Messwerte auswerten und Ergebnis ausgeben | Sensor-Controller an PC/SPS mit i.O./n.i.O.-Anzeige; nur Schnittstelle, Programmierung abgegrenzt | – | Was muss der Prüfer am Ende sehen? | |
| TF9 Rohr entnehmen und zuordnen | Manuell entnehmen, getrennte Ablagen i.O./n.i.O. | – | Wie verhinderst du, dass ein n.i.O.-Rohr in die Fertigung geht („sicher“)? | |
| Querschnitt: sauber und ölfrei halten (3.2) | Kontaktflächen nur Kunststoff, Führungen/Antriebe unterhalb oder abseits, ölfreier Druckluftfilter | – | Welche Bauteile über dem Rohr könnten Abrieb oder Öl abgeben? | |

Weitere Suchrichtungen: vertikales Hängen, Zugvorspannung, Luftlager, rotierender Sensor statt drehendes Rohr.

## Nächste Schritte

- [ ] Janek legt die Teilfunktionen fest
- [ ] Janek trägt je Zeile mindestens eine eigene Idee ein
- [ ] Abhängigkeiten markieren
- [ ] Grober F-Check aller Ideen
- [ ] 2–4 Gesamtvarianten als Pfade bilden (Auswahl: Janek)

## KI-Logbuch

| Datum | Chat | Zweck | Art der Hilfe |
| --- | --- | --- | --- |
| 07.11.2026 | 06 | Morphologischer Kasten | Prüffragen zu Teilfunktionen; Teilfunktionsliste als KI-Vorschlag; je Teilfunktion ein gekennzeichneter KI-Lösungsvorschlag mit Denkfrage und grobem F-Check; Übertragung in Dokument |
