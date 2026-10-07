# **Datenquellen**

Regeln:

- Rohdaten in `data/raw/` werden nie verändert; Aufbereitung im Code (`LE2_system_dynamics/model.py`).
- Status: `verwendet`, `nicht verfügbar` (mit Umgang im Modell).

| Grösse | Datensatz | Anbieter | Räuml. Auflösung | Zeitraum | Einheit | Datei | Status |
|---|---|---|---|---|---|---|---|
| Niederschlag | CHIRPS v2.0, jährlich (ERDDAP `chirps20GlobalAnnualP05`) | UCSB Climate Hazards Center / NOAA | 0.05°, Mittel über Rechteck um Kaffrine | 1991–2023 | mm/Jahr | `raw/chirps_kaffrine_1991_2023.csv` | verwendet |
| Bevölkerung | Volkszählungen RGPH-4 (2013) und RGPH-5 (2023) | ANSD Senegal | Region | 2013, 2023 | Personen | `raw/ansd_bevoelkerung_kaffrine.csv` | verwendet |
| Abwanderung | RGPH-5 2023, Kapitel 6 Migrationen | ANSD Senegal | Region | Momentaufnahme 2023 | Personen | `raw/ansd_migration_kaffrine_2023.csv` | verwendet |
| Ertrag, Produktion, Einkommen | Agrarstatistik / FAOSTAT | DAPSA / FAO | Region / Land | – | – | – | nicht verfügbar für Kaffrine; als Index mit Annahmen |
| Rücküberweisungen | – | – | – | – | – | – | nicht verfügbar; Annahme |
