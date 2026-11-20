# Regel-Audit – Technikerarbeit Janek Bauer

Stand: 20.11.2026. Grundlage: CLAUDE.md im Repo, Janeks Vorgaben in den Chats und den Übergaben unter
`projekt/uebergaben/`. Ältere Chats 00–11 sind nicht einsehbar; was dort steht, ist hier nur insoweit erfasst,
wie es in Übergaben oder im Cockpit auftaucht.

Der Initialisierungs-Prompt für neue Chats steht in `projekt/Master-Prompt_Technikerarbeit.md`.

---

## Teil 1: Regeln (Checkliste)

### Rolle & Identität
- [ ] Claude Code als Projektassistent für Janek Bauer. Keine Rolle als Entwickler oder Gutachter.

### Zielgruppe
- [ ] Janek selbst (Anrede „Janek“).
- [ ] Doku und Präsentation: Schule (Fachausschuss Hr. Graudejus de Olio, 2 Lehrkräfte) und Betrieb (Hr. Baidinger, BD Gamer).

### Tonfall & Stil
- [ ] Deutsch, sachlich und knapp.
- [ ] Keine Schönfärberei. Unsicherheiten und Widersprüche offen benennen.

### Formatierung
- [ ] Cockpit-Daten: eine JSON-Zeile pro Eintrag, `id` bleibt erhalten, UTF-8.
- [ ] Commit-Nachrichten auf Deutsch: was und warum.

### Umfang & Struktur
- [ ] Vor jeder Aufgabe `git pull`.
- [ ] Datenänderung: JSON bearbeiten → `python cockpit/build.py` → `cockpit/daten` und `docs/index.html` zusammen committen und pushen.
- [ ] Nach jeder abgeschlossenen Aufgabe committen und pushen.
- [ ] Übergaben unter `projekt/uebergaben/` ablegen.

### Sprache & Grammatik
- [ ] Keine Pronomen aus Namen ableiten. Unbekannte Pronomen: neutral (sie/ihnen).

### Inhaltliche Einschränkungen
- [ ] Vertrauliche Betriebsunterlagen (Rohrspezifikationen, Prüfanweisung) bleiben im Repo. Nicht erneut nachfragen (Entscheidung 20.11.).
- [ ] Bei Abweichungen zwischen Übergaben und Cockpit gilt das Cockpit (Entscheidung 19.11.).
- [ ] Kein Sperrvermerk für die Doku. Spezifikationen nicht beifügen, nur paraphrasieren (Entscheidung 06.11.).
- [ ] Fachliche Texte für die Dokumentation nur mit schriftlicher Erlaubnis von Hrn. Graudejus (W8 offen).
- [ ] Nichts löschen. Ältere Versionen nach `_Versionen` verschieben.

### Quellen & Belege
- [ ] Jede Aussage mit Quelle (Datum, Chat, mündlich oder schriftlich). Mündliche Angaben als „nicht belegt“ kennzeichnen.

### Spezifische Befehle & Trigger
- [ ] „Projektabgleich“ nur auf ausdrücklichen Zuruf. Dann gleichen wir die Daten mit den Dokumenten im Repo ab; das Repo gewinnt.
- [ ] Jede KI-Hilfe in `cockpit/daten/kilog.json` eintragen (Datum, Chat, Art, `fach` true/false).
- [ ] Vorschläge (Termine, Fristen, Werte) als „Vorschlag“ kennzeichnen und nicht ohne Bestätigung ins Cockpit übernehmen.

---

## Teil 2: Analyse

### Regel-Historie & Widersprüche
| Thema | Stand | Widerspruch | Offen bei |
|---|---|---|---|
| Termine | 14.11.: PH V1 maßgeblich | 18.11.: Cockpit maßgeblich | Janek bestätigt Cockpit (aktuell gültig) |
| Variantenauswahl | Übergaben: 04.12. | Cockpit: 11.12. (18.11.) | Janek |
| PH-Freigabe | Fragenliste: 20.11. | Cockpit: 27.11. | Janek (aktuell 27.11.) |
| Finale AS an FSL | Cockpit t14: 30.11. | Rillsoft 1.1.4: 04.12. | Janek (Frage `q-abgabe-as-frist`) |
| Branch-Name | CLAUDE.md: `Main_JJJJ-MM-TT_HH-MM` | Sitzung: `claude/migrate-technikerarbeit-github-wbqsgp` | Janek |
| Commit-Attribution | Hinweis: „Co-Authored-By: Claude Haiku 5.5“ | Systemhinweis: keine Modellnamen in Commits | Janek |
| KI-Regel (W8) | Cockpit: offen | Erlaubnis nur mündlich | Hr. Graudejus (Frage `q-ki-erlaubnis-schriftlich`) |
| Repo-Sichtbarkeit | Repo öffentlich (cockpit/README.md) | Übergabe: auf privat setzen | Janek (Aufgabe `t-repo-sichtbarkeit`) |

### Lücken
- Ausgabeformat der Doku (Word oder PDF, Schulvorlage V10) ist nicht festgelegt.
- Zieltermine: Gliederung V1 mit Hrn. Graudejus bis MS 3 (19.03.2027), Doku-Abgabe 05.04.2027.
- Präsentation: 13–15 Min. plus Fragen, Fachausschuss, 1/3 Endnote (Chat 11).
- Vorgeschlagene Fristen, die noch niemand bestätigt hat (im Cockpit als „Vorschlag“ markiert).
- Offen aus MS 1: Protokoll wird nach dem Umbau der Struktur nachgereicht (Entscheidung Janek 20.11.).

---

## Teil 3: Entscheidungen von Janek (20.11.2026)

- MS-1-Protokoll nach dem Umbau der Struktur nachreichen; Auswertung bis dahin offen.
- Claude-Artefakt TA-Cockpit: abgeglichen, veraltet, wird ignoriert und gelöscht. Maßgeblich ist das Repo.
- PC-Ablage: veraltet, vorerst ignoriert.
- Morpho-Testdateien (.doc/.rtf): nicht archivieren.

Im Cockpit stehen diese Entscheidungen unter `decisions.json` (Einträge `e-20261120-…`).

---

## Stand nach Abarbeitung (20.11.2026)

| Punkt | Entscheidung |
|---|---|
| Variantenauswahl | 11.12.2026 (Cockpit gilt; 04.12. aus den Übergaben überholt) |
| Finale AS an FSL | 30.11.2026 (t14); Rillsoft 1.1.4 angleichen |
| Repo-Sichtbarkeit | bleibt öffentlich; vertrauliche Betriebsunterlagen bleiben trotzdem im Repo |
| Branch-Regel | CLAUDE.md gilt für neue Branches; diese Sitzung bleibt auf `claude/migrate-technikerarbeit-github-wbqsgp` |
| Commit-Attribution | wie bisher (mit Modellname). **Konflikt:** Systeminstruktion verbietet Modellnamen in Commits. Bleibt offen markiert. |
| Ausgabeformat Doku | noch offen (Frage `q-doku-format`) |

Die übrigen Lücken (Zieltermine Gliederung und Abgabe, Präsentationsrahmen, Vorschlagsfristen) bleiben bestehen.

Entscheidungen im Cockpit: `e-20261120-variantenauswahl`, `e-20261120-as-abgabe`, `e-20261120-repo-oeffentlich`, `e-20261120-branch-regel`, `e-20261120-attribution`.
