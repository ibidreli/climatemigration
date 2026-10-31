# **LE2 – Systemdynamik**

Zusammenfassung des Notebooks `01_model.ipynb` (Textfassung `01_model.pct.py`). Daten, Modell und Auswertung stehen vollständig im Notebook. Alle Zahlen stammen aus dem ausgeführten Notebook.

## **1. Problemstellung und Systemgrenzen**

Untersucht wird, wie stark Dürren über Ertrag und Einkommen die dauerhafte Abwanderung aus der Region Kaffrine (Senegal) erhöhen und wie die Abwanderung über Bevölkerung, Netzwerke und Rücküberweisungen zurückwirkt. Grundlage ist das Kernmodell der Causal Loop Map aus LE1, simuliert mit BPTK-Py.

- **Von aussen vorgegeben:** Niederschlag (Daten bis 2023, danach Szenario), Produktivitätstrend des Ertrags (Daten bis 2023, danach Annahme), natürliches Wachstum (Volkszählungen bis 2023, danach konstant)
- **Im Modell berechnet:** Bevölkerung, Abwanderung, Zuzug, Abgewanderte, Ertrag, Produktion, Einkommen und Nahrung pro Kopf, Rücküberweisungen
- **Vereinfacht:** Wasserverfügbarkeit als normierter Niederschlag, Zuzug mit konstanter Rate
- **Ausserhalb:** Zielorte, saisonale Migration, Preise, Bewässerung, Politik, Konflikte
- **Zeit:** Backtest 2013–2023, Szenarien 2024–2050, Zeitschritt 1 Jahr

## **2. Daten und Parameter**

- **Niederschlag:** CHIRPS 1991–2023, Normaljahr 569 mm
- **Bevölkerung:** Volkszählungen 2013 (566 992) und 2023 (820 405)
- **Natürliches Wachstum:** Geburten minus Sterbefälle, 3.79 % (2013) linear auf 3.36 % (2023), danach konstant
- **Migration:** Fünfjahresfenster der Volkszählungen 2013 und 2023. Wegzugsrate 1.27 % (2008–2013) und 0.74 % (2018–2023)
- **Ertrag:** ANSD SES 2009–2023 für Hirse und Erdnuss. Elastizität auf den Niederschlag 0.46 bzw. 0.94 (Modell 0.7), Trend 5.1 % bzw. 2.2 % pro Jahr (Modell 3.5 % bis 2023)
- **Kalibrierung:** Die Basis-Abwanderungsrate (0.94 %) ist so eingestellt, dass das Modell die 27 588 Wegzüge 2018–2023 trifft
- **Annahmen:** Netzwerkwirkung, Verweildauer, Rücküberweisungen, Wirkung des Einkommens und der Arbeitskräfte. Sie werden in der Sensitivitätsanalyse halbiert und verdoppelt

## **3. Modellstruktur**

- **Stocks:** Bevölkerung, Abgewanderte Personen (Netzwerk), verzögerter Abwanderungsdruck
- **Flows:** natürliches Wachstum, Zuzug, Abwanderung, Abgang aus dem Netzwerk
- **Wirkungskette:** Niederschlag → Ertrag (mit Produktivität) → Produktion → Haushaltseinkommen pro Kopf → Abwanderungsdruck → Abwanderungsrate
- **Netzwerk:** wirkt wie die Rücküberweisungen über den Anteil der Abgewanderten an der Bevölkerung, nicht über ihre absolute Zahl
- **Abwanderungsdruck:** nur über das Einkommen pro Kopf. Die Nahrung pro Person ist dasselbe Signal und bleibt Kenngrösse, um eine Doppelzählung zu vermeiden
- **Verzögerung:** erster Ordnung mit 1 Jahr (Ernte im Herbst, Abwanderung in der folgenden Trockenzeit)
- **Schleifen:** R1 Arbeitskräfte, B1 Versorgung pro Kopf, R2 Netzwerk, B2 Rücküberweisungen, R3 natürliches Wachstum
- **Diagramm:** Stock-and-Flow-Diagramm in `stock_flow_diagram.png`, Quelle `stock_flow_diagram.dot`

## **4. Validierung**

