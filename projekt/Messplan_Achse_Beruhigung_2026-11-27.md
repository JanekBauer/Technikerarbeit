# Messplan: Anfahr-, Brems- und Beruhigungszeit der Verfahrachse

Stand 27.11.2026 · erstellt von KI (Claude Code) als Vorlage · **keine Festlegung**. Durchführung und Auswertung: Janek. Werte ohne Messung bleiben als Annahme `[S]` oder `[offen]` gekennzeichnet.

Kennzeichnung: **[S]** Annahme · **[offen]** Wert fehlt · **[M]** wird bei der Messung ermittelt

## 1. Ziel

Die Stop-and-go-Zeit in `projekt/Zeitrechnung_Zylindrizitaet_2026-11-27.xlsx` (Blatt „Stop_1Grad“) hängt von drei Werten ab, die bisher nur angenommen sind:

1. **Verfahrzeit** zwischen zwei Messpunkten (Anfahren, Fahren, Abbremsen), Annahmen 40 bis 400 ms `[S]`
2. **Beruhigungszeit** nach dem Halt, bis der Sensor stabil misst `[S]`
3. **Restschwingung**: Abweichung der Messposition oder des Messwerts nach dem Halt `[offen]`

Die Messung soll diese drei Werte für die Achse ermitteln, die am Aufbau eingesetzt wird.

## 2. Fragen, die die Messung beantwortet

- Wie lange dauert es vom Start der Bewegung bis zum Stillstand bei 2 mm und bei 1 mm Verfahrweg? `[M]`
- Ab welchem Zeitpunkt nach dem Halt weicht der Messwert nicht mehr als ein festgelegter Grenzwert ab? `[M]`
- Wie groß ist die Streuung der Messwerte an einer festen Stelle, nachdem die Achse steht? `[M]`
- Hängt die Beruhigungszeit von der Verfahrgeschwindigkeit ab? `[M]`

## 3. Versuchsaufbau

| Teil | Angabe | Status |
|---|---|---|
| Verfahrachse | Typ, Hersteller, Hub, max. Geschwindigkeit, Beschleunigung | `[offen]` |
| Messsensor | Typ (z. B. LS-9030D), Messrate, Mittelung im Versuch | `[offen]` |
| Messnormal | Stab oder Ring mit bekanntem Durchmesser, fest eingespannt, ohne Drehung | `[offen]` |
| Datenerfassung | Zeitstempel je Messwert, Auflösung ≤ 1 ms | `[offen]` |
| Referenz | Zeitmessung über Lichtschranke oder Encoder der Achse | `[offen]` |

Der Sensor steht während des Versuchs fest. Die Achse fährt nur den Sensor, nicht das Rohr. So lassen sich Achsbewegung und Messwert eindeutig zuordnen.

## 4. Versuchsablauf

1. **Vorbereitung:** Achse und Sensor einschalten, Aufwärmzeit laut Herstellerangabe `[offen]`. Messnormal einspannen, Abstand zum Sensor auf die Mitte des Messbereichs einstellen.
2. **Nullmessung:** Achse steht, 30 s messen. Daraus ergibt sich die Grundstreuung ohne Bewegung.
3. **Verfahrversuch:** Achse fährt von Punkt A nach Punkt B, Verfahrweg 2 mm `[S]`. Sensor misst ab dem Start der Bewegung durchgehend mit Zeitstempel.
4. **Wiederholung:** Jede Variante mindestens 30-mal wiederholen, damit die Streuung der Beruhigungszeit sichtbar wird.
5. **Varianten:** Verfahrweg 2 mm und 1 mm; Verfahrgeschwindigkeit 50 mm/s (3 m/min) und, falls möglich, eine niedrigere Stufe `[S]`.

## 5. Auswertung

- **Verfahrzeit:** Zeit vom Start der Bewegung bis zum Stillstand der Achse, aus dem Encoder oder der Referenz. Mittelwert und Streuung je Variante.
- **Beruhigungszeit:** Zeit vom Stillstand bis zu dem Zeitpunkt, ab dem der Messwert innerhalb des Grenzwerts um den Endwert bleibt. Der Grenzwert muss festgelegt werden, siehe Abschnitt 6 `[offen]`.
- **Restschwingung:** Maximale Abweichung des Messwerts nach dem Halt, im Zeitfenster der Beruhigungszeit.
- **Auswertung:** Mittelwert, Standardabweichung und Maximum über alle Wiederholungen je Variante.

Die Ergebnisse werden in die Tabelle des Blatts „Stop_1Grad“ übertragen. Die gelben Felder für die Verfahrzeit ersetzen dann die Annahmen von 40, 200 und 400 ms.

## 6. Offene Punkte vor dem Versuch

1. **Grenzwert für die Beruhigung:** Die Abweichung muss kleiner sein als ein Anteil der Messunsicherheit. Die Analyse nennt σ_GRR ≤ 0,43 µm für Szenario A `[R]`. Der Grenzwert ist bis zur Entscheidung E-008 `[offen]`.
2. **Achse:** Ob die Achse des Aufbaus schon feststeht. Ohne Typ- und Herstellerangabe sind die Werte nicht übertragbar.
3. **Sensor für den Versuch:** Ob der LS-9030D schon verfügbar ist oder ein anderer Sensor getestet wird.
4. **Sicherheit:** Der Sensor arbeitet mit LED, nicht mit Laser. Die Achse braucht die üblichen Verfahr- und Endlagenschutzmaßnahmen des Herstellers `[offen]`.

## 7. Ergebnis dokumentieren

Je Versuch festhalten: Datum, Achse, Sensor, Verfahrweg, Geschwindigkeit, Anzahl Wiederholungen, Grenzwert und Ergebnisse. Die Rohdaten gehören in ein eigenes Blatt oder eine CSV-Datei unter `projekt/`, damit die Auswertung nachvollziehbar bleibt.
