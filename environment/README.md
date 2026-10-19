# **Setup**

## **Umgebung anlegen**

```
mamba env create -f environment/environment-sd.yml
```

`conda` statt `mamba` funktioniert ebenfalls, ist aber langsamer. Alternativ mit pip in einer Python-3.11-Umgebung: `pip install -r requirements.txt`. BPTK-Py 1.9.0 braucht `setuptools<81`, weil es `pkg_resources` importiert.

## **Kernel registrieren**

```
conda activate mss-sd
python -m ipykernel install --user --name mss-sd --display-name "Python (mss-sd)"
```

## **Umgebung aktualisieren**

```
mamba env update -f environment/environment-sd.yml
```

## **Notebook**

| Notebook | Kernel |
|---|---|
| `LE2_system_dynamics/01_model.ipynb` (Textfassung `01_model.pct.py`) | mss-sd |

Vor der Abgabe das Notebook mit «Restart Kernel and Run All» vollständig ausführen. Die Plausibilitätsprüfung bricht bei einem Fehler ab. LE1 und LE4 liegen als Markdown vor und brauchen keine Umgebung.
