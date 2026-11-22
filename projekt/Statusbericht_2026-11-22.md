# Statusbericht Technikerarbeit, Stand 22.11.2026

Grundlage: Pflichtenheft V8.7 final (MS 1) und Cockpit-Daten in `cockpit/daten/` (Stand main nach `a3c2efd`).
Hinweis: „V02 Bauer-TA-PH-V1“ wurde als V1.2 gelesen; die aktuelle Fassung ist V8.7. Die Unterschiede zwischen V1.2 und V8.7 sind hier nicht aufgeführt.
Vertraulich: Rohrspezifikationen und interne Prüfanweisung werden nur sinngemäß verwendet (PH Kap. 5.2).

## 1. Ziel und Abgabezustand (laut PH V8.7)

**Ziel:** Neukonzeption und CAD-Konstruktion einer automatisierten Messmaschine im Wareneingang für Rundheit (Ovalität) und Maßhaltigkeit von Nitinol-, Edelstahl- und Tantal-Rohren bis 3 m Länge.

**Zu übergebende Ergebnisse (PH Kap. 2):**
1. CAD-Baugruppe der Messanlage (3D)
2. Fertigungszeichnungen
3. Stückliste (Eigenfertigungs- und Kaufteile)
4. Angebote für die Kaufteile
5. Beschreibung des Messprozesses inkl. Sensorkonzept
6. Funktionsbeschreibung der Anlage
7. Technische Dokumentation inkl. Pneumatikplan und Elektronikplan
8. Anforderungsliste

**Abgrenzung:** kein Bau, keine Inbetriebnahme, keine Steuerungsprogrammierung, keine MFU am realen System, kein Einlegeautomat (Einlegen manuell), keine Wandstärke/Konzentrizität/Geradheit.

**Termine laut PH (Kap. 5.2):** Kick-off 23.10.2026 (erledigt), PH-Freigabe 06.11.2026, Variantenauswahl 04.12.2026, Konstruktionsfreigabe 22.01.2027, Übergabe/Projektabschluss 26.02.2027.

## 2. Stand Anforderungen

Die Anforderungsliste ist fast vollständig bestätigt (`reqs.json`: 17 bestätigt, 1 offen).

| Nr. | Anforderung | Stand |
|---|---|---|
| 1.1–1.5 | Werkstoff, Länge 1–3 m, Ø 1–6,5 mm | bestätigt |
| 2.1 | Ovalität NiTi 0,010 mm, Edelstahl 0,025 mm | bestätigt |
| 2.2 | Ø-Toleranz ±13 µm | bestätigt |
| 2.3 | Messpunktabstand 2 mm | bestätigt |
| 2.4 | %GRR ≤ 10 % (AIAG MSA) | bestätigt |
| 2.5 | Jeder Messwert in der Toleranz, keine Mittelwerte | bestätigt |
| 3.1–3.3 | Keine plastische Verformung, sauber, Durchbiegung ohne Einfluss | bestätigt |
| 4.1 | Taktzeit pro Rohr | **offen** (Entscheidung „Taktzeit pro Rohr“ ist für 04.12. eingetragen) |
| 4.2 | Manuell einlegen, Messen und Auswerten automatisch | bestätigt |
| 5.1 | Platzbedarf | bestätigt im Cockpit, im PH noch „offen“ → angleichen |

**Auffällig:** Die Ovalitätsanforderung (10 µm) ist sehr eng. Bei %GRR ≤ 10 % darf die Messsystemstreuung über 6σ nur etwa 1 µm betragen (σ ≈ 0,17 µm). Das ist die zentrale technische Frage der Messtechnik.

## 3. Stand der Arbeitspakete (`packages.json`)

