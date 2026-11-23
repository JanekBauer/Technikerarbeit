# Aufgabenmodell in Issue-Trackern und Projektwerkzeugen

Zugriffsdatum aller Quellen: 2026-11-23. Die meisten Quellen sind undatiert; Aussagen zum Stand 2026 sind daher nicht überall belegt. Für Jira-Server/Data-Center-Seiten gilt: Server ist ein älterer Stand, Jira Cloud kann abweichen. Die Seiten von linear.app, docs.github.com, www.openproject.org, www.redmine.org, support.atlassian.com, help.notion.com und developers.asana.com konnten im Lauf nicht abgerufen werden (DNS-Fehler in der Sitzung). Alle Aussagen zu diesen Tools stammen deshalb aus Suchergebnis-Ausschnitten, nicht aus dem vollständigen Text. Sie sind im Text entsprechend gekennzeichnet, wo es die Quelle nahelegt.

## Welche Felder und Status sind verbreitet?

### Takeaway
Übereinstimmend: Ein Eintrag hat einen Titel, genau einen Status aus einem Workflow, einen Typ oder Tracker, eine Priorität und optional Verantwortliche, Fälligkeit und Verknüpfungen. Status ist fast überall eine Liste frei benennbarer Zustände, die einer festen Kategorie zugeordnet sind (offen/in Arbeit/erledigt). Das Abschließen wird meist als Kategorie oder Flag geführt, nicht als eigener Status für "gelöscht".

