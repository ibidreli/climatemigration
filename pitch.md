# **MSS Mini-Challenge — Projektübersicht**

**Modul:** Modellierung und Simulation komplexer Systeme (FHNW, Angewandte Data Science)
**Team:** Zweierteam
**Zielnote:** 5.5–6.0
**Abgabeumfang (Zweierteam):** LE1 (voll) + LE2 (voll) + LE3 (skizziert)

---

## **1. Modul-Rahmendaten**

- Typ: Portfolio, Niveau Intermediate, 3 Credits
- Kompetenznachweis: 2 Teile, je 50% der Modulnote
  1. Abgabe der Mini-Challenge-Ergebnisse (Jupyter-Notebook oder R-Markdown)
  2. Mündliche Modulschlussprüfung zur abgegebenen Challenge
- Zweierteam-Prüfungsdauer: 40 Minuten
- Empfehlung: laufende Abgabe/Feedback über GitLab-Repo (ein Repo für alle LEs)

**Wichtige Termine:**

| Meilenstein | Datum |
|---|---|
| Kick-off | 15.09.2026 |
| Deep Dive | 19.10.2026 |
| Vorabgabe Mini-Challenges | laufend bis 17.11.2026 |
| Feedback zu Mini-Challenges | laufend bis 01.12.2026 |
| Formative Prüfung | 01.–15.12.2026 |
| Abgabe Mini-Challenges | 15.12.2026 |
| Mündliche Prüfungen | ab Semesterende |

---

## **2. Projektthema: Klimabedingte Migration in der Sahel-Zone**

**Fragestellung:** Wie beeinflusst zunehmender Klimastress (Dürre, Ernteausfälle, Wasserknappheit) individuelle Migrationsentscheidungen, und welche Rückkopplungen entstehen zwischen Migration, lokaler Resilienz und weiterem Klimastress?

**Region:** Sahel-Zone (Mali, Niger, Burkina Faso)

Begründung der Regionalwahl:
- Gut dokumentierte Push-Faktoren (Dürreperioden, Ernteausfälle, Wasserknappigkeit)
- Reichhaltige offene Datenlage (siehe Abschnitt 6)
- Überschaubare Anzahl Distrikte für die Agentensimulation
- Vom World Bank Groundswell Report als stark von klimabedingter Binnenmigration betroffene Region identifiziert

Fallback-Alternative: Bangladesch (Meeresspiegelanstieg, Zyklone) — falls sich die Sahel-Datenlage im Detail als lückenhaft erweist.

---

## **3. LE1 — Systemkarte (voll, offizielle Pflichtabgabe)**

Gemäss offizieller Mini-Challenge-Beschreibung ("Von der vage umrissenen Sorge zur Systemkarte") besteht die Abgabe aus folgenden **Pflicht-Artefakten**:

1. **Causal Loop Map** mit Identifikation der wichtigsten verstärkenden und abschwächenden Schleifen
2. **Stakeholder Map**
3. **Definition der Systemgrenzen**
4. Eine Karte, die den Gedankenprozess fassbar macht — **Connected Circle Map** oder **Cluster System Map**

Optional/empfohlen: Darstellung in Graphdatenbank/Darstellungswerkzeug, Exploration der Kausalschleifen-Dynamik in Loopy.

### 3.1 Causal Loop Map — Inhalte

**Push-Faktoren:**
- Dürre / Niederschlagsdefizit
- Ernteausfälle und Ernährungsunsicherheit
- Wasserknappheit
- Bodendegradation
- Ressourcenkonflikte (klimaverstärkt)

**Pull-Faktoren:**
- Wirtschaftliche Chancen in Zielregionen (urbane Zentren, Küstenstädte, Ausland)
- Bestehende soziale Netzwerke / Diaspora
- Politische Stabilität der Zielregion

**Zentrale Rückkopplungsschleifen:**
1. Dürre → Ernteausfall → Migration → Remittances → erhöhte lokale Resilienz → reduzierter Migrationsdruck (abschwächende Schleife, B)
2. Migration → Verlust an Arbeitskräften in der Landwirtschaft → sinkende lokale Erträge → mehr Migrationsdruck (verstärkende Schleife, R)
3. Diaspora-Netzwerke → sinkende Migrationskosten (Information, Unterkunft) → höhere Folgemigration (verstärkende Schleife, R, "network effect")

### 3.2 Stakeholder Map — Beteiligte

