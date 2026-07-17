# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.1.9  |  Capitolo 6.1 - Le primitive geometriche
# Sezione: Il raggio - ReferenceIntersectorsec:raggio

from Autodesk.Revit.DB import (ReferenceIntersector, XYZ,
    FindReferenceTarget, ElementCategoryFilter, BuiltInCategory)

FT_M = 0.3048

# view3d = una vista 3D attiva (es. doc.ActiveView, se e' una View3D)
# Crea l'intersector su una vista 3D (necessaria)
cat_filt    = ElementCategoryFilter(BuiltInCategory.OST_StructuralColumns)
intersector = ReferenceIntersector(cat_filt,
                  FindReferenceTarget.Face, view3d)
intersector.FindReferencesInRevitLinks = False

# Raggio verticale verso il basso dall'asse EC-01
origin    = XYZ(32.40 / FT_M, 18.20 / FT_M, 8.00 / FT_M)   # da 8 m
direction = XYZ(0, 0, -1)                                      # verso il basso

result = intersector.FindNearest(origin, direction)
if result:
    t_m = result.Proximity * FT_M
    print("Prima superficie colpita a {:.3f} m".format(t_m))
    print("Riferimento: {}".format(result.GetReference().ElementId))
else:
    print("Nessuna superficie colpita nella direzione data.")
