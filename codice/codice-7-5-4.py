# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.5.4  |  Capitolo 7.5 - La caduta di tensione
# Sezione: Passo 4 - verificare contro il 4%

# ============================================================
# 0. RIPARTENZA                            [PY]+[REVIT]+[ENG]
#    blocco autonomo: ricrea la caduta percentuale dU_pct
# ============================================================
import math
from Autodesk.Revit.DB import LocationCurve
from Autodesk.Revit.UI.Selection import ObjectType

FT_M = 0.3048
# dati del passo 2: V, A, cosphi, mm2, ohm*mm2/m
Un, Ib, cosphi, S, rho = 400.0, 28.0, 0.85, 6.0, 0.0225

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document
refs  = uidoc.Selection.PickObjects(ObjectType.Element,
                                    "Seleziona tutto il percorso, poi Finish")

L_mod = 0.0
for r in refs:
    loc = doc.GetElement(r.ElementId).Location
    if isinstance(loc, LocationCurve):
        L_mod += loc.Curve.Length * FT_M
L = L_mod * 1.05                    # lunghezza del cavo (+ 5% di sfrido)

dU_pct = (math.sqrt(3) * rho * L * Ib * cosphi) / S / Un * 100.0

# ============================================================
# 1. PASSO 4, LA VERIFICA CEI 64-8                       [ENG]
#    conforme se la caduta sta sotto il limite del 4%
# ============================================================
LIMITE = 4.0        # caduta massima ammessa (%) - CEI 64-8
conforme = dU_pct <= LIMITE

# ============================================================
# 2. IL VERDETTO                                         [OUT]
# ============================================================
print("DeltaU% = {:.2f} %   limite = {:.0f} %".format(dU_pct, LIMITE))
print("---")
if conforme:
    print("ESITO: CONFORME (margine {:.2f} punti)".format(
        LIMITE - dU_pct))
else:
    print("ESITO: NON CONFORME - serve una sezione maggiore")