- Migrierende Haushalte / zurückbleibende Familienmitglieder
- Lokale Regierungen (Herkunfts- und Zielregionen)
- Internationale Organisationen (UNHCR, IOM, World Bank)
- NGOs vor Ort (humanitäre Hilfe, Entwicklungszusammenarbeit)
- Diaspora-Gemeinschaften in Zielregionen
- Landwirtschaftliche Gemeinschaften / lokale Wirtschaft

### 3.3 Systemgrenzen

- Räumlich: definierte Distrikte innerhalb Mali, Niger, Burkina Faso (Herkunftsregionen) sowie ausgewählte urbane Zielregionen
- Zeitlich: historische Kalibrierungsperiode + Zukunftshorizont mehrerer Jahrzehnte (konsistent mit LE2/LE3)
- Nicht modelliert (Umgebung): globale Wirtschaftskrisen, bewaffnete Konflikte als exogene Schocks (nur als Kontextfaktor, nicht endogen simuliert)

### 3.4 Connected Circle Map / Cluster System Map

Gruppierung der Schlüsselfaktoren in Cluster: Klima/Umwelt, Wirtschaft/Ressourcen, Soziales/Netzwerke, Politik/Institutionen — mit Wechselwirkungen zwischen den Clustern visualisiert.

---

## **4. LE2 — Systemdynamiksimulation (voll, offizielle Pflichtabgabe)**

Gemäss offizieller Mini-Challenge-Beschreibung ("Von der Systemkarte zur Systemdynamik"), empfohlenes Tool: **BPTK-Py**, integriert in Jupyter Notebook.

**Pflicht-Checkliste der Abgabe:**

1. Simulationsmodell mit Anfangszustand (implementiert in BPTK-Py)
2. Angabe der Systemgrenzen (Bezug zur Systemkarte aus LE1)
3. Graphik der zeitlichen Entwicklung der wesentlichen Systemeigenschaften
4. Kurze Aufzählung der Anfangswerte/Modellparameter mit Annahmen/Datenquellen
5. Backtest gegenüber historischen Daten oder postulierten Werten
6. Aus der Simulation gewonnene Erkenntnisse
7. Kausalschleifen des simulierten Systems (optional: mit berechneten Gewichtungen)

**Zu beantwortende Leitfragen (laut Vorgabe):**
- Welche Problemstellung(en)? Welche Kenngrössen? Braucht es Szenarien?
- Systemgrenzen? Umgebung?
- Stocks und Flows? Welche Kausalschleifen werden abgedeckt?
- Zeithorizont? Zeitschritt?
- Wie werden Anfangszustand/Parameter bestimmt?
- Wie entwickeln sich die Kenngrössen in der Zukunft? Erkenntnisse?
- Backtest-Validierung?

### 4.1 Modellentwurf für unser Projekt

**Stocks:**
- Wasserverfügbarkeit (pro Distrikt)
- Bodenqualität
- Nahrungsmittelvorräte
- Bevölkerung im Distrikt (als kumulativer Stock, der durch Migration ab-/zunimmt)

**Flows:**
- Niederschlag (Zufluss zu Wasserverfügbarkeit)
- Verdunstung/Verbrauch (Abfluss)
- Landwirtschaftlicher Ertrag (abhängig von Wasserverfügbarkeit und Bodenqualität)
- Migrationsrate (Abfluss aus Bevölkerungs-Stock, abhängig von Klimastress-Index)
- Remittance-Zufluss (Rückkopplung auf lokale Resilienz/Nahrungsmittelvorräte)

**Zeithorizont:** Jahrzehnte, Zeitschritt: Jahre (konsistent mit verfügbaren Klimadaten wie CHIRPS)

**Anfangszustand/Parameter:** aus historischen Niederschlags- und Ernteertragsdaten (FEWS NET, CHIRPS) abgeleitet

**Backtest:** Vergleich simulierter Migrations-/Vertreibungszahlen gegen historische UNHCR/IDMC-Daten für den betrachteten Zeitraum

**Kausalschleifen im Modell:** identisch zu LE1, ggf. mit aus der Simulation berechneten Gewichtungen ergänzt

---

## **5. LE3 — Agentenbasierte Modellierung (nur skizziert)**

Da für ein Zweierteam nur eine Lösungsskizze nötig ist, reicht hier eine schrittweise Lösungsstrategie und Auswertungsstrategie sowie die Identifikation der Datenquellen — keine vollständige Implementierung.

**Skizze:**

