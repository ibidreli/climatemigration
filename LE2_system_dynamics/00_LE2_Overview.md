# **LE2 – Systemdynamik**

Simulation des in LE1 kartierten Systems (Region Kaffrine, Senegal) mit BPTK-Py.

## **Aufbau**

| Datei | Inhalt |
|---|---|
| `01_LE2_Systemdynamik.ipynb` | Problemstellung, Systemgrenzen, Daten, Modellstruktur, Parameter, Basislauf, Backtest, Szenarien, Sensitivität, Schleifen, Erkenntnisse |
| `model.py` | Daten laden, Parameter (mit Quelle bzw. Annahme), Modell in BPTK-Py, Niederschlagsszenarien |
| `../data/raw/` | Rohdaten: CHIRPS-Niederschlag, Volkszählungen und Migration (ANSD) |

## **Checkliste Mini-Challenge LE2**

- [x] Simulationsmodell mit Anfangszustand in BPTK-Py
- [x] Systemgrenzen anhand der Systemkarte aus LE1
- [x] Grafik der zeitlichen Entwicklung der wesentlichen Systemeigenschaften
- [x] Anfangszustand und Parameter mit Daten bzw. Annahmen
- [x] Backtest
- [x] Erkenntnisse aus der Simulation
- [x] Kausalschleifen des simulierten Systems
