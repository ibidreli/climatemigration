# MSS Mini-Challenge – Projektübersicht

**Modul:** Modellierung und Simulation komplexer Systeme  
**Team:** Rodrigo Urech, Elias Pulver

## Projektthema

**Thema:** Klimabedingte Migration in der Sahel-Zone

**Leitfrage:**

> Wie beeinflussen Dürre, Wasserknappheit und Ernteausfälle die Abwanderungsrate, und welche Rückwirkungen hat die Abwanderung auf die lokale Bevölkerung und Landwirtschaft?

**Region:** Sahel-Zone, spätere Eingrenzung auf eine ausgewählte Teilregion

---

## Modellierungsansatz

Für unser Zweierteam bearbeiten wir:

- **LE1 – Systemkartierung** *(vollständig)* – System erfassen
- **LE2 – Systemdynamik** *(vollständig)* – System vereinfachen und simulieren
- **LE4 – Szenario- und integrierte Analyse** *(Lösungsskizze)* – Szenarien ableiten

---

### LE1 – Systemkartierung

**Systemkartierung** stellt wichtige Faktoren, Akteure und Zusammenhänge des Systems übersichtlich dar.

Geplante Artefakte:

- **Causal Loop Map:** Zeigt wichtige Grössen, Einflüsse und Rückkopplungen.
- **Stakeholder Map:** Zeigt relevante Akteure und ihre Rollen.
- **Systemgrenzen:** Legen fest, was zum betrachteten System gehört.
- **Cluster System Map oder Connected Circle Map:** Strukturiert wichtige Systemelemente und ihre Zusammenhänge.

Mögliche Themenbereiche:

- Klima und Umwelt
- Wasserverfügbarkeit
- Landwirtschaft und Ernährung
- wirtschaftliche Situation
- Bevölkerung und Abwanderung
- soziale Netzwerke
- politische und institutionelle Faktoren

Das System wird zunächst breit betrachtet und für LE2 gezielt vereinfacht.

---

### LE2 – Systemdynamik

**System Dynamics** untersucht, wie sich wichtige Grössen über die Zeit verändern und gegenseitig beeinflussen.

Wichtige Begriffe:

- **Stock:** Bestand, z.B. Bevölkerung oder Wasservorrat.
- **Flow:** Zu- oder Abnahme eines Stocks, z.B. Abwanderung.
- **Rückkopplung:** Veränderungen wirken über andere Grössen wieder auf das System zurück.

Aus dem Kausalkreisdiagramm aus LE1 wird ein vereinfachtes Simulationsmodell erstellt.

**Tool: BPTK-Py**

Python-Framework zur Erstellung und Simulation von System-Dynamics-Modellen.

Mögliche zentrale Grössen:

- Niederschlag / Dürre
- Wasserverfügbarkeit
- landwirtschaftlicher Ertrag
- Bevölkerung
- Abwanderungsrate

**Anfangszustand:** Ausgangslage der Simulation.  
**Modellparameter:** Bestimmen die Stärke der Zusammenhänge.

Werte werden soweit möglich aus realen Daten abgeleitet und Annahmen dokumentiert.

---

### LE4 – Szenario- und integrierte Analyse (Skizze)

Die **Szenarioanalyse** untersucht, wie sich das System unter unterschiedlichen zukünftigen Bedingungen entwickeln könnte.

Mögliche Szenarien:

- stärkere oder häufigere Dürren
- verbesserte Wasserversorgung
- veränderte landwirtschaftliche Erträge
- Massnahmen zur Verringerung klimabedingter Auswirkungen

**Beispiel für einen Übertragungskanal:**

Dürre → weniger Wasser → geringerer Ernteertrag → höhere Abwanderungsrate → Veränderungen bei Bevölkerung und Landwirtschaft

Für LE4 wird keine vollständige Simulation umgesetzt, sondern eine mögliche Szenarioanalyse skizziert.