# **Setup**

## **Umgebungen anlegen**

```
mamba env create -f environment/environment-sd.yml        # LE2 + LE4 (Szenarien)
mamba env create -f environment/environment-climada.yml   # LE4 (optional, Climada)
```

`conda` statt `mamba` funktioniert ebenfalls, ist aber langsamer.

## **Kernel registrieren**

```
conda activate mss-sd
python -m ipykernel install --user --name mss-sd --display-name "Python (mss-sd)"

conda activate mss-climada
python -m ipykernel install --user --name mss-climada --display-name "Python (mss-climada)"
```

## **Quarto installieren**

Jupytext verwendet Quarto für das `.qmd`-Format: https://quarto.org/docs/get-started/

Bestehende Umgebung aktualisieren (installiert Jupytext):

```
mamba env update -f environment/environment-sd.yml
```

Vor der Abgabe alle Notebooks mit «Restart Kernel and Run All» vollständig ausführen.

## **Welches Notebook mit welchem Kernel**

| Notebook | Kernel |
|---|---|
| `LE2_system_dynamics/*.qmd` | mss-sd |
| `LE4_scenario_analysis/01_uebertragungskanaele_szenarien.qmd` | mss-sd |
| `LE4_scenario_analysis/02_climada_exploration.qmd` | mss-climada |
