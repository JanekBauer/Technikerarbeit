---
name: preferences
description: Wie Claude im Projekt Technikerarbeit antworten und arbeiten soll
---
- Möchte in jeder Antwort als Erstes mit seinem Namen „Janek“ angesprochen werden (Kontrolle gegen Halluzinationen).
- Dateien der Technikerarbeit sollen ins Archiv des TA-Cockpits und in den PC-Ordner C:\_Janek_Bauer\Cloude\Technikerarbeit\Archiv abgelegt werden – doppelte Absicherung; Ablauf im Skill „TA-Dateiablage“.
- Stand 14.11.2026: Ablage nur bei finalen Fassungen (Stand für Betrieb, Schule oder Meilenstein), zusammen mit dem Übergabeblock und wenn Janek „ablegen“ sagt; bei Zwischenständen nur eine Zeile „Ablage offen: <Datei Vn>“. Erfolgte Ablage mit „Abgelegt: …“ bestätigen.
- Abgleich und Ablage sollen möglichst wenig Tokens verbrauchen: Projektabgleich inkrementell (nur Änderungen seit dem letzten Stand), Voll-Abgleich nur auf ausdrücklichen Wunsch.
