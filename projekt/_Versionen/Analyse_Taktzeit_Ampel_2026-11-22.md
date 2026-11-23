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

## Korrektur 22.11.2026 (Servo dreht durchgehend)

Frühere Fassung: Jede Station brauchte 3 s Drehung plus 0,5 s Bremsen. Das war falsch. Der Servo dreht durchgehend mit konstanter Drehzahl und hält nicht an. Angehalten wird nur die Achse zwischen den Messstationen.

Neues Modell:
- Umdrehungszeit T = N / Bildrate, mit N = 72 Bilder je Umdrehung (5°-Schritt). Die Drehzahl wird so eingestellt, dass alle Bilder gerade rechtzeitig vorliegen.
- Station = T + 0,5 s (Verfahrachse anhalten und beruhigen). Kein Bremsen des Servos.
- 1D-Sensor: Umdrehung 1 s (Annahme für die kleinste sinnvolle Drehzahl), Station = 1,5 s.

Ergebnis je 3-m-Rohr (1501 Prüfstellen):
| Sensor | Stationen | Station | Taktzeit | Ampel |
|---|---|---|---|---|
| RF656.2D-40x50 | 60 | 1,94 s | 1,9 min | gelb |
| RF656.2D-25x35 | 86 | 1,94 s | 2,8 min | gelb |
| RF656.2D-15x20 | 150 | 1,94 s | 4,8 min | gelb (knapp) |
| RF656.2D-8x10 | 300 | 1,94 s | 9,7 min | rot |
| RF657.2D-60x80 | 38 | 3,5 s | 2,2 min | gelb |
| RF657.2D-40x50 | 60 | 3,5 s | 3,5 min | gelb |
| RF657.2D-25x35 | 86 | 3,5 s | 5,0 min | rot (knapp) |
| RF657.2D-15x20 | 150 | 3,5 s | 8,8 min | rot |
| RF657R.2D (alle Größen) | 30–120 | 9–37 min | rot |
| 1D (alle) | 1501 | 1,5 s | 37,5 min | rot |

Begründung der Grenze: Die Bildrate (RF656 mit Controller SuM 50/s, RF657 24/s) bestimmt die Umdrehungszeit. Ein schnellerer Servo hilft nur, wenn die Bildrate mitzieht. Der Winkelschritt wird durch die Oberwellen-Frage (pv-ent-oberwellen) bestimmt. Bei 2,5° verdoppeln sich die Bilder je Umdrehung.

Offen: Ob die Verfahrachse ohne Helix wirklich nur zwischen den Stationen anhält (Anf. 2.3 und Entscheidung pv-ent-drehung-stationen), und die Dynamik eines durchgehend drehenden dünnen Nitinol-Rohrs.

## Nachtrag (4): Alle Sensoren neu, Modell mit durchgehend drehendem Rohr

Modell: 72 Winkel je Umdrehung (5°). 1D-Sensor: je 2-mm-Punkt eine Messzeit nach Rep-Bedingung des Herstellers (Mittelung ÷ Rate), mindestens eine Umdrehung, plus Achse anhalten je Punkt. 2D-Sensor: Umdrehung = 72 Bilder ÷ Bildrate, plus Achse anhalten je Station. Ergebnis je 3-m-Rohr (1501 Prüfstellen bzw. 3000 mm ÷ Feldlänge).

Achse anhalten je Punkt (t_move): 0,5 s (konservativ, Ampel im Sensorvergleich), 0,1 s und 0,05 s als Empfindlichkeit.

| Sensor | 0,5 s | 0,1 s | 0,05 s |
|---|---|---|---|
| LS-9030 / -M / -D, LS-9120M | 15,7 min | 5,7 min | 4,5 min |
| ODC2700-10 / -40 | 14,2 | 4,2 | 3,0 |
| ODC2520-46 / -090 | 13,2 | 3,2 | 2,0 |
| ODC1200 / 1201 (alle) | 12,5 | 2,5 | 1,3 |
| LSM-501S / -503S / -506S | 16,5 | 6,5 | 5,3 |
| LSM-512S / -516S / -6902H / -9506 | 20,5 | 10,5 | 9,3 |
| XLS13XY / XLS35XY (alle) | 37,5 | 27,5 | 26,3 |
| RF656.2D-40x50 / 25x35 / 15x20 / 8x10 | 1,9 / 2,8 / 4,8 / 9,7 | 1,5 / 2,2 / 3,9 / 7,7 | 1,5 / 2,1 / 3,7 / 7,5 |
| RF657.2D-60x80 / 40x50 / 25x35 / 15x20 | 2,2 / 3,5 / 5,0 / 8,8 | 2,0 / 3,1 / 4,4 / 7,8 | 1,9 / 3,0 / 4,4 / 7,6 |
| RF657R.2D (rund, alle) | 9–37 | 9–36 | 9–36 |

Zur Frage „LS-9030 unter 3 min“: Die Abtastrate (16.000/s) ist nicht der Engpass. Der Engpass ist die Wiederholgenauigkeit ±0,1 µm, die nur mit 2048-facher Mittelung gilt. Das braucht 0,128 s je Punkt. Bei 1501 Punkten sind das allein 192 s = 3,2 min, ohne jede Achsbewegung. Unter 3 min ist mit dieser Rep-Bedingung nicht möglich.

Zusätzlich zu prüfen: Mittelung über 2048 Werte bei drehendem Rohr mittelt die Breiten über den Winkel. Bei 1 Umdrehung je s würden so rund 46° gemittelt und die Form ginge verloren. Die Mittelung muss also winkelsynchron erfolgen oder das Rohr steht. Das ist eine Frage an Keyence: Rep bei kleinerer Mittelung (z. B. 256 oder 512) und bei Einzelmessung.

Hinweis Anforderung 2.4 (Mindestanforderung %GRR ≤ 10 %): ODC1200/1201 (Rep 40–140 µm) und ODC2520 (5 µm) erfüllen die Rep-Anforderung in allen drei Szenarien nicht. Sie scheiden damit unabhängig von der Taktzeit aus.

Dubletten: mws0ln0abedtb (XLS13XY), mws0lnc4mbahq (LSM-501S), mws0lnnai0kol (LSM-503S) wurden nach cockpit/daten/_Versionen/sensors_dubletten_2026-11-22.json verschoben, nicht gelöscht.

Offen: Wert für t_move (Entscheidung Janek, pv-ent-taktampel). Die Ampel im Sensorvergleich rechnet mit 0,5 s.
