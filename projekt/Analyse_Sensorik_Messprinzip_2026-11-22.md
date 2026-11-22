# Analyse: Sensor-Vorprüfung und Messprinzip (Arbeitspakete 2 und 3)

Stand 22.11.2026 · erstellt von KI (Claude Code) · reine Katalogprüfung, keine Messung · **keine Auswahl**. Janek entscheidet.

Kennzeichnung: **[H]** Herstellerangabe · **[PH]** Pflichtenheft V1.2 (Janek: V0.2) · **[R]** eigene Rechnung (KI) · **[S]** Schätzung (KI) · **[Q?]** Quelle nicht eindeutig

## 1. Verwendete Quellen (im Repo, selbst gelesen)

| Kürzel | Dokument | Stelle | Ablage |
|---|---|---|---|
| ME | Micro-Epsilon, Katalog optoCONTROL (DE) | S. 12–13 (ODC2700), S. 17 (ODC2520), S. 23 (ODC1200) | `docs/archiv/6 Recherche Messtechnik/Micro-Epsilon optoCONTROL – Katalog/` |
| KY | Keyence, Datenblatt LS-9030, Stand 2026/11/13 (Druckdatum Website) | S. 1, Fußnoten *2, *3 | `docs/archiv/6 Recherche Messtechnik/Keyence LS-9030 – Datenblatt/` |
| RF | RIFTEK, Handbuch 2D Optical Micrometers RF65x.2D, Rev. 1.0.2, 30.09.2025 | Kap. 6.1, PDF-S. 5–6 | `docs/archiv/6 Recherche Messtechnik/Riftek RF65x.2D – Handbuch …/` |

Neue Datenblätter konnten in dieser Sitzung **nicht** heruntergeladen werden, weil die Netzwerkregel der Umgebung die Herstellerseiten sperrt (siehe Abschnitt 5).

## 2. Was die Herstellerwerte wirklich aussagen

Alle Wiederholgenauigkeiten gelten für ein **ruhendes Messnormal mit starker Mittelung**, nicht für ein bewegtes Rohr:

| Sensor | Wiederholgenauigkeit [H] | Bedingung laut Fußnote [H] | Mittelungszeit [R] |
|---|---|---|---|
| Keyence LS-9030 / -M / -D | ±0,1 µm | ±2σ, Messnormal Ø 10 mm, Mitte Messbereich, 2048-fache Mittelung (KY *2) | 2048 / 16 000 s⁻¹ = **0,128 s** |
| Micro-Epsilon ODC2700-10 | ≤ 0,03 µm | 95-%-Konfidenz, Durchmesser, Mittelung 1024 Werte „über einen Zeitraum von 5 Minuten“, temperaturstabilisiert, 45 min Warmlauf (ME S. 13, Fn. 6) | 1024 / 15 000 s⁻¹ = **0,068 s** [Q?: Bedeutung „über 5 Minuten“ unklar] |
| Micro-Epsilon ODC2700-40 | ≤ 0,1 µm | wie oben | 0,068 s |
| Micro-Epsilon ODC2520-46 | ≤ 5 µm | gleitendes Mittel 32 Werte (ME S. 17) | – |
| Micro-Epsilon ODC1200 / 1201 | ≤ 40 … 140 µm | ±2σ, statisches Rauschen über 3 min (ME S. 23) | – |
| RIFTEK RF656.2D / RF657.2D | nicht angegeben | – (RF Kap. 6.1 nennt nur „Measurement error“) | – |

### 2.1 Umrechnung auf σ und Vergleich mit den Szenarien aus der Toleranz-Analyse [R]

Szenarien: A σ ≤ 0,43 µm, B σ ≤ 0,17 µm, C σ ≤ 0,42 µm (siehe `Analyse_Toleranz_GRR_2026-11-22.md`).

| Sensor | σ (mit Mittelung) | A | B | C |
|---|---|---|---|---|
| LS-9030 | 0,1 / 2 = 0,05 µm | ja | ja | ja |
| ODC2700-10 | ≈ 0,03 / 1,96 ≈ 0,015 µm [Annahme: Angabe ist ±-Halbbreite] | ja | ja | ja |
| ODC2700-40 | ≈ 0,05 µm [gleiche Annahme] | ja | ja | ja |
| ODC2520-46 | ≥ 2,5 µm | nein | nein | nein |
| ODC1200 / 1201 | ≥ 20 µm | nein | nein | nein |
| RIFTEK | keine Angabe | ? | ? | ? |

