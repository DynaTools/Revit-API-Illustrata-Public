# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.1.5  |  Capitolo 7.1 - Lo staffaggio
# Sezione: Bonus - tutte le passerelle del modello

# ============================================================
# 0. PREPARAZIONE                        [PY]+[REVIT]+[ENG]
#    blocco autonomo: librerie, documento e dati di progetto
# ============================================================
import math
from Autodesk.Revit.DB import (FilteredElementCollector,
                               BuiltInCategory, Transaction)

FT_M = 0.3048
PESI = {"FG16 4G95": 4.10, "FG16 5G16": 1.35, "FG16 3G2.5": 0.18}
PESO_PASSERELLA = 5.00
INTERASSE       = 1.50

doc = __revit__.ActiveUIDocument.Document

# ============================================================
# 1. BONUS, TUTTE LE PASSERELLE                        [REVIT]
#    il collector al posto del clic
# ============================================================
tratti = (FilteredElementCollector(doc)
          .OfCategory(BuiltInCategory.OST_CableTray)
          .WhereElementIsNotElementType())

# ============================================================
# 2. CALCOLO E SCRITTURA SU OGNI TRATTO        [ENG] + [REVIT]
#    stesse formule dei passi 2--4, una sola transazione
# ============================================================
tot = 0
t = Transaction(doc, "Staffaggio del modello")
t.Start()
for tr in tratti:
    par_n = tr.LookupParameter("Staffe n")
    par_i = tr.LookupParameter("Staffe interasse")
    if par_n is None or par_i is None:
        print("{}: SALTATO, parametri staffe assenti".format(tr.Name))
        continue
    L = tr.Location.Curve.Length * FT_M
    w_t = PESO_PASSERELLA
    for nome, peso in PESI.items():
        par = tr.LookupParameter(nome)
        w_t += peso * (par.AsInteger() if par else 0)
    n_t = int(math.ceil(L / INTERASSE)) + 1
    par_n.Set(n_t)
    par_i.Set(INTERASSE / FT_M)
    tot += n_t
    print("{}: L = {:5.2f} m  w = {:5.2f} kg/m  ->  {} staffe".format(
        tr.Name, L, w_t, n_t))
t.Commit()

# ============================================================
# 3. IL TOTALE DEL MODELLO                               [OUT]
# ============================================================
print("---")
print("Totale staffe nel modello: {}".format(tot))
