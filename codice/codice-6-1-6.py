# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.1.6  |  Capitolo 6.1 - I primitivi geometrici
# Sezione: Il bounding box allineato (AABB) - BoundingBoxXYZ

from Autodesk.Revit.DB import (Outline, BoundingBoxIntersectsFilter,
    FilteredElementCollector, BuiltInCategory)

FT_M = 0.3048

# element = il tuo elemento (es. uidoc.Selection.PickObject(...))
# AABB dell'elemento selezionato
bb = element.get_BoundingBox(None)
d  = bb.Max - bb.Min                     # vettore dimensioni (in piedi)
C  = bb.Min + d * 0.5                    # centro
V  = d.X * d.Y * d.Z * (FT_M ** 3)     # volume in m^3

print("Min: ({:.2f}, {:.2f}, {:.2f}) m".format(
    bb.Min.X*FT_M, bb.Min.Y*FT_M, bb.Min.Z*FT_M))
print("Max: ({:.2f}, {:.2f}, {:.2f}) m".format(
    bb.Max.X*FT_M, bb.Max.Y*FT_M, bb.Max.Z*FT_M))
print("Volume AABB: {:.2f} m^3   Volume OBB reale: 0.36 m^3".format(V))

# Clash detection con strutture: elementi che intersecano questo AABB
outline  = Outline(bb.Min, bb.Max)
bb_filt  = BoundingBoxIntersectsFilter(outline)
clash = (FilteredElementCollector(doc)
         .OfCategory(BuiltInCategory.OST_StructuralFraming)
         .WherePasses(bb_filt)
         .ToElements())
print("Strutture nell'AABB: {}".format(len(clash)))
