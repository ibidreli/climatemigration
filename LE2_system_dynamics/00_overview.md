# **LE2 – Systemdynamik**

Zusammenfassung des Notebooks `01_model.ipynb` (Textfassung `01_model.pct.py`). Daten, Modell und Auswertung stehen vollständig im Notebook. Alle Zahlen stammen aus dem ausgeführten Notebook.

## **1. Problemstellung und Systemgrenzen**

Untersucht wird, wie stark Dürren über Ertrag und Einkommen die dauerhafte Abwanderung aus der Region Kaffrine (Senegal) erhöhen und wie die Abwanderung über Bevölkerung, Netzwerke und Rücküberweisungen zurückwirkt. Grundlage ist das Kernmodell der Causal Loop Map aus LE1, simuliert mit BPTK-Py.

- **Von aussen vorgegeben:** Niederschlag (Daten bis 2023, danach Szenario), Produktivitätstrend des Ertrags (Daten bis 2023, danach Annahme)
- **Im Modell berechnet:** Bevölkerung, Abwanderung, Zuzug, Abgewanderte, Ertrag, Produktion, Einkommen und Nahrung pro Kopf, Rücküberweisungen
- **Vereinfacht:** Wasserverfügbarkeit als normierter Niederschlag, Zuzug mit konstanter Rate
- **Ausserhalb:** Zielorte, saisonale Migration, Preise, Bewässerung, Politik, Konflikte
- **Zeit:** Backtest 2013–2023, Szenarien 2024–2050, Zeitschritt 1 Jahr

## **2. Daten und Parameter**

- **Niederschlag:** CHIRPS 1991–2023, Normaljahr 569 mm
- **Bevölkerung:** Volkszählungen 2013 (566 992) und 2023 (820 405)
- **Migration:** Fünfjahresfenster der Volkszählungen 2013 und 2023. Wegzugsrate 1.27 % (2008–2013) und 0.74 % (2018–2023)
- **Ertrag:** ANSD SES 2009–2023 für Hirse und Erdnuss. Elastizität auf den Niederschlag 0.46 bzw. 0.94 (Modell 0.7), Trend 5.1 % bzw. 2.2 % pro Jahr (Modell 3.5 % bis 2023)
- **Kalibrierung:** Die Basis-Abwanderungsrate (0.88 %) ist so eingestellt, dass das Modell die 27 588 Wegzüge 2018–2023 trifft
- **Annahmen:** Netzwerkwirkung, Verweildauer, Rücküberweisungen, Wirkung des Einkommens und der Arbeitskräfte. Sie werden in der Sensitivitätsanalyse halbiert und verdoppelt

## **3. Modellstruktur**

- **Stocks:** Bevölkerung, Abgewanderte Personen (Netzwerk), verzögerter Abwanderungsdruck
- **Flows:** natürliches Wachstum, Zuzug, Abwanderung, Abgang aus dem Netzwerk
- **Wirkungskette:** Niederschlag → Ertrag (mit Produktivität) → Produktion → Haushaltseinkommen pro Kopf → Abwanderungsdruck → Abwanderungsrate
- **Abwanderungsdruck:** nur über das Einkommen pro Kopf. Die Nahrung pro Person ist dasselbe Signal und bleibt Kenngrösse, um eine Doppelzählung zu vermeiden
- **Verzögerung:** erster Ordnung mit 1 Jahr (Ernte im Herbst, Abwanderung in der folgenden Trockenzeit)
- **Schleifen:** R1 Arbeitskräfte, B1 Versorgung pro Kopf, R2 Netzwerk, B2 Rücküberweisungen, R3 natürliches Wachstum

## **4. Validierung**

- **Bevölkerung 2023:** um 8.3 % unterschätzt. Erst 4.2 % natürliches Wachstum statt 3.36 % würde die Volkszählung treffen
- **Migration:** Wegzüge +0.4 % (Kalibrierung), Zuzüge −8.9 % (Folge der tieferen Modellbevölkerung)
- **Richtung:** Modell und Daten zeigen eine sinkende Abwanderungsrate zwischen 2013 und 2018–2023
- **Ertrag ausserhalb der Stichprobe (Schätzung bis 2018, Vorhersage 2019–2023):** Der Niederschlag verbessert die Vorhersage für Hirse (12.1 % statt 17.8 % mittlerer Fehler), nicht aber für Erdnuss (17.9 % statt 5.4 %)
- **Zeitschritt:** dt = 0.25 statt 1 ändert die Bevölkerung um weniger als 0.3 % und die kumulierte Abwanderung um +3.9 %
- **Plausibilität:** Anfangswerte, Bestandsbilanz, Wertebereich, Wirkungsrichtung und Parameterdokumentation werden bei jedem Lauf geprüft

## **5. Szenarien und Sensitivität**

| Szenario | Niederschlag ab 2024 | Abwanderung 2024–2050 gegenüber basis |
|---|---|---|
| basis | jedes Jahr Normaljahr | – |
| duerren | alle 5 Jahre −30 % | +3.7 % (rund 14 400 Personen) |
| trockener | dauerhaft −15 % | +8.3 % (rund 31 800 Personen) |

- **Grösste Einflüsse:** Netzwerkwirkung (−13.3 % bis +37.1 %), Migrationsraten des Fensters 2008–2013 (+25.3 %), natürliches Wachstum 2013 (+23.8 %)
- **Klimakette:** Die Elastizität des Ertrags verändert die Abwanderung über die ganze Spannweite nur um ±1.3 %
- **Produktivität ab 2024:** 2 % Wachstum pro Jahr senkt die Abwanderung um 28.0 %
- **Verzögerung:** 2 bzw. 3 Jahre ändern die Abwanderung um −1.4 % bzw. −2.5 %
- **R1 oder B1:** B1 überwiegt. Eine Abwanderungsspirale über fehlende Arbeitskräfte entsteht nur bei schrumpfender Bevölkerung

## **6. Erkenntnisse und Grenzen**

- Dürren erhöhen die dauerhafte Abwanderung messbar, sind aber nicht der dominierende Treiber
- Entscheidend ist, ob die Landwirtschaft mit dem Bevölkerungswachstum Schritt hält. Der starke Anstieg der Abwanderung im Basislauf folgt aus der Annahme stagnierender Produktivität
- Die wichtigste Wissenslücke sind Netzwerkeffekte und eine Migrationszeitreihe, nicht genauere Klimadaten
- Nur dauerhafte Abwanderung, keine Altersstruktur, ein Ertragsindex für zwei Kulturen, nur ein unabhängiger Vergleichswert für den Backtest
- Szenarien sind keine Prognosen

## **7. Dateien**

- **`01_model.ipynb`:** ausgeführtes Notebook mit Daten, Modell, Auswertung und allen Grafiken (für die Abgabe)
- **`01_model.pct.py`:** Quelle des Notebooks, mit Jupytext gekoppelt
- **`../data/raw/`, `../data/SOURCES.md`:** Rohdaten und Quellen
