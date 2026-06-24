# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 3.2.2  |  Capitolo 3.2 - Il primo script: raccogliere ed elencare
# Sezione: Il collector: la domanda che si fa al modello

n = (
    FilteredElementCollector(doc)            # R4 - costruttore senza new
    .OfCategory(BuiltInCategory.OST_Walls)   # R2 + R6
    .WhereElementIsNotElementType()          # LEGGE III - solo istanze
    .GetElementCount()                       # R2 - metodo, con ( )
)
print(n)
