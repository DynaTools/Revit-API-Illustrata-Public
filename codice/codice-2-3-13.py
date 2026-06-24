# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 2.3.13  |  Capitolo 2.3 - Revit Python Shell: il playground
# Sezione: Mettendo insieme nel playground

from Autodesk.Revit.DB import *

walls = FilteredElementCollector(doc)\
    .OfClass(Wall)\
    .WhereElementIsNotElementType()

total = 0
grossas = 0
for wall in walls:
    total = total + 1
    if wall.Width > 0.2:
        grossas = grossas + 1

print("Muri in totale:", total)
print("Spessi (> 0.2):", grossas)
