# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 3.3.1  |  Capitolo 3.3 - Il collector fino in fondo
# Sezione: Tre modi di aprire lo schedario

from Autodesk.Revit.DB import FilteredElementCollector

# 1. l'archivio intero
tutto = FilteredElementCollector(doc)

# 2. solo cio' che una vista itera (non "cio' che vedo")
vista = FilteredElementCollector(doc, doc.ActiveView.Id)

# 3. solo un mazzo di schede che hai gia' in mano
scelti = FilteredElementCollector(doc, uidoc.Selection.GetElementIds())

print("archivio intero  ->", len(list(tutto)))
print("nella vista      ->", len(list(vista)))
print("nella selezione  ->", len(list(scelti)))