- **Bevölkerung 2023:** um 6.2 % unterschätzt. Erst ein konstantes natürliches Wachstum von gut 4.2 % würde die Volkszählung treffen
- **Migration:** Wegzüge −0.4 % (Kalibrierung), Zuzüge −7.2 % (Folge der tieferen Modellbevölkerung)
- **Netzwerkanteil:** Der Anteil der Abgewanderten an der Bevölkerung sinkt im Modell und bei den Lebenszeitwegzügen der Volkszählungen fast gleich stark (Faktor 0.75 und 0.74 von 2013 bis 2023)
- **Richtung:** Modell und Daten zeigen eine sinkende Abwanderungsrate zwischen 2013 und 2018–2023. Das ist Konsistenz, keine Bestätigung des Mechanismus, weil die Richtung im Modell aus den Annahmen folgt
- **Ertrag ausserhalb der Stichprobe (Schätzung bis 2018, Vorhersage 2019–2023):** Der Niederschlag verbessert die Vorhersage für Hirse (12.1 % statt 17.8 % mittlerer Fehler), nicht aber für Erdnuss (17.9 % statt 5.4 %)
- **Zeitschritt:** dt = 0.25 statt 1 ändert die Bevölkerung um weniger als 1 % und die kumulierte Abwanderung um +2.6 %
- **Plausibilität:** Anfangswerte, Bestandsbilanz, Wertebereich, Wirkungsrichtung und Parameterdokumentation werden bei jedem Lauf geprüft

## **5. Szenarien und Sensitivität**

| Szenario | Niederschlag ab 2024 | Abwanderung 2024–2050 gegenüber basis |
|---|---|---|
| basis | jedes Jahr Normaljahr | – |
| duerren | alle 5 Jahre −30 % | +3.4 % (rund 9 300 Personen) |
| trockener | dauerhaft −15 % | +7.5 % (rund 20 500 Personen) |

- **Grösste Einflüsse:** Migrationsraten des Fensters 2008–2013 (+43.8 %), Netzwerkwirkung (−37.4 % bis +9.9 %), natürliches Wachstum 2013 (+10.3 %)
- **Zusatzabwanderung durch Dürren:** Referenz rund 9 300 Personen, je nach einzelner Annahme 4 800 bis 17 200. Am stärksten wirken die Wirkung des Einkommens (−48 % bis +85 %) und die Elastizität des Ertrags (rund ±34 %)
- **Klimakette:** Die Elastizität des Ertrags verändert die gesamte Abwanderung nur um ±1.1 %, die Zusatzabwanderung aber um rund ±34 %
- **Produktivität ab 2024:** 2 % Wachstum pro Jahr senkt die Abwanderung um 23.4 %
- **Verzögerung:** 2 bzw. 3 Jahre ändern die Abwanderung um −1.6 % bzw. −2.8 %
- **R1 oder B1:** B1 überwiegt. Eine Abwanderungsspirale über fehlende Arbeitskräfte entsteht nur bei schrumpfender Bevölkerung

## **6. Erkenntnisse und Grenzen**

- Dürren erhöhen die dauerhafte Abwanderung messbar, sind aber nicht der dominierende Treiber
- Entscheidend ist, ob die Landwirtschaft mit dem Bevölkerungswachstum Schritt hält. Der Anstieg der Abwanderungsrate im Basislauf folgt aus der Annahme stagnierender Produktivität
- Die wichtigsten Wissenslücken sind die Reaktion der Abwanderung auf das Einkommen (für den Dürreeffekt) sowie Netzwerkeffekte und eine Migrationszeitreihe (für die gesamte Abwanderung), nicht genauere Klimadaten
- Nur dauerhafte Abwanderung, keine Altersstruktur, ein Ertragsindex für zwei Kulturen, Nichtlinearitäten aus LE1 linear vereinfacht, wenige unabhängige Vergleichswerte für den Backtest
- Szenarien sind keine Prognosen

## **7. Dateien**

- **`01_model.ipynb`:** ausgeführtes Notebook mit Daten, Modell, Auswertung und allen Grafiken (für die Abgabe)
- **`01_model.pct.py`:** Quelle des Notebooks, mit Jupytext gekoppelt
- **`stock_flow_diagram.png`, `stock_flow_diagram.dot`:** Stock-and-Flow-Diagramm und seine Quelle (Graphviz)
- **`../data/raw/`, `../data/SOURCES.md`:** Rohdaten und Quellen
