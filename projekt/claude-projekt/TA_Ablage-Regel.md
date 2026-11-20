# Ablage-Regel – jede Datei doppelt sichern (gilt für alle Chats 00–11)

*Angelegt 04.11.2026 auf Wunsch von Janek. Ziel: Jede Datei der Technikerarbeit liegt gleichzeitig im **Archiv des TA-Cockpits** und im **PC-Ordner**.*

> Archiv-Hinweis (20.11.2026): Regel aus dem claude.ai-Projekt. Das Claude-Artefakt ist seit 18.11. archiviert; maßgeblich ist das GitHub-Cockpit (`cockpit/daten`, `docs/archiv`).

- **Cockpit (Artefakt):** https://claude.ai/artifact/LZiNTP2ktcUetHv3DgQAVK → Bereich „Archiv“ (Collection `files`)
- **PC-Ordner (Spiegel des Archivs):** `C:\_Janek_Bauer\Cloude\Technikerarbeit\Archiv\<Ordner>\<Datei>`; ältere Versionen unter `<Ordner>\_Versionen\<Dokument>\<Version>_<Datei>`

## Wann
Immer wenn Janek in einem Chat eine Datei **einfügt** oder Claude ihm eine Datei **erstellt oder aktualisiert** (neue Datei oder neue Version, z. B. PH V7, AS V4, Protokoll, Fragenkatalog, Datenblatt). Nicht für Zwischenstände, die nur Claude selbst braucht.

## Ordner im Archiv
1 Betrieb & Ausschreibung · 2 Aufgabenstellung · 3 Pflichtenheft · 4 Projektplan · 5 Projektsteuerung & Protokolle · 6 Recherche Messtechnik · 7 Schule - Vorlagen · 8 Schule - Unterstützungsprogramm · 9 Uploads zu Terminen. Neue Ordner nur, wenn keiner passt (z. B. „9 CAD & Zeichnungen“). Keine Doppelpunkte in Ordnernamen (Windows).

## Ablauf (Claude)
1. **Einordnen:** Ordner, Dokument („family“, z. B. „Pflichtenheft“), Version (`ver`, z. B. „V7“; `seq` = Zahl), Datum, kurze Notiz, was sich geändert hat. Vorher `files` lesen (ArtifactData list): Gibt es das Dokument schon → nächste Version; gibt es einen Platzhalter mit `missing: true` für genau diese Version → diesen Eintrag füllen (update mit if_version) statt neu anlegen.
2. **Ins Artefakt hochladen** (Artifact, `asset: true`, `url` = Cockpit):
   - PDF, Bild, CSV, MD, TXT → Datei direkt hochladen.
   - Word/Excel/PowerPoint/xls → erst `base64 -w0 datei > datei.b64.txt`, dann die .txt hochladen (jede Textdatei in einem eigenen Aufruf). Im Eintrag `enc: "b64"` setzen.
3. **Eintrag schreiben** (ArtifactData, Collection `files`): `{name, folder, family, ver, seq, date, note, kind, src: "asset", assetId, enc?, mime, size, by: "Chat XX", updated: <jetzt ISO>}`.
4. **Auf den PC** (nur wenn die Verbindung zum PC steht): Originaldatei nach `/mnt/user-data/outputs/…` kopieren und mit `device_commit_files` nach `…\Archiv\<Ordner>\<Datei>` schreiben; die bisher neueste Version zusätzlich nach `…\_Versionen\<Dokument>\<Version>_<Datei>`. Danach `tools/pcsync` aktualisieren (`files.<doc_id> = updated`, `at` = jetzt). PC aus → nur ins Artefakt; das Cockpit zeigt „nicht auf PC“, und der Knopf **„PC-Ordner abgleichen“** holt es später nach.
5. **Kurz bestätigen:** „Abgelegt: Cockpit-Archiv › <Ordner> › <Dokument> <Version> · PC ✓/ausstehend“.

## Grenzen
- Geht nur in Chats, in denen Claude die Artefakt-Werkzeuge hat. Fehlen sie, sagt Claude das und Janek lädt die Datei im Archiv per „Neue Version“ selbst hoch.
- Auf dem PC wird nichts gelöscht. Dateien, die nur auf dem PC liegen, bietet Claude beim Abgleich zum Hochladen an.
- Fachliche Inhalte schreibt Claude dadurch nicht – die Regel betrifft nur das Ablegen.