- **Agenten:** Haushalte in den Distrikten aus LE1/LE2
- **Agenteneigenschaften:** Vermögen/ökonomischer Puffer, Haushaltsgrösse, Risikoaversion, Diaspora-Bindung, Distanz zu Zielregionen
- **Zielfunktion:** Schwellenwert- oder Nutzenfunktion aus Klimastress (Output von LE2), ökonomischem Puffer, Risikoaversion, Netzwerkstärke
- **Interaktion:** Informationsaustausch innerhalb Distrikt, Remittances von migrierten zu verbliebenen Haushaltsmitgliedern
- **Aktivierung/Zeit/Ort:** diskrete Jahresschritte, räumliches Gitter/Graph der Distrikte mit Distanzen als Migrationskosten
- **Geplantes Tool:** Mesa (Python)
- **Validierungsstrategie:** Backtest gegen historische UNHCR/IDMC-Vertreibungszahlen (analog LE2)

---

## **6. LE4 — Szenario-/integrierte Analysemodelle (ausserhalb des Abgabeumfangs)**

Für Zweierteams nicht Teil der Pflichtabgabe. Offizielle Mini-Challenge-Beschreibung für LE4 ist laut Modulseite noch in Entwicklung. Falls später relevant: mögliche Anknüpfung über CLIMADA oder NGFS-Klimaszenarien für Transitionsrisiken, die auf die Sahel-Region übertragen werden könnten.

---

## **7. Datenquellen**

| Quelle | Verwendung |
|---|---|
| World Bank Groundswell Report | Regionale Einordnung, Referenzwerte für Migrationsprognosen |
| UNHCR / IDMC (Internal Displacement Monitoring Centre) | Historische Vertreibungs-/Migrationszahlen zur Validierung (Backtest) |
| FEWS NET (Famine Early Warning Systems Network) | Ernteausfall- und Ernährungsunsicherheitsdaten |
| CHIRPS | Niederschlagsdaten für LE2-Anfangszustand/Parameter |
| ACLED | Konfliktdaten als zusätzlicher Kontextfaktor |

---

## **8. Werkzeuge**

- **LE1:** Systemkartierung — Miro/Kumu/Mermaid/yEd oder Papier+Stift, optional Loopy für Kausalschleifen-Exploration, optional Neo4j für Graphdatenbank-Darstellung
- **LE2:** BPTK-Py (empfohlen, Python-basiert, transparente Gleichungsdarstellung), integriert in Jupyter Notebook
- **LE3 (Skizze):** Mesa (Python, agentenbasierte Modellierung)
- **Repo:** GitLab-Repo für laufende Abgabe/Feedback über alle LEs hinweg

---

## **9. Zeitplan**

| Meilenstein | Datum | Inhalt |
|---|---|---|
| Kick-off | 15.09.2026 | Themenwahl |
| Deep Dive | 19.10.2026 | Offene methodische Fragen klären |
| LE1-Abgabe (Systemkarte) | bis ca. 01.11.2026 | Causal Loop Map, Stakeholder Map, Systemgrenzen, Cluster/Circle Map |
| LE2-Implementierung | bis ca. 10.11.2026 | BPTK-Py-Modell, Backtest, Erkenntnisse |
| LE3-Skizze | bis ca. 12.11.2026 | Lösungs- und Auswertungsstrategie, Datenquellen |
| Vorabgabe | bis 17.11.2026 | Zwischenstand einreichen (GitLab) |
| Verfeinerung nach Feedback | bis 01.12.2026 | Feedback einarbeiten |
| Formative Prüfung | 01.–15.12.2026 | Testlauf für mündliche Prüfung |
| Abgabe Mini-Challenges | 15.12.2026 | Finales Jupyter Notebook |

---

## **10. Elevator Pitch**

Wir modellieren klimabedingte Binnenmigration in der Sahel-Zone: Eine Systemkarte (LE1, voll) verankert die zentralen Rückkopplungen zwischen Klimastress, Migration, Remittances und lokaler Resilienz. Ein Systemdynamikmodell in BPTK-Py (LE2, voll) simuliert die Entwicklung von Wasserverfügbarkeit und landwirtschaftlichem Ertrag und leitet daraus einen Klimastress-Index ab, validiert per Backtest gegen historische UNHCR/IDMC-Vertreibungsdaten. Ergänzend skizzieren wir (LE3), wie ein agentenbasiertes Modell individuelle Haushaltsentscheidungen auf Basis dieses Klimastress-Index simulieren würde.