| Paket | Ampel | Stand |
|---|---|---|
| Aufgabenstellung | gelb | AS V4.2 an PH V8.7 angeglichen; offen: KI-Formulierung (W8), FSL-Prüfung (W5), Unterschriften bis 30.11. |
| Pflichtenheft | gelb | V8.7 final für MS 1; offen: Freigabe + Unterschrift (20.11. ist überschritten), Termin im PH anpassen, 5 Formfehler, W10–W14 |
| Projektplan (Rillsoft) | rot | seit 16.10. unverändert |
| Lösungsansätze (PDF für MS 1) | gelb | 1 Idee; Skizze, Denkfragen, 2. Variante, weitere Hersteller fehlen |
| MS-1-Termin + Vor-Ort-Termin | rot | nicht angefragt (Stand 06.11.) |
| Messtechnik-Recherche | rot | **nur Keyence betrachtet**; Herstellervergleich dringend |
| Spann- und Handhabungskonzept | gelb | Morphologischer Kasten V2 (12.11.): 13 Teilfunktionen + 3 Querschnittsfunktionen; Ideen überwiegend KI-Vorschläge; eigene Ideen nur bei TF1/TF3/TF4; keine Gesamtvarianten |
| Variantenbewertung | grau | nicht begonnen |
| CAD-Konstruktion | grau | nicht begonnen |
| Messprozess, Sensorintegration | grau | nach Variantenwahl |
| Dokumentation | grau | Gliederung (9 Kapitel) als Idee; Doku-Speicher leer |
| Präsentation | grau | ab Mai 2027 |

**Ergebnisse, die noch komplett fehlen:** CAD, Fertigungszeichnungen, Stückliste, Angebote (nur Anfrage-Aufgabe offen), Funktionsbeschreibung, Pneumatik- und Elektronikplan.

## 4. Sensorik: Stand und erste Vorprüfung

Im Cockpit sind 26 Sensorvarianten erfasst (Keyence 4, Micro-Epsilon 11, RIFTEK 11). Eine Vorprüfung nur anhand der Katalogwerte, ohne Messung:

- **Laser-Mikrometer (Micro-Epsilon ODC2520, ODC1200):** Wiederholgenauigkeit 5 µm bis 140 µm. Für die 10-µm-Ovalität zu grob → voraussichtlich ausscheiden.
- **Lichtband-Mikrometer Keyence LS-9030 / LS-9030M:** Wiederholgenauigkeit ±0,1 µm (2σ), Linearität ±2 µm, Ø 0,3–30 mm. Die Angabe gilt für ein ruhendes Normal Ø 10 mm; bewegt sind es ±2 µm. Für Ø 1–6,5 mm plausibel, muss beim Hersteller bestätigt werden.
- **LED-Mikrometer Micro-Epsilon ODC2700-10 / -40:** Wiederholgenauigkeit ≤ 0,03 bzw. ≤ 0,1 µm, Linearität ≤ 0,5 bzw. ≤ 1 µm. Auf dem Papier die präzisesten Kandidaten. Messbereich 10 mm passt zu 6,5 mm.
- **RIFTEK RF656.2D / RF657.2D (2D-Schattenbild):** Linearität ±0,8 bis ±4,5 µm, aber Wiederholgenauigkeit im Handbuch nicht angegeben. Vorteil: Ovalität lässt sich aus einem Schattenbild direkt bestimmen, ohne Drehung. Die Abtastrate ist mit 24–65 Messungen/s begrenzt; das passt zu einer Mess-Taktzeit, muss aber geprüft werden.

**Offene Frage für den Betrieb:** Herstellerangaben für Ø 1–6,5 mm (Keyence hat die 40-mm-Angabe bei LS-9120M ausdrücklich nur für Ø 40 mm gemacht) und die Wiederholgenauigkeit bei einem Rohr statt eines Normals.

## 5. Offene Fragen und Entscheidungen

Aus `decisions`/`tasks` (Stand offen):

