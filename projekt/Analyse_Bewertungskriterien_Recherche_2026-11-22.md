# Recherche und Überarbeitung: Bewertungskriterien für die Variantenauswahl

Stand 22.11.2026 · erstellt von KI (Claude Code) · **Vorschlag, keine Festlegung**. Gewichtung und Auswahl macht Janek.

Kennzeichnung der Belege: **[H]** Herstellerangabe oder Normbezug, **[Q2]** durch zweite unabhängige Quelle bestätigt, **[Q1]** nur eine Quelle gefunden, **[PH]** Pflichtenheft V1.2 (Janek: V0.2), **[S]** Schätzung der KI.

## 1. Was die Recherche belegt

| Aussage | Quelle | Beleg |
|---|---|---|
| K.-o.-Kriterien sind Filter. Eine Option, die sie nicht erfüllt, wird nicht bewertet. K.-o.-Kriterien gehören nicht in die Gewichtung. | business-wissen.de (Beispiel Nutzwertanalyse); Lernarena (IHK-Material) | [Q2] |
| Bewertungskriterien müssen eindeutig und überschneidungsfrei definiert sein. | Schulungs-/Praxisseite zur Nutzwertanalyse (Quelle wie oben, Abschnitt Konstruktion) | [Q1] |
| Paarweiser Vergleich mit 2 / 1 / 0 Punkten; bei fünf Kriterien zehn Paare. | Nutzwert-Quellen oben; die Schulunterlage nutzt dasselbe Verfahren (Seite 11) | [Q2] |
| Teilnutzen = Gewicht × Erfüllungsgrad, dann summieren. | Nutzwert-Quellen oben | [Q2] |
| Forderungen (Muss) von Wünschen (Soll) trennen; Festanforderungen vorab sortieren. | Lehrveranstaltungszusammenfassung zur Anforderungsliste (rwu.de) | [Q1] |
| Auflösung des Messgeräts sollte kleiner als 5 % der Toleranz sein. | VDA-QMC-Pressebericht 2011 zu VDA 5 (vda-qmc.de) | [Q1] |
| Messunsicherheit ist ein zentrales Auswahlkriterium; dazu Messgeschwindigkeit, Auflösung. | Wächter der Produktqualität, QZ 03/2021; Hexagon-Fachbeitrag zur KMG-Auswahl | [Q2] |
| Berührungslose Messung, wenn Werkstücke nicht berührt werden dürfen. Kontaktmessung ist meist günstiger. | Hexagon; industrial-production.de | [Q2] |
| Kosten sind bei der Auswahl das letzte Kriterium, nicht das erste. | Hexagon | [Q1] |

### 1.1 Nicht bestätigt, daher nicht verwendet

- **Verhältnis Messunsicherheit zu Toleranz 1:5.** Die Suche fand nur eine Nennung in einem Hexagon-Text, keine Norm. Das ist ein Richtwert aus der Praxis, nicht gesichert. Ich übernehme ihn nicht als Kriterium.
- **Wert „Ø Messbereich 1–6,5 mm“ als Bewertungskriterium.** Das ist eine Festanforderung (PH 1.3) und gehört in die K.-o.-Prüfung, nicht in die Gewichtung.
- **Konkrete Kriterien aus VDI 2225 Blatt 1/2 und Pahl/Beitz.** Die Originalquellen sind aus dieser Umgebung nicht erreichbar (Download gesperrt). Die Methode (technische Wertigkeit x, wirtschaftliche Wertigkeit y, Ideal = 1) stimmt mit der Schulunterlage und mit den Suchtreffern überein. Die Kriterienliste aus der Richtlinie konnte ich nicht prüfen.

### 1.2 Was offen bleibt

- Die beiden Richtlinientexte (VDI 2225 Blatt 3 bzw. Bachelorarbeit HAW Hamburg zu optischen Messsystemen) konnte ich nicht lesen. Wenn du die PDFs ins Archiv legst, werte ich sie aus.
- Die Recherche liefert allgemeine Methodik. **Die konkreten Kriterien ergeben sich aus deinem Pflichtenheft.** Das ist im Vergleich wichtiger als jede Online-Liste.

## 2. Festanforderungen als K.-o.-Filter (PH V1.2, Anforderungsliste)

Diese Punkte entscheiden vorab, ob eine Variante überhaupt bewertet wird. Sie werden **nicht** gewichtet. Die Variantenauswahl prüft sie schon je Variante.

| PH | Festanforderung |
|---|---|
| 1.1 | Werkstoff NiTi / Edelstahl |
| 1.2 | Rohrlänge 1000–3000 mm |
| 1.3 | Außendurchmesser 1–6,5 mm |
| 2.1 | Zylinderform (Ø max − Ø min) erfassbar |
| 2.2 | Außendurchmesser ±13 µm erfassbar |
| 2.5 | Ein Wert je Messpunkt, keine Mittelwerte |
| 3.1 | Keine plastische Verformung beim Messen |
| 3.2 | Keine Beschädigung, sauber und ölfrei |
| 3.3 | Durchbiegung und Lage verfälschen das Ergebnis nicht |
| 4.2 | Rohr manuell einlegen, Messung und Auswertung automatisch |

## 3. Vorschlag für die Bewertungsmatrix

Regeln: 5 bis 10 Kriterien (Aufwand), **positiv formuliert** (mehr Punkte = besser), eindeutig und ohne Überschneidung. Jedes Kriterium stammt aus einer M- oder W-Anforderung des Pflichtenhefts und ist mit der Nummer verknüpft.

