# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.7.2  |  Capitolo 7.7 - Lo spazio da difendere
# Sezione: Passo 3 - chi interseca la zona

from Autodesk.Revit.DB import (BoundingBoxIntersectsFilter,
    ElementId)
from System.Collections.Generic import List

# PASSO 3: filtro spaziale AABB-AABB sulla zona
filt = BoundingBoxIntersectsFilter(Outline(zmin, zmax))

esclusi = List[ElementId]([quadro.Id])     # non l'intruso: e' il quadro stesso

intrusi = (FilteredElementCollector(doc)
           .WherePasses(filt)
           .Excluding(esclusi)
           .WhereElementIsNotElementType()
           .ToElements())

# scarto il muro retrostante: non e' un ostacolo "davanti"
intrusi = [e for e in intrusi
           if e.Category and e.Category.Id.IntegerValue
              != int(BuiltInCategory.OST_Walls)]

print("Elementi che invadono la zona: {}".format(len(intrusi)))
for e in intrusi:
    print("  - {} ({})".format(e.Category.Name, e.Name))
