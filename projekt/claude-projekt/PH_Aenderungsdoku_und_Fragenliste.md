# Pflichtenheft – Änderungsdokumentation & Fragenliste Betrieb

*Angelegt 24.10.2026 in Chat 02. Werte nur eintragen, wenn sie vom Betrieb (Quelle + Datum) stammen. Ausführlicher Fragenkatalog: Excel „Fragenkatalog_PH_V3_TA_Bauer.xlsx“ (30.10.2026).*

> Archiv-Hinweis (20.11.2026): Stand bis V7. Maßgeblich ist Kap. 6 im Pflichtenheft (seit 13.11. PH V1 mit neuer Zählung) und `cockpit/daten/questions.json`.

**Entscheidung Janek 05.11.2026:** V1–V6 waren interne Entwürfe (weder Betrieb noch Schule vorgelegt). Die Änderungsdokumentation **im PH (Kap. 6)** beginnt deshalb mit **V7 als erster vorgelegter Fassung** (Ausgangsstand). Die Tabelle A unten bleibt als interne Entwurfshistorie (Nachweis für KI-Logbuch), kommt aber nicht ins PH.

## A. Interne Entwurfshistorie (nicht im PH)

| Version | Datum | Kapitel | Änderung | Grund | Entschieden von |
|---|---|---|---|---|---|
| V1 | 16.10.2026 | alle | Gerüst aus Schulvorlage, Inhalte aus AS V2, offene Punkte markiert | Start PH | Janek (KI-unterstützt, s. Logbuch) |
| V1.x | vor 24.10.2026 | Anf. 1.1, 1.2 | Werkstoff „Nitinol / Edelstahl“; Rohrlänge 1000–3000 mm | Quelle offen | offen |
| V2 | 24.10.2026 | 2 | Ist-Zustand: 100-%-Sichtprüfung im WE durch QM; Rundheit/Maßhaltigkeit nur über Lieferantendokumente; Rohrfehler meist erst beim Laserschneiden | Rundgang 23.10.2026 | Janek (Quelle QM offen) |
| V3 | 30.10.2026 | Titel, 2, 3, Anf. | Automatisierung entfernt; Länge, Ø, Werkstoffe angepasst; Gesprächsergebnisse 30.10. eingetragen | Überarbeitung / Gespräch 30.10. | Janek |
| V4 | 30.10.2026 | Titel, 3, 4, Anf., 5 | Automatisierung (manuell einlegen, Messen/Auswerten automatisch) wieder aufgenommen; Tantal; 3 m; MS 2 Mitte Feb. | Notizen Gespräch 30.10. | Janek / Betrieb (bestätigen) |
| V5 | 30.10.2026 | 2, 3, Anf., 5 | Anf. 2.3 Messpunkte max. 2 mm; Kontaktdaten; betriebl. MS (Kick-off, PH-Freigabe, Übergabe); Variantenauswahl/Konstruktionsfreigabe entfernt; Auslegungsberechnungen gestrichen; Logo | Überarbeitung Janek | Janek |
| V6 | 30.10.2026 | Titel, 3, 4, 6 | Titel AS V3; Angebote Kaufteile als Ergebnis; Abgrenzung Bestellung/Beschaffung; Kap. 6 angelegt | Abgleich AS V3 / Cockpit | Janek |
| V7 | 05.11.2026 | 2, 5.2, 5.4, 6 | Betriebliche MS ergänzt **als Vorschlag** (gelb): Variantenauswahl 04.12.2026, Konstruktionsfreigabe 22.01.2027; Kap. 6 auf V7 als Ausgangsstand zurückgesetzt; W1: 5.4 verweist auf AS (V3); W3: Ist-Zustand nennt Rohre aus Nitinol, Edelstahl und Tantal | Wunsch/Entscheidung Janek 05.11.; MS-Termine von Claude vorgeschlagen (Fr = Projekttag) – **mit Hr. Baidinger abstimmen** | Janek |

## B. Änderungsdokumentation im PH (Kap. 6)

| Version | Datum | Kapitel | Änderung | Grund | Entschieden von |
|---|---|---|---|---|---|
| V7 | 05.11.2026 | alle | Erste Fassung zur Abstimmung mit dem Betrieb; Ausgangsstand für alle weiteren Änderungen | Vorlage zur PH-Freigabe am 06.11.2026 | Janek |

## C. Offene Fragen an den Betrieb (Stand V7)

### Priorität 1 – bis PH-Freigabe 06.11.2026
1. Anf. 2.1 Rundheit „10 %“: 10 % wovon? Welche Rundheitstoleranz gilt?
2. Anf. 2.3 Messpunkte „alle 2 mm“: Abstand entlang der Rohrlänge (bei 3 m ≈ 1500 Messquerschnitte) oder etwas anderes?
3. Anf. 2.2 Durchmessertoleranz, 2.4 Reproduzierbarkeit (Wert, Einheit, Nachweis)
4. Anf. 4.1 Taktzeit: Vorgabe oder bewusst offen?
5. Automatisierungsgrad bestätigen
6. ~~Angebote: Teil der Ergebnisse?~~ ✅ erledigt (V6): Angebote = Ergebnis, Bestellung/Beschaffung = Abgrenzung – Bestätigung Hr. Baidinger offen
7. **Betriebliche MS-Vorschläge bestätigen oder ändern:** Variantenauswahl 04.12.2026, Konstruktionsfreigabe 22.01.2027
8. Pneumatikplan / Elektronikplan: Umfang?

### Priorität 2
9. Ansprechpartner QM (Quelle Ist-Zustand), Zusammenarbeit mit Abteilungen
10. Druckluft: Druck in bar
11. Rohrspezifikationen Edelstahl und Tantal; Werkstoffnormen
12. Anf. 3.1 zulässige Durchbiegung; 3.2 Definition Beschädigung/Kontamination
13. Dokumentation/Rückverfolgbarkeit der Messwerte; QM-Vorgaben (ISO 13485)

### Cockpit-Widersprüche (Stand 05.11.2026)
- W1 ✅ PH 5.4 verweist auf AS (V3) – PH V7
- W2 ✅ entschieden (Janek 05.11.): Begriff „Elektronikplan“; PH bleibt, **AS V3 muss angepasst werden („Elektroplan“ → „Elektronikplan“) – Chat 01**
- W3 ✅ Ist-Zustand nennt Rohre aus Nitinol, Edelstahl und Tantal – PH V7
- W6 🟡 Variantenauswahl 04.12.2026 und Konstruktionsfreigabe 22.01.2027 als Vorschlag im PH V7 – Bestätigung Hr. Baidinger am 06.11.
