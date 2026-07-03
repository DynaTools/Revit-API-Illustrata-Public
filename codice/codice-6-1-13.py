# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.1.13  |  Capitolo 6.1 - I primitivi geometrici
# Sezione: I primitivi applicati alle categorie Revit

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

FT_M = 0.3048

categorie = [
    ("CableTray", BuiltInCategory.OST_CableTray),
    ("Conduit",   BuiltInCategory.OST_Conduit),
    ("Pipe",      BuiltInCategory.OST_PipeCurves),
    ("Duct",      BuiltInCategory.OST_DuctCurves),
]

for nome, bic in categorie:
    elementi = (FilteredElementCollector(doc)
                .OfCategory(bic)
                .WhereElementIsNotElementType().ToElements())
    L = 0.0
    for e in elementi:
        L += e.Location.Curve.Length * FT_M   # vale per ogni MEPCurve
    print("{:>10}: {:>2} elementi, {:>6.2f} m".format(nome, len(elementi), L))
