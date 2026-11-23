# Entscheidungsdokumentation: Decision Records, Decision Logs und Register

Stand der Recherche: 2026-11-23. Zugriff auf alle URLs: 2026-11-23, sofern nicht anders vermerkt.

**Quellenlage (wichtig für den Berichtschreiber):** Die Primärquellen adr.github.io, cognitect.com (Nygard-Artikel), en.wikipedia.org, confluence.atlassian.com, www.nasa.gov und www.adr.zone waren aus dieser Sitzung nicht erreichbar (DNS-Auflösung fehlgeschlagen, Host nicht in den erlaubten Netzdomänen). Belegt sind daher vor allem die MADR-Templates und die Projektseiten auf github.com sowie Suchtreffer (Sekundärquellen, nur Snippet gelesen). Aussagen, die nur aus Suchtreffern stammen, sind als solche markiert. Für die Mehrheit der Aussagen zu Nygard, Confluence, Notion, Jira und Systems Engineering fehlt eine direkte Lektüre der Primärquelle.

---

## Wie werden Entscheidungen erfasst? (Felder und Format)

### Takeaway
Das gängige Minimalset ist: Titel, Kontext/Problem, betrachtete Optionen, Entscheidung, Konsequenzen, Status. Die Templates von MADR zeigen zusätzlich optionale Metadaten (Entscheider, Datum, Konsultierte, Informierte). Ein Datum und ein Entscheider sind in den Quellen durchgängig als Metadaten vorgesehen, aber nicht in jedem Minimal-Template verpflichtend.

