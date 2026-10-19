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

## **Umgebung aktualisieren**

```
mamba env update -f environment/environment-sd.yml
```

Alternativ mit pip in einer Python-3.11-Umgebung: `pip install -r requirements.txt`. BPTK-Py 1.9.0 braucht `setuptools<81`, weil es `pkg_resources` importiert.

Die LE4-Notebooks liegen noch als `.qmd` vor. Zum Öffnen braucht Jupytext dafür Quarto: https://quarto.org/docs/get-started/

Vor der Abgabe alle Notebooks mit «Restart Kernel and Run All» vollständig ausführen. Die Plausibilitätsprüfung im LE2-Notebook bricht bei einem Fehler ab.

## **Welches Notebook mit welchem Kernel**

| Notebook | Kernel |
|---|---|
| `LE2_system_dynamics/01_model.pct.py` | mss-sd |
| `LE4_scenario_analysis/01_scenarios.qmd` | mss-sd |
| `LE4_scenario_analysis/02_climada.qmd` | mss-climada |
