# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 3.3.1  |  Capitolo 3.3 - Il collector fino in fondo
# Sezione: I quattro ingressi dello schedario

from Autodesk.Revit.DB import FilteredElementCollector

# 1. l'archivio intero
tutto = FilteredElementCollector(doc)

# 2. gli elementi che Revit puo' iterare nella vista attiva
vista = FilteredElementCollector(doc, doc.ActiveView.Id)

# 3. solo un mazzo di schede che hai gia' in mano
scelti = FilteredElementCollector(doc, uidoc.Selection.GetElementIds())

print("archivio intero  ->", tutto.GetElementCount())
print("nella vista      ->", vista.GetElementCount())
print("nella selezione  ->", scelti.GetElementCount())