- 27.11.: **MS 1 nachfragen** (Entscheidung), **Zylinderform**, **Variantenauswahl: Datum im PH klären**, **Projektabschluss: Datum im PH klären**
- 27.11.: Aufgabe **Bilder Stents und Marker holen** (Hr. Baidinger)
- 04.12.: **PH-Freigabe: Datum im PH klären**, **Taktzeit pro Rohr**
- 04.12.: Aufgabe **Zulässige Kontaktstellen und Kontaktwerkstoffe** (Auflage/Führung, PH Anf. 3.2)
- 27.01.: Bilder/Werte für die Präsentation
- 19.03.: Gliederung TA-Doku abstimmen

**Terminwidersprüche PH ↔ Cockpit:** Variantenauswahl (PH 04.12. / Cockpit 11.12.), Konstruktionsfreigabe (PH 22.01. / Cockpit 15.01.), Projektabschluss (PH 26.02. / Cockpit 05.03. bzw. 19.03.). Diese sind im Postfach als Entscheidungen angelegt.

## 6. Was du jetzt schon erarbeiten kannst

Priorisiert nach Wirkung auf die Abgabe:

1. **Sensor-Shortlist eingrenzen (hoch).** Die Vorprüfung oben in eine Tabelle übernehmen, Kriterien aus den Anforderungen 2.1–2.4 nehmen. Offene Herstellerfragen formulieren. Das ist die Grundlage für die „Angebote“ und das Messprozess-Kapitel.
2. **Messprinzip klären (hoch).** Ob Ovalität über mehrere Winkel aus Einzelmessungen oder direkt aus einem 2D-Bild kommt, entscheidet die Sensorauswahl. Das ist deine fachliche Entscheidung; sie sollte vor der Sensorfrage stehen.
3. **Morphologischen Kasten vervollständigen (hoch, aber mit Vorsicht).** Die Teilfunktionen TF2, TF5 bis TF13 sind nur mit KI-Vorschlägen gefüllt. Die Formatvorlage erlaubt KI nur zur sprachlichen Optimierung. Eigene Ideen müssen von dir kommen; ich kann die Lücken aufzeigen und Kriterien vorschlagen, nicht die Lösungen schreiben.
4. **Bewertungskriterien für die Variantenauswahl (mittel).** Die Gewichtung aus den Festanforderungen (F) und Mindestanforderungen (M) ist vorbereitbar. Die Vorlage „eval“ im Cockpit ist noch leer.
5. **Herstellerfragen und Angebotsanfragen (mittel, aber außen wirksam).** Der Entwurf kann vorbereitet werden; die Anfrage geht von dir raus.
6. **Gliederung der Dokumentation umsetzen (mittel).** Kapitel 2 (Problemstellung) kann aus dem PH sinngemäß entstehen; Janek schreibt, nicht die KI.
7. **Termine im PH angleichen (niedrig, aber bald).** Die drei Terminwidersprüche und die Taktzeit-Entscheidung klären; danach die PH-Freigabe-Unterschrift.
8. **Platzbedarf (Anf. 5.1) aus dem Betrieb holen.** Im PH steht „offen“; im Cockpit ist die Anforderung bestätigt.

**Nicht sinnvoll jetzt:** CAD-Konstruktion, Fertigungszeichnungen, Stückliste (hängt an der Variantenwahl am 04.12.).

## 7. Risiken

- **Termin PH-Freigabe:** Unterschrift war bis 20.11. geplant und ist überschritten; Festlegung ist 27.11. bzw. 04.12. Die Entscheidung dazu fehlt noch.
- **Messtechnik:** Ohne Herstellervergleich fehlt die Grundlage für die Variantenauswahl am 04.12.
- **KI-Anteil:** Teile des morphologischen Kastens und der AS-Texte stammen von KI. Das muss im KI-Logbuch dokumentiert sein (kilog, `fach: true`) und in der Dokumentation ausgewiesen werden.
- **Projektplan:** seit 16.10. nicht aktualisiert (rot).
