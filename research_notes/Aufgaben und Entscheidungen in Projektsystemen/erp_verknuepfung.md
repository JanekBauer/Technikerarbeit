# ERP- und Anforderungssysteme: Verknüpfung von Aufgaben, Entscheidungen, Anforderungen und Änderungsdatensätzen

Zugriffsdatum aller Quellen: 2026-11-23. Quellen aus der Suche sind mit "(Suchausschnitt)" markiert: Die Seite selbst konnte nicht abgerufen werden (siehe Hinweis unten), die Aussage stammt aus der Zusammenfassung des Suchergebnisses und ist nicht am Originaltext geprüft.

**Hinweis zur Quellenlage:** Die Hosts docs.frappe.io, www.odoo.com, support.ptc.com, help.jamasoftware.com, docs.plm.automation.siemens.com und www.thecoresolution.com waren aus der Cloud-Sitzung nicht auflösbar (DNS-Fehler, vermutlich nicht in den erlaubten Netzwerkdomänen). Die Aussagen zu ERPNext, Odoo, Codebeamer, Jama, Polarion und ISO 9001 stützen sich deshalb nur auf Suchausschnitte. Vor einer Verwendung in der Arbeit sollten die Originalseiten gelesen werden. Die Adressen stehen unten unter den jeweiligen Punkten.

**Abgrenzung:** Keine der Quellen beschreibt eine Verknüpfung in genau der Kette Anforderung, Aufgabe, Entscheidung, Test/Nachweis, wie sie das Projekt nutzt. Die Befunde sind Bausteine dafür.

## Wie Tools Aufgaben, Anforderungen und Nachweise verknüpfen

### Takeaway
ERP-Projektmodule (ERPNext, Odoo, Dolibarr) verknüpfen Aufgaben mit Projekten und Aufgaben untereinander (Abhängigkeiten). Eine Verknüpfung zu Anforderungen oder Nachweisen ist dort nicht als Standard belegt. Requirements-Werkzeuge (Jama, codebeamer, Polarion) modellieren Rückverfolgbarkeit als typisierte Beziehungen zwischen Arbeitselementen. Ihr Kernmechanismus für Änderungsfolgen ist der "Suspect Link".

