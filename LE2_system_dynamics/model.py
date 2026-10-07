"""
SD-Modell Kaffrine in BPTK-Py (LE2): Daten laden, Parameter, Modell, Simulation.

Umsetzung des Kernmodells aus LE1:
Niederschlag -> Wasserverfuegbarkeit (Proxy) -> Ertrag -> Produktion -> Einkommen -> Abwanderung
mit den Schleifen R1 (Arbeitskräfte), R2 (Netzwerk), B1 (Versorgung), B2 (Rücküberweisungen)
und dem natürlichen Bevölkerungswachstum (R3).

Bevölkerung und Abwanderung in Personen, Klima bis Einkommen als Index (1 = Normaljahr bzw. 2013).
"""
from dataclasses import dataclass, asdict, replace
from pathlib import Path

import pandas as pd
from BPTK_Py import Model, bptk
from BPTK_Py import sd_functions as sd

DATA_RAW = Path(__file__).resolve().parent.parent / "data" / "raw"
REFERENZ = (1991, 2020)  # Normalperiode für den Niederschlag


# ---------------------------------------------------------------------------
# Daten
# ---------------------------------------------------------------------------

def lade_niederschlag():
    """Jahresniederschlag Kaffrine (mm), Mittel über alle CHIRPS-Rasterzellen, und Referenz 1991-2020."""
    raw = pd.read_csv(DATA_RAW / "chirps_kaffrine_1991_2023.csv", skiprows=[1])  # 2. Zeile: Einheiten
    raw["jahr"] = pd.to_datetime(raw["time"]).dt.year
    reihe = raw[raw["jahr"] <= 2023].groupby("jahr")["precip"].mean()
    ref = reihe.loc[REFERENZ[0]:REFERENZ[1]].mean()
    return reihe, ref


def lade_bevoelkerung(datentyp=None):
    """Bevoelkerungsreihe laden; optional auf einen Datentyp filtern."""
    raw = pd.read_csv(DATA_RAW / "ansd_bevoelkerung_kaffrine.csv")
    if datentyp is not None:
        datentypen = [datentyp] if isinstance(datentyp, str) else list(datentyp)
        raw = raw[raw["datentyp"].isin(datentypen)]
    return raw.set_index("jahr")["bevoelkerung"]


def lade_migration(vollstaendig=False):
    """Migration laden; standardmaessig als Series fuer die Modellkompatibilitaet."""
    raw = pd.read_csv(DATA_RAW / "ansd_migration_kaffrine_2023.csv")
    if vollstaendig:
        return raw
    return raw.set_index("groesse")["personen"]


def niederschlag_szenario(reihe, ref, aenderung=0.0, duerre_alle=None, duerre_staerke=0.3, ab=2024, bis=2050):
    """
    Daten bis 2023, danach Szenario:
    - aenderung: dauerhafte Änderung gegenüber der Referenz (z.B. -0.15)
    - duerre_alle: alle n Jahre ein Dürrejahr mit duerre_staerke weniger Niederschlag
    """
    punkte = {j: mm for j, mm in reihe.items() if j < ab}
    for j in range(ab, bis + 1):
        mm = ref * (1 + aenderung)
        if duerre_alle and (j - ab) % duerre_alle == 0:
            mm *= 1 - duerre_staerke
        punkte[j] = mm
    return punkte


# ---------------------------------------------------------------------------
# Parameter
# ---------------------------------------------------------------------------

@dataclass
class Param:
    wert: float
    einheit: str
    beschreibung: str
    quelle: str
    status: str  # "Daten" oder "Annahme"


PARAMS = {
    "starttime": Param(2013, "Jahr", "Start: Volkszählung 2013", "ANSD, RGPH-4", "Daten"),
    "stoptime": Param(2050, "Jahr", "Ende des Szenariohorizonts", "Systemgrenze LE1", "Annahme"),
    "dt": Param(1, "Jahr", "Zeitschritt; Niederschlag liegt jährlich vor", "CHIRPS", "Annahme"),
    "bevoelkerung_0": Param(566_992, "Personen", "Bevölkerung Kaffrine 2013", "ANSD, RGPH-4", "Daten"),
    "abwanderungsrate_basis": Param(0.0074, "1/Jahr", "Abwanderungsrate im Normaljahr",
                                    "ANSD, RGPH-5: 27 588 Wegzüge in 5 Jahren (innerhalb Senegals)", "Daten"),
    "rate_natuerliches_wachstum": Param(0.0336, "1/Jahr", "Geburten minus Todesfälle pro Person; regionale Näherung 2023",
                                        "ANSD, RGPH-5 2023: 38.6‰ Geburten minus 5.0‰ Sterbefälle", "Annahme"),
    "verweildauer": Param(20, "Jahre", "Zeit, die eine abgewanderte Person zum Netzwerk zählt", "Annahme", "Annahme"),
    "elast_ertrag": Param(1.0, "-", "10 % weniger Regen = 10 % weniger Ertrag", "Annahme (Regenfeldbau)", "Annahme"),
    "elast_arbeit": Param(0.3, "-", "10 % weniger Arbeitskräfte = 3 % weniger Produktion (R1)", "Annahme", "Annahme"),
    "anteil_rueck": Param(0.15, "-", "Anteil Rücküberweisungen am Haushaltseinkommen (B2)", "Annahme", "Annahme"),
    "wirkung_einkommen": Param(1.0, "-", "10 % weniger Einkommen pro Kopf = 10 % mehr Abwanderung", "Annahme", "Annahme"),
    "wirkung_nahrung": Param(1.0, "-", "10 % weniger Nahrung pro Person = 10 % mehr Abwanderung (B1)", "Annahme", "Annahme"),
    "wirkung_netzwerk": Param(0.5, "-", "10 % mehr Abgewanderte = 5 % mehr Abwanderung (R2)", "Annahme", "Annahme"),
}


