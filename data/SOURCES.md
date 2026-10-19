# **Datenquellen**

Regeln:

- Rohdaten in `data/raw/` werden nicht aufbereitet; die Aufbereitung geschieht im Notebook `LE2_system_dynamics/01_model.ipynb`.
- Die ANSD-Tabellen sind von Hand aus den PDF-Berichten übertragen. Fundstellen, Widersprüche und Varianten sind in `source_review.md` dokumentiert.
- Status: `verwendet`, `Vergleich` (nur Plausibilisierung, keine Kalibrierung), `verfügbar` (noch nicht extrahiert), `nicht verfügbar` (mit Umgang im Modell).

| Grösse | Datensatz | Anbieter | Räuml. Auflösung | Zeitraum | Einheit | Datei | Status |
|---|---|---|---|---|---|---|---|
| Niederschlag | CHIRPS v2.0, jährlich (ERDDAP `chirps20GlobalAnnualP05`) | UCSB Climate Hazards Center / NOAA | 0.05°, Mittel über Rechteck um Kaffrine | 1991–2023 | mm/Jahr | `raw/chirps_kaffrine_1991_2023.csv` | verwendet |
| Bevölkerung, beobachtet | Volkszählungen RGPH-4 (2013) und RGPH-5 (2023) | ANSD Senegal | Region | 2013, 2023 | Personen | `raw/ansd_bevoelkerung_kaffrine.csv` (`datentyp = Volkszaehlung`) | verwendet (Anfangswert, Backtest) |
| Bevölkerung, historisch und geschätzt | SES Kaffrine 2010–2023 | ANSD Senegal | Region bzw. Vorgängergebiet | 1976–2022 | Personen | `raw/ansd_bevoelkerung_kaffrine.csv` | Vergleich |
| Bevölkerung, Projektion | Projections démographiques 2023–2073 | ANSD Senegal | Region | 2024–2050 | Personen | `raw/ansd_bevoelkerung_kaffrine.csv` (`datentyp = Projektion`) | Vergleich (externes Referenzszenario) |
| Natürliches Wachstum | Geburten- und Sterberaten RGPH 2013 und 2023 | ANSD Senegal (SES 2013, SES 2022–2023) | Region | 2013, 2023 | ‰ | – (Parameter im LE2-Notebook) | verwendet (Wert 2023) |
| Binnenmigration | RGPH-5 2023, Kapitel 6; SES Kaffrine 2013 | ANSD Senegal | Region | Lebenszeit-, Fünf- und Einjahresfenster, Erhebungen 2013 und 2023 | Personen | `raw/ansd_migration_kaffrine_2023.csv` | verwendet (Fünfjahresfenster 2023 für Kalibrierung und Zuzugsrate, Fünfjahresfenster 2013 für Backtest und Bandbreiten), übrige Fenster als Vergleich |
| Internationale Migration | RGPH-5 2023, Kapitel 6; SES Kaffrine 2013 | ANSD Senegal | Region | Fünf- und Einjahresfenster | Personen | `raw/ansd_migration_kaffrine_2023.csv` | Vergleich |
| Ertrag, Anbaufläche, Produktion (Hirse, Erdnuss) | SES Kaffrine 2013, 2017–2018, 2020–2021, 2022–2023, Kapitel Landwirtschaft | ANSD Senegal / DRDR Kaffrine | Region | 2009–2013, 2017–2023 | ha, kg/ha, t | `raw/ansd_ertrag_kaffrine.csv` | verwendet (Schätzung von `elast_ertrag` und `ertrag_trend`, Test ausserhalb der Stichprobe) |
| Einkommen | – | – | – | – | – | – | nicht verfügbar; Index mit Annahmen |
| Rücküberweisungen | – | – | – | – | – | – | nicht verfügbar; Annahme |
