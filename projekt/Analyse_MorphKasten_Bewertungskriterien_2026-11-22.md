# Analyse: Lücken im Morphologischen Kasten und Bewertungskriterien (Arbeitspakete 4 und 5)

Stand 22.11.2026 · erstellt von KI (Claude Code) · **keine Lösungsideen**, nur Lücken, Abhängigkeiten und Kriterien. Die Ideen und die Gewichtung sind Janeks Sache.

Quellen: `cockpit/daten/tools.json` (Eintrag `morph`, Stand 19.11.2026; Eintrag `eval`, leer), PH V1.2 (Janek: V0.2), Kap. 3 Anforderungsliste, Kap. 4 Abgrenzung.

## 1. Stand des Kastens (gezählt aus `tools.json`)

| TF | Teilfunktion | Ideen | als KI-Vorschlag markiert | hängt ab von |
|---|---|---|---|---|
| tf1 | Rohr einlegen | 6 | nein | – |
| tf2 | Durchbiegung begrenzen | 5 | ja | tf3, tf4 |
| tf7 | Rohr auflagern und ausrichten | 5 | ja | tf3, tf5 |
| tf8 | Rohr gegen Bewegung sichern | 5 | ja | tf3 |
| tf9 | Rohrtyp und Sollwerte vorgeben | 4 | ja | – |
| tf10 | Rohranfang und -ende erkennen | 4 | ja | – |
| tf5 | Durchmesser berührungslos erfassen | 5 | ja | tf3, tf7 |
| tf3 | Querschnitt in mehreren Winkellagen erfassen | 5 | ja | tf2, tf5, tf8, tf7, tf4 |
| tf4 | Messposition entlang der Länge ändern | 5 | ja | tf2, tf11, tf3 |
| tf11 | Position erfassen und zuordnen | 5 | ja | tf4 |
| tf6 | Messwerte auswerten, i.O./n.i.O. | 4 | ja | – |
| tf12 | Rohr entnehmen und zuordnen | 4 | ja | – |
| tf13 | Messsystem prüfen und einstellen | 4 | ja | – |
| q1–q3 | Querschnittsfunktionen | 5 / 5 / 4 | ja | – |

Gesamtvarianten: **keine** (`variants: []`).

## 2. Lücken (ohne Lösungen)

**2.1 Eigene Ideen.** Alle Teilfunktionen außer tf1 tragen im Namen „(KI-Vorschlag)“. Laut Statusbericht stammen in tf3 und tf4 einzelne Ideen von Janek. Aus den Daten lässt sich das nicht je Idee erkennen. Vorschlag zur Prüfung: Janek markiert je Idee, ob sie von ihm stammt. So lässt sich der KI-Anteil in der Dokumentation belegen (Formatvorlage: KI nur zur sprachlichen Optimierung).

**2.2 Anforderungen ohne zugehörige Teilfunktion:**
- Anf. 2.6 (W) Rauheit und 2.7 (W) Beschädigung oder Kontamination feststellen: Keine Teilfunktion erfasst sie. Janek muss entscheiden, ob sie als TF aufgenommen oder bewusst ausgelassen werden (W).
- Anf. 3.1 (F) Spannung unter der Streckgrenze: Sie wirkt auf tf2, tf7 und tf8. Der Kasten nennt sie nur in [F?]-Hinweisen; eine Teilfunktion „Belastung begrenzen bzw. nachweisen“ fehlt. Ob das eine eigene TF oder ein Kriterium ist, entscheidet Janek.
- Rohr in Drehung versetzen bzw. Winkellage antreiben und erfassen: tf3 beschreibt, *dass* mehrere Winkellagen erfasst werden. tf11 nennt den Drehgeber als eine Idee. Ob Antrieb der Drehung und Winkelerfassung eigene Teilfunktionen sind, ist offen.
- Abhängigkeit von der Definition der Zylinderform (je Querschnitt oder ganzes Rohr, siehe `pv-ent-zylinderform-bezug`): Sie bestimmt tf3 und tf4, ist aber im Kasten nicht vermerkt.

