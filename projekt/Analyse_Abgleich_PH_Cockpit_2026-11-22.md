# Analyse: Abgleich PH V1.2 gegen Cockpit und Dubletten (Arbeitspakete 6 und 8)

Stand 22.11.2026 · erstellt von KI (Claude Code). Grundlage: PH V1.2 (Janek: V0.2), `docs/archiv/3 Pflichtenheft/Pflichtenheft/V1.2_Bauer_TA_PH_V1.docx`, Stand 20.11.2026, sowie `cockpit/daten/*.json` nach `git pull` am 22.11.2026. Bei Wertkonflikten gewinnt das PH (CLAUDE.md). Alle Änderungen sind nur **Vorschläge im Postfach**.

## 1. Anforderungen (`reqs.json` gegen PH Kap. 3)

| Cockpit-ID | Cockpit | PH V1.2 | Vorschlag |
|---|---|---|---|
| r06 | 2.1 „Ovalität“, max 0,010 / 0,025 mm, bestätigt | 2.1 Zylinderform (Ø max − Ø min), NiTi [?], Edelstahl [?] | Text auf Zylinderform, Werte leer, Status offen → `pv-daten-r06` |
| r18 | 5.1 Art F, bestätigt | 5.1 Art W, Wert „offen“ (gelb) | Art W, Status offen → `pv-daten-r18` |
| r02 | Nr. 1.2 Tantal | Nr. 1.5 | Nummer angleichen → `pv-auf-reqs-nummern` |
| r03 | Nr. 1.3 Rohrlänge | Nr. 1.2 | wie oben |
| r04 | Nr. 1.4 Außendurchmesser | Nr. 1.3 | wie oben |
| r05 | Nr. 1.5 Wandstärke, Gruppe „Messaufgabe“ | Nr. 1.4, Gruppe Prüfobjekt | wie oben |
| r10–r12 | Gruppen „Spannen und Handhabung“, „Automatisierung und Betrieb“ | 2.5–2.7 gehören zu „Messaufgabe“ | Gruppe angleichen |
| r13–r15 | Gruppen „Automatisierung und Betrieb“, „Aufstellung“ | 3.1–3.3 gehören zu „Spannen und Handhabung“ | Gruppe angleichen |
| r16, r17 | Gruppe leer | 4.1, 4.2 gehören zu „Betrieb“ | Gruppe angleichen |
| r11 | 2.6 Rauheit max 0,4 µm | 2.6 ohne Wert | Janek entscheidet, ob der Wert aus der Rohrspezifikation (vertraulich, nur sinngemäß) im Cockpit bleibt |
| r12 | Hinweis „Defekte > 10 % Wandstärke (Spez.)“ | 2.7 ohne Maßstab | nur zur Kenntnis |
| r01–r18 | Quelle oft „PH V8.7“ (9 Einträge) | – | Quelle auf PH V1.2 (20.11.2026) umstellen, denn V8.7 gibt es nicht mehr |

Formhinweis zum PH selbst (für die nächste PH-Fassung, Janeks Entscheidung): 2.1 und 2.2 verwenden beide das Symbol ΔD. In der Änderungsdokumentation des PH ist die Zeile V1.2 eingetragen. Unter Kap. 5.4 steht „Aufgabenstellung (V3)“, das Cockpit führt dagegen AS V4.x. Janek prüft, welche Fassung gemeint ist.

## 2. Termine und Entscheidungen

