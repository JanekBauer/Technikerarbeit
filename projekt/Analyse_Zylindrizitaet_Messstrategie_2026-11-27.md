# Analyse: Zeitbedarf Stop-and-go gegenüber Helix-Messung bei Zylindrizität

Stand 27.11.2026 · erstellt von KI (Claude Code) als Entscheidungsgrundlage · **keine Festlegung**. Janek und der Betrieb entscheiden.

Kennzeichnung: **[PH]** Pflichtenheft · **[H]** Herstellerangabe · **[R]** eigene Rechnung · **[S]** Annahme (Zahlenwert nicht belegt, nur zum Rechnen) · **[offen]** Wert fehlt

Bezug: Entscheidung E-007 (Messgröße Zylinderform / Zylindrizität). Dieser Text erklärt nur den Zeitbedarf, nicht die Messgenauigkeit.

## 1. Ausgangslage

- Messfeld: Rohre Ø 1 bis 6,5 mm, Länge 1 bis 3 m. [PH, Herstellerentwurf]
- Messpunkte im Abstand von 2 mm über die gesamte Länge. [PH, Herstellerentwurf]
- Zylindrizität ist eine Formtoleranz nach ISO 1101. Sie wird an einem Querschnitt über mehrere Winkellagen und über die Länge bestimmt. Für eine Aussage zur Rundheit braucht man mindestens drei Winkellagen je Querschnitt. [R]

## 2. Stop-and-go-Messung

Der Sensor hält an jedem Messpunkt an. Das Rohr oder der Sensor wird an eine Winkellage gedreht, dort wird gemessen, dann weiter.

Zeit je Messpunkt und Winkellage:

    t_Punkt = t_Fahr + t_Beruhigen + n_Mittel · t_Einzel

- t_Fahr: Beschleunigen, Abbremsen, Positionieren
- t_Beruhigen: Abklingen von Schwingungen des Rohrs nach jeder Bewegung
- n_Mittel · t_Einzel: Mittelung für die Wiederholgenauigkeit. Die Hersteller nennen Mittelungen von 8, 32 und 128 Werten als Fragen, siehe Herstellerentwurf Frage 2. [H, Frage offen]

Gesamtzeit:

    T_Stop = N_z · N_θ · t_Punkt

- N_z: Anzahl der Querschnitte. Bei 3 m und 2 mm Abstand ca. 1 500 bei Ø 1 bis 6,5 mm. [R]
- N_θ: Winkellagen je Querschnitt, mindestens 3. [R]

Der Zeitanteil für Fahren und Beruhigen wird je Punkt wiederholt. Er fällt bei jedem der N_z · N_θ Punkte an.

## 3. Helix-Messung

Das Rohr dreht sich kontinuierlich, der Sensor fährt gleichmäßig in Achsrichtung. Die Messbahn ist eine Schraubenlinie (Helix) mit der Ganghöhe p.

    T_Helix = L / v_z
    v_z = p · n_Dreh

- L: Rohrlänge (bzw. Messstrecke)
- v_z: Vorschubgeschwindigkeit
- n_Dreh: Drehzahl
- p: Ganghöhe, also Vorschub je Umdrehung

Die Messwerte werden mit einem Drehgeber dem Winkel und der Achsposition zugeordnet. Die Anzahl der Umdrehungen ist L / p.

Wählt man p gleich dem Abstand der Querschnitte (2 mm), entspricht eine Umdrehung einem Querschnitt. Die Messbahn deckt dann die gleichen Punkte ab wie die Stop-and-go-Messung, nur kontinuierlich.

## 4. Vergleich

| Größe | Stop-and-go | Helix |
|---|---|---|
| Fahren/Beschleunigen | bei jedem Punkt | nur am Anfang und Ende |
| Beruhigen | bei jedem Punkt | keines, Rohr läuft gleichmäßig |
| Mittelung | je Punkt, in der Stillstandszeit | während der Bewegung, mehr Samples je Umdrehung nötig |
| Zeitbedarf | wächst mit N_z · N_θ · Haltezeit | wächst mit L / v_z |

**Kernaussage:** Bei Stop-and-go zahlt man die Anfahr- und Beruhigungszeit tausendfach, bei der Helix einmal. Der Unterschied ist umso größer, je mehr Querschnitte und je mehr Winkellagen gemessen werden.

**Beispielrechnung mit Annahmen [S]:**
- N_z = 1 500, N_θ = 3, t_Fahr + t_Beruhigen = 0,5 s, n_Mittel · t_Einzel = 0,1 s [S]
- T_Stop = 1 500 · 3 · 0,6 s = 2 700 s = 45 min [R, nur Rechnung]
- Helix mit v_z = 2 mm/s bei L = 3 m: T_Helix = 3 000 mm / 2 mm/s = 1 500 s = 25 min [R, nur Rechnung]

Die Werte sind frei gewählt. Sie zeigen die Größenordnung, nicht das Ergebnis. Das Ergebnis hängt von Sensor-Abtastrate, Drehzahl und Mittelungszahl ab. Diese Werte sind [offen].

## 5. Nachteile der Helix, die geprüft werden müssen

- **Zuordnung:** Jeder Messwert muss exakt einem Winkel und einer Achsposition zugeordnet werden. Ein ungenauer Drehgeber verfälscht die Zylindrizität.
- **Rohrbewegung:** Ein drehendes Rohr kann schwingen oder sich durchbiegen. Die Herstellerfrage 4 zu bewegten oder rotierenden Objekten ist dafür direkt relevant. [H, offen]
- **Abtastrate:** Der Sensor muss genug Messwerte je Umdrehung liefern, sonst bleiben Lücken. Die nötige Rate ist [offen].
- **Mittelung:** Bei bewegtem Messobjekt ist die Mittelung über die Zeit nicht dasselbe wie im Stillstand. Das muss der Hersteller bestätigen.

## 6. Offene Punkte

1. Abtastrate und Mittelungsmöglichkeit des gewählten Sensors bei bewegtem Objekt. [H, offen]
2. Maximale Drehzahl und Vorschub, die das Rohr ohne Schwingung zulässt. [offen]
3. Ob das QM Zylindrizität nach ISO 1101 oder die Form Ø max − Ø min verlangt (E-007). [offen]

## 7. Vorschlag

Vorschlag: Vor der Entscheidung E-007 die Abtastrate und die Rotationsfähigkeit des Sensors klären. Ohne diese Angaben lässt sich nicht sagen, ob die Helix schneller und ausreichend genau ist. Die Zeitdifferenz aus Abschnitt 4 ist eine Rechnung mit Annahmen, keine Messung.
