"""
Zentrale Parameterdatei für das SD-Modell (LE2) und die Szenarien (LE4).

Jeder Eintrag dokumentiert: Wert, Einheit, Typ, Quelle bzw. Annahme, Status.
Werte sind bewusst leer (None), bis sie aus Daten abgeleitet oder als Annahme
begründet sind. Keine Werte ohne Eintrag in `quelle` setzen.

Status: "offen" | "Annahme" | "Daten" | "kalibriert"
Typ:    "Zeit" | "Anfangswert" | "Parameter" | "exogen"
"""
from dataclasses import dataclass, asdict


@dataclass
class Param:
    wert: object
    einheit: str
    typ: str
    beschreibung: str
    quelle: str = ""
    status: str = "offen"


# ENTWURF: Liste nach der fachlichen Klärung der Modellstruktur anpassen.
PARAMS = {
    # --- Simulationszeit ---
    "starttime": Param(None, "Jahr", "Zeit", "Beginn der Simulation"),
    "stoptime":  Param(None, "Jahr", "Zeit", "Ende der Simulation"),
    "dt":        Param(None, "Jahr", "Zeit", "Zeitschritt"),

    # --- Anfangswerte ---
    "bevoelkerung_0": Param(None, "Personen", "Anfangswert",
                            "Bevölkerung Kaffrine zu starttime"),

    # --- Parameter ---
    "rate_natuerliches_wachstum": Param(None, "1/Jahr", "Parameter",
                                        "Geburten minus Todesfälle pro Person und Jahr"),
    "abwanderungsrate_basis": Param(None, "1/Jahr", "Parameter",
                                    "Abwanderungsrate unter Referenzbedingungen"),
    "niederschlag_referenz": Param(None, "mm/Jahr", "Parameter",
                                   "Referenzniederschlag (z.B. Mittel einer Normalperiode)"),

    # --- Exogene Zeitreihen (Werte kommen aus data/processed) ---
    "niederschlag": Param(None, "mm/Jahr", "exogen",
                          "Jahresniederschlag Kaffrine als Zeitreihe [[jahr, wert], ...]"),
}


def value(name, params=None):
    """Wert eines Parameters; Fehler, falls noch nicht gesetzt."""
    p = (params or PARAMS)[name]
    if p.wert is None:
        raise ValueError(f"Parameter '{name}' ist noch nicht gesetzt (Status: {p.status}).")
    return p.wert


def missing(params=None):
    """Namen aller Parameter ohne Wert."""
    return [k for k, p in (params or PARAMS).items() if p.wert is None]


def as_dataframe(params=None):
    """Parametertabelle für die Dokumentation im Notebook."""
    import pandas as pd
    rows = []
    for k, p in (params or PARAMS).items():
        d = asdict(p)
        if isinstance(d["wert"], (list, tuple)):
            d["wert"] = f"Zeitreihe ({len(d['wert'])} Werte)"
        rows.append({"name": k, **d})
    return pd.DataFrame(rows).set_index("name")
