"""
SD-Modell Kaffrine in BPTK-Py.

Minimalmodell zuerst: ein Stock (Bevölkerung), zwei Flows.
Die Wirkungskette Niederschlag -> Wasser -> Ertrag -> Einkommen -> Abwanderungsrate
wird erst nach der fachlichen Klärung (Einheiten, funktionale Form) ergänzt.
"""
import copy

from BPTK_Py import Model
from BPTK_Py import sd_functions as sd

from parameters import PARAMS, value, missing


def build_model(params=None, name="kaffrine_sd"):
    params = params or PARAMS
    fehlend = missing(params)
    if fehlend:
        raise ValueError("Fehlende Parameter: " + ", ".join(fehlend))

    m = Model(starttime=value("starttime", params),
              stoptime=value("stoptime", params),
              dt=value("dt", params),
              name=name)

    # --- Exogene Grössen ---
    m.points["niederschlag"] = value("niederschlag", params)
    niederschlag = m.converter("niederschlag")
    niederschlag.equation = sd.lookup(sd.time(), "niederschlag")

    # --- Konstanten ---
    r_wachstum = m.constant("rate_natuerliches_wachstum")
    r_wachstum.equation = value("rate_natuerliches_wachstum", params)
    r_abw_basis = m.constant("abwanderungsrate_basis")
    r_abw_basis.equation = value("abwanderungsrate_basis", params)

    # --- Stocks ---
    bevoelkerung = m.stock("bevoelkerung")                   # Personen
    bevoelkerung.initial_value = value("bevoelkerung_0", params)

    # --- Converter ---
    abwanderungsrate = m.converter("abwanderungsrate")      # 1/Jahr
    # TODO (nach fachlicher Klärung): Abhängigkeit von Niederschlag/Ertrag/Einkommen.
    abwanderungsrate.equation = r_abw_basis

    # --- Flows ---
    natuerliches_wachstum = m.flow("natuerliches_wachstum")  # Personen/Jahr
    natuerliches_wachstum.equation = bevoelkerung * r_wachstum
    abwanderung = m.flow("abwanderung")                      # Personen/Jahr
    abwanderung.equation = bevoelkerung * abwanderungsrate

    bevoelkerung.equation = natuerliches_wachstum - abwanderung
    return m


def with_overrides(overrides, params=None):
    """Kopie der Parameter mit geänderten Werten (für Szenarien/Sensitivität)."""
    p = copy.deepcopy(params or PARAMS)
    for k, v in overrides.items():
        p[k].wert = v
    return p
