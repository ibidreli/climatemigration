# MSS Mini-Challenge – Projektübersicht

**Modul:** Modellierung und Simulation komplexer Systeme  
**Team:** Rodrigo Urech, Elias Pulver

## Projektthema

### Klimabedingte Migration in der Sahel-Zone

**Leitfrage:**

> Wie beeinflussen Dürre, Wasserknappheit und Ernteausfälle die Migration in der Sahel-Zone, und welche Rückwirkungen hat Migration auf die betroffenen Regionen?

**Region:** Sahel-Zone

---

## Modellierungsansatz

Das Projekt wird über mehrere Lerneinheiten schrittweise konkretisiert.

Grundprinzip ist, das System in LE1 zunächst möglichst vollständig zu erfassen und erst für die nachfolgenden Modelle gezielt zu vereinfachen.

### LE1 – Systemkartierung

**Systemkartierung** hilft dabei, ein komplexes System übersichtlich darzustellen. Dabei werden wichtige Faktoren, beteiligte Akteure und ihre Zusammenhänge sichtbar gemacht, bevor daraus später ein Simulationsmodell erstellt wird.

Ziel ist ein breites Verständnis des Systems und seiner wichtigsten Zusammenhänge.

Geplante Artefakte:

- **Causal Loop Map / Kausalkreisdiagramm:** Zeigt wichtige Grössen und wie diese sich gegenseitig beeinflussen. Daraus können verstärkende oder abschwächende Rückkopplungen entstehen.

- **Stakeholder Map:** Zeigt die wichtigsten beteiligten oder betroffenen Akteure des Systems, z.B. Haushalte, Regierungen oder Hilfsorganisationen, und hilft dabei, deren Rollen und Beziehungen einzuordnen.

- **Systemgrenzen:** Legen fest, welche Teile des realen Systems im Modell berücksichtigt werden und welche ausserhalb liegen.

- **Cluster System Map:** Sammelt und gruppiert wichtige Elemente eines Systems. Sie dient dazu, ein komplexes Problem zunächst breit zu erfassen und erste Zusammenhänge sichtbar zu machen.

- **Connected Circle Map:** Stellt wichtige Elemente eines Systems in einem Kreis dar und verbindet diese anhand ihrer Beziehungen miteinander.

Mögliche Themenbereiche der Systemkarte:

- Klima und Umwelt
- Wasserverfügbarkeit
- Landwirtschaft und Ernährung
- wirtschaftliche Situation
- Bevölkerung und Migration
- soziale Netzwerke
- politische und institutionelle Faktoren

Die Komplexität wird zunächst bewusst beibehalten. Die Vereinfachung erfolgt insbesondere beim Kausalkreisdiagramm, das als Grundlage für LE2 dient.

---

### LE2 – Systemdynamik

**System Dynamics** untersucht, wie sich wichtige Grössen eines Systems über die Zeit verändern und gegenseitig beeinflussen.

Wichtige Begriffe:

- **Stock:** Ein Bestand, der sich über die Zeit verändern kann, z.B. Bevölkerung oder Wasservorrat.

- **Flow:** Eine Zu- oder Abnahme eines Stocks, z.B. Migration oder Wasserverbrauch.

- **Rückkopplung:** Eine Veränderung wirkt auf andere Grössen und kann später wieder auf die ursprüngliche Grösse zurückwirken.

Aus dem Kausalkreisdiagramm aus LE1 wird ein vereinfachtes Simulationsmodell erstellt.

**Tool: BPTK-Py**

BPTK-Py ist ein Python-Framework für die Erstellung von Simulationsmodellen. Damit können Stocks, Flows und ihre Zusammenhänge in Python definiert und über einen bestimmten Zeitraum simuliert werden. Die Ergebnisse können anschliessend beispielsweise als Tabellen oder Diagramme ausgewertet werden.

Mögliche zentrale Grössen:

- Wasserverfügbarkeit
- landwirtschaftlicher Ertrag
- Bevölkerung
- Migration
- lokale Resilienz

**Anfangszustand:** Gibt an, wie das System zu Beginn der Simulation aussieht, z.B. wie gross die Bevölkerung am Anfang ist.

**Modellparameter:** Legen fest, wie stark bestimmte Zusammenhänge wirken, z.B. wie stark sinkende Ernteerträge die Migration beeinflussen.

Die Anfangswerte und Parameter sollen soweit möglich aus realen Daten abgeleitet werden. Falls Annahmen notwendig sind, werden diese dokumentiert.

Ziel ist es zu untersuchen, wie sich die wichtigsten Grössen des Systems über die Zeit entwickeln.

---

### LE3 – Agentenbasierte Modellierung

**Agentenbasierte Modellierung (ABM)** untersucht, wie sich das Verhalten einzelner Akteure auf das gesamte System auswirkt.

Dabei werden einzelne **Agenten** mit eigenen Eigenschaften und Regeln erstellt. Diese Agenten können Entscheidungen treffen und miteinander oder mit ihrer Umgebung interagieren.

Für unser Modell könnten **Haushalte die Agenten** darstellen.

Eine Migrationsentscheidung könnte zum Beispiel von folgenden Faktoren abhängen:

- Klimastress
- wirtschaftliche Situation
- verfügbare Ressourcen
- soziale Netzwerke

**Tool: Mesa**

Mesa ist ein Python-Framework für agentenbasierte Simulationen. Damit können Agenten, ihre Eigenschaften, ihre Regeln und ihre Interaktionen programmiert und simuliert werden.

Ziel ist es zu untersuchen, wie aus den Entscheidungen einzelner Haushalte grössere Muster entstehen, z.B. steigende oder sinkende Migration.

Die genaue Modelllogik wird erst auf Basis der Ergebnisse aus LE1 und LE2 festgelegt.

---

### LE4 – Szenario- und integrierte Analyse

Bei einer **Szenarioanalyse** wird untersucht, wie sich das System unter verschiedenen zukünftigen Bedingungen entwickeln könnte.

Mögliche Szenarien:

- stärkere oder häufigere Dürren
- verbesserte Wasserversorgung
- Veränderungen landwirtschaftlicher Erträge
- Massnahmen zur Erhöhung der lokalen Resilienz

Bei der **integrierten Analyse** wird betrachtet, wie Veränderungen in einem Bereich Auswirkungen auf andere Bereiche haben.

Ein Beispiel wäre:

Dürre → weniger Wasser → geringere Ernte → höherer Migrationsdruck

Solche Wirkungsketten werden als **Übertragungskanäle** bezeichnet.

Die konkreten Szenarien werden erst festgelegt, wenn die Modelle aus den vorherigen Lerneinheiten entwickelt wurden.

---

## Datenquellen

Mögliche Datenquellen werden während der Modellierung geprüft und konkretisiert.

| Quelle | Mögliche Verwendung |
|---|---|
| **CHIRPS** | Niederschlags- und Dürredaten |
| **FEWS NET** | Landwirtschaft und Ernährungssicherheit |
| **UNHCR / IDMC** | Migration und Vertreibung |
| **World Bank** | Sozioökonomische und migrationsbezogene Daten |
| **ACLED** | Konfliktdaten als möglicher Kontextfaktor |

Die Daten können zur Bestimmung von Anfangswerten und Modellparametern sowie zur Überprüfung der Simulationsergebnisse verwendet werden.

