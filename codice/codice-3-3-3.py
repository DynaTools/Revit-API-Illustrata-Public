# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 3.3.3  |  Capitolo 3.3 - Il collector fino in fondo
# Sezione: Filtri rapidi e filtri lenti

from Autodesk.Revit.DB import (FilteredElementCollector, Wall,
                               ElementLevelFilter)

# prima la maglia grossa (rapido), poi quella fine (lento)
muri_pt1 = (FilteredElementCollector(doc)
            .OfClass(Wall)                            # rapido
            .WherePasses(ElementLevelFilter(liv.Id))  # lento
            .ToElements())
