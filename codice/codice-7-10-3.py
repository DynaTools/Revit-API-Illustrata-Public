# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.10.3  |  Capitolo 7.10 - La distanza minima fra due percorsi
# Sezione: Bonus - il clash di prossimità su tutto il modello

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

# raccolgo i percorsi MEP (passerelle, tubi, cavidotti, condotti)
cats = [BuiltInCategory.OST_CableTray, BuiltInCategory.OST_PipeCurves,
        BuiltInCategory.OST_Conduit,   BuiltInCategory.OST_DuctCurves]
perc = []
for cat in cats:
    perc += list(FilteredElementCollector(doc).OfCategory(cat)
                 .WhereElementIsNotElementType())

FRANCO = 0.20                      # m
sotto = []
for i in range(len(perc)):
    for j in range(i + 1, len(perc)):
        ki = perc[i].Location.Curve
        kj = perc[j].Location.Curve
        C1, C2, s, t = distanza_segmenti(
            ki.GetEndPoint(0), ki.GetEndPoint(1),
            kj.GetEndPoint(0), kj.GetEndPoint(1))
        dij = C1.DistanceTo(C2) * FT_M
        if dij < FRANCO:
            sotto.append((perc[i].Name, perc[j].Name, dij))

print("Coppie sotto il franco di {:.2f} m: {}".format(FRANCO, len(sotto)))
for na, nb, dij in sotto:
    print("  {} <-> {}: {:.2f} m".format(na, nb, dij))
