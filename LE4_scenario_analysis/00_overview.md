# **LE4 – Szenario- und integrierte Analyse (Lösungsskizze)**

## **Fragestellungen**

- **F1:** Wie stark erhöhen wiederkehrende Dürren und ein trockeneres Klima die Abwanderung aus Kaffrine bis 2050?
- **F2:** Wie viel davon lässt sich mit stabileren Erträgen (Bewässerung, dürretolerante Sorten) oder steigender Produktivität vermeiden?
- **F3:** Welcher Kanal prägt die Abwanderung stärker, das Klima oder die Entwicklung von Produktivität und Bevölkerung?

## **Aufbau**

| Datei | Inhalt |
|---|---|
| `01_scenarios.qmd` | Skizze: Fragestellungen, Systemgrenzen, Übertragungskanäle, Parameter, geplante Szenarien, Hypothesen, Backtest-Beschreibung |
| `02_climada.qmd` | Skizze, wie CLIMADA den Kanal Dürre → Ertrag ergänzen könnte (nicht ausgeführt) |

LE4 wird nur skizziert, nicht gerechnet. Gerechnet würde mit dem LE2-Modell (`../LE2_system_dynamics/model.py`), damit LE2 und LE4 dieselben Parameter verwenden. Die Ertragsbeziehung (`elast_ertrag` = 0.7) ist bereits in LE2 aus ANSD-Daten geschätzt.

## **Geplante Szenarien**

- **Klima:** basis, wiederkehrende Dürren (alle 5 Jahre −30 %), trockener (dauerhaft −15 %). Die Richtung stützt sich auf CMIP6-Projektionen für den westlichen Sahel (Wane et al. 2025, Science Advances 11, eadu5415), die Stärke ist eine Annahme.
- **Handlungsoptionen:** keine, stabile Erträge (Elastizität halbiert), Produktivität (+2 % pro Jahr ab 2024), beides.

## **Hypothesen**

- Klimabedingte Zusatzabwanderung ohne Anpassung in der Grössenordnung der LE2-Szenarien (rund 21 000 bis 45 000 Personen bis 2050).
- Stabile Erträge verringern den Klimaeffekt etwa im Verhältnis der Elastizität.
- Produktivitätswachstum senkt die gesamte Abwanderung, aber kaum den Klimaeffekt.
- Die Versorgung pro Kopf prägt die Abwanderung stärker als der Niederschlag.

## **Checkliste Mini-Challenge LE4 (Skizze)**

- [x] Analysemodell mit Anfangszustand (LE2-Modell, beschrieben)
- [x] Systemgrenzen anhand der Systemkarte aus LE1
- [x] Graph der Übertragungskanäle (Zyklen aufgebrochen)
- [ ] Grafik der Ergebnisse (nur geplant, nicht gerechnet)
- [x] Kennzahlen und Funktionsparameter (zuerst schätzen, dann Daten)
- [x] Beschreibung des Backtests
- [x] Erwartete Erkenntnisse

Szenarien sind keine Prognosen. Sie beschreiben konsistente mögliche Entwicklungen unter expliziten Annahmen.