„ja“ heißt nur, dass der **Sensoranteil allein** unter der Grenze liegt, und zwar mit voller Mittelung am ruhenden Normal. Mechanik, Einlegen und Durchbiegung (Anf. 3.3) sind nicht enthalten.

**Korrektur zum Statusbericht vom 22.11. (Abschnitt 4.2):** Dort hieß es, die Keyence-Werte seien „vermutlich nicht ausreichend“. Begründet wurde das mit der Linearität von ±2 µm. Die Linearität gehört aber nicht zur %GRR, sondern zur Messabweichung (siehe Toleranz-Analyse, Punkt 5). Nach der Wiederholgenauigkeit liegen LS-9030 und ODC2700 **beide** im Rahmen, sofern die Mittelung zulässig ist.

### 2.2 Ohne Mittelung [S]

Nimmt man weißes Rauschen an, wächst σ ohne Mittelung mit √N. Das ist eine grobe Schätzung, kein Herstellerwert:

- LS-9030: 0,05 µm · √2048 ≈ **2,3 µm** je Einzelabtastung
- ODC2700-10: 0,015 µm · √1024 ≈ **0,5 µm** je Einzelabtastung

Für Szenario B (0,17 µm) bräuchte man danach etwa (2,3/0,17)² ≈ 180 Abtastungen beim LS-9030, also rund 11 ms. Beim ODC2700-10 wären es etwa (0,5/0,17)² ≈ 9 Abtastungen, unter 1 ms. **Die Werte zeigen nur die Größenordnung.** Belastbare Werte für die Einzelmessung muss der Hersteller liefern (Herstellerfragen, Entwurf).

**Entscheidend ist deshalb die Frage an den Betrieb:** Verbietet Anf. 2.5 „Mittelwerte unzulässig“ auch die zeitliche Mittelung im Sensor an **einem** Messpunkt? Oder meint sie nur, dass man nicht über mehrere Messpunkte bzw. die Rohrlänge mitteln darf? → Postfach `pv-ent-mittelung`.

### 2.3 Lage im Messfeld und Durchbiegung [H]

- ODC2700-10: Linearität ≤ 0,5 µm nur im Messfeld 1 (Z = ±0,5 mm in Strahlrichtung), ≤ 1 µm bei Z = ±1,5 mm, ≤ 2,5 µm bei Z = ±2,5 mm, gemessen mit 2-mm-Prüfstift (ME S. 13, Fn. 7).
- ODC2700-40: ≤ 1 µm bei Z = ±2,5 mm, ≤ 3 µm bei Z = ±10 mm (ME S. 13, Fn. 8).
- LS-9030: ±2 µm für ein **bewegtes** Normal Ø 10 mm im Feld 10 × 20 mm (KY *3). Laut Cockpit gilt für die LS-9030D ein Feld von 10 × 10 mm, außerhalb ±5 µm. Das stammt aus `sensors.json` und wurde hier nicht neu geprüft.
- Folgerung [R]: Die Rohrlage in Strahlrichtung geht direkt in die Messabweichung ein. Das betrifft vor allem Durchbiegung, Einlegen und Rundlauf beim Drehen. Daher ist Anf. 3.3 eine Anforderung an die Mechanik, nicht nur an den Sensor. Zahlen dazu gibt es erst, wenn das Auflagekonzept steht.
- Keine Angabe gibt es zu Ø 1 mm: Alle Wiederholgenauigkeiten gelten für Ø 10 mm (Keyence) bzw. ohne Ø-Angabe (Micro-Epsilon). → Herstellerfrage.

## 3. Messzeit bei 3 m Rohr und 2 mm Messpunktabstand [R]

Messpunkte: 3000 mm / 2 mm + 1 = **1501** (Anf. 1.2 max. Länge, Anf. 2.3).

| Sensor | Zeit je Messwert | 1 Winkellage | k Winkellagen |
|---|---|---|---|
| LS-9030, volle Mittelung | 0,128 s | 1501 · 0,128 s ≈ **192 s** | k · 192 s |
| ODC2700, volle Mittelung | 0,068 s | 1501 · 0,068 s ≈ **103 s** | k · 103 s |
| RF656.2D (65 Bilder/s) | 1/65 s | ≥ 23 s, wenn ein Bild ein Messpunkt ist | k · 23 s |
| RF657.2D (24 Bilder/s) | 1/24 s | ≥ 63 s, wenn ein Bild ein Messpunkt ist | k · 63 s |

