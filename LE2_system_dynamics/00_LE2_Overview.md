# LE2 – Systemdynamik

## 1. Problemstellung und Systemgrenzen

### Untersuchungsgegenstand

Untersucht wird, wie sich Dürren auf die Abwanderung aus der Region Kaffrine (Senegal) auswirken und wie die Abwanderung auf Bevölkerung, Landwirtschaft und Versorgung zurückwirkt. Grundlage ist das Kernmodell der Causal Loop Map aus LE1. Das System wird mit BPTK-Py simuliert.

### Zentraler Zusammenhang

Niederschlag → landwirtschaftlicher Ertrag → Produktion → Einkommen und Nahrung pro Person → Abwanderung

Die Wasserverfügbarkeit wird vereinfacht über den Zusammenhang zwischen Niederschlag und Ertrag berücksichtigt. Ein eigener Wasserbestand wird nicht modelliert.

### Im Modell berücksichtigt

- Niederschlag (wirkt von aussen auf das System)
- landwirtschaftlicher Ertrag und Produktion
- Haushaltseinkommen und Nahrungsmittelverfügbarkeit pro Person
- Bevölkerung und natürliches Bevölkerungswachstum
- Abwanderung, abgewanderte Personen, Netzwerke und Rücküberweisungen
- Zuzug als einfacher Zufluss mit konstanter Rate

### Migrationsbegriff

Abgebildet wird dauerhafte Abwanderung, also ein Wechsel des Wohnorts über die Regionsgrenze. Grundlage ist das Fünfjahresfenster der Volkszählung. Saisonale und zirkuläre Migration sind nicht Teil des Modells.

### Ausserhalb des direkten Modellfokus

- konkrete Zielorte der Abwanderung
- Rückkehrmigration und saisonale Migration
- Lebensmittelpreise und wirtschaftliche Alternativen
- Bewässerung und staatliche Unterstützung
- Konflikte und politische Entwicklungen

Diese Faktoren können das System beeinflussen, werden aber nicht selbst detailliert modelliert. Bewässerung wird in LE4 als mögliche Massnahme betrachtet.

### Zeitliche Grenze

- **2013–2023:** Vergleich mit echten Daten (Backtest)
- **2024–2050:** Szenarien für die Zukunft
- **Zeitschritt:** 1 Jahr

## 2. Datengrundlage und Annahmen

### Niederschlag

- **Quelle:** CHIRPS
- **Zeitraum:** 1991–2023
- Jahresniederschlag als Mittel über ein Rechteck um Kaffrine
- Mittelwert 1991–2020 als Referenz für ein Normaljahr

### Bevölkerung und Abwanderung

- **Quelle:** ANSD, Volkszählungen 2013 und 2023
- **Bevölkerung zu Beginn:** 566 992 Personen im Jahr 2013
- **Abwanderung:** 27 588 Wegzüge innerhalb Senegals in den fünf Jahren vor der Volkszählung 2023
- **Basisrate der Abwanderung:** rund 0.74 % pro Jahr, aus den Wegzügen und der Bevölkerung im Vergleichszeitraum abgeleitet
- **Zuzug:** 13 645 Zuzüge im selben Fenster, daraus eine Zuzugsrate von rund 0.36 % pro Jahr

Die Abwanderungsdaten enthalten keine Auswanderung ins Ausland. Diese ist mit rund 2 400 Wegzügen in fünf Jahren klein. Das Einjahresfenster 2022 bis 2023 weist mit 25 956 Wegzügen eine rund viermal höhere Rate aus. Das spricht für saisonale und zirkuläre Migration, die das Modell nicht abbildet.

### Zentrale Annahmen

- **Natürliches Bevölkerungswachstum:** 3.36 % pro Jahr (Geburten- minus Sterberate 2023)
- **Niederschlag und Ertrag:** 10 % weniger Niederschlag führen zu 10 % weniger Ertrag.
- **Arbeitskräfte und Produktion:** 10 % weniger Arbeitskräfte führen zu 3 % weniger Produktion. Die Bevölkerung dient als Näherung für die verfügbaren Arbeitskräfte.
- **Rücküberweisungen:** Anteil von 15 % am Haushaltseinkommen im Ausgangszustand
- **Netzwerk:** Abgewanderte Personen zählen im Mittel 20 Jahre zum Netzwerk.

