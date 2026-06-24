# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 2.1.1  |  Capitolo 2.1 - La Pietra di Rosetta
# Sezione: Decifrare da capo a fondo

walls = FilteredElementCollector(doc)\
    .OfCategory(BuiltInCategory.OST_Walls)\
    .WhereElementIsNotElementType()      # Legge III - solo istanze

for wall in walls:                     # Regola 7 - for diretto
    p = wall.LookupParameter("Commenti") # Regola 2 - metodo ( )
    print(wall.Name, p.AsString())       # Regola 1 - proprietà
