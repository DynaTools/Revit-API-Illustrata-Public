# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.4.2  |  Capitolo 7.4 - Lo schema L--2L
# Sezione: In Revit - la formula del centro genera i punti

# ============================================================
# 0. RIPARTENZA                                 [PY] + [REVIT]
#    blocco autonomo: rilegge la stanza, rifa' passo e bordo
# ============================================================
from Autodesk.Revit.DB import XYZ
from Autodesk.Revit.UI.Selection import ObjectType

FT_M  = 0.3048
uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

ref = uidoc.Selection.PickObject(ObjectType.Element,
                                 "Seleziona la stanza")
bb  = doc.GetElement(ref.ElementId).get_BoundingBox(None)

x0 = bb.Min.X * FT_M;  A = (bb.Max.X - bb.Min.X) * FT_M
y0 = bb.Min.Y * FT_M;  B = (bb.Max.Y - bb.Min.Y) * FT_M
z  = bb.Max.Z * FT_M                       # quota soffitto

nx, ny = 4, 3
sx = A / nx;  sy = B / ny

# ============================================================
# 1. LA FORMULA DEL CENTRO                        [PY] + [ENG]
#    x = x0 + (i + 1/2)*s: il doppio ciclo genera la griglia
# ============================================================
punti = []
for i in range(nx):
    for j in range(ny):
        x = x0 + (i + 0.5) * sx        # centro cella lungo x
        y = y0 + (j + 0.5) * sy        # centro cella lungo y
        punti.append(XYZ(x / FT_M, y / FT_M, z / FT_M))   # XYZ in piedi

# ============================================================
# 2. IL RISULTATO                                        [OUT]
# ============================================================
print("Punti generati: {}".format(len(punti)))
for p in punti[:4]:
    print("  ({:.2f}, {:.2f}) m".format(p.X * FT_M, p.Y * FT_M))
print("  ...")
