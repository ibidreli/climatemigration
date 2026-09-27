# **Datenquellen**

Regeln:

- Rohdaten in `data/raw/` werden nie verändert; jede Bereinigung erfolgt im Code und landet in `data/processed/`.
- Jeder Datensatz erhält einen Eintrag in dieser Tabelle, bevor er im Modell verwendet wird.
- Status: `Kandidat` (noch nicht geprüft), `geprüft`, `verwendet`, `verworfen` (mit Grund).

| Grösse | Datensatz | Anbieter | Räuml. Auflösung | Zeitraum | Einheit | Abrufdatum | Lizenz | Datei | Status |
|---|---|---|---|---|---|---|---|---|---|
| Niederschlag | CHIRPS | UCSB Climate Hazards Center | | | mm | | | | Kandidat |
| Ernteertrag | FAOSTAT Crops and livestock | FAO | Land | | t/ha | | | | Kandidat |
| Ernteertrag regional | Agrarstatistik Senegal (DAPSA) | Senegal | Region | | | | | | Kandidat |
| Bevölkerung | Volkszählungen / Projektionen | ANSD Senegal | Region | | Personen | | | | Kandidat |
| Migration | Volkszählungen (Wohnort vs. Geburtsort) | ANSD Senegal | Region | | Personen | | | | Kandidat |

Hinweis: Die Kandidaten sind noch nicht auf Verfügbarkeit für Kaffrine geprüft.

## **Offene Datenlücken**

- Regionale Migrationszeitreihe für Kaffrine: vorhanden? Falls nicht, Backtest gegen postulierte Werte (begründen).
