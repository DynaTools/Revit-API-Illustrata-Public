# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.5.1  |  Capitolo 6.5 - Lo schema L-2L
# Sezione: In Revit - leggere la stanza e posare le luci

# -*- coding: utf-8 -*-
from Autodesk.Revit.DB import XYZ
from Autodesk.Revit.UI.Selection import ObjectType

FT_M = 0.3048

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

# clicca la stanza e leggi il suo riquadro (AABB)
ref  = uidoc.Selection.PickObject(ObjectType.Element, "Seleziona la stanza")
room = doc.GetElement(ref.ElementId)
bb   = room.get_BoundingBox(None)

x0 = bb.Min.X * FT_M;  A = (bb.Max.X - bb.Min.X) * FT_M
y0 = bb.Min.Y * FT_M;  B = (bb.Max.Y - bb.Min.Y) * FT_M
z  = bb.Max.Z * FT_M                       # quota soffitto

# scelta della griglia
nx, ny = 4, 3
sx = A / nx
sy = B / ny

print("Stanza: {:.2f} x {:.2f} m".format(A, B))
print("Griglia {}x{}  ->  passo {:.2f} x {:.2f} m".format(nx, ny, sx, sy))
print("Bordo: {:.2f} x {:.2f} m".format(sx/2, sy/2))