Die reine Mess- bzw. Mittelungszeit enthält kein Verfahren, Drehen, Beschleunigen und kein Einlegen. Die Zahl k der Winkellagen ist offen, sie hängt an der Definition der Zylinderform. Zur Einordnung, ohne Bewertung: Laut PH misst der Lieferant bei NiTi 4 Punkte im Abstand von etwa 90° (PH Kap. 2, sinngemäß).

Bei durchgehender Bewegung und voller Mittelung wäre die Geschwindigkeit v = 2 mm / Mittelungszeit, also ≈ 16 mm/s (LS-9030) bzw. ≈ 29 mm/s (ODC2700). Jeder Messwert wäre dann über die vollen 2 mm verschmiert. Ob das mit Anf. 2.5 „je Messpunkt“ vereinbar ist, ist Teil der Frage `pv-ent-mittelung`.

## 4. Messprinzip: Entscheidungsgrundlage (Arbeitspaket 3)

### 4.1 Wichtige Klarstellung

Ein **2D-Schattenbild** (RIFTEK RF65x.2D) ist eine **Projektion aus einer Blickrichtung** über einen Längenabschnitt (RF Kap. 5: „shadow image is projected … onto the 2D CMOS sensor“). Es zeigt den Durchmesser in **einer** Richtung entlang einiger Millimeter Rohr. Ø max − Ø min über den **Umfang** eines Querschnitts liefert ein einzelnes Bild nicht. Auch das 2D-Prinzip braucht also mehrere Winkellagen.

„ThruBeam mit Drehung oder 2D-Bild“ ist deshalb **kein Entweder-oder** für die Zylinderform. Die Achsen der Entscheidung sind:

1. **Wie** werden mehrere Winkellagen erzeugt (Morphologischer Kasten TF3)?
2. **Wie viele** Längenpositionen erfasst ein Messvorgang? Ein Linienstrahl erfasst eine, ein 2D-Bild einen Abschnitt.

Der Statusbericht vom 22.11. (Abschnitt 4.2, „Zylinderform lässt sich aus einem Schattenbild direkt bestimmen“) wird hiermit korrigiert.

### 4.2 Vorfrage, die das Prinzip bestimmt

Gilt Ø max − Ø min **je Querschnitt** (Ovalität an jedem Messpunkt) oder **über das ganze Rohr** (alle Messwerte, dann einschließlich Konizität bzw. Verlauf über die Länge)? → Postfach `pv-ent-zylinderform-bezug`.

### 4.3 Vergleichskriterien (ohne Wertung)

| Kriterium | Woher | Was zu klären ist |
|---|---|---|
| Erfüllt die Definition nach 2.1 | PH 2.1, 5.3 | Anzahl Winkellagen k, je Querschnitt oder ganzes Rohr |
| %GRR-Anteil Sensor | PH 2.4 | Werte ohne Mittelung (Hersteller), Zulässigkeit der Mittelung |
| Messabweichung im zulässigen Lagefeld | PH 2.2, 3.3 | Z-Feld (ME Fn. 7/8, KY *3) gegen die erreichbare Rohrlage |
| Messzeit | PH 4.1 (W) | Abschnitt 3 dieser Analyse, k offen |
| Kontakt und Belastung durch Drehen oder Führen | PH 3.1, 3.2 | Kontaktwerkstoffe (offene Aufgabe), Spannkräfte |
| Mechanischer Aufwand (Drehachse, Schwenkkopf, Linearachse) | PH Kap. 3 Ergebnisse (Pneumatik-, Elektronikplan) | – |
| Datenlage beim Hersteller | – | RIFTEK ohne Wiederholgenauigkeit, alle ohne Angabe für Ø 1 mm |

Die Bewertung und die Wahl trifft Janek. → Postfach `pv-ent-messprinzip`.

## 5. Weitere Hersteller: Kandidaten ohne eingesehenes Datenblatt

Die folgenden Geräte decken nach Web-Suchergebnissen (22.11.2026) den Bereich Ø 1–6,5 mm ab und werden mit hoher Wiederholgenauigkeit beworben. **Datenblatt nicht eingesehen. Daher keine Zahlen und kein Eintrag in `sensors.json`.**

