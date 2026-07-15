# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.2.2  |  Capitolo 7.2 - La lunghezza del circuito
# Sezione: Passo 3 - la lunghezza 3D contro quella in pianta

# ============================================================
# 0. RIPARTENZA                                 [PY] + [REVIT]
#    blocco autonomo: riclicca l'intero percorso
# ============================================================
import math
from Autodesk.Revit.DB import LocationCurve
from Autodesk.Revit.UI.Selection import ObjectType

FT_M  = 0.3048
uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document
refs  = uidoc.Selection.PickObjects(ObjectType.Element,
                                    "Seleziona tutto il percorso, poi Finish")

# ============================================================
# 1. PASSO 3, 3D CONTRO PIANTA                           [ENG]
#    per ogni tratto: lunghezza 3D e ombra in pianta (solo xy)
# ============================================================
L3d_ft = 0.0
Lpl_ft = 0.0
for r in refs:
    loc = doc.GetElement(r.ElementId).Location
    if isinstance(loc, LocationCurve):
        c  = loc.Curve
        p0 = c.GetEndPoint(0)
        p1 = c.GetEndPoint(1)
        L3d_ft += c.Length                                # 3D reale
        Lpl_ft += math.hypot(p1.X - p0.X, p1.Y - p0.Y)    # proiezione in pianta

L3d = L3d_ft * FT_M
Lpl = Lpl_ft * FT_M

# ============================================================
# 2. L'ESITO                                             [OUT]
# ============================================================
print("Lunghezza in pianta:  {:.2f} m".format(Lpl))
print("Lunghezza 3D (reale): {:.2f} m".format(L3d))
print("Salite e discese:     {:.2f} m".format(L3d - Lpl))