def with_overrides(params=None, **neue_werte):
    """Kopie der Parameter mit geänderten Werten, z.B. with_overrides(elast_arbeit=0.6)."""
    p = dict(params or PARAMS)
    for name, wert in neue_werte.items():
        p[name] = replace(p[name], wert=wert)
    return p


def parameter_tabelle(params=None):
    return pd.DataFrame({k: asdict(p) for k, p in (params or PARAMS).items()}).T


# ---------------------------------------------------------------------------
# Modell
# ---------------------------------------------------------------------------

GROESSEN = ["bevoelkerung", "abgewanderte", "abwanderung", "abwanderungsrate", "niederschlag_index",
            "wasserverfuegbarkeit_index",
            "produktion_index", "nahrung_pk_index", "haushaltseinkommen_index"]


def build_model(niederschlag, ref, params=None, name="kaffrine"):
    p = params or PARAMS
    v = lambda k: p[k].wert
    m = Model(starttime=v("starttime"), stoptime=v("stoptime"), dt=v("dt"), name=name)

    c = {}
    for k in ["rate_natuerliches_wachstum", "abwanderungsrate_basis", "verweildauer", "elast_ertrag",
              "elast_arbeit", "anteil_rueck", "wirkung_einkommen", "wirkung_nahrung", "wirkung_netzwerk"]:
        c[k] = m.constant(k)
        c[k].equation = v(k)

    bev_0 = v("bevoelkerung_0")
    abg_0 = v("abwanderungsrate_basis") * bev_0 * v("verweildauer")  # Gleichgewicht im Normaljahr

    # Stocks
    bev = m.stock("bevoelkerung")
    bev.initial_value = bev_0
    abg = m.stock("abgewanderte")
    abg.initial_value = abg_0

    # Niederschlag (von aussen)
    m.points["niederschlag"] = sorted([[j, mm] for j, mm in niederschlag.items()])
    ns = m.converter("niederschlag")
    ns.equation = sd.lookup(sd.time(), "niederschlag")
    ns_idx = m.converter("niederschlag_index")
    ns_idx.equation = ns / ref

    # Klima -> Wasserverfuegbarkeit -> Landwirtschaft. Die Wasserverfuegbarkeit
    # ist mangels eigener Wasserbilanz ein normierter Niederschlagsproxy.
    wasser = m.converter("wasserverfuegbarkeit_index")
    wasser.equation = ns_idx
    ertrag = m.converter("ertrag_index")
    ertrag.equation = sd.max(0, 1 + c["elast_ertrag"] * (wasser - 1))
    bev_idx = m.converter("bevoelkerung_index")
    bev_idx.equation = bev / bev_0
    prod = m.converter("produktion_index")                                   # R1
    prod.equation = ertrag * (1 + c["elast_arbeit"] * (bev_idx - 1))

    # Pro Kopf
    nahrung = m.converter("nahrung_pk_index")                                # B1
    nahrung.equation = prod / bev_idx
    rueck = m.converter("rueck_pk_index")                                    # B2
    rueck.equation = (abg / bev) / (abg_0 / bev_0)
    hh = m.converter("haushaltseinkommen_index")
    hh.equation = (1 - c["anteil_rueck"]) * (prod / bev_idx) + c["anteil_rueck"] * rueck

    # Abwanderungsrate
    druck = m.converter("druck")
    druck.equation = c["wirkung_einkommen"] * (1 - hh) + c["wirkung_nahrung"] * (1 - nahrung)
    netz = m.converter("netzwerk_faktor")                                    # R2
    netz.equation = sd.max(0, 1 + c["wirkung_netzwerk"] * (abg / abg_0 - 1))
    rate = m.converter("abwanderungsrate")
    rate.equation = c["abwanderungsrate_basis"] * sd.max(0, 1 + druck) * netz

    # Flows
    wachstum = m.flow("natuerliches_wachstum")
    wachstum.equation = bev * c["rate_natuerliches_wachstum"]
    abw = m.flow("abwanderung")
    abw.equation = bev * rate
    abgang = m.flow("abgang_netzwerk")
    abgang.equation = abg / c["verweildauer"]

    bev.equation = wachstum - abw
    abg.equation = abw - abgang
    return m


def simuliere(niederschlag, ref, params=None, name="basis"):
    """Ein Lauf als DataFrame (Index: Jahr)."""
    m = build_model(niederschlag, ref, params, name)
    b = bptk()
    b.register_model(m)
    b.register_scenario_manager({f"sm_{name}": {"model": m, "base_constants": {}}})
    b.register_scenarios(scenario_manager=f"sm_{name}", scenarios={name: {}})
    df = b.run_scenarios(scenario_managers=[f"sm_{name}"], scenarios=[name], equations=GROESSEN, return_format="df")
    df.index = df.index.astype(int)
    df.index.name = "jahr"
    return df