- **Mitutoyo Laser-Scan-Mikrometer LSM-501S / LSM-503S** (Laser-Scan-Prinzip mit rotierendem Spiegel; in TF5 des Morphologischen Kastens schon als Prinzip genannt). Gesuchte Quelle: Mitutoyo Bulletin „Laser Scan Micrometer“ (mitutoyo.com).
- **Aeroel (Marposs) XLS13XY**, zweiachsiges Laser-Mikrometer. In TF5 als „Aeroel – ungeprüft“ genannt. Gesuchte Quelle: Datenblatt XLS XY auf marposs.com. Laut Suchergebnis hängt die Wiederholgenauigkeit stark von der Mittelungszeit ab, Einzelmessung und Mittel über 1 s unterscheiden sich. Diese Aussage ist ungeprüft.

Gesperrte Hosts in dieser Sitzung: `www.mitutoyo.com`, `www.marposs.com`, `res.cloudinary.com`, `pdf.directindustry.com`. → Postfach `pv-auf-datenblaetter`.

## 6. Kurzfazit für Janek (Vorprüfung, keine Entscheidung)

1. ODC1200/1201 und ODC2520 scheiden nach der Wiederholgenauigkeit in allen drei Szenarien aus [H, R].
2. LS-9030 (alle Varianten) und ODC2700-10/-40 liegen mit voller Mittelung unter allen drei Grenzen. Ohne Mittelung ist der ODC2700-10 nach grober Schätzung deutlich besser [S].
3. Für RIFTEK fehlt die Wiederholgenauigkeit. Ohne Herstellerangabe ist keine %GRR-Aussage möglich.
4. Die Sensorwahl hängt an drei Klärungen: Toleranzwerte, Zulässigkeit der Mittelung, Definition der Zylinderform (je Querschnitt oder ganzes Rohr).

## Nachtrag 22.11.2026: Datenblätter Mitutoyo und Aeroel

Janek hat die Datenblätter geliefert. Sie liegen jetzt im Archiv und sind ausgewertet. Die Werte und Notizen stehen im Sensorvergleich unter Nr. 9 und 10. Abschnitt 5 ist damit erledigt. Die Einordnung gegen die Szenarien ist eine eigene Rechnung der KI: σ aus der ±2σ-Angabe des Herstellers.

| Sensor | Wiederholgenauigkeit [H] | Bedingung [H] | σ [R] | A / B / C |
|---|---|---|---|---|
| Mitutoyo LSM-501S | ±0,04 µm | ±2σ, Ø 10 mm, 0,32 s / 512-fach (Bulletin 2101, S. 12) | 0,02 µm | ja / ja / ja |
| Mitutoyo LSM-503S | ±0,11 µm | wie oben (S. 14) | 0,055 µm | ja / ja / ja |
| Mitutoyo LSM-6902H/6900 | ±0,03 µm (Ø 10 mm) | ±2σ, 1,28 s / 1024-fach (S. 8) | 0,015 µm | ja / ja / ja |
| Mitutoyo LSM-506S | ±0,36 µm | wie LSM-501S (S. 16) | 0,18 µm | ja / nein / ja |
| Aeroel XLS13XY/1500 (/A) | ±0,04 µm | T = 1 s, ±2σ (Datenblatt S. 4, Fn. 11) | 0,02 µm | ja / ja / ja |
| Aeroel XLS13XY/480 (/A) | ±0,15 µm | T = 1 s, ±2σ | 0,075 µm | ja / ja / ja |

Neu ist: Aeroel gibt als einziger Hersteller die **Einzelabtastung** an (Fn. 11). Für das XLS13XY/1500 sind das ±0,75 µm (±2σ) bei Ø ≤ 3 mm und ±1,5 µm bei Ø > 3 mm. Das ergibt σ ≈ 0,38 bzw. 0,75 µm. Diese Werte sind die erste Herstellerangabe zur Frage `pv-ent-mittelung`. Ohne Mittelung liegt danach auch das XLS13XY/1500 über Szenario B.

## Nachtrag 22.11.2026 (2): Drehung des Rohres und Schattenbild

Frage: Ergibt ein 2D-Schattenbild bei 360°-Drehung des Rohres die Zylinderform?

**Antwort (Physik, eigene Überlegung):** Das Schattenbild liefert pro Drehwinkel φ die Breite des Rohres in der Messrichtung. Ø max(φ) − Ø min(φ) je Längenposition ist die Zylinderform nach PH-Definition (PH Kap. 5.3). Die Breite in fester Richtung ändert sich bei einem runden Querschnitt nicht, wenn die Rohrachse quer zum Strahl wandert. Grenzen:

