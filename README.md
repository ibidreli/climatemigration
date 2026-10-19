# climatemigration

MSS Mini Challenge (FHNW, HS26): klimabedingte Abwanderung aus der Region Kaffrine (Senegal) in der Sahel-Zone. Team Rodrigo Urech und Elias Pulver.

## Abgabe

| LE | Umfang | Zu bewertende Dateien |
|---|---|---|
| LE1 Systemkarte | gelöst | `LE1_system_mapping/01_system_map.md` mit den Karten im selben Ordner |
| LE2 Systemdynamik | gelöst | `LE2_system_dynamics/01_model.ipynb` (ausgeführt), Zusammenfassung in `00_overview.md` |
| LE4 Szenario- und integrierte Analyse | Lösungsskizze | `LE4_scenario_analysis/01_sketch.md` mit dem Graphen der Übertragungskanäle im selben Ordner |

Nicht zu bewerten sind `LE1_system_mapping/previous_versions/` (frühere Versionen zur Nachvollziehbarkeit), `docs/` (Aufgabenstellungen) und `environment/`.

Übersicht über das Projekt in `project_overview.md`, Datenquellen in `data/SOURCES.md`, Setup der Umgebungen in `environment/README.md`.

## Notebook-Workflow (Jupytext)

Quelle jedes Notebooks ist eine `.pct.py`-Datei im Percent-Format. Jupytext koppelt sie gemäss `jupytext.toml` mit dem `.ipynb`. Beim Speichern in JupyterLab werden beide Dateien geschrieben.

Ablauf:

1. `git pull`
2. Paar abgleichen: `jupytext --sync LE2_system_dynamics/*.pct.py`
3. Das `.ipynb` in JupyterLab öffnen, arbeiten und speichern
4. Vor dem Commit Kernel neu starten und alle Zellen ausführen, Zahlen im Text mit der Ausgabe abgleichen. Die Plausibilitätsprüfung muss bestehen
5. `.pct.py` und, wo für die Abgabe vorgesehen, das ausgeführte `.ipynb` committen

Regeln:

- Immer zuerst pullen, bevor im Notebook gearbeitet wird
- Möglichst nicht gleichzeitig im selben Notebook arbeiten
- Commits klein halten, ein Branch pro Thema, Merge per Pull Request
