# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 3.3.2  |  Capitolo 3.3 - Il collector fino in fondo
# Sezione: Filtri rapidi e filtri lenti

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

# stessi canali, due domande diverse
istanze = (FilteredElementCollector(doc)
           .OfCategory(BuiltInCategory.OST_DuctCurves)
           .WhereElementIsNotElementType())   # i pezzi posati

tipi = (FilteredElementCollector(doc)
        .OfCategory(BuiltInCategory.OST_DuctCurves)
        .WhereElementIsElementType())         # le ricette a catalogo

print("canali posati    ->", istanze.GetElementCount())
print("tipi a catalogo  ->", tipi.GetElementCount())
