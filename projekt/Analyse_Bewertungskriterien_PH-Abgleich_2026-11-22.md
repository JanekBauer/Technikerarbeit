# Bewertungskriterien: Abgleich mit dem Pflichtenheft und Vorschläge

Stand 22.11.2026 · KI (Claude Code) · Vorschlag, keine Festlegung. Maßgeblich ist PH V1.2 (Janek: V0.2), Datei `docs/archiv/3 Pflichtenheft/Pflichtenheft/V1.2_Bauer_TA_PH_V1.docx`, Anforderungsliste Kap. 3.

Hinweis zur Nummerierung: Im Cockpit stand „1.2 Werkstoff: Tantal“. Im PH V1.2 ist Tantal Nr. 1.5 (W). Die Cockpit-Liste `reqs.json` hat noch die alte Nummerierung (Pflichtenheft-Abgleich, Aufgabe pv-auf-reqs-nummern).

## 1. Aus dem Pflichtenheft: Festanforderungen (F) als K.-o.-Filter

Nicht gewichtet. Eine Variante, die eine F nicht erfüllt, wird nicht bewertet. Das prüft die Variantenauswahl bereits.

| PH | Festanforderung | Hinweis |
|---|---|---|
| 1.1 | Werkstoff NiTi / Edelstahl | |
| 1.2 | Rohrlänge 1000–3000 mm | |
| 1.3 | Außendurchmesser 1–6,5 mm | |
| 1.4 | Wandstärke n. a. | nicht Bestandteil |
| 2.1 | Zylinderform (Ø max − Ø min) je Rohrtyp | Toleranzwerte [?] |
| 2.2 | Außendurchmesser ±13 µm | |
| 2.5 | Ein Wert je Messpunkt, keine Mittelwerte | Frage pv-ent-mittelung |
| 3.1 | Keine plastische Verformung | |
| 3.2 | Keine Beschädigung, sauber und ölfrei | Kontaktwerkstoffe offen |
| 3.3 | Durchbiegung und Lage verfälschen das Ergebnis nicht | |
| 4.2 | Manuell einlegen, Messung und Auswertung automatisch | |

Mindestanforderung 2.3 (Messpunkte alle 2 mm): binär, also K.-o. und nicht gewichtet. Vorschlag, Janek entscheidet.

Zusätzlich aus deiner Vorgabe: Taktzeit über 5 min je Rohr ist ebenfalls K.-o. (4.1 unten).

## 2. Aus dem Pflichtenheft: als gewichtete Kriterien geeignet

Gewichtete Kriterien sind Mindest- und Wunschanforderungen, die sich abstufen lassen (mehr = besser).

| Nr. PH | Kriterium (Wortlaut für die Bewertung) | Art | Abstufung 0–4 |
|---|---|---|---|
| 2.4 | Reproduzierbarkeit %GRR – Reserve zur 10-%-Grenze | M | 4 = große Reserve, 0 = Grenze erreicht |
| 1.5 | Werkstoff Tantal | W | 4 = ohne Einschränkung, 0 = nicht prüfbar |
| 2.6 | Rauheit messen | W | 4 = vollständig, 0 = nicht möglich |
| 2.7 | Beschädigung oder Kontamination feststellen | W | 4 = vollständig, 0 = nicht möglich |
| 4.1 | Taktzeit pro Rohr (über 5 min entfällt) | W | 4 = unter 1 min, 0 = 5 min |
| 5.1 | Max. Platzbedarf L × B | W | 4 = kleinster, 0 = größter |

Bewusst ausgelassen: 2.3 (binär, siehe oben). Kosten werden über die wirtschaftliche Wertigkeit getrennt bewertet (Doppelzählung vermeiden).

Vorher beschlossen (Recherche vom 22.11., Analyse Bewertungskriterien): Herstellkosten nicht als Kriterium.

## 3. Eigene Vorschläge aus der Recherche (nicht aus dem PH)

Die Recherche bringt für Messmittel-Auswahl und Vorrichtungen wenig konkrete Kriterienkataloge. Die Vorschläge sind deshalb Einschätzungen, mit dem Belegstand dahinter.

| Vorschlag | Begründung | Beleg | Überschneidung |
|---|---|---|---|
| A. Kalibrier- und Nachweisaufwand gering (Rückführbarkeit, Kalibrierzertifikat, Zugriffsschutz) | Prüfmittel braucht Kalibrierzertifikat, Fälligkeit, Historie; Eingriffe müssen verhindert werden | Prüfmittelmanagement-Quellen (qz-online, testotis.de), Q1 | ISO 13485 (PH 5.3) |
| B. Umrüstaufwand für andere Rohr-Ø gering (1–6,5 mm) | Rüsten darf kein Problem sein; Verstellbarkeit der Auflagen | Hoffmann Group (Spanntechnik), Q1 | Festanforderung 1.3 (K.-o.) bleibt getrennt |
| C. Bedienaufwand beim Einlegen | Manuelles Einlegen ist F (4.2), die Güte des Einlegens aber nicht | keine Quelle; Schätzung | 4.2 (F) |
| D. Auflösung ≥ Faktor 10 zur Toleranz | Faustregel aus Prüfmittelliteratur | Q1, Quelle nicht gegengeprüft | K1 (%GRR-Reserve) |

Empfehlung: Vorschlag A und B aufnehmen (zusammen mit den sechs aus dem PH: acht Kriterien, im Rahmen der Obergrenze 10). Vorschlag C und D nicht, weil sie sich mit bestehenden Kriterien überschneiden oder nicht belegt sind.

## 4. Ergebnis für die Bewertungsmatrix

- **K.-o.-Filter (Variantenauswahl):** PH 1.1–1.4, 2.1, 2.2, 2.5, 3.1–3.3, 4.2 sowie Taktzeit über 5 min.
- **Gewichtet (Bewertung):** 2.4, 1.5, 2.6, 2.7, 4.1, 5.1 (aus dem PH) sowie Vorschlag A und B.
- **Nicht gewichtet:** 2.3 (binär), Kosten (separate wirtschaftliche Wertigkeit).

Gewichte und Punktskala bleiben offen (paarweiser Vergleich 2/1/0; Skala 0–4 nach VDI 2225 bisher).

## 5. Quellen

- Prüfmittelmanagement, qz-online: https://www.qz-online.de/a/grundlagenartikel/pruefmittelmanagement-und-kalibrierung-t-316751
- testotis.de, Fibel Prüfmittelmanagement und Kalibrierung: https://www.testotis.de/fileadmin/DE/downloads/download-center/de/fibeln-lexika/fibel-pruefmittelmanagement-und-kalibrierung.pdf
- Hoffmann Group, Effizientes Spannen: https://www.hoffmann-group.com/IT/de/hoi/e/1341264/
- kvp.de, Nutzwertanalyse: https://www.kvp.de/wissen/lexikon/nutzwertanalyse/
- Schulunterlage „Konstruktionsmethodik und -systematik“, Seiten 10 und 11.
- Pflichtenheft V1.2, Kap. 3 (Anforderungsliste) und Kap. 4 (Abgrenzung).