Für Ertrag, Einkommen und Rücküberweisungen fehlen regionale Daten. Diese Grössen werden als Indizes gerechnet. Ein Wert von 1 entspricht dem Referenzzustand. Die Wirkungsstärken sind Annahmen und werden in der Sensitivitätsanalyse variiert.

## 3. Modellstruktur

Das Stock-and-Flow-Modell beschreibt Bestände und ihre jährlichen Zu- und Abflüsse.

### Bestände

- **Bevölkerung:** Menschen, die in Kaffrine leben
- **Abgewanderte Personen:** Menschen ausserhalb der Region, die im Modell zum Netzwerk gehören und Rücküberweisungen leisten können

Der Anfangsbestand der Abgewanderten wird aus Basisrate, Anfangsbevölkerung und Verweildauer abgeleitet. Er beträgt rund 84 000 Personen und ist kein direkt gemessener Bestand.

### Zu- und Abflüsse

- **Natürliches Wachstum:** Erhöht die Bevölkerung durch Geburten minus Todesfälle.
- **Zuzug:** Erhöht die Bevölkerung mit konstanter Rate.
- **Abwanderung:** Verringert die Bevölkerung und erhöht den Bestand der Abgewanderten.
- **Abgang aus dem Netzwerk:** Verringert den Bestand der Abgewanderten. Er bedeutet keine Rückkehr nach Kaffrine.

### Berechnete Zusammenhänge

- Der Niederschlag beeinflusst den landwirtschaftlichen Ertrag.
- Ertrag und verfügbare Arbeitskräfte bestimmen die Produktion.
- Die Produktion wird auf die Bevölkerung verteilt, um Nahrung und landwirtschaftliches Einkommen pro Person zu berechnen.
- Rücküberweisungen ergänzen das Haushaltseinkommen.
- Weniger Einkommen und Nahrung pro Person erhöhen den Druck wegzuziehen.
- Ein grösseres Netzwerk abgewanderter Personen erhöht die Abwanderungsrate.

## 4. Rückkopplungen

Die Simulation übernimmt die zentralen Rückkopplungen aus LE1 und ergänzt das natürliche Bevölkerungswachstum.

### Zentrale Rückkopplungen

- **R1 Arbeitskräfte–Einkommen (verstärkend, Vermutung aus LE1):** Wer wegzieht, fehlt als Arbeitskraft. Die Produktion sinkt. Ob dadurch weitere Abwanderung entsteht, hängt davon ab, wie stark die Produktion gegenüber der Bevölkerung abnimmt.
- **R2 Netzwerk (verstärkend):** Wer schon weg ist, erleichtert anderen das Wegziehen. Die Abwanderungsrate steigt.
- **B1 Versorgung (ausgleichend):** Weniger Menschen bedeuten bei gleicher Produktion mehr Nahrung pro Person. Der Druck wegzuziehen sinkt.
- **B2 Rücküberweisungen (ausgleichend):** Geld von Abgewanderten erhöht das Einkommen der Zurückbleibenden. Der Druck wegzuziehen sinkt.
- **R3 Natürliches Wachstum (verstärkend):** Eine grössere Bevölkerung führt bei gleicher Wachstumsrate zu einem grösseren jährlichen Bevölkerungszuwachs.

Mit den gewählten Annahmen überwiegt bei R1 und B1 die Entlastung durch weniger Menschen. Die in LE1 vermutete verstärkende Wirkung fehlender Arbeitskräfte zeigt sich deshalb im Modell nicht.

## 5. Basislauf und Backtest

### Basislauf

Bis 2023 wird der gemessene Niederschlag verwendet. Ab 2024 entspricht der Niederschlag jedes Jahr dem Mittelwert 1991–2020.

Betrachtet werden Bevölkerung, jährliche Abwanderung, Abwanderungsrate und der Bestand der Abgewanderten. Einkommen und Nahrung pro Person zeigen, wie sich die Versorgung der Zurückbleibenden verändert.

### Vergleich mit echten Daten

- Bevölkerung im Jahr 2023
- gesamte Wegzüge und Zuzüge im Zeitraum 2018–2022
- relativer Fehler zwischen Simulation und Vergleichswert