| Nr. | Kriterium (positiv) | Quelle PH | Art | Belegstatus | Bewertung 0–4 (Vorschlag) |
|---|---|---|---|---|---|
| K1 | Reserve bei der Wiederholgenauigkeit zur %GRR-Grenze | 2.4 | M | [H][Q2] | 4 = mehr als 50 % Reserve, 0 = Grenze gerade erreicht oder überschritten |
| K2 | Eignung für die Messpunktdichte (2 mm über die Länge) | 2.3 | M | [Q1] | 4 = Messrate reicht für 1500 Punkte je Winkellage mit Reserve, 0 = nicht erreichbar |
| K3 | Reserve bei Lageabweichung im Messfeld | 3.3 | F (Mechanik) | [H][S] | 4 = große Reserve im Lagefeld, 0 = Lagefeld schon bei Solllage überschritten |
| K4 | Messgeschwindigkeit je Rohr (Taktzeit) | 4.1 | W | [Q2] | 4 = kürzeste Messzeit, 0 = längste |
| K5 | Einfache Integration in die Auswertung und Steuerung | 4.2 | F (Auswertung), W (Aufwand) | [Q1] | 4 = Schnittstelle vorhanden, Auswertung ohne Zusatzsoftware, 0 = Zusatzaufwand |
| K6 | Geringer Platzbedarf | 5.1 | W | [PH] | 4 = kleinster Platzbedarf, 0 = größter |
| K7 | Eignung für Tantal (zusätzlich zur Prüfung) | 1.5 | W | [PH] | 4 = geeignet ohne Anpassung, 0 = nicht geeignet |
| K8 | Zusatzprüfung Rauheit und Oberfläche möglich | 2.6, 2.7 | W | [PH] | 4 = beide möglich, 0 = nicht möglich |

**Bewusst nicht als Kriterium:**
- **Herstellkosten.** Sie werden in der Bewertung getrennt über die wirtschaftliche Wertigkeit y bewertet (Kosten ≤ H_zul). Als Kriterium würden sie doppelt zählen. Das ist eine Überschneidung, die die Quellen ausdrücklich vermeiden.
- **Wandstärke, Konzentrizität, Geradheit.** Sind laut PH Kap. 4 ausgeschlossen.

**Hinweis zu K1:** Die Reserve ist eine eigene Rechnung auf Basis der Szenarien (Analyse Toleranz/%GRR). Der Wert hängt davon ab, welches Szenario gilt. Solange die Toleranzen offen sind, ist K1 nur als Richtung brauchbar.

**Bewertungsskala:** 0 bis 4 wie bisher (VDI-2225-Auswertung). Die Schulunterlage nutzt 0 bis 10. Die Umstellung ist eine Entscheidung für Janek.

## 4. Gewichtung

Keine Gewichte vorgegeben. Der paarweise Vergleich (2 / 1 / 0) läuft in der Bewertungsmatrix. Mit acht Kriterien sind es 28 Paare. Das ist viel für eine Sitzung, deshalb evtl. auf sechs Kriterien kürzen: K5 und K8 sind die schwächsten und könnten in K3 bzw. K4 aufgehen. Entscheidung für Janek.

## 5. Abgleich mit dem bisherigen Vorschlag

Der Vorschlag `pv-daten-eval` (Postfach, Status neu) enthält die Kriterien 2.3, 2.4, 2.6, 2.7, 4.1, 5.1, 1.5 ohne Reihenfolgeprüfung. Die Kriterien 2.6/2.7 bleiben als K8 erhalten. Neu sind K3 (Lageabweichung), K5 (Integration) und K1 als Reserve statt Ja/Nein. **Der bisherige Vorschlag sollte durch diesen ersetzt werden.**

## 6. Quellen

- business-wissen.de, „Beispiel für eine Nutzwertanalyse“ — https://www.business-wissen.de/hb/beispiel-fuer-eine-nutzwertanalyse/
- Lernarena, „Nutzwertanalyse: Beispiele, Kriterien und Übungen“ — https://lernarena.app/lernen/nutzwertanalyse
- Wächter der Produktqualität, QZ 03/2021 — https://res.cloudinary.com/sternwald-systems/raw/upload/v1/hugoprd/ARTIKEL_ATTACH/0028EE82_D0166BAF21FF/d95da1acb02444907c5c64e02bdd23d1956d8044/W_chter der  Produktqualit_t - QZ 03 2021.pdf
- Hexagon, „Die Wahl des richtigen KMG“ — https://hexagon.com/de/resources/resource-library/how-select-cmm
- Hexagon, „Scannen oder nicht scannen“ — https://hexagon.com/de/resources/resource-library/should-you-scan
- industrial-production.de, „Messen und Prüfen – Prüfsysteme“ — https://www.industrial-production.de/sensorik---messtechnik/messen-und-pruefen---pruefsysteme---wer--die-wahl-hat---.htm
- VDA-QMC, Pressebericht 2011 „Messsystem und Messprozess sind zweierlei“ — https://vda-qmc.de/wp-content/uploads/2024/02/Pressebericht-2011-QZ-Messsystem-und-Messprozess-sind-zweierlei-Ueberarbeiteter-VDA-Band-5-–-Pruefprozesseignung.pdf
- rwu.de, Zusammenfassung Anforderungsliste — https://elearning.rwu.de/pluginfile.php/230667/mod_resource/content/5/Zusammenfassung%20Anforderungsliste.pdf
- Schulunterlage „Konstruktionsmethodik und -systematik“, Seiten 10 und 11 (Carl-Benz-Schule, Stand 23.09.2025), von Janek bereitgestellt.
- Nicht erreichbar: VDI 2225 Blatt 3 (ressource-deutschland.de), HAW-Hamburg-Bachelorarbeit (reposit.haw-hamburg.de).
