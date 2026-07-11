# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.5.3  |  Capitolo 7.5 - La caduta di tensione
# Sezione: Passo 3 - calcolare la caduta

# ============================================================
# 0. RIPARTENZA                            [PY]+[REVIT]+[ENG]
#    blocco autonomo: ricrea lunghezza e dati elettrici
# ============================================================
from Autodesk.Revit.UI.Selection import ObjectType

FT_M = 0.3048
# dati del passo 2: V, A, cosphi, mm2, ohm*mm2/m
Un, Ib, cosphi, S, rho = 400.0, 28.0, 0.85, 6.0, 0.0225

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document
refs  = uidoc.Selection.PickObjects(ObjectType.Element,
                                    "Seleziona i tratti del percorso")

L = 0.0
for r in refs:
    L += doc.GetElement(r.ElementId).Location.Curve.Length * FT_M

# ============================================================
# 1. PASSO 3, LA FORMULA TRIFASE                         [ENG]
#    DeltaU = (sqrt(3) * rho * L * Ib * cosphi) / S
# ============================================================
import math

dU  = (math.sqrt(3) * rho * L * Ib * cosphi) / S    # in volt
dU_pct = dU / Un * 100.0                             # in percentuale

# ============================================================
# 2. L'ESITO                                             [OUT]
# ============================================================
print("Caduta di tensione DeltaU: {:.2f} V".format(dU))
print("Caduta percentuale DeltaU%: {:.2f} %".format(dU_pct))