### Cited Findings
- Nygard-Format (Original Nov. 2011, Blog Relevance/Cognitect): fünf Teile, Titel, Status, Kontext, Entscheidung, Konsequenzen. Die Entscheidung wird im Stil "We will ..." formuliert; negative und neutrale Konsequenzen gehören ebenfalls hinein. Quelle nur als Sekundärbeschreibung: [albertml.com Nygard-Seite](https://albertml.com/Literature/Documenting+Architecture+Decisions+(Nygard)) (Suchtreffer, Snippet gelesen), [DEV-Community-Template-Beispiel](https://dev.to/sascha-ms/architecture-decision-records-template-and-example-3d11) (Suchtreffer). Der Originaltext war nicht abrufbar.
- MADR Full Template (Version 4.0.0, GitHub-Datei gelesen): Front-Matter mit `status` (Werte u.a. `proposed | rejected | accepted | deprecated | … | superseded by ADR-xxxx`), `date` (Datum der letzten Aktualisierung, YYYY-MM-DD), `decision-makers`, `consulted`, `informed`. Abschnitte: Titel, `Context and Problem Statement`, `Decision Drivers` (optional), `Considered Options`, `Decision Outcome` (gewählte Option mit Begründung), `Consequences` (optional, gut/schlecht), `Confirmation` (optional), `Pros and Cons of the Options` (optional), `More Information` (optional). Quelle: [madr adr-template.md @4.0.0](https://github.com/adr/madr/blob/4.0.0/template/adr-template.md?plain=1). Hinweis: Der Text wurde über einen Zusammenfassungsschritt gelesen, nicht wörtlich; die Feldnamen sind aber übernommen.
- MADR Minimal Template (Version 4.0.0, GitHub-Datei gelesen): Pflichtabschnitte sind Titel, `Context and Problem Statement`, `Considered Options`, `Decision Outcome` mit `Consequences` (dort als "optional element, feel free to remove" markiert). Kein Front-Matter im Minimal-Template gelesen; Status- und Datumsfelder fehlen dort nach dieser Lektüre. Quelle: [madr adr-template-minimal.md @4.0.0](https://github.com/adr/madr/blob/4.0.0/template/adr-template-minimal.md?plain=1) (wörtlich gelesen, Überschriften und Kommentare).
- MADR-Projekt: vier Varianten (Full, Minimal, Bare, Bare-Minimal), Semantic Versioning 2.0.0, Lizenz MIT und CC0. Der Projektname lautet inzwischen "Markdown Any Decision Records" (Suchtreffer-Angabe, auf der Projektseite als "Markdown Architectural Decision Records" gelesen). Quelle: [github.com/adr/madr](https://github.com/adr/madr). Ein Versionsdatum war auf der Seite nicht sichtbar.
- Eine Übersicht der ADR-Varianten (13 Stück, u.a. Nygard, arc42, MADR, Y-Statements, Planguage) führt das Repository [joelparkerhenderson/architecture-decision-record](https://github.com/joelparkerhenderson/architecture-decision-record) auf. Es empfiehlt keine verbindlichen Statuswerte.
- Entscheidungsregister/Decision Log (Vendor-Sekundärquelle, Suchtreffer): typische Felder sind Entscheidung, Owner, Datum, Begründung, Optionen, Status, Review-Auslöser. Ein Decision Log ist eher chronologisch, ein Register stärker strukturiert (Verantwortung, Begründung, Status, Verknüpfungen, Review). Quelle: [nortrue.com, What Is a Decision Register](https://nortrue.com/guides/what-is-a-decision-register/) (Suchtreffer). Ergänzend: [plane.so Decision log](https://plane.so/blog/decision-log-what-it-is-why-teams-use-it-and-template) (Suchtreffer, nur Titel/Snippet).
- Die Sekundärquellen einigen sich darauf, dass ein Eintrag die Entscheidung, die verworfenen Alternativen, die Randbedingungen und die Begründung zum damaligen Zeitpunkt enthalten sollte (Suchtreffer-Zusammenfassung, mehrere Quellen).

### Inferences
- Der Kern über alle Formate hinweg ist: Kontext + Optionen + gewählte Option + Begründung/Konsequenzen. Titel und Status sind ebenfalls durchgängig vorhanden. Datum und Entscheider sind die häufigsten Ergänzungen.
- Die Abgrenzung "optional" betrifft bei MADR vor allem Decision Drivers, Confirmation, Pros-and-Cons und More Information.

### Gaps
- Originaltext Nygard (cognitect.com) nicht abrufbar. Die exakte Wortwahl der Originalvorlage ist nicht verifiziert.
- MADR-Website (adr.github.io) nicht abrufbar. Die Statusliste ist nur aus dem Template-Kommentar belegt, nicht aus der Dokumentation.
- Keine Quelle zu Bedeutung/Pflichtstatus der Felder in ISO/IEEE 15288 oder INCOSE gelesen (NASA-Handbuch nicht erreichbar).

---

## Statuslebenszyklus (proposed, accepted, superseded, deprecated, rejected)

### Takeaway
Die Statuswerte sind in MADR und in Vendor-Vorlagen weitgehend gleich: proposed, accepted, rejected, deprecated, superseded. Die Quellen unterscheiden sich bei Zusatzstufen (z.B. "Researching", "Evaluating") und die Zuordnung von "superseded" zu einer Nachfolge-ID ist uneinheitlich.

### Cited Findings
- MADR-Template-Front-Matter (4.0.0): `status: "{proposed | rejected | accepted | deprecated | … | superseded by ADR-0123"}`. Quelle: [madr adr-template.md @4.0.0](https://github.com/adr/madr/blob/4.0.0/template/adr-template.md?plain=1) (Zusammenfassung).
- Joel-Parker-Henderson-Repository: Es gibt kein verbindliches Statusset. Das Beispiel "Initiating, Researching, Evaluating, Implementing, Maintaining, Sunsetting" wird als Illustration genannt. Ersetzungen laufen über ein neues ADR, nicht durch Änderung des alten: "When an AD is made that replaces or invalidates a previous ADR, then a new ADR should be created." Quelle: [github.com/joelparkerhenderson/architecture-decision-record](https://github.com/joelparkerhenderson/architecture-decision-record) (Zusammenfassung).
- Jira-Guides (Sekundär, Suchtreffer-Zusammenfassung): ein Select-Statusfeld mit Proposed, Accepted, Deprecated, Superseded, das den ADR-Lebenszyklus spiegelt. Die Zusammenfassung nennt keine eindeutige Einzelquelle; Kandidaten aus den Treffern sind u.a. [Decision Log using Jira and Automation (Medium)](https://medium.com/bethink-pl/decision-log-using-jira-and-automation-the-holy-grail-of-documenting-decisions-8d37ad3f1f2b) und [vantageos.tech](https://www.vantageos.tech/blog/how-to-track-decisions-jira). Vollinhalt nicht gelesen.
- Notion-Vorlagen (Suchtreffer, Vendor): Vorschlag Proposed, Accepted, Superseded, Rejected als Select-Feld, weil freier Text die Datenbank unbrauchbar macht. Quelle: [WhyChose ADR Template für Notion](https://whychose.com/seo/adr-template-notion) (Suchtreffer; Vollinhalt nicht gelesen).
- Confluence-Decision-Blueprint (Sekundär, Forum von ca. 2018, Suchtreffer): Status "Not started", "In process", "Decided". Quelle: [Seibert Group Answers](https://answers.seibert.group/t/confluence-can-you-explain-the-decision-blueprint/565) (Suchtreffer). Dieser Stand ist veraltet; aktuelle Atlassian-Dokumentation war nicht abrufbar.
- Atlassian-Blog 2015 (Suchtreffer): Statusänderung über das Status-Makro, das die Beteiligten benachrichtigt. Quelle: [confluence.atlassian.com Blog 2015/09](https://confluence.atlassian.com/doc/blog/2015/09/how-to-make-better-decisions-as-a-development-team) (Suchtreffer, nicht selbst gelesen). Alter: 2015.

### Inferences
- "superseded" und "deprecated" sind unterschiedlich: superseded verweist auf eine Nachfolge-Entscheidung, deprecated nimmt die Entscheidung ohne Nachfolger zurück. Diese Unterscheidung ist in den MADR-Werten angelegt ("superseded by ...").
- Ein Status "rejected" wird in MADR als eigener Zustand für verworfene Vorschläge geführt, nicht als Löschung.

### Gaps
- Keine Primärquelle zu einer Definition der Statuswerte von Confluence (aktuell) oder Notion (offizielle Vorlage) gelesen.

---

## Widerruf und Ersetzung (Supersession, nie löschen)

### Takeaway
Die Standardpraxis: eine geänderte oder aufgehobene Entscheidung wird nicht überschrieben. Eine neue Entscheidung wird angelegt, die alte erhält Status "superseded" mit Verweis auf die neue ID, und der Verweis zeigt in beide Richtungen. Die Quellen warnen, dass der Rückverweis oft vergessen wird.

### Cited Findings
- Joel-Parker-Henderson-Repository: "Don't alter existing information in an ADR." Änderungen erfolgen durch Ergänzung oder Supersession. Viele Teams führen ADRs als "living document" mit datierten Nachträgen. Quelle: [github.com/joelparkerhenderson/architecture-decision-record](https://github.com/joelparkerhenderson/architecture-decision-record) (Zusammenfassung). Eine ausdrückliche Lösch-Regel fand sich dort nicht.
- MADR-Template: Status "superseded by ADR-0123" im Front-Matter; der alte Datensatz bleibt erhalten. Quelle: [madr adr-template.md @4.0.0](https://github.com/adr/madr/blob/4.0.0/template/adr-template.md?plain=1).
- Sekundärquellen (Suchtreffer-Zusammenfassung, mehrere Blogs): Man schreibt einen neuen Eintrag statt einen akzeptierten zu überarbeiten, und setzt im alten Eintrag den Status auf den neuen Verweis. Quelle: Suchtreffer [MADR template guide (adr.zone)](https://www.adr.zone/adr-template/madr) (nicht erreichbar); Aussage stammt aus dem Suchtreffer-Snippet der Websuche "MADR markdown architectural decision records template status superseded".
- Decision Register werden laut Suchtreffer-Zusammenfassung mit Review-Auslösern geführt; die Zusammenfassung nennt keine Einzelquelle mit Löschregel. Quelle: Suchtreffer-Zusammenfassung zur Websuche "systems engineering decision management rationale capture decision register" (u.a. [nortrue.com](https://nortrue.com/guides/what-is-a-decision-register/)). Eine ausdrückliche Nicht-Lösch-Regel aus einer Register-Quelle ist nicht belegt.

### Inferences
- Ein sauberes Modell hat zwei Richtungen: alt -> neu (Status/Feld "ersetzt durch") und neu -> alt ("ersetzt"). Nur so bleibt die Historie beim Lesen eindeutig.
- Werte aus einer aufgehobenen Entscheidung sollten nicht stillschweigend geändert werden, sondern über eine neue Entscheidung oder eine neue Korrektur.

### Gaps
- Keine gelesene Quelle, die Löschregeln für Decision Logs in Confluence oder Notion beschreibt.
- Keine Quelle zur Behandlung von "rejected" versus "superseded" bei bereits verlinkten Aufgaben.

---

## Entscheidung versus offene Frage oder Vorschlag

### Takeaway
Die Standardabgrenzung läuft über den Status: "proposed" ist ein Vorschlag, "accepted" ist bindend. Offene Fragen sind in den gelesenen Quellen kein eigener Typ im ADR-Format; sie werden häufig als eigener Eintrag oder als Status "Not started/In process" geführt.

### Cited Findings
- MADR-Template: Status "proposed" und "accepted" bilden die Grenze; die Entscheidung im Abschnitt "Decision Outcome" gilt erst nach Annahme. Quelle: [madr adr-template.md @4.0.0](https://github.com/adr/madr/blob/4.0.0/template/adr-template.md?plain=1) (Zusammenfassung).
- Sekundär (Suchtreffer): Status "proposed", wenn die Stakeholder noch nicht zugestimmt haben; "accepted", wenn sie zugestimmt haben. Quelle: Suchtreffer-Zusammenfassung zu Nygard, siehe [albertml.com](https://albertml.com/Literature/Documenting+Architecture+Decisions+(Nygard)).
- Confluence (Sekundär, veraltet): "Not started / In process / Decided" trennt offene Punkte von Entscheidungen. Quelle: [Seibert Group Answers](https://answers.seibert.group/t/confluence-can-you-explain-the-decision-blueprint/565).
- Notion-Vorlage DACI (Suchtreffer): Feldpaar Driver (Treiber) und Approver (Freigeber), getrennt von Contributors und Informed. Quelle: [notion.com DACI-Vorlage](https://www.notion.com/templates/daci-decision-framework-for-cross-functional-teams) (Suchtreffer).

### Inferences
- Für eine bindende Entscheidung braucht es mindestens: ein Status "accepted"/"decided", eine Freigabeperson und ein Datum. Ohne diese drei ist der Eintrag ein Vorschlag, auch wenn der Text nach Entscheidung klingt.
- Offene Fragen sollten als eigener Typ oder Status (z.B. "offen") geführt werden, nicht als Entscheidung mit leerem Ergebnis.

### Gaps
- Keine Quelle gelesen, die offene Fragen als eigenen Datensatztyp mit Verknüpfung zur späteren Entscheidung beschreibt.

---

## Verknüpfung mit Aufgaben, Anforderungen und Dokumenten

### Takeaway
Die Verknüpfung ist in den gelesenen Quellen kaum standardisiert. Sie wird meist über Felder (Link auf Ticket, Requirement oder Dokument) oder über Relationen in der Tool-Datenbank gelöst. Ein formaler Standard (z.B. IDEF6 für Design-Rationale) existiert, war aber nicht direkt lesbar.

### Cited Findings
- Design-Rationale-Standard IDEF6 erfasst Begründungen über alle Phasen der Systementwicklung (Wikipedia-Eintrag, Suchtreffer). Quelle: [Wikipedia IDEF6](https://en.wikipedia.org/wiki/IDEF6) (nur Suchtreffer; Wikipedia war nicht abrufbar).
- Design rationale wird als Begründung plus die Argumentation definiert, die zur Entscheidung führte. Quelle: [Wikipedia Design rationale](https://en.wikipedia.org/wiki/Design_rationale) (Suchtreffer).
- TUM Lehrstuhl für Angewandte Softwaretechnik: Rationale ist das schwierigste Informationsgut zum Pflegen; das Erfassen ist eine Vorabinvestition mit langfristigem Nutzen. Quelle: [ase.in.tum.de](https://ase.in.tum.de/lehrstuhl_1/component/content/article/43-books/234) (Suchtreffer, nur Snippet).
- Vendor-Sicht (Suchtreffer): Erfassung klappt am besten im Arbeitsablauf, weil ein separater Schritt unter Termindruck ausfällt. Quelle: [Tandem, Design Rationale Capture](https://tandem.inc/resources/design-rationale-capture-tool-hardware-teams) (Vendor-Aussage, nicht unabhängig belegt).
- Jira (Suchtreffer, Vendor): Ein eigener Issue-Typ "Decision" macht Entscheidungen durchsuchbar; Verknüpfung über normale Issue-Links. Quelle: [Jira Decision Log Medium-Artikel](https://medium.com/bethink-pl/decision-log-using-jira-and-automation-the-holy-grail-of-documenting-decisions-8d37ad3f1f2b), [resolution.de Decision log template](https://www.resolution.de/post/decision-log-template/) (beide nur Suchtreffer).

### Inferences
- Tragfähig ist ein Modell, in dem die Entscheidung auf die Aufgabe zeigt, die sie auslöst, und die Anforderungen und Dokumente, die sie betrifft, über Verweis-Felder führen. Die Gegenrichtung (Aufgabe -> Entscheidung) ist über die Aufgabe abbildbar.
- Ein Review-Datum oder Auslöser (Zeitraum, Ereignis) erhöht die Pflegbarkeit; dazu liegen Vendor-Hinweise vor, keine unabhängigen Studien.

### Gaps
- Keine gelesene Quelle mit einer konkreten Feldliste für Entscheidung->Anforderung->Dokument-Verknüpfung in einem ADR-Tool.
- IDEF6-Details nicht gelesen.

---

## Kennung: Nummerierung, Präfix, Datum

### Takeaway
Die verbreitete Praxis ist eine laufende Nummer mit führenden Nullen (z.B. ADR-0123) oder eine Dateinummer nnnn-titel.md. Das Datum steht als Metadatum, nicht als ID. Das Repository von Joel Parker Henderson empfiehlt Dateinamen im Format "verb-phrase.md" in Kleinbuchstaben mit Bindestrichen.

### Cited Findings
- MADR-Anleitung: Vorlage für jede Entscheidung als `nnnn-title.md` kopieren (Zusammenfassung der Projektseite). Quelle: [github.com/adr/madr](https://github.com/adr/madr).
- Joel Parker Henderson: Dateinamen klein, mit Bindestrichen, Imperativ-Verbphrase, z.B. `choose-database.md`; keine Nummerierungsregel. Quelle: [github.com/joelparkerhenderson/architecture-decision-record](https://github.com/joelparkerhenderson/architecture-decision-record) (Zusammenfassung).
- MADR-Template: Feld `date` im Front-Matter ist das Datum der letzten Aktualisierung. Quelle: [madr adr-template.md @4.0.0](https://github.com/adr/madr/blob/4.0.0/template/adr-template.md?plain=1).

### Inferences
- Die ID sollte stabil bleiben, auch wenn der Titel sich ändert. Ein Präfix pro Sammlung (Entscheidung, Aufgabe, Anforderung) verhindert Verwechslung, ist aber in den gelesenen Quellen nicht als Standard beschrieben.
- Die Nummer sollte nicht wiederverwendet werden, auch nicht nach Verwerfen eines Eintrags.

### Gaps
- Keine gelesene Quelle zu Präfixkonventionen in Decision Registers.

---

## Bekannte Stolperfallen (dokumentiert)

### Takeaway
Die Quellen nennen drei wiederkehrende Probleme: Entscheidungen gehen im Chat oder in Meetings verloren, es fehlt die Begründung, und es gibt keinen namentlichen Verantwortlichen. Die Stolperfallen sind in den Quellen meist als Praxiserfahrung formuliert, nicht empirisch belegt.

### Cited Findings
- Decision Logs werden damit begründet, dass Entscheidungen ohne zentrale Ablage nicht auffindbar sind. Quelle: Suchtreffer-Zusammenfassung zur Websuche "decision log template" (keine Einzelquelle gelesen; Treffer u.a. [plane.so](https://plane.so/blog/decision-log-what-it-is-why-teams-use-it-and-template), nur Titel gesehen). Als schwach einzustufen.
- Mehrere Vendor-Guides empfehlen genau einen Verantwortlichen pro Eintrag statt einer Gruppe. Quelle: [resolution.de Decision log template](https://www.resolution.de/post/decision-log-template/) (Suchtreffer).
- Free-Text-Status macht Datenbanken unbrauchbar; Status als Auswahlfeld festlegen. Quelle: [WhyChose ADR Notion](https://whychose.com/seo/adr-template-notion) (Suchtreffer).
- Verweise auf superseded-Entscheidungen werden oft nur einseitig gepflegt, dadurch sind tote Verweise in der Historie. Quelle: Suchtreffer-Zusammenfassung der MADR-Recherche (siehe oben).

### Inferences
- Die häufigsten Ursachen für verlorene Entscheidungen sind fehlender Ort (Chat), fehlender Owner und fehlende Begründung. Das passt zu den Vendor-Aussagen, ist aber keine gemessene Häufigkeit.

### Gaps
- Keine empirische Studie zu Anteilen verlorener oder unbegründeter Entscheidungen gelesen.
- Keine Primärquelle von Atlassian oder Notion zu diesen Stolperfallen.

---

## Zusammenfassung der Quellenqualität (für den Berichtschreiber)

- Stark (primär, gelesen): MADR-Template 4.0.0 (Full, Minimal) auf GitHub; Joel-Parker-Henderson-Repository auf GitHub; MADR-Projektseite auf GitHub.
- Schwach (Sekundär, nur Suchtreffer): Nygard-Original (nur Beschreibungen), Confluence-Blueprint (Stand ca. 2018), Notion-Vorlagen, Jira-Guides, Decision-Register-Ratgeber.
- Nicht erreichbar in dieser Sitzung: adr.github.io, cognitect.com, en.wikipedia.org, confluence.atlassian.com, www.nasa.gov, www.adr.zone. Diese Hosts müssten im Netzwerk der Sitzung freigegeben werden, damit die Quellen direkt nachgeprüft werden können.
- Alter der Quellen: Nygard 2011, Confluence-Blueprint-Stand ca. 2018, Atlassian-Blog 2015. Die übrigen Vendor-Quellen sind 2024 bis 2026, Alter nicht sicher prüfbar.
