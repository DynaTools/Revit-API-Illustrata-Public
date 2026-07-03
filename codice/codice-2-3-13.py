# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 2.3.13  |  Capitolo 2.3 - RevitPythonShell: il playground
# Sezione: Mettendo insieme nel playground

from Autodesk.Revit.DB import *

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document

walls = FilteredElementCollector(doc)\
    .OfClass(Wall)\
    .WhereElementIsNotElementType()

total = 0
spessi = 0

for wall in walls:
    total = total + 1
    if wall.Width > 0.2:
        spessi = spessi + 1

print("Muri in totale:", total)
print("Spessi (> 0.2):", spessi)
