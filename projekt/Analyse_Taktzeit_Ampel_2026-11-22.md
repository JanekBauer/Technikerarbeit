# Taktzeit-Ampel je 3-m-Rohr (Modellrechnung)

Stand 22.11.2026 · KI (Claude Code) · Modellrechnung, keine Messung. Grundlage für die Entscheidung, welche Sensoren in der Hauptliste bleiben.

## Regel (Janek)
- Über 5 min je Rohr: entfällt (Anforderung nicht erfüllt, Taktzeit über 5 min).
- 1 bis 5 min: gelb (erfüllt, aber schlechter).
- Unter 1 min: grün.
- Rohr 3 m, 1501 Prüfstellen (alle 2 mm).

## Annahmen (eigene, bitte prüfen)
- Keine Helix (Anf. 2.3): Drehung nur an festen Stationen.
- Je Station eine Umdrehung in 3 s, Einschwingzeit 0,5 s.
- Winkelschritt 5° (passt bis Oberwelle n ≈ 6, siehe Nachtrag (3) der Sensorik-Analyse; Frage pv-ent-oberwellen).
- 1D-Sensor: eine Prüfstelle je Station, also 1501 Stationen.
- 2D-Sensor: Stationen = 3000 mm / größere Feldseite (Feldausrichtung im Rohr unbekannt, optimistisch).
- Bildrate: RF657.2D 24/s, RF656.2D 50/s (Controller SuM), RF657R.2D 4/s. Nicht begrenzend bei 5° und 3 s außer RF657R.
- Verfahr- und Beschleunigungszeiten sind nicht enthalten.

Formel: Taktzeit = Stationen × (max(3 s; 72 Bilder / Bildrate) + 0,5 s).

## Ergebnis
| Sensor(en) | Typ | Stationen | Taktzeit | Ampel |
|---|---|---|---|---|
| RF656.2D-40x50, RF657.2D-40x50 | 2D | 60 | 3,5 min | gelb |
| RF657.2D-60x80 | 2D | 38 | 2,2 min | gelb |
| RF656.2D-25x35, RF657.2D-25x35 | 2D | 86 | 5,0 min | rot (knapp) |
| RF656.2D-15x20, RF657.2D-15x20 | 2D | 150 | 8,8 min | rot |
| RF656.2D-8x10 | 2D | 300 | 17,5 min | rot |
| RF657R.2D (25 / 45 / 70 / 100) | 2D rund | 120 / 67 / 43 / 30 | 37,0 / 20,7 / 13,3 / 9,2 min | rot |
| Alle 1D-Sensoren (Keyence LS-, Micro-Epsilon ODC, Mitutoyo LSM, Aeroel XLS) | 1D | 1501 | 87,6 min | rot |
| Grün | – | – | – | keiner |

## Was das bedeutet
1. **Unter diesen Annahmen ist kein Sensor grün.** Grün (<1 min) brauchte Feldlängen über ca. 175 mm. Das gibt keines der Datenblätter her.
2. **Alle 1D-Sensoren fallen raus**, solange die Drehung an jeder Station gilt. Das ist schon bei 1 s je Umdrehung der Fall (1501 × 1,5 s ≈ 37 min). Ein 1D-Sensor braucht also eine andere Messstrategie. Das ist eine Entwurfsfrage und gehört nicht in diese Analyse.
3. **Die drei gelben Sensoren** sind alle 2D mit großem Feld. Die Entscheidung hängt an Frage pv-ent-drehung-stationen und pv-ent-oberwellen.
4. **Empfindlich:** Das Ergebnis hängt stark an Drehzeit und Winkelschritt. Bei 2 s je Umdrehung und 5° wäre der RF656.2D-25x35 rund 3,4 min (gelb). Beim Winkelschritt von 2,5° verdoppeln sich die Bilder je Umdrehung, und bei RF657 wird die Rate zum Engpass.

## Doubletten im Sensorvergleich
Drei Sensoren aus der Web-Suche sind doppelt eingetragen (IDs mws0ln0abedtb XLS13XY, mws0lnc4mbahq LSM-501S, mws0lnnai0kol LSM-503S). Sie kommen von der Übernahme im Postfach. Die Ansicht setzt sie in „Entfallen“, gelöscht ist nichts. Bereinigen über das Postfach (Aufgabe pv-auf-dubletten-sensoren).

## Umsetzung im Cockpit
Sensorvergleich: Spalte „Taktzeit je Rohr“ mit Ampelpunkt. Rote Sensoren und Dubletten stehen im Kasten „Entfallen“. Die Werte stehen als Tabelle `TAKT` in cockpit/vorlage.html, nicht in sensors.json.
