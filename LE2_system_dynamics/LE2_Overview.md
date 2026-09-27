# **LE2 – Systemdynamik**

Simulation des in LE1 kartierten Systems (Region Kaffrine, Senegal) mit BPTK-Py.

## **Aufbau**

| Datei | Inhalt |
|---|---|
| `parameters.py` | Alle Anfangswerte und Parameter mit Einheit, Typ, Quelle bzw. Annahme |
| `model.py` | Modellstruktur in BPTK-Py (Stocks, Flows, Converter) |
| `01_daten.ipynb` | Datenexploration, Ableitung von Anfangswerten und Parametern |
| `02_modell.ipynb` | Problemstellung, Systemgrenzen, Modellstruktur, Basislauf |
| `03_backtest.ipynb` | Validierung gegen historische bzw. postulierte Werte |
| `04_szenarien_sensitivitaet.ipynb` | Szenarien und Sensitivitätsanalyse |

## **Checkliste Mini-Challenge LE2**

- [ ] Simulationsmodell mit Anfangszustand in BPTK-Py
- [ ] Systemgrenzen anhand der Systemkarte aus LE1
- [ ] Grafik der zeitlichen Entwicklung der wesentlichen Systemeigenschaften
- [ ] Anfangszustand und Parameter mit Daten bzw. Annahmen
- [ ] Backtest
- [ ] Erkenntnisse aus der Simulation
- [ ] Kausalschleifen des simulierten Systems (optional mit errechneten Gewichtungen)

## **Zu beantwortende Fragen**

- Welche Problemstellung(en) sollen beantwortet werden? Welche Kenngrössen? Braucht es Szenarien?
- Was sind die Systemgrenzen? Wie wird die Umgebung behandelt?
- Welche Stocks und Flows? Welche Kausalschleifen werden damit abgedeckt?
- Was ist der Zeithorizont? Welcher Zeitschritt ist sinnvoll?
- Wie werden Anfangszustand und Parameter bestimmt?
- Wie entwickeln sich die Kenngrössen? Welche Erkenntnisse ergeben sich?
- Wie lässt sich die Simulation an der Vergangenheit validieren?
