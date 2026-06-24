# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.1.10  |  Capitolo 6.1 - I primitivi geometrici
# Sezione: I primitivi applicati alle categorie Revit

from Autodesk.Revit.DB import (FilteredElementCollector, BuiltInCategory, XYZ)

FT_M = 0.3048

wall = (FilteredElementCollector(doc)
        .OfCategory(BuiltInCategory.OST_Walls)
        .WhereElementIsNotElementType().FirstElement())

axis = wall.Location.Curve          # asse del muro (centerline)
n    = wall.Orientation             # normale: punta verso l'esterno
p0   = axis.GetEndPoint(0)

print("Asse muro da ({:.2f}, {:.2f}) a ({:.2f}, {:.2f}) m".format(
    p0.X*FT_M, p0.Y*FT_M,
    axis.GetEndPoint(1).X*FT_M, axis.GetEndPoint(1).Y*FT_M))
print("Normale (esterno): ({:.0f}, {:.0f}, {:.0f})".format(n.X, n.Y, n.Z))

# Da che lato del muro si trova il centro della EC-01?
C = XYZ(32.40 / FT_M, 18.20 / FT_M, 4.00 / FT_M)
d = n.DotProduct(C - p0) * FT_M     # distanza con segno
lato = "esterno" if d > 0 else "interno"
print("EC-01 sul lato {}: {:.2f} m dall'asse".format(lato, abs(d)))
