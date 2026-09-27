# climatemigration

MSS Mini-Challenge (FHNW): Klimabedingte Migration in der Sahel-Zone. Übersicht in `mss_project_overview.md`, Setup der Umgebungen in `environment/README.md`.

## Notebook-Workflow (Quarto + Jupytext)

Im Repo liegen die Notebooks ausschliesslich als `.qmd`. Das `.ipynb` ist nur eine lokale Arbeitskopie und über `.gitignore` von Git ausgeschlossen. Jupytext koppelt beide Dateien gemäss `jupytext.toml`: Beim Speichern in JupyterLab wird das `.qmd` automatisch aktualisiert, beim Öffnen gilt die jeweils neuere Datei.

Voraussetzung: Quarto und Jupytext sind installiert (siehe `environment/README.md`).

Ablauf:

1. `git pull`
2. Das `.qmd` in JupyterLab öffnen (Rechtsklick > *Open With* > *Notebook*)
3. Arbeiten und speichern, das `.qmd` wird dabei mitgeschrieben
4. Vor dem Commit Kernel neu starten und alle Zellen ausführen
5. `git diff` prüfen: Es dürfen nur die eigenen Änderungen im `.qmd` erscheinen
6. Nur das `.qmd` committen und pushen

Regeln:

- Immer zuerst pullen, bevor im Notebook gearbeitet wird
- Möglichst nicht gleichzeitig im selben Notebook arbeiten
- Neues Notebook: als `.ipynb` anlegen und speichern, Jupytext erzeugt das `.qmd` automatisch