**2.3 Veraltete Verweise im Kasten** (nur Hinweis, keine Änderung):
- tf6 nennt „Ovalität“. Seit PH V1.2 heißt es Zylinderform.
- Die [F?]-Hinweise verweisen auf „W7“ und „W10“. Das sind alte Nummern aus der Widerspruchsliste zum früheren PH-Stand, keine Anforderungsnummern nach PH V1.2. Gemeint ist vermutlich Anf. 2.4 (%GRR) bzw. 1.3 (Messbereich Ø). Janek prüft das.
- tf1 verweist auf „[F? 4.2 Bauhöhe]“ und „[F? 2.7 Reibung, Platz]“. Nach PH V1.2 ist 4.2 der Ablauf (manuell einlegen) und 2.7 Beschädigung oder Kontamination. Der Platzbedarf ist 5.1. Ob die Verweise noch stimmen, prüft Janek.

**2.4 Abgrenzungen, die Ideen ausschließen könnten** (PH Kap. 4): Automatisches Zuführen bzw. Einlegen ist ausgeschlossen. Ideen in tf1 und tf12 deshalb gegen 4.2 und die Abgrenzung prüfen. Gleiches gilt für die Anbindung an IT- und QM-Systeme (tf6, tf9).

## 3. Kriterien aus den Anforderungen 2.5, 3.1, 3.2, 3.3 und 4.2

Das sind Festanforderungen (F), also **K.-o.-Kriterien** je Teillösung bzw. Variante:

| Anf. | Prüffrage je Idee bzw. Variante | betrifft TF |
|---|---|---|
| 2.5 | Liefert die Lösung einen Wert je Messpunkt, ohne über Punkte zu mitteln? | tf3, tf4, tf5, tf6, tf11 |
| 3.1 | Bleiben Spannungen aus Auflage, Führung, Spannen und Eigengewicht unter 380 MPa (NiTi) bzw. 690 MPa (Edelstahl)? Ein Nachweis ist nötig. | tf2, tf7, tf8 |
| 3.2 | Bleibt das Rohr unbeschädigt, sauber und ölfrei? Kontaktwerkstoff zulässig? (offene Aufgabe Kontaktwerkstoffe) | tf1, tf2, tf7, tf8, tf12, q1 |
| 3.3 | Kann die Lösung Durchbiegung und Lage so begrenzen, dass sie im Lagefeld des Sensors bleibt (siehe Sensor-Analyse 2.3)? | tf2, tf7, tf8, tf4 |
| 4.2 | Ist nur das Einlegen manuell, Messung und Auswertung aber automatisch? | tf1, tf4, tf6, tf12 |

## 4. Bewertungskriterien für die Variantenauswahl am 11.12. (Arbeitspaket 5)

Das Cockpit (Seite „Bewertung“) prüft die Festanforderungen schon automatisch als Ausschluss. Gewichtet werden nur Mindest- und Wunschanforderungen. Vorschlag für die Kriterienliste, **Gewichtung offen** (paarweiser Vergleich durch Janek):

| K | Kriterium | Art | Quelle |
|---|---|---|---|
| K1 | 2.3 Messpunktabstand 2 mm über die Rohrlänge | M | PH 2.3 |
| K2 | 2.4 Reproduzierbarkeit %GRR ≤ 10 % (Reserve zur Grenze) | M | PH 2.4 |
| K3 | 2.6 Rauheit messen | W | PH 2.6 |
| K4 | 2.7 Beschädigung oder Kontamination feststellen | W | PH 2.7 |
| K5 | 4.1 Taktzeit pro Rohr (Reduzierung erwünscht) | W | PH 4.1 |
| K6 | 5.1 Platzbedarf L × B | W | PH 5.1 |
| K7 | 1.5 Tantal-Rohre prüfbar | W | PH 1.5 |

Zur Diskussion, ob weitere Kriterien aus den Rahmenbedingungen kommen. Das sind keine Anforderungen nach PH und daher nur mit Janeks Zustimmung aufzunehmen: Kosten (das Cockpit hat dafür das Feld „zulässige Herstellkosten“), CE-gerechte Konstruktion (PH Kap. 3 Ziel), Aufwand für den Nachweis nach QM bzw. ISO 13485 (PH 5.3).

Vorschlag als Postfach-Eintrag `pv-daten-eval` (Sammlung `tools`, Eintrag `eval`). Er ersetzt den leeren Eintrag. Varianten und Gewichte bleiben leer.