### Grenzen des Backtests

- Das Modell unterschätzt die Bevölkerung 2023 auch mit Zuzug um rund 8 %. Natürliches Wachstum und Nettomigration erklären die beobachtete Bevölkerungsentwicklung nicht vollständig.
- Mögliche Gründe sind das 2013 höhere natürliche Wachstum (3.79 % statt 3.36 %) oder Unterschiede in der Erfassung beider Volkszählungen.
- Der Vergleich der Wegzüge und Zuzüge ist eine Konsistenzprüfung, weil beide Raten aus denselben Daten abgeleitet wurden.
- Zwei Vergleichswerte reichen nicht aus, um die angenommenen Wirkungsstärken unabhängig zu prüfen.

## 6. Szenarien und Sensitivitätsanalyse

Die Szenarien zeigen, wie das Modell auf unterschiedliche Niederschlagsannahmen ab 2024 reagiert. Sie sind keine Prognosen.

### Niederschlagsszenarien

- **Basis:** Jedes Jahr entspricht einem Normaljahr.
- **Wiederkehrende Dürren:** Alle fünf Jahre fällt 30 % weniger Niederschlag, erstmals 2024.
- **Dauerhaft trockener:** Jedes Jahr fällt 15 % weniger Niederschlag.

Verglichen werden die Bevölkerung 2050 und die gesamte Abwanderung von 2024 bis 2050.

### Sensitivitätsanalyse

Die angenommenen Wirkungsparameter, die natürliche Wachstumsrate, die Verweildauer im Netzwerk sowie die Abwanderungs- und die Zuzugsrate werden einzeln halbiert und verdoppelt. Gemessen wird die Veränderung der gesamten Abwanderung im Basisszenario.

Zusätzlich wird die Abhängigkeit der Produktion von Arbeitskräften im Dürreszenario variiert. Damit wird untersucht, unter welchen Annahmen die vermutete Schleife R1 verstärkend wirkt und wann die Versorgungsschleife B1 überwiegt.

## 7. Erkenntnisse und Grenzen

### Zentrale Erkenntnisse

- **Bevölkerungswachstum:** Im Modell wächst die Produktion langsamer als die Bevölkerung. Einkommen und Nahrung pro Person sinken, und die Abwanderung steigt auch ohne zusätzliche Dürren.
- **Dürren:** Weniger Niederschlag verringert den Ertrag und erhöht die Abwanderung gegenüber dem Basislauf. Bis 2050 sind es bei wiederkehrenden Dürren rund 27 000 und bei dauerhaft trockenerem Klima rund 62 000 zusätzliche Abwandernde.
- **Versorgung:** Abwanderung entlastet unter den gewählten Annahmen die Zurückbleibenden stärker, als der Verlust an Arbeitskräften die Produktion verringert.
- **Netzwerke:** Der Bestand der Abgewanderten verändert sich über Jahre. Dadurch können die Folgen einer Dürre über das Netzwerk nachwirken.
- **Annahmen:** Die Ergebnisse reagieren besonders auf natürliches Wachstum, Netzwerke, die beiden Migrationsraten, die Wirkung der Nahrung und die Abhängigkeit der Produktion von Arbeitskräften.

### Aussagekraft des Modells

Das Modell macht mögliche Zusammenhänge und Rückkopplungen sichtbar. Die Ergebnisse gelten für die gewählten Annahmen und belegen nicht, wie viele Menschen tatsächlich wegen einer Dürre abwandern.

Für belastbarere Aussagen werden insbesondere Migrationsdaten über mehrere Zeitpunkte sowie regionale Daten zu landwirtschaftlicher Produktion, Einkommen und Rücküberweisungen benötigt.

### Zugehörige Dateien

- **`01_LE2_Systemdynamik.qmd`:** Ausführliche Analyse mit Modellstruktur, Parametern, Simulationen, Backtest, Szenarien und Sensitivität
- **`model.py`:** Datenaufbereitung und Umsetzung des Modells in BPTK-Py
- **`../data/raw/`:** Rohdaten zu Niederschlag, Bevölkerung und Abwanderung
- **`../data/SOURCES.md`:** Übersicht der verwendeten Datenquellen und Datenlücken
