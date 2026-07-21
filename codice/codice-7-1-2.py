# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.1.2  |  Capitolo 7.1 - La lunghezza del circuito
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
#    solo i tratti dritti: 3D reale e ombra in pianta (x,y)
# ============================================================
L3d_ft = 0.0
Lpl_ft = 0.0

for r in refs:
    elem_id = r.ElementId
    elem    = doc.GetElement(elem_id)
    loc     = elem.Location

    if isinstance(loc, LocationCurve):
        curva = loc.Curve
        p0    = curva.GetEndPoint(0)      # punto iniziale
        p1    = curva.GetEndPoint(1)      # punto finale

        dx = p1.X - p0.X                  # differenza in x
        dy = p1.Y - p0.Y                  # differenza in y

        L3d_ft += curva.Length                   # 3D reale
        Lpl_ft += math.sqrt(dx * dx + dy * dy)   # ombra in pianta

L3d = L3d_ft * FT_M
Lpl = Lpl_ft * FT_M

# ============================================================
# 2. L'ESITO                                             [OUT]
# ============================================================
print("Lunghezza in pianta:  {:.2f} m".format(Lpl))
print("Lunghezza 3D (reale): {:.2f} m".format(L3d))
print("Salite e discese:     {:.2f} m".format(L3d - Lpl))
