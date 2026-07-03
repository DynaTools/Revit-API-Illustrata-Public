# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.21.1  |  Capitolo 7.21 - Il numero di alzate di una scala
# Sezione: Passi 1--2 - il dislivello e il numero di alzate

import math
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

FT_M = 0.3048                      # 1 piede = 0.3048 m

doc = __revit__.ActiveUIDocument.Document

# PASSO 1: leggi i livelli e ordinali per quota
livelli = (FilteredElementCollector(doc)
           .OfCategory(BuiltInCategory.OST_Levels)
           .WhereElementIsNotElementType()
           .ToElements())
livelli = sorted(livelli, key=lambda L: L.Elevation)

inf = livelli[0]                   # piano di partenza (quota piu' bassa)
sup = livelli[1]                   # piano di arrivo (il successivo)

# dislivello fra i due livelli, in metri
H = (sup.Elevation - inf.Elevation) * FT_M

# PASSO 2: numero di alzate = ceil(H / alzata massima)
A_MAX = 0.18                       # alzata massima di norma (m)
n_alzate = int(math.ceil(H / A_MAX))

print("Da '{}' a '{}'".format(inf.Name, sup.Name))
print("Dislivello H: {:.2f} m".format(H))
print("H / a_max: {:.2f}".format(H / A_MAX))
print("Numero di alzate (ceil): {}".format(n_alzate))
