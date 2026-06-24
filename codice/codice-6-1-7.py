# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.1.7  |  Capitolo 6.1 - I primitivi geometrici
# Sezione: Il raggio - ReferenceIntersector

from Autodesk.Revit.DB import (ReferenceIntersector, XYZ,
    FindReferenceTarget, ElementCategoryFilter, BuiltInCategory)

FT_M = 0.3048

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