| Cockpit | Stand Cockpit | PH V1.2 Kap. 5.2 | Vorschlag |
|---|---|---|---|
| Entscheidung `mwruyef4g4mwo` „Variantenauswahl: Datum im PH klären“ | offen; Text nennt Daten aus der alten Fassung | 11.12.2026 = Cockpit `d14` | Abschluss → `pv-abs-variantenauswahl` |
| Entscheidung `mwruy9eersqb9` „Projektabschluss: Datum im PH klären“ | offen | 05.03.2027 = Cockpit `d09` | Abschluss → `pv-abs-projektabschluss` |
| Entscheidung `mwruy7jmo06ve` „PH-Freigabe: Datum im PH klären“ | offen | 27.11.2026 | Abschluss → `pv-abs-ph-freigabe` |
| Termin `d04` „PH-Freigabe + Unterschrift“ | **04.12.2026**, Notiz: „Festgelegt 18.11.: Fr. 27.11.26“, geändert am 21.11. | 27.11.2026 | Janek bestätigt, welches Datum gilt → `pv-daten-d04` (schlägt 27.11. vor) |
| Checkliste `mwqihgy46r8oo` „PH-Freigabe + Unterschrift“ | Hinweis „04.12.2026“ | 27.11.2026 | nach der Entscheidung zu d04 von Hand anpassen |
| Entscheidung `mwruykcaqi0bj` „Zylinderform“ | offen (Definition und Toleranzen) | Definition festgelegt (Ø max − Ø min, Kap. 5.3), Toleranzen [?] | Abschluss nur für die Definition → `pv-abs-zylinderform`; Toleranzen gehen in `pv-ent-toleranz-grr` über |

Die Termine Kick-off (23.10.), Variantenauswahl (11.12.), Konstruktionsfreigabe (15.01.) und Projektabschluss (05.03.) stimmen zwischen PH und Cockpit überein.

## 3. Dubletten (Arbeitspaket 8)

Die im Statusbericht genannten Dubletten-IDs (`mwqieyis7lqnk`, `mwqziec7vx9bf`, `mwqief827m65y`, `mwrst4h2yg4ju`, `mwqif9og0838q`, `mwqzj17mgv7lj`) sind **nicht mehr in `tasks.json`**. Die drei Datumsfragen gibt es dort heute je **einmal**. Sie haben aber eine inhaltliche Doppelung zu den Terminen `d04`, `d09` und `d14` in `deadlines.json`.

Mehrfach-Einträge gibt es noch im **Postfach** (alle schon „übernommen“ oder „verworfen“, also nur Verlauf):

| Thema | Postfach-IDs |
|---|---|
| Variantenauswahl: Datum | pf-pruef-28, mwrutps8v4e40, mwruu0rgzvqn7 (verworfen) |
| PH-Freigabe: Datum | pf-pruef-29, mwrutx9qm9chd |
| Projektabschluss: Datum | pf-pruef-30, mwrutrrm93c1y |
| Bilder Stents und Marker | pf-tasks-t-bilder-problemstellung, mwp43c9poj1dx, mwrutktdzabyg, mwruvuvx1j4sy |
| Bilder/Werte Präsentation | pf-tasks-t-praesentation-w14, mwp43iglli2c3, mwrutyd0s71xx |
| Kontaktstellen/-werkstoffe | pf-tasks-t-kontaktstellen, mwp43f04y57my, mwrutssdzwdr7 |
| Zylinderform | pf-questions-q17, mwrutoyc8r6tt |
| Werkstoffe | pf-questions-mw2iuzjkwhcgv, mwruu2vao9d8r |
| %GRR abschätzen | pf-tasks-t-grr-abschaetzung, mwp2rlt35eyxi |
| Gliederung Doku | pf-tasks-t-gliederung-abstimmen, mwp43jmdvjyvn |

Außerdem verweist die Checkliste `mwqihgy46r8oo` noch auf `mwrst4h2yg4ju` (die alte Kopie). Nichts wurde gelöscht. → `pv-auf-dubletten`.

## 4. Offene Punkte aus dem PH ohne Cockpit-Eintrag

Diese Punkte hat die KI als Vorschlag ins Postfach gelegt:
- Platzbedarf L × B (Anf. 5.1) → `pv-ent-platzbedarf`
- QM-Vorgaben ISO 13485 für ein neues Prüfmittel (PH 5.3) → `pv-ent-qm-pruefmittel`
- Die früheren Aufgaben „Toleranzen je Werkstoff mit QM“ und „%GRR bestätigen“ fehlen in `tasks.json`. Laut CLAUDE.md gelten sie damit als gelöscht. Inhaltlich sind sie in `pv-ent-toleranz-grr` wieder enthalten; Janek entscheidet.
