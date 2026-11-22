# Bewertung der Konzepte A bis D (Vorschlag der KI)

Stand 22.11.2026 · KI (Claude Code) · **Vorschlag, keine Festlegung**. Die Bewertung entscheidet der Betrieb. Punktskala 0 = unbefriedigend … 4 = ideal (wie Bewertung im Cockpit).

Grundlage: Konzepte aus `cockpit/daten/tools.json` (Morph. Kasten, Repo-Stand 22.11.2026). Zuordnung im Repo: „Konzept 100“ → A, B → B, C → C, D → D (Annahme, bitte bestätigen).

## 1. Was sich zwischen den Konzepten unterscheidet

| Teilfunktion | A (Konzept 100) | B | C | D |
|---|---|---|---|---|
| Auflage und Ausrichtung | Rollenpaar (Kunststoff oder Keramik) | Rollenpaar | festes V-Prisma (Kunststoff) | festes V-Prisma |
| Halten gegen Bewegung | beide Enden gefasst, Antrieb und Gegenseite | Spannzange/Futter mit Kunststoff an einem Ende | beide Enden gefasst | Spannzange an einem Ende |
| Längenposition erfassen | Geber im Antriebsmotor | direktes Längenmesssystem (Magnetband/Glasmaßstab) | Geber im Antriebsmotor | direktes Längenmesssystem |

Gleich in allen Konzepten: Einlegen von oben, Nullpunkt am festen Endanschlag, Drehung des Rohres während der Messung, Sensor fährt die Länge ab, Entnahme in zwei Ablagen. Der Sensor ist in keinem Konzept festgelegt. Die Kriterien Tantal, Rauheit, Beschädigung, Taktzeit und Platzbedarf hängen zu einem großen Teil am Sensor, deshalb sind dort die Punkte für alle gleich.

## 2. Punkte (Vorschlag)

| Kriterium (Gewicht aus Cockpit-Screenshot) | A | B | C | D | Begründung |
|---|---|---|---|---|---|
| K1 1.5 Werkstoff Tantal (10 %) | 2 | 3 | 2 | 3 | Kunststoffeinsatz am Halteende schont das weiche Tantal; beide Enden gefasst eher nicht. Schätzung. |
| K2 2.4 %GRR-Reserve (33,3 %) | 2 | 3 | 2 | 3 | Direktes Längenmesssystem ohne Schlupf (B, D). Radial stabiler (V-Prisma, C, D) bei Lage und Durchbiegung. Schätzung. |
| K3 2.6 Rauheit messen (10 %) | 0 | 0 | 0 | 0 | Kein Konzept sieht eine Rauheitsmessung vor. |
| K4 2.7 Beschädigung/Kontamination feststellen (16,7 %) | 0 | 0 | 0 | 0 | Kein Konzept erkennt Beschädigung. Nur durch Sensorerweiterung möglich. |
| K5 4.1 Taktzeit (26,7 %) | 2 | 2 | 2 | 2 | Die Konzepte unterscheiden sich nicht im Takt; bestimmend sind Achsstopp und Sensor. |
| K6 5.1 Platzbedarf (3,3 %) | 2 | 3 | 2 | 3 | Ein Halteende braucht weniger Platz als zwei. |

Gewichtete Erfüllung (Gewichte aus dem Screenshot, Summe Punkte × Gewicht ÷ 4):

| | A | B | C | D |
|---|---|---|---|---|
| Nutzwert (0–4) | 1,47 | 1,93 | 1,47 | 1,93 |
| Erfüllung | 37 % | 48 % | 37 % | 48 % |

## 3. Warnhinweise zu Festanforderungen (K.-o.-Prüfung, nicht Punkte)

- **C und D (V-Prisma mit drehendem Rohr):** Das Rohr dreht durchgehend, die Auflage ist fest. Gleitkontakt kann Kratzer und Abrieb erzeugen. Das betrifft 3.2 (F, keine Beschädigung, sauber) und 2.7. Wenn das so ist, scheiden C und D aus.
- **B und D (Spannzange an einem Ende):** Die Morph-Notiz selbst nennt „Spannkraft ovalisiert“. Das betrifft 3.1 (F, keine plastische Verformung) und 2.1 (Zylinderform). Wenn die Spannkraft das Rohr verformt, scheiden B und D aus.
- **A und C (Enden gefasst, Geber im Motor):** Ein Antrieb mit Schlupf verfälscht die Längenposition. Das wirkt auf 3.3 und 2.3 (Messpunkte alle 2 mm). Das ist nachzuprüfen.

Die Punkte sind deshalb nur bedingt belastbar. Die Warnhinweise sind wichtiger als die Summe.

## 4. Offene Punkte für die Bewertung

- Bestätigung der Zuordnung Konzept 100 → A.
- Ob Gleitkontakt am drehenden Rohr zulässig ist (Kontaktwerkstoffe, offene Aufgabe).
- Ob die Spannkraft das Rohr ovalisiert (Festigkeitsnachweis, PH 3.1).
- Gewichte und Punktskala bleiben beim Betrieb (paarweiser Vergleich).