### Cited Findings
- Jira-Workflows bestehen aus Statuses und Transitions; ein Vorgang hat zu jedem Zeitpunkt genau einen Status; eine Transition ist einseitig, Hin- und Rückweg brauchen zwei Transitions. Quelle (Server/DC-Dokumentation, älterer Stand): [Atlassian, Workflows](https://confluence.atlassian.com/display/Jira/Configuring+Workflow) (Suchausschnitt, Zugriff 2026-11-23)
- Jira Server/DC: Offen oder geschlossen hängt am Feld Resolution, nicht am Status; ein Workflow muss Resolution in einer Transition setzen, wenn er "geschlossen" erzwingen soll. Quelle: [Atlassian, Workflows (Server)](https://confluence.atlassian.com/display/Jira/Configuring+Workflow) (Suchausschnitt)
- Jira Work Management: Jeder Status gehört zu genau einer von drei festen Kategorien (To Do, In Progress, Done); eigene Status müssen einer Kategorie zugeordnet werden; die Kategorie steuert Darstellung in Listen, Boards und Reports, und JQL fragt sie als `statusCategory` ab. Quellen: [Atlassian, Workflows and statuses for the board](https://support.atlassian.com/jira-work-management/docs/workflows-and-statuses-for-the-board) und [Atlassian, Defining status field values (Server)](https://confluence.atlassian.com/adminjiraserver0905/defining-status-field-values-1207177444.html) (Suchausschnitte)
- Notion: Status-Eigenschaft mit drei festen Gruppen (To-do, In Progress, Complete); eigene Status-Optionen können nur innerhalb dieser Gruppen angelegt werden. Quelle: [Notion Help, Database properties](https://www.notion.com/en-gb/help/database-properties) (Suchausschnitt). Die Einführung des Status-Typs ist in den [Notion-Release-Notes 2022-06-29](https://www.notion.com/releases/2022-06-29) belegt (älter).
- Linear Projekte: eigene Projekt-Statuskategorien Backlog, Planned, Started, Completed, Canceled. Quelle: [Linear, Configuring workflows](https://linear.app/docs/configuring-workflows) (Suchausschnitt, nicht abgerufen).
- Linear Prioritäten: No priority, Low, Medium, High, Urgent; Einträge ohne Priorität werden ans Ende sortiert; Urgent löst Benachrichtigung aus. Projekte nutzen dieselbe Skala. Quelle: [Linear, Priority](https://linear.app/docs/priority) (Suchausschnitt); Projekt-Priorität laut [Linear Changelog 2024-07-25](https://linear.app/changelog/2024-07-25-priority-for-projects-and-micro-adjust) (älter, Suchausschnitt).
- Jira-Prioritäten (Standard): Highest, High, Medium, Low, Lowest. Quelle: Suchausschnitt in [Atlassian, Defining priority field values (Server)](https://confluence.atlassian.com/adminjiraserver105/defining-priority-field-values-1561363674.html) (älter).
- GitHub Projects: Feldtypen Single-Select (z. B. für Priorität), Iteration (Sprints/Wochen), Status; das Board nutzt standardmäßig das Status-Feld; bis zu 50 Felder pro Projekt; eingebaute Workflows können Status z. B. bei Schließen auf "Done" setzen. Quelle: [GitHub Docs, Quickstart for Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/quickstart-for-projects) (Suchausschnitt aus Enterprise-Server- und github.com-Seiten)
- Redmine: Status-Liste frei veränderbar; pro Status ein Flag "Issue closed", mehrere Status dürfen geschlossen sein. Quelle: [Redmine Wiki, Issue tracking setup](https://www.redmine.org/projects/redmine/wiki/RedmineIssueTrackingSetup) (Suchausschnitt)
- OpenProject: Standard-Typen Milestone, Phase, Task; Status kann je Typ verschieden sein; Standard-Status für Task laut Suchausschnitt: New, In progress, Done, On hold, Rejected, Closed; Status-Flags für "schließt das Paket", "schreibgeschützt" und "Standard"; Fortschritt in % möglich. Quelle: [OpenProject, Manage work package types](https://www.openproject.org/docs/system-admin-guide/manage-work-packages/work-package-types/) und [Manage work package status](https://www.openproject.org/docs/system-admin-guide/manage-work-packages/work-package-status/) (Suchausschnitte, nicht abgerufen)
- Taiga: Eigene Statussätze für Epics, User Stories, Tasks und Issues; Konfiguration unter Settings > Attributes > Statuses; Status mit Flag "Closed" zählt als erledigt; Flag "Archived" klappt Status auf dem Kanban-Board ein. Quelle: [Taiga Community, Customisation for your projects](https://community.taiga.io/t/customisation-for-your-projects/127) (Community-Forum, kein offizielles Doc, Suchausschnitt)

### Inferences
- Minimale gemeinsame Feldmenge über alle Tools (aus den Quellen abgeleitet, nicht als Standard belegt): Titel, Status (mit Kategorie offen/in Arbeit/erledigt), Typ oder Tracker, Priorität, Verantwortlicher, Fälligkeit, Verknüpfungen, Beschreibung, Anhänge.
- Die Trennung "offen" vs. "erledigt" wird fast überall über eine Kategorie oder ein Flag gelöst, nicht über einen eigenen Status je Abschlussart. Abschlussarten (erledigt, abgelehnt, Duplikat) landen über Close-Reasons, Resolution oder Canceled-Kategorie in derselben Kategorie.
- Die Anzahl der Status ist in den Beispielen klein (3 Kategorien mit wenigen Status je Kategorie bei Jira Work Management und Notion; 5 Kategorien bei Linear-Projekten). Mehr Status werden in den Quellen nicht als Standard genannt.

### Gaps
- Keine Quelle zur Frage, wie viele Status Tools empfehlen (Minimalzahl). Nicht belegt.
- Keine Standardwerte für Priorität bei Redmine, Trello, Asana, Notion, Taiga aus den Quellen.
- Asana-Statusmodell (Abschnitte, Status-Updates) nicht gesucht.
- Linear-Workflow-Details (Zahl der Status je Kategorie, Standard-Status) nur aus Snippet, Seite nicht abgerufen.
- Trello hat laut Suchergebnissen Listen statt Status-Workflow; Details zu Listen als Status nicht geprüft.

## Wie trennen Tools "zu erledigen" von "zu entscheiden" oder "Information"?

### Takeaway
Keines der geprüften Tools führt "Entscheidung" in der Kernlogik als eigenen Zustand. Die Trennung erfolgt über den Typ oder Tracker (Jira Issue Type, GitHub Issue Type, Redmine Tracker, OpenProject Work Package Type) mit eigenem Workflow. Die Aussage "Entscheidung" als eigener Typ ist in den Quellen nur über Community-Beispiele und eine Thesis belegt, nicht über Standardfunktionen.

### Cited Findings
- Redmine: Tracker (Bug, Feature, Defect usw.) haben je einen eigenen Standard-Status für neue Issues, eine Einstellung, ob sie in der Roadmap erscheinen, und einen eigenen Workflow. Quelle: [Redmine Wiki, Issue tracking setup](https://www.redmine.org/projects/redmine/wiki/RedmineIssueTrackingSetup) (Suchausschnitt); Verschiebung des Standard-Status auf die Tracker-Seite in Redmine 3.0.0 (älter).
- Jira: Workflow-Schemata ordnen Issue-Typen Workflows zu, damit verschiedene Typen im selben Projekt verschiedene Abläufe haben. Quelle: [Atlassian, Workflows (Server)](https://confluence.atlassian.com/display/Jira/Configuring+Workflow) (Suchausschnitt, älter).
- GitHub: Issue Types sind organisationsweit definierbar, um Issues über Repositories hinweg einheitlich zu klassifizieren; GA-Ankündigung 2025. Quelle: [GitHub Changelog, Evolving GitHub Issues and Projects (2025-04-08)](https://github.blog/changelog/2025-04-08-evolving-github-issues-and-projects/) (Suchausschnitt).
- OpenProject: Standardtypen Milestone, Phase, Task; Typen müssen je Projekt aktiviert werden; häufig ergänzt um Typen wie Bug oder Feature. Quelle: Suchausschnitt [OpenProject, Work package types](https://www.openproject.org/docs/system-admin-guide/manage-work-packages/work-package-types/) und [OpenProject FAQ](https://www.openproject.org/docs/user-guide/work-packages/work-packages-faq/) (nicht abgerufen).
- Notion: Statusgruppen To-do / In Progress / Complete sind die einzige Ebene, die Notion fest vorgibt; Datenbanken können darüber hinaus beliebige Select-Eigenschaften haben. Quelle: [Notion Help, Database properties](https://www.notion.com/en-gb/help/database-properties) (Suchausschnitt).
- Taiga: Epics dienen laut Taiga-Blog als Container für User Stories, als Referenz oder als Ablage für Anforderungen, Wireframes und Designs. Quelle: [Taiga Blog, What's an epic](https://blog.taiga.io/whats-an-epic-our-research.html) (Suchausschnitt; die Frage, ob Epics im Sprint oder Kanban leben, ist laut Suche offen).
- ADR-Beispiele: Ein Issue-Template für Architekturentscheidungen nutzt den Titel-Präfix "ADR:" und setzt kein Entscheidungs-Label. Quelle: Suchausschnitt aus einem Template-Repo (öffentliches Beispiel, Qualität nicht geprüft).
- Eine Thesis zu Jira-Issues untersucht Entscheidungsinhalte in Issues und nutzt Labels, um Entscheidungstypen zu finden. Quelle: Suchausschnitt [Thesis (UB Groningen), Version 8 Final](https://fse.studenttheses.ub.rug.nl/31767/1/Version_8_Final.pdf) (nicht abgerufen, akademische Arbeit, kein Standard).

### Inferences
- Das übliche Muster ist: Typ/Tracker trennt Arbeitsarten, Workflow trennt Ablauf. Ein "Entscheidung"-Typ wäre damit ein eigener Typ mit eigenem, kürzerem Workflow (z. B. offen, entschieden, verworfen), kein Status innerhalb der Aufgabe. Das ist eine Ableitung aus dem Tracker-/Workflow-Modell, nicht aus einer Quelle belegt.
- Information (ohne Handlungsbedarf) ist in den Quellen nicht als eigener Typ belegt. Naheliegend ist ein Feld oder Label, nicht ein Status. Nicht belegt.

### Gaps
- Keine Quelle, die für Jira Cloud, Linear, GitHub, Asana oder Notion einen Typ "Entscheidung" als Standard beschreibt. Der Befund ist nur "nicht im Standard gefunden", nicht "gibt es nicht".
- Keine Quelle zur Abgrenzung "Information" (Notiz, Hinweis) vs. Aufgabe.
- Keine Suche nach Jira Service Management, ClickUp, Monday oder Azure DevOps, die eigene Typen für Anfragen oder Änderungen haben.

## Wie modellieren Tools Triage und Eingangsqueues?

### Takeaway
Linear hat die klarste dokumentierte Lösung: eine eigene Statuskategorie "Triage" als Team-Posteingang mit Annehmen, Ablehnen und Zurückstellen. Für die übrigen Tools fand ich keine gleichwertige, belegte Beschreibung. Die Muster dort sind Standardstatus für neue Items (Redmine), Workflows mit Pflicht-Transitionen (Jira) oder Labels/Filter (GitHub).

### Cited Findings
- Linear Triage: Triage ist eine zusätzliche Statuskategorie und dient als Eingang des Teams, getrennt von den Standard-Workflow-Status. Issues aus Integrationen, aus der Triage-Ansicht oder von Personen außerhalb des Teams starten in Triage. Quelle: [Linear, Triage](https://linear.app/docs/triage) (Suchausschnitt; Seite konnte nicht abgerufen werden).
- Linear Triage-Aktionen: Annehmen verschiebt das Item in den Standardstatus des Teams (optional mit Kommentar); Ablehnen verschiebt es in den Typ Canceled (mit Begründungskommentar); Zurückstellen (Snooze) blendet es bis zu einem Zeitpunkt oder bis zu neuer Aktivität aus. Quelle: [Linear, Triage](https://linear.app/docs/triage) (Suchausschnitt).
- Linear: Triage-Issues sind standardmäßig aus allen Ansichten ausgeschlossen; sichtbar nur mit Filter. Quelle: [Linear, Triage](https://linear.app/docs/triage) (Suchausschnitt).
- Linear: Triage-Regeln, Triage Intelligence und Triage Responsibility sind laut Suchausschnitt nur in den Business- und Enterprise-Tarifen verfügbar. Quelle: [Linear, Triage](https://linear.app/docs/triage) (Suchausschnitt; Tarife können sich geändert haben).
- Redmine: Neue Issues bekommen den Standard-Status ihres Trackers (siehe oben). Quelle: [Redmine Wiki](https://www.redmine.org/projects/redmine/wiki/RedmineIssueTrackingSetup) (Suchausschnitt).
- GitHub: Keine Triage-Kategorie in den Suchausschnitten; Projekte haben Status- und Single-Select-Felder, die als Eingangsfilter genutzt werden können. Quelle: [GitHub Docs, Quickstart for Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/quickstart-for-projects) (Suchausschnitt).

### Inferences
- Der Unterschied zwischen "Posteingang" und "Arbeitsstatus" ist nur bei Linear als Status-Kategorie gelöst. Bei den übrigen Tools ist die Trennung durch Status-Name, Filter oder Projektansicht gelöst. Das ist eine Ableitung aus dem Fehlen belegter Gegenbeispiele.
- Die Ablehnung im Eingang wird bei Linear nicht gelöscht, sondern in einen Abschlusszustand (Canceled) verschoben. Das passt zum Muster "nichts löschen".

### Gaps
- Keine belegte Beschreibung eines Eingangs für Jira, OpenProject, Asana, Notion, Trello, Taiga, Redmine (außer Standardstatus).
- Linear: Ob Duplicate eine eigene Kategorie ist oder unter Canceled liegt, widersprechen sich die Suchausschnitte. Nicht geklärt.
- Keine Quelle zum Muster "Vorschlag aus dem Web, der erst vom Verantwortlichen übernommen wird" (Trennung Vorschlag vs. Übernahme). Die Muster in den Quellen sind Eingangsstatus oder Filter, nicht ein Freigabeschritt mit Vorschlagsobjekt.

## Wie werden Items verknüpft (blockiert, verwandt, Eltern/Kind, Abhängigkeit, Dokument)?

### Takeaway
Die Verknüpfungstypen sind fast gleich: "blocks / is blocked by", "relates to", "duplicates", teils "clones" oder "copied to". Hierarchie läuft über Sub-Issues oder Subtasks. Verknüpfung zu Dokumenten oder Anforderungen ist in den Quellen über Felder, Relationen-Datenbanken oder externe Links gelöst, nicht über einen eigenen Anforderungs-Typ.

### Cited Findings
- Jira: Standard-Linktypen: relates to, duplicates, blocks, clones, mit paarigen Beschreibungen (inward/outward). Admins können Linktypen hinzufügen, umbenennen oder löschen. Quelle: [Atlassian, Configuring issue linking (Server)](https://confluence.atlassian.com/adminjiraserver0914/configuring-issue-linking-1385109361.html) (Suchausschnitt, älter).
- Jira: JQL-Funktion `linkedIssues(issueKey, linkType)`; eine andere Quelle nennt `hasLinkType(linkType)`. Quelle: Suchausschnitt (Community-Beiträge), Widerspruch nicht geklärt.
- Jira-Forum (unbelegt): "Blocks/is blocked by" seien die einzigen Links mit Funktion; andere seien rein visuell. Quelle: Community-Beitrag, nicht offiziell, nur als Behauptung.
- GitHub: Sub-Issues: bis zu 100 je Eltern-Issue, bis zu acht Verschachtelungsebenen; Hinzufügen per UI oder `gh issue edit --add-sub-issue`. Quelle: [GitHub Docs, Adding sub-issues](https://docs.github.com/en/enterprise-cloud@latest/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues) (Suchausschnitt).
- Redmine: Relationstypen: related to, duplicates, duplicated by, precedes/follows, blocks/blocked by, copied to. Quelle: [Redmine API, IssueRelation](https://www.rubydoc.info/github/redmine/redmine/IssueRelation) (Suchausschnitt). Laut Wiki schließt "duplicates" den anderen Issue, wenn das Original geschlossen wird, aber nicht umgekehrt (Suchausschnitt, Wiki-Seite nicht abgerufen).
- Redmine: Elternaufgabe bekommt Fortschritt als gewichteten Mittelwert der Kinder, Start des frühesten, Fälligkeit des spätesten Kindes. Quelle: Suchausschnitt Redmine-Wiki (nicht abgerufen).
- Redmine: Mehrere Defekte zu Vorgänger/Nachfolger zwischen Unteraufgaben (u. a. Zyklusfehler, CSV-Import), teils geschlossen, Stand heute nicht geprüft. Quellen: [Redmine #13586](https://www.redmine.org/issues/13586), [Redmine #35560](https://redmine.org/issues/35560) (Suchausschnitte, älter).
- Asana: Abhängigkeiten sind "blocked by" und "blocking"; eine Aufgabe kann insgesamt höchstens 30 Abhängigkeiten und Abhängige haben (laut API-Doku-Ausschnitt). Quelle: [Asana Developers, Tasks](https://developers.asana.com/docs/tasks) und [Asana Help, Task dependencies](https://help.asana.com/s/article/task-dependencies) (Suchausschnitte).
- Asana: Referenz-Custom-Fields (nur in den Tarifen Advanced, Enterprise, Enterprise+) verlinken Aufgaben, Projekte, Portfolios oder Ziele, ohne formale Abhängigkeit. Quelle: [Asana Help, Reference custom fields](https://help.asana.com/s/article/reference-custom-fields) (Suchausschnitt).
- Notion: Relation-Eigenschaft verbindet Datenbanken; Relation ist ein Array von Seiten-IDs; einseitige Relationen sind möglich; die Zieldatenbank muss für die Verbindung zugänglich sein. Quelle: [Notion Developers, Property object](https://developers.notion.com/reference/property-object) (Suchausschnitt).
- Notion: bis zu 500 Eigenschaften je Datenbank. Quelle: [Notion Help, Database properties](https://www.notion.com/en-gb/help/database-properties) (Suchausschnitt).
- OpenProject: Beziehungen zwischen Arbeitspaketen (z. B. "follows", "blocks") und Hierarchie über Eltern-Arbeitspakete. Nicht belegt, da Quelle nicht abgerufen.

### Inferences
- Gemeinsames Verknüpfungs-Vokabular über Tools: blockiert/blockiert von, verwandt, Duplikat, Vorgänger/Nachfolger, Eltern/Kind. Für die Modellierung ist Blocks eindeutig mit Richtung, Relates bewusst ohne Richtung.
- Verknüpfungen zu Dokumenten oder Anforderungen laufen in den Quellen über Relations-Datenbanken (Notion, Asana-Referenzfelder) oder externe Links. Kein Tool in den Quellen hat einen fest eingebauten Anforderungs-Typ.

### Gaps
- Keine belegte Angabe zu Verknüpfung mit Dokumenten im Jira- oder Linear-Standard (Confluence-Links, Linear-Dokumente nicht geprüft).
- Linear-Relationen (blocks, related, duplicate) nicht aus einer abgerufenen Seite belegt.
- GitHub: Verknüpfung über "tracked by / tracks" (Sub-Issues) und Erwähnungen nur aus Ausschnitten; Details nicht geprüft.
- Trello: Keine Verknüpfungsfunktion außer Karten-Verknüpfungen/Kommentaren in den Suchergebnissen gefunden.
- Jira-Widerspruch: ob `linkedIssues` oder `hasLinkType` die korrekte JQL-Funktion ist. Nicht geklärt.

## Wie werden IDs vergeben (Nummern, Präfixe)?

### Takeaway
Jira und Linear nutzen Präfix plus Zähler (ABC-123, ENG-123), projekt- bzw. team-bezogen. GitHub nummert pro Repository, Issues und Pull Requests teilen sich die Nummernfolge. Redmine vergibt IDs global, Projektnummern werden als Wunsch diskutiert. Für Notion, Trello, Asana, Taiga und OpenProject fand ich keine belegte ID-Regel.

### Cited Findings
- Jira: Issue-Key ist `<Projektschlüssel>-<Nummer>`; Nummer ist ein Zähler je Projekt, der normalerweise bei 1 beginnt. Projektschlüssel per Regex; Standard früher mindestens zwei Großbuchstaben, neuere Doku: Bindestrich nicht erlaubt. Quelle: [Atlassian, Changing the project key format (Server)](https://confluence.atlassian.com/display/ADMINJIRASERVER/Changing+the+project+key+format) (Suchausschnitt, älter; Regeln je Version verschieden).
- Linear: Issue-ID = Team-Schlüssel plus laufende Nummer innerhalb des Teams (TEAM-NUMBER). Beim Wechsel des Teams erhält das Item eine neue ID aus der Folge des Zielteams; alte IDs bleiben auffindbar. Quelle: [Linear, Creating issues](https://linear.app/docs/creating-issues) (Suchausschnitt). Die Schlüssellänge (2–10 Großbuchstaben) stammt aus einer Drittanbieter-Bibliothek, nicht aus Linear-Doku.
- GitHub: Nummern sind je Repository vergeben (Autoincrement); Issues und PRs teilen dieselbe Folge. Quelle: Community-Beiträge (LLVM-Mailingliste, Backdrop-Issue-Kommentar), nicht offizielle GitHub-Doku.
- GitHub: Verschieben eines Issues zwischen Repositories soll laut einem Community-Kommentar Nummern ändern; das ist nicht offiziell belegt. Offizielle Doku (Enterprise Server) sagt: Kommentare, Labels und Assignees bleiben erhalten; Verschieben nur innerhalb desselben Eigentümer-Kontos. Quelle: [GitHub Docs, Transferring an issue to another repository (Enterprise Server)](https://docs.github.com/en/enterprise-server@3.19/issues/tracking-your-work-with-issues/administering-issues/transferring-an-issue-to-another-repository) (Suchausschnitt, älter).
- Redmine: Feature-Anfrage #5765 zu projektbezogenen Issue-Nummern (impliziert globale Nummern als Standard). Quelle: [Redmine Feature #5765](https://www.redmine.org/issues/5765) (Suchausschnitt).

### Inferences
- Für ein eigenes Präfix-Modell (Präfix je Sammlung plus Nummer) ist das Muster "Präfix plus Zähler, Zähler nie wiederverwendet" die übliche Form. Die Quellen belegen aber nicht ausdrücklich, dass Nummern nach Löschung nie wiederverwendet werden. Ob Löschen Lücken erzeugt, ist offen.
- Ein Verschieben in einen anderen Bereich (Linear-Team, GitHub-Repo) vergibt bei Linear und vermutlich bei GitHub neue Nummern, die alte ID bleibt auflösbar (bei Linear belegt, bei GitHub nur für Verlinkung nicht geprüft).

### Gaps
- Notion, Trello, Asana, OpenProject, Taiga: keine ID-Regel gefunden.
- Ob Jira-Nummern nach Löschung wiederverwendet werden: nicht belegt.
- Linear: interne Zählweise (lückenlos oder nicht) nicht belegt.
- GitHub: Renummerierung bei Transfer nicht offiziell belegt.

## Wie wird Verlauf gehalten (Audit-Log, Feldänderungen)?

### Takeaway
Jira führt pro Vorgang eine History (Feldänderungen mit Zeitpunkt und Benutzer) und ein Systemaudit-Log für Konfigurationsänderungen. GitHub hält Verlauf im Issue-Timeline; Abschlussgründe sind ein Feld. Trello archiviert statt zu löschen; Löschen ist endgültig und setzt Archivierung voraus. Für die übrigen Tools fand ich keine ausreichende Quelle zum Verlauf.

### Cited Findings
- Jira Cloud: Jeder Vorgang hat im Activity-Bereich einen Reiter History mit Feldänderungen (z. B. Status, Verantwortlicher, Priorität). Quelle: [Atlassian Community, Jira issue history (Suchausschnitt)](https://community.atlassian.com/forums/discussion/3172230/jira-issue-history-how-to-track-filter-and-group-field-changes) (Community, nicht offiziell; Suchausschnitt).
- Jira: Das Audit-Log unter Settings > System (Recht "Administer Jira") erfasst Konfigurationsänderungen, nicht vollständig alle Aktivität. Quelle: [Atlassian, Audit log events in Jira (Server)](https://confluence.atlassian.com/adminjiraserver0819/audit-log-events-in-jira-1085207318.html) und [Atlassian, Auditing in Jira applications (Cloud)](https://confluence.atlassian.com/adminjiracloud/auditing-in-jira-applications-818578846.html) (Suchausschnitte).
- Jira Data Center: REST-API liefert den Verlauf mit `expand=changelog`. Quelle: [Atlassian KB, How to analyze the history or changelog of an issue](https://support.atlassian.com/jira/kb/how-to-analyze-the-history-or-changelog-of-an-issue-in-jira/) (Suchausschnitt, Data Center, Jira 8/9).
- GitHub: Beim Schließen wird ein Grund gesetzt: completed, not planned, duplicate; "reopened" ist ein eigener Wert im offenen Zustand. Quelle: [gh issue close, man page](https://manpages.opensuse.org/Tumbleweed/gh/gh-issue-close.1.en.html) (Suchausschnitt) und GraphQL-Schema [jsr.io, IssueStateReason](https://jsr.io/@luxass/github-schema/doc/~/IssueStateReason) (Drittanbieter-Dokumentation des Schemas). Der Grund "not planned" wurde laut Issue-Diskussion im Mai 2022 eingeführt (älter; [actions/stale #744](https://redirect.github.com/actions/stale/issues/744)).
- GitHub REST: Bei PATCH ohne Angabe von state_reason wird laut Drittanbieter-Workflow "completed" gesetzt (nicht offiziell belegt). Quelle: [tessl.io, GitHub issues bug workflow](https://tessl.io/registry/testland/github-issues-bug-workflow/files) (Drittanbieter, Suchausschnitt).
- Trello: Archivieren statt Löschen. Eine archivierte Liste erscheint nicht auf dem Board, ebenso wenig die darin enthaltenen Karten; Rückholung über das Board-Menü. Löschen ist nur für bereits archivierte Karten möglich; Löschen gilt als endgültig. Quellen: [Atlassian, Archive or delete a card](https://support.atlassian.com/trello/docs/archiving-and-deleting-cards) und [Atlassian, Archiving lists, deleting lists](https://support.atlassian.com/trello/docs/archiving-lists-deleting-lists) (Suchausschnitte). Ein Community-Guide nennt "kein zweiter Papierkorb" (Community, nicht offiziell).
- Trello REST API: eigene Endpunkte, um alle Karten einer Liste zu archivieren und Listen zu archivieren/entarchivieren. Quelle: [Trello REST API, Lists](https://developer.atlassian.com/cloud/trello/rest/api-group-lists/) (Suchausschnitt).
- Taiga: Status mit Flag "Archived" werden auf dem Kanban-Board eingeklappt, bleiben aber erhalten. Quelle: [Taiga Community, Customisation for your projects](https://community.taiga.io/t/customisation-for-your-projects/127) (Forum, Suchausschnitt).
- Redmine: Status "Issue closed" statt Löschen (siehe Status-Abschnitt). Quelle: [Redmine Wiki](https://www.redmine.org/projects/redmine/wiki/RedmineIssueTrackingSetup) (Suchausschnitt).

### Inferences
- Das Muster "nichts löschen" wird über drei Wege gelöst: Abschlussflag (Redmine, Taiga, Linear Canceled), Abschlussgrund (Jira Resolution, GitHub state_reason) und Archivierung (Trello). Die Quellen belegen aber nicht, dass ein Tool das Löschen ausdrücklich verbietet; sie zeigen nur, dass Löschen nicht der Normalweg ist.
- Ein Feldverlauf ist bei Jira nativ vorhanden, bei Trello und Taiga nur als Aktivität/Archiv. Vollständiger Feldverlauf mit alt/neu-Werten ist in den geprüften Quellen nur bei Jira belegt.

### Gaps
- Linear, Asana, Notion, OpenProject, Redmine (Journal/Historie) und Taiga: kein belegter Feldverlauf aus einer abgerufenen Seite.
- Jira Cloud: aktueller Stand der REST-Changelog-Dokumentation nicht geprüft (Suchergebnisse nur Server/DC und Drittanbieter).
- Keine Quelle, ob Trello, Asana oder Notion Papierkorb- oder Wiederherstellungsfristen haben (Notion-Papierkorb nicht geprüft).
- Keine Quelle zu Aufbewahrung oder Audit-Pflichten (z. B. Revisionssicherheit), nur Produktfunktionen.