### Cited Findings
- ERPNext: Tasks sind über das Feld Project einem Projekt zugeordnet. Das Feld "Depends On" / "Dependent Tasks" blockiert den Abschluss einer Aufgabe, solange die Vorgänger-Aufgabe nicht fertig ist. Abhängigkeiten werden im Gantt-Diagramm angezeigt. — [docs.frappe.io, Tasks-Seite](https://docs.frappe.io/erpnext/tasks.md) (Suchausschnitt, Quelle aktuell laut Suchergebnis; ältere Manuals v12/v13 ebenfalls indexiert)
- ERPNext-Foren: Abhängigkeiten gehen beim Duplizieren eines Projekts oder einer Projektvorlage verloren. Nutzer fordern Abhängigkeitstypen wie in MS Project. — [discuss.frappe.io, Task dependencies in Projects and Project Templates](https://discuss.frappe.io/t/task-dependencies-in-projects-and-project-templates/58034) (Suchausschnitt, Community-Quelle, Datum unbekannt)
- Odoo (Dokumentation Version 18): Die Aufgabenabhängigkeit wird in den Einstellungen aktiviert; danach erscheint der Reiter "Blocked by" am Task. Unterauftrags-Tasks ("Sub-task"-Reiter) bilden eine Hierarchie. — [odoo.com 18.0 Project management](https://www.odoo.com/documentation/18.0/applications/services/project/project_management.html) (Suchausschnitt, offizielle Seite); Detailangaben aus [cybrosys.com Odoo 18 CE Tasks](https://www.cybrosys.com/odoo/odoo-books/v18-ce/project/tasks/) (Drittanbieter, Suchausschnitt, nicht offiziell)
- Odoo: Tasks können manuell oder automatisch erzeugt werden, z. B. aus E-Mails oder Website-Formularen. — [odoo.com 18.0 Task creation](https://www.odoo.com/documentation/18.0/applications/services/project/tasks/task_creation.html) (Suchausschnitt)
- Dolibarr: Das Projektmodul verwaltet Projekte als Hierarchie von Aufgaben, unterstützt benutzerdefinierte Felder und Dokumentvorlagen. Es bietet laut Wiki keine automatische Planung und keine Berechnung eines kritischen Pfads. Tabellen: `llx_projet` (Projekte), `llx_projet_task` (Aufgaben), `llx_projet_task_time` (Zeiten), `llx_element_contact` (Verknüpfung Aufgabe zu Benutzer/Kontakt). — [wiki.dolibarr.org, Module Projects](https://wiki.dolibarr.org/index.php/Module_Projects) und [Module Projects (developer)](https://wiki.dolibarr.org/index.php/Module_Projects_(developer)) (Suchausschnitt)
- Jama Connect: Beziehungen zwischen Anforderungen, Tests und anderen Elementen (Traceability). Ändert sich ein vorgelagertes Element, erhalten nachgelagerte verknüpfte Elemente einen Suspect Link. Ausgelöst wird er nur durch Änderungen an Feldern, die der Administrator je Item-Typ festlegt. — [help.jamasoftware.com, Clear suspect links](https://help.jamasoftware.com/en/manage-content/coverage-and-traceability/relationships/clear-suspect-links.html) und [Find suspect links](https://help.jamasoftware.com/ah/en/reference/quick-find/find-suspect-links.html) (Suchausschnitt)
- Jama: Ein Reviewer kann einen Suspect Link löschen (Clear), nachdem er die Auswirkung geprüft oder die nötigen Änderungen gemacht hat. Auffindbar über Project > Suspect links, über die Relationship Status Indicator und über Filter. — ebenda (Suchausschnitt)
- Jama, Community: Suspect-Markierung läuft nach Angabe von Jama-Mitarbeitern nur in Richtung nachgelagerter Elemente. — [Jama Community, Bi-directional traceability](https://community.jamasoftware.com/discussion/comment/7274/) (Community-Quelle, Datum unbekannt, Richtungsangabe ggf. veraltet)
- Jama, Change Management: Ein Change Request ist ein eigenes Element. Es sammelt die betroffenen Artefakte über einen vordefinierten Filter. Das Review-Paket zeigt Unterschiede. — [Jama Blog, Features in Five: Change Management, 2025-05-02](https://www.jamasoftware.com/blog/2025/05/02/jama-connect-features-in-five-change-management/) (Blog, Suchausschnitt, Werbematerial)
- codebeamer (PTC): Ein Baseline ist ein Snapshot von Anforderungen, Tracker-Elementen, Wiki-Seiten, Dokumenten, Kommentaren und Anhängen. Baselines lassen sich vergleichen; Änderungen werden mit Urheber und Zeitpunkt markiert. — [support.ptc.com, codebeamer Baseline](https://support.ptc.com/help/codebeamer/r2.2/en/codebeamer/cbx_user_guide/baseline.html) (Suchausschnitt, Release 2.2, älter)
- Polarion (Siemens): Ein Document Baseline ist eine Revision mit zusätzlichen Daten, z. B. einem vom Nutzer vergebenen Namen. Ein Workflow-Übergang kann automatisch einen Baseline erzeugen. Das Löschen einer Baseline entfernt die zugrundeliegende Revision nicht. — [docs.plm.automation.siemens.com, Document Baselines (Polarion 20)](https://docs.plm.automation.siemens.com/content/polarion/20/help/en_US/user_and_administration_help/user_guide/work_with_documents/document_baselines.html) (Suchausschnitt)
- Gotel und Finkelstein (ICRE 1994, Titel laut Suchergebnis): Die Autoren unterscheiden Traceability vor und nach der Anforderungsspezifikation (pre-RS und post-RS). Sie stellen fest, dass viele Traceability-Probleme auf eine unzureichende pre-RS-Traceability zurückgehen. Sie führen "Contribution Structures" ein, also das Netz der Personen, die an einem Anforderungsartefakt mitgewirkt haben. — [UCL Discovery, Eprint-Liste](https://discovery-pp.ucl.ac.uk/id/eprint/747/1/2.0_contrib.pdf) und [City Research Online](https://openaccess.city.ac.uk/id/eprint/26460/) (Suchausschnitt; Volltexte nicht gelesen; Älter: 1994)
- OpenReq: EU-Projekt Horizon 2020 (Laufzeit um 2016 bis 2019 laut Projektseite). Es liefert Empfehlungs- und Priorisierungs-Dienste als Microservices, die Projekt-Website nennt keine Änderungsprotokolle. — [GitHub OpenReqEU](https://github.com/OpenReqEU) und [CORDIS, Projekt 732463](https://cordis.europa.eu/project/id/732463/reporting) (Suchausschnitt; Älter)
- Ein anderes Werkzeug mit dem Namen "OpenReq" (SourceForge, Webanwendung für Anforderungsmanagement, GPLv2, Java) ist nicht identisch mit dem EU-Projekt. — [SourceForge, openreqmgmt](https://sourceforge.net/projects/openreqmgmt/) (Suchausschnitt)

### Inferences
- In den ERP-Modulen ist Verknüpfung in erster Linie Projekt-zu-Aufgabe und Aufgabe-zu-Aufgabe (Abhängigkeit). Eine Kette bis zu Anforderungs- oder Testnachweisen ist in den gefundenen Quellen nicht belegt.
- In den Requirements-Werkzeugen ist die Verknüpfung als typisierte Beziehung zwischen Elementen modelliert. Die Änderungsfolge läuft über Suspect Links.

### Gaps
- Keine Quelle, die Traceability-Kette Anforderung zu Aufgabe zu Entscheidung zu Testnachweis in einer ERP-Software beschreibt. Die Originalseiten von ERPNext und Odoo sind nicht abrufbar.
- Ob Odoo und ERPNext Aufgaben direkt an Anforderungen oder Qualitätspunkte koppeln können (z. B. Odoo Quality, ERPNext Quality Procedure/Quality Goal), wurde nicht geprüft.
- Die Richtung der Suspect-Markierung bei Jama ist nur durch eine Community-Aussage belegt.

## Änderungsprotokoll: alter Wert, neuer Wert, Grund, Version, Freigeber

### Takeaway
Die Systeme halten Änderungen an Datensätzen über Versionsprotokolle oder Revisionen fest. Die gefundenen Quellen belegen Versionsnummer, Urheber und Zeitpunkt. Ein eigenes Feld für den Änderungsgrund ist nicht belegt. Für Freigeber und Freigabeschritt liefert nur Odoo PLM eine Quelle mit Stufenmodell.

### Cited Findings
- ERPNext: Versionierung wird pro DocType aktiviert ("Track changes"). Für jede geänderte Instanz entsteht ein Version Log mit Links auf die einzelnen Versionen. — [docs.frappe.io, Document Versioning](https://docs.frappe.io/erpnext/document-versioning.md) (Suchausschnitt, Stand laut Suche aktuell; v13/v14-Versionen ebenfalls indexiert)
- ERPNext/Frappe: Das DocType "Version" wurde ursprünglich nur für Web Page und Blog Post genutzt und ab Version 7.3 für Dokumente erweitert. — [frappe.io Blog, Versioning and Audit Trail, 2017](https://frappe.io/blog/erpnext-features/versioning-and-audit-trail) (Suchausschnitt, älter, 2017)
- Frappe Framework, Audit Trail: Bei stornierten und wieder geänderten (amended) Belegen ändert sich der Dokumentname. Das Version-DocType verfolgt die Änderungen dann schwer. Das Audit Trail-Werkzeug zeigt höchstens 5 frühere Änderungsstände eines übermittelbaren Dokuments. — [docs.frappe.io, Audit Trail](https://docs.frappe.io/framework/user/en/audit-trail) (Suchausschnitt)
- Odoo PLM (Version 19.0): ECOs (Engineering Change Orders) erfassen, umsetzen und ggf. zurücknehmen von Änderungen an Produkten und Stücklisten. Standard-Stufen: New, In Progress, Validated, Effective. Stufen und ECO-Typen sind anpassbar. Genehmigungen sollen Änderungen vor der Umsetzung prüfen lassen. — [odoo.com 19.0, Engineering change orders](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/plm/manage_changes/engineering_change_orders.html) und [ECO types and stages](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/plm/manage_changes/eco_type.html) (Suchausschnitt)
- codebeamer: Jede Bearbeitung, jeder Kommentar und jeder Workflow-Übergang eines Tracker-Elements erzeugt eine neue Issue-Version mit eindeutiger Versionsnummer. Beim Wiederherstellen einer alten Version wird keine ältere Version gelöscht: Es entsteht eine neue Nummer mit dem alten Inhalt. — [support.ptc.com, Versioning and Access History (r3.0)](https://support.ptc.com/help/codebeamer/r3.0/en/codebeamer/user_guide/versioning_and_access_history.html) (Suchausschnitt, Release 3.0, älter); Tracker-Historie in Codebeamer X ebenfalls laut Suchausschnitt
- Polarion: Jede Revision eines Dokuments wird automatisch gespeichert; Baselines sind benannte Revisionen. — [Polarion Document Baselines](https://docs.plm.automation.siemens.com/content/polarion/20/help/en_US/user_and_administration_help/user_guide/work_with_documents/document_baselines.html) (Suchausschnitt)
- ISO 9001:2015, Klausel 8.5.6 (Lenkung von Änderungen): Der Standard verlangt dokumentierte Information über das Ergebnis der Änderungsprüfung, über die Person(en), die die Änderung autorisieren, und über notwendige Folgemaßnahmen. Die Prüfung erfolgt vor der Umsetzung. — Wortlaut laut Sekundärquelle: [thecoresolution.com, Clause 8.5.6](https://www.thecoresolution.com/clause-8-5-6-iso-9001-2015-explained) (Suchausschnitt, Beratungsseite; Originaltext nicht geprüft)
- ISO 9001 Klausel 6.3 (Planung von Änderungen am QMS) wird von 8.5.6 (Lenkung betrieblicher Änderungen) abgegrenzt. — ebenda (Suchausschnitt)

### Inferences
- Die gefundenen Systeme protokollieren Änderungen über Versionen mit Urheber und Zeitpunkt. Ein eigenes Feld "alter Wert / neuer Wert / Grund" pro Änderung ist in den Quellen nicht belegt. Es lässt sich nur indirekt aus dem Versionsvergleich ableiten.
- Die ISO-Anforderung (Ergebnis der Prüfung, Autorisierer, Folgemaßnahmen) ist ein brauchbares Mindestfeldset für einen Änderungsdatensatz. Sie ist aus einer Beratungsquelle entnommen und sollte am Originaltext geprüft werden.

### Gaps
- Keine Quelle zu einem Änderungsfeld "Grund" in ERPNext, Odoo, Dolibarr, Jama, codebeamer oder Polarion gefunden.
- Keine Quelle zu Versionsnummer-Schemata für Anforderungen (z. B. Revisionsbuchstabe A, B, C oder Major.Minor) gefunden. Ob Odoo ECO Revisionen auf Stücklisten mit Nummern zählt, ist nicht bestätigt.

## Nummerierung: Präfixe, Sequenzen, Revisionen

### Takeaway
ERPNext vergibt Nummern über "Naming Series" mit Präfix, Datumsbestandteilen und Zähler (z. B. `ACC-SINV-.YYYY.-`). Die Zählung lässt sich auf einen bestehenden Stand setzen. Requirements-Werkzeuge vergeben Nummern meist automatisch an Elemente, und Revisionen laufen über Versionen oder Baselines. Revisionsbuchstaben sind in den gefundenen Quellen nicht belegt.

### Cited Findings
- ERPNext: Naming Series mit Präfix und Formatzeichen (`.YYYY.`, `####`, Feldwerte wie `.vendor_id.`). Konfiguration unter Settings > Naming Series. Der erste Eintrag ist Standard. Die Option "User must always select" erzwingt eine Auswahl. — [docs.frappe.io, Naming series](https://docs.frappe.io/erpnext/naming-series) und [Document naming settings](https://docs.frappe.io/erpnext/document-naming-settings) (Suchausschnitt; Versionen v13/v14 ebenfalls indexiert)
- ERPNext: Der Zählerstand lässt sich pro Serie setzen, z. B. zum Übernehmen aus einem Altsystem. — [docs.frappe.io, naming series current value](https://docs.frappe.io/erpnext/naming-series-current-value) (Suchausschnitt)
- ERPNext: Die Nummerierung kann pro Firma getrennt sein (z. B. `SINV-A-0001`). Amendierte Belege erhalten über einen "Amend Counter" eigene Namen. — [docs.frappe.io, company wise naming series](https://docs.frappe.io/erpnext/company-wise-naming-series.md) (Suchausschnitt)
- ERPNext: Das "Document Naming Rule"-Feature wählt die Serie aufgrund von Feldbedingungen und fällt auf die Standardserie zurück. — [docs.frappe.io, Document naming](https://docs.frappe.io/erpnext/document-naming) (Suchausschnitt; neueres Feature)
- Odoo: Projekte sind in Aufgaben gegliedert, Aufgaben in Phasen (Kanban). Eine eigene Nummernlogik für Aufgaben ist in den gefundenen Quellen nicht beschrieben. — [odoo.com 18.0 Project management](https://www.odoo.com/documentation/18.0/applications/services/project/project_management.html) (Suchausschnitt)
- Odoo PLM: ECO-Typen und -Stufen sind frei definierbar. — [odoo.com 19.0, ECO types and stages](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/plm/manage_changes/eco_type.html) (Suchausschnitt)
- Dolibarr: Nummerierung von Projekten und Aufgaben nicht belegt; Dokumentmodelle für Berichte vorhanden. — [wiki.dolibarr.org, Module Projects](https://wiki.dolibarr.org/index.php/Module_Projects) (Suchausschnitt)
- Polarion: Dokumentrevisionen werden automatisch gezählt; Baselines erhalten einen Namen und optional eine Revisionsnummer in einem Custom-Feld (Community-Erweiterung "Create Baseline"). — [Polarion Document Baselines](https://docs.plm.automation.siemens.com/content/polarion/20/help/en_US/user_and_administration_help/user_guide/work_with_documents/document_baselines.html) und [extensions.polarion.com, Workflow Function: Create Baseline](https://extensions.polarion.com/extensions/61-workflow-function-create-baseline) (Suchausschnitt; Community-Erweiterung)

### Inferences
- Das übliche Muster in ERP-Systemen ist Präfix plus Zähler, optional mit Jahr oder Firmenkennung. Das passt zum Muster des Projekts (Präfix je Sammlung plus dreistellige Nummer), ist aber ohne Revisionsteil.
- Revision wird in den Quellen über Versionen (Codebeamer, Polarion) oder Baselines abgebildet, nicht über Buchstaben.

### Gaps
- Keine Quelle zu Revisionsbuchstaben (A, B, C) oder zu Revisionskennzeichnung nach ISO/IEC-Konfigurationsmanagement gefunden. Die Suche danach wurde nicht durchgeführt.
- Keine Angabe, ob gelöschte Nummern wiederverwendet werden (ERPNext-Zähler laufen nur vorwärts laut Suchausschnitt, nicht bestätigt).

## Umgang mit gelöschten und veralteten Datensätzen

### Takeaway
Die Quellen zeigen zwei Muster: Stornieren oder Amendieren (ERPNext) und Wiederherstellen als neue Version (codebeamer). Polarion bleibt beim Löschen einer Baseline die Revision erhalten. Ein allgemeines Statusmodell "entfallen / ersetzt durch" ist nicht belegt.

### Cited Findings
- ERPNext: Amendierte Belege erhalten einen neuen Namen; die Verfolgung über das Version-DocType wird dadurch erschwert. — [docs.frappe.io, Audit Trail](https://docs.frappe.io/framework/user/en/audit-trail) (Suchausschnitt)
- codebeamer: Ältere Versionen werden beim Wiederherstellen nicht überschrieben; es entsteht eine neue Versionsnummer. — [support.ptc.com, Versioning and Access History r3.0](https://support.ptc.com/help/codebeamer/r3.0/en/codebeamer/user_guide/versioning_and_access_history.html) (Suchausschnitt)
- Polarion: Das Löschen einer Baseline lässt die Revision bestehen. Gelöschte Work Items lassen sich über die Versionshistorie des Speichers zurückholen (per SVN-Client, nicht über die Oberfläche). — [Polarion Document Baselines](https://docs.plm.automation.siemens.com/content/polarion/20/help/en_US/user_and_administration_help/user_guide/work_with_documents/document_baselines.html) und [Siemens Blog, Recovering deleted Polarion data](https://blogs.sw.siemens.com/polarion/recovering-deleted-polarion-data-part-1-of-2/) (Suchausschnitt)
- Jama: Suspect Links werden geklärt (Clear), nicht gelöscht. — [help.jamasoftware.com, Clear suspect links](https://help.jamasoftware.com/en/manage-content/coverage-and-traceability/relationships/clear-suspect-links.html) (Suchausschnitt)
- Odoo PLM: ECOs können "zurückgenommen" werden (Revert). Der genaue Mechanismus ist nicht belegt. — [odoo.com 19.0, Engineering change orders](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/plm/manage_changes/engineering_change_orders.html) (Suchausschnitt)

### Inferences
- Die Projektregel (Löschen nur über Vorschlag, bei Verweisen Status "entfallen") entspricht dem Muster "nicht löschen, sondern als ungültig markieren". Die gefundenen Systeme nutzen dagegen Versionen und Stornierung, nicht ein eigenes Status-Feld.

### Gaps
- Keine Quelle, die für Anforderungen oder Entscheidungen ein Status-Feld "obsolet / ersetzt durch" mit Nachfolge-Verweis beschreibt.
- Das Verhalten beim Löschen von Aufgaben mit Verweisen in ERPNext oder Odoo ist nicht geprüft.

## Freigabe- und Genehmigungsworkflow vor einer Änderung

### Takeaway
Odoo PLM bildet ECOs als Stufenmodell mit Genehmigung ab. ERPNext nutzt Dokumentstatus (Entwurf, übermittelt, storniert) und Workflows. Requirements-Werkzeuge nutzen Review-Pakete und Change Requests. Die konkrete Rollenverteilung (wer genehmigt) ist nur für ISO 9001 als Anforderung belegt.

### Cited Findings
- Odoo PLM: Die Standard-Stufen eines ECO sind New, In Progress, Validated, Effective. Genehmigungen erlauben den Stakeholdern, Änderungen vor der Umsetzung zu prüfen. — [odoo.com 19.0, ECO types and stages](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/plm/manage_changes/eco_type.html) und [Engineering change orders](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/plm/manage_changes/engineering_change_orders.html) (Suchausschnitt)
- Odoo PLM, Drittanbieter (Pokutsoft, bezahlt, Odoo 18): Ergänzt "submit", "start review", "approve stage", "apply", "close". — [apps.odoo.com, Engineering Change Order (ECO / PLM)](https://apps.odoo.com/apps/modules/18.0/engineering_change_order) (Suchausschnitt, Drittanbieter)
- Jama: Change Request mit Review-Paket, Impact Analysis und Versionsvergleich vor der Änderung. — [Jama Blog, Change Management, 2025](https://www.jamasoftware.com/blog/2025/05/02/jama-connect-features-in-five-change-management/) (Suchausschnitt)
- codebeamer: Baselines dienen als Vergleichsbasis vor und nach einer Änderung; PTC-Tutorial zum Vergleich von HEAD mit einer Baseline. — [community.ptc.com, Versioning and Baselines](https://community.ptc.com/t5/Codebeamer-Tips/Versioning-and-Baselines-Features-A-Guide-to-Change-Management/ta-p/989469) (Suchausschnitt, Community)
- Polarion: Workflow-Übergänge können Baselines automatisch erzeugen. — [Polarion Document Baselines](https://docs.plm.automation.siemens.com/content/polarion/20/help/en_US/user_and_administration_help/user_guide/work_with_documents/document_baselines.html) (Suchausschnitt)
- ISO 9001:2015, 8.5.6: Vor der Umsetzung prüfen, Personen benennen, die die Änderung autorisieren, Folgemaßnahmen festhalten. — [thecoresolution.com, Clause 8.5.6](https://www.thecoresolution.com/clause-8-5-6-iso-9001-2015-explained) (Suchausschnitt, Sekundärquelle)
- ERPNext: Dokumentstatus und Workflows sind vorhanden; Details nicht abgerufen. — [docs.frappe.io, Document Versioning](https://docs.frappe.io/erpnext/document-versioning.md) (Suchausschnitt, nur indirekt)

### Inferences
- Typischer Ablauf in den Quellen: Antrag (Change Request/ECO), Prüfung und Auswirkungsanalyse, Freigabe durch Befugte, Umsetzung, Abschluss. Der Ablauf lässt sich aus Odoo und Jama ableiten, nicht aus einer vollständigen Norm.

### Gaps
- Kein Nachweis, wie ERPNext oder Odoo Rollen für Freigeber trennen (Vier-Augen-Prinzip).
- Keine Quelle zum Vergleich mit einem Änderungsprozess ohne Software (Papier-Prozess).

## Intake / Eingang getrennt von freigegebenen Datensätzen

### Takeaway
Die Suche liefert wenig zu diesem Punkt. Odoo legt Tasks aus E-Mails oder Formularen automatisch an. Jama und Codebeamer trennen über Status, Reviews und Baselines zwischen Entwurf und freigegebenem Stand. Eine eigene Eingangsablage wie das Postfach des Projekts ist in den Quellen nicht belegt.

### Cited Findings
- Odoo 18: Tasks lassen sich manuell oder automatisch aus E-Mails und Website-Formularen erzeugen. — [odoo.com 18.0 Task creation](https://www.odoo.com/documentation/18.0/applications/services/project/tasks/task_creation.html) (Suchausschnitt)
- Odoo PLM: ECOs befinden sich in Stufen (New, In Progress, Validated, Effective); "Effective" markiert den freigegebenen Stand. — [odoo.com 19.0, ECO types and stages](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/plm/manage_changes/eco_type.html) (Suchausschnitt)
- codebeamer: Baselines frieren einen Stand ein; das Arbeitsstand (HEAD) bleibt davon getrennt. — [codebeamer Baseline](https://support.ptc.com/help/codebeamer/r2.2/en/codebeamer/cbx_user_guide/baseline.html) (Suchausschnitt)

### Inferences
- Die Trennung von Entwurf und freigegebenem Stand erfolgt in den Quellen über Stufen (Odoo) oder Baselines (codebeamer, Polarion). Das entspricht der Trennung zwischen Vorschlag und Übernahme im Projekt.

### Gaps
- Keine Quelle, die einen Eingangskorb für Vorschläge mit Übernahme durch eine berechtigte Person beschreibt.

## Quellenliste

- ERPNext Tasks: https://docs.frappe.io/erpnext/tasks.md (Zugriff 2026-11-23, Suchausschnitt; Originalseite nicht abrufbar)
- ERPNext Document Versioning: https://docs.frappe.io/erpnext/document-versioning.md (Zugriff 2026-11-23, Suchausschnitt)
- ERPNext Naming Series: https://docs.frappe.io/erpnext/naming-series (Zugriff 2026-11-23, Suchausschnitt)
- Frappe Audit Trail: https://docs.frappe.io/framework/user/en/audit-trail (Zugriff 2026-11-23, Suchausschnitt)
- Frappe Blog Versioning, 2017 (älter): https://frappe.io/blog/erpnext-features/versioning-and-audit-trail (Zugriff 2026-11-23, Suchausschnitt)
- Discuss Frappe, Task dependencies (Community): https://discuss.frappe.io/t/task-dependencies-in-projects-and-project-templates/58034 (Zugriff 2026-11-23, Suchausschnitt)
- Odoo 18 Project management: https://www.odoo.com/documentation/18.0/applications/services/project/project_management.html (Zugriff 2026-11-23, Suchausschnitt)
- Odoo 18 Task creation: https://www.odoo.com/documentation/18.0/applications/services/project/tasks/task_creation.html (Zugriff 2026-11-23, Suchausschnitt)
- Odoo 19 ECO: https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/plm/manage_changes/engineering_change_orders.html (Zugriff 2026-11-23, Suchausschnitt)
- Odoo 19 ECO types: https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/plm/manage_changes/eco_type.html (Zugriff 2026-11-23, Suchausschnitt)
- Cybrosys Odoo 18 Tasks (Drittanbieter): https://www.cybrosys.com/odoo/odoo-books/v18-ce/project/tasks/ (Zugriff 2026-11-23, Suchausschnitt)
- Apps Odoo, ECO Drittanbieter: https://apps.odoo.com/apps/modules/18.0/engineering_change_order (Zugriff 2026-11-23, Suchausschnitt)
- Dolibarr Module Projects: https://wiki.dolibarr.org/index.php/Module_Projects (Zugriff 2026-11-23, Suchausschnitt)
- Dolibarr Module Projects (developer): https://wiki.dolibarr.org/index.php/Module_Projects_(developer) (Zugriff 2026-11-23, Suchausschnitt)
- Jama Clear suspect links: https://help.jamasoftware.com/en/manage-content/coverage-and-traceability/relationships/clear-suspect-links.html (Zugriff 2026-11-23, Suchausschnitt)
- Jama Find suspect links: https://help.jamasoftware.com/ah/en/reference/quick-find/find-suspect-links.html (Zugriff 2026-11-23, Suchausschnitt)
- Jama Community, Bi-directional traceability: https://community.jamasoftware.com/discussion/comment/7274/ (Zugriff 2026-11-23, Suchausschnitt; Datum unbekannt)
- Jama Blog Change Management, 2025-05-02: https://www.jamasoftware.com/blog/2025/05/02/jama-connect-features-in-five-change-management/ (Zugriff 2026-11-23, Suchausschnitt)
- codebeamer Baseline (Release 2.2, älter): https://support.ptc.com/help/codebeamer/r2.2/en/codebeamer/cbx_user_guide/baseline.html (Zugriff 2026-11-23, Suchausschnitt)
- codebeamer Versioning and Access History (Release 3.0, älter): https://support.ptc.com/help/codebeamer/r3.0/en/codebeamer/user_guide/versioning_and_access_history.html (Zugriff 2026-11-23, Suchausschnitt)
- PTC Community, Versioning and Baselines: https://community.ptc.com/t5/Codebeamer-Tips/Versioning-and-Baselines-Features-A-Guide-to-Change-Management/ta-p/989469 (Zugriff 2026-11-23, Suchausschnitt)
- Polarion Document Baselines (Polarion 20): https://docs.plm.automation.siemens.com/content/polarion/20/help/en_US/user_and_administration_help/user_guide/work_with_documents/document_baselines.html (Zugriff 2026-11-23, Suchausschnitt)
- Siemens Blog, recovering deleted Polarion data: https://blogs.sw.siemens.com/polarion/recovering-deleted-polarion-data-part-1-of-2/ (Zugriff 2026-11-23, Suchausschnitt)
- Polarion Extensions, Create Baseline: https://extensions.polarion.com/extensions/61-workflow-function-create-baseline (Zugriff 2026-11-23, Suchausschnitt; Community-Erweiterung)
- Gotel/Finkelstein 1994, UCL Discovery: https://discovery-pp.ucl.ac.uk/id/eprint/747/1/2.0_contrib.pdf (Zugriff 2026-11-23, Suchausschnitt; älter, 1994)
- Gotel/Finkelstein, City Research Online: https://openaccess.city.ac.uk/id/eprint/26460/ (Zugriff 2026-11-23, Suchausschnitt)
- ISO 9001:2015 Klausel 8.5.6, Sekundärquelle: https://www.thecoresolution.com/clause-8-5-6-iso-9001-2015-explained (Zugriff 2026-11-23, Suchausschnitt; Originalnorm nicht geprüft)
- CORDIS OpenReq (EU-Projekt, älter): https://cordis.europa.eu/project/id/732463/reporting (Zugriff 2026-11-23, Suchausschnitt)
- OpenReq GitHub: https://github.com/OpenReqEU (Zugriff 2026-11-23, Suchausschnitt)
- SourceForge openreqmgmt: https://sourceforge.net/projects/openreqmgmt/ (Zugriff 2026-11-23, Suchausschnitt)

Nicht abgerufen (DNS-Fehler in der Sitzung): docs.frappe.io (Volltext), www.odoo.com (Volltext), support.ptc.com (Volltext), help.jamasoftware.com (Volltext), docs.plm.automation.siemens.com (Volltext), www.thecoresolution.com (Volltext). Diese Seiten müssen für die Arbeit nachgelesen werden, sobald die Domains in den Netzwerkeinstellungen der Sitzung freigegeben sind.