1. Versatz entlang der optischen Achse verändert den Messfehler (RIFTEK Handbuch Kap. 6.1: Fehler nur gültig bis ±1 mm bzw. ±5 mm entlang der Achse, je Modell).
2. Winkelauflösung = Bildrate / Drehzahl. Bei 3 s je Umdrehung (Schätzung): RF656.2D ~1,8°, RF657.2D ~5°, RF657R.2D ~30° (Bilder 65/24/4 je s, RIFTEK Kap. 6.1).
3. Keine Helixabtastung (Cockpit, Entscheidung Baidinger 13.11.): Drehung nur an festen Stationen. 2D-Sensor: ca. 150–200 Stationen je 3-m-Rohr, grob 9–12 min je Rohr (Schätzung). 1D-Sensor (ODC2700): jeder der 1501 Punkte eine Station, grob 75 min je Rohr (Schätzung).
4. Dynamik beim Drehen dünner Nitinol-Rohre (Schwingung, Durchbiegung) und offene Kontaktstellen (PH 3.2).

**Korrektur zu Abschnitt 3 (Messzeit):** Die Zeiten dort setzen ein Bild je Messpunkt voraus. Für den 2D-Sensor trifft das nicht zu (viele Punkte je Bild). Ohne Drehung an den Stationen fehlt außerdem die Zeit für das Drehen. Die Zahlen gelten nur als Messzeit je Punkt; die Gesamtzeit ist nach Abschnitt 'Nachtrag (2)' neu zu rechnen.

**Offene Frage:** Zylinderform nach PH (Ø max − Ø min) oder nach ISO 1101 (Abweichung vom Bestzylinder). Siehe pv-ent-zylinderform-bezug.

## Nachtrag 22.11.2026 (3): Bildrate und Winkelschritt (Drehung, keine Helix)

Ausgangslage: Keine Helixabtastung (Anforderung: Zylinderform je Messpunkt alle 2 mm innerhalb der Toleranz). Frage: Welche Bildrate ist nötig, damit die Winkelschritte nicht zu groß werden?

**Winkelschritt aus der Formordnung (eigene Rechnung):** Annahme: Oberwelle n mit Amplitude A = 10 µm; Fehler von Max/Min durch Abtastung höchstens 1 µm (10 % einer Toleranz von 10 µm). Fehler ≈ A·(1 − cos(n·Δφ/2)) ≤ 1 µm ⇒ Δφ ≤ 51,6°/n.
n = 2: 25,8° · n = 3: 17,2° · n = 6: 8,6° · n = 10: 5,2° · n = 12: 4,3° · n = 20: 2,6°.
Offen: welche Oberwellen real auftreten (QM / Baidinger).

**Bildrate bei fester Frequenz (eigene Rechnung):** f = 360° / (Δφ · T_Umdrehung).
- Δφ 5°: T = 3 s → 24/s; T = 6 s → 12/s
- Δφ 2,5°: T = 3 s → 48/s; T = 6 s → 24/s
- Δφ 1,8°: T = 3 s → 67/s; T = 6 s → 33/s

**Korrektur zur Bildrate RF656.2D:** Mit Controller SuM sind 50 Messungen/s die Grenze, nicht 65/s (RIFTEK Kap. 6.1 und Sensor-Eintrag). Der RF657.2D ist mit 24/s begrenzt, der RF657R.2D mit 4/s.

**Auslösung über den Drehgeber:** Der RIFTEK-Sensor hat 1 Synchronisationseingang (Kap. 6.1). Bei Auslösung je Winkelschritt hängt der Schritt nicht von der Bildrate ab. Limit: Verarbeitung des Controllers. Bei SuM (50/s) und 3 s je Umdrehung ist der kleinste Schritt rund 2,4°.

**Stationszeit (Schätzung, ohne Verfahren, 150–200 Stationen je 3-m-Rohr):**
- 3 s je Umdrehung: ca. 10–12 min je Rohr; Schritt nur ab ca. 2,4° möglich
- 6 s je Umdrehung, 2,5°: ca. 20–25 min je Rohr
- 6 s je Umdrehung, 5°: ca. 15–20 min je Rohr; nur bis Oberwelle ca. 10

**Bewegungsunschärfe:** Belichtung RF657 15 µs, RF656 100 µs. An den Silhouettenkanten verläuft die Bewegung parallel zur Kante; Unschärfe dort voraussichtlich gering. Am Aufbau zu prüfen.

**Empfehlung (Analyse, keine Festlegung):** Zuerst Oberwellen klären. Bis n = 6 genügen 5°-Schritte; darüber 2,5° oder feiner. Der RF657.2D ist nur mit Drehgeber-Auslösung sinnvoll; der RF656.2D mit SuM ist knapp.
