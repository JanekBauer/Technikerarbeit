# TA-Cockpit (statische Fassung)

Lesefassung des Cockpits „Messanlage für Rohre“. Läuft ohne Claude, ohne Server und ohne Anmeldung.
Die Regeln für Claude stehen in `CLAUDE.md` (Version 2, 23.11.2026). Hier steht, wie das Cockpit bedient wird.

## Ansehen
- Die Seite: `docs/index.html` im Browser öffnen (funktioniert auch lokal als einzelne Datei) oder über GitHub Pages.
- Die Seite wird von der GitHub-Action `cockpit-bauen.yml` neu erzeugt, sobald sich `cockpit/daten/`, `cockpit/vorlage.html` oder `cockpit/build.py` ändern.

## Wo was liegt
| Ort | Inhalt |
|---|---|
| `cockpit/daten/<sammlung>.json` | Projektstand, einzige Datenquelle der Seite. Nur Übernahmen aus dem Postfach ändern sie. |
| `cockpit/daten/postfach.json` | Eingang für alle Vorschläge, Aufgaben, Entscheidungen und Änderungen |
| `cockpit/vorlage.html` | Oberfläche (Quelle) |
| `docs/archiv/` | Dokumente und Versionen |
| `cockpit/_Versionen/` | Alte Stände. Nichts wird gelöscht, nur dorthin verschoben. |

Sammlungen in `daten/`: `tasks` (Aufgaben und Entscheidungen), `deadlines`, `reqs`, `sensors`, `sources`, `doku`, `kilog`, `checks`, `tools`, `packages`, `files`, `optionen`, `freitage`, `changes`, `postfach`.

Die Präfixe der IDs (`t-`, `e-`, `p-`, `k-`, `d-`, …) stehen in `CLAUDE.md`, Abschnitt 2.

## Bearbeiten im Cockpit
Oben rechts „Bearbeiten freischalten“ wählen und ein GitHub-Zugriffstoken einfügen (fein abgestuftes Token, nur dieses Repo, Berechtigung „Contents: Read and write“). Das Token bleibt nur im Browser.

**Jede Änderung an Daten wird ein Vorschlag im Postfach** (Art `daten`). Ausnahmen: Checklisten-Haken und Werkzeuge (Morph. Kasten, Bewertung) werden direkt gespeichert.
1. Bearbeiten, Löschen oder Ziehen in der Oberfläche legt einen Vorschlag an. Die Daten bleiben unverändert.
2. Unten links erscheint „N Änderungen nur im Browser“. „Aktualisieren“ schreibt die Vorschläge in einem Commit nach `cockpit/daten/postfach.json`. „Verwerfen“ nimmt sie zurück.
3. Im Postfach übernimmst du den Vorschlag oder verwirfst ihn. Erst die Übernahme schreibt den Eintrag in die Sammlung.
4. Änderst du denselben Eintrag mehrfach, wird der offene Vorschlag aktualisiert. Er wird nicht doppelt angelegt.

Die Anzeige im Browser ändert sich erst nach der Übernahme. Bis dahin bleibt der alte Stand sichtbar, mit dem offenen Vorschlag im Postfach.

## Aufgaben und Entscheidungen
- Aufgaben haben die Status offen, in Arbeit, erledigt, entfallen.
- Entscheidungen haben die Status offen (Frage), entschieden (gilt) und entfallen (aufgehoben). Entschieden verlangt „Entschieden von“ und „Begründung“.
- Eine aufgehobene Entscheidung wird nie gelöscht. Sie bekommt „Ersetzt durch“, die neue Entscheidung „Ersetzt“. Ohne Nachfolger steht der Grund unter „Grund, wenn ohne Nachfolger entfallen“.
- Ausführlich begründet in `projekt/` (Bericht „Aufgaben und Entscheidungen in Projektsystemen“) und CLAUDE.md, Abschnitt 2a.

## Dateien hoch- und herunterladen
Im Archiv gibt es „Datei hochladen“, „Neue Version“ und „Datei hinzufügen“. Die Datei wird direkt als Commit nach `docs/archiv/<Ordner>/<Dokument>/<Version>_<Name>` gelegt (max. 20 MB). Der Eintrag in `cockpit/daten/files.json` läuft als Vorschlag ins Postfach und wird erst mit der Übernahme sichtbar.
Herunterladen geht direkt über die Seite.

## Datenschutz
Das Repo ist öffentlich. Janek hat am 20.11.2026 entschieden, dass die vorhandenen Rohrspezifikationen und die Prüfanweisung im Repo bleiben. Keine weiteren Betriebsunterlagen (Angebote, Mails, Spezifikationen) hochladen, die nicht schon im Repo liegen. Dateinamen mit Angebot, Quotation, RM0, IP0, Spez_ oder .eml lösen eine Rückfrage aus.

## Neu bauen (nur zum Testen)
`python cockpit/build.py` schreibt `docs/index.html`. Diese Datei committest du nicht von Hand. Das macht die Action nach dem Push.

## Veröffentlichen (GitHub Pages)
Repo-Einstellungen → Pages → Quelle „GitHub Actions“. Der Workflow `cockpit-seite.yml` veröffentlicht `docs/` nach jedem Push auf `main`.
