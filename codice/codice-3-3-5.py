# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 3.3.5  |  Capitolo 3.3 - Il collector fino in fondo
# Sezione: Combinare i filtri

from System.Collections.Generic import List
from Autodesk.Revit.DB import (FilteredElementCollector,
                               BuiltInCategory,
                               ElementMulticategoryFilter)

# canali, tubazioni e passerelle in un colpo solo
categorie = List[BuiltInCategory]([BuiltInCategory.OST_DuctCurves,
                                   BuiltInCategory.OST_PipeCurves,
                                   BuiltInCategory.OST_CableTray])

rete_mep = (FilteredElementCollector(doc)
            .WherePasses(ElementMulticategoryFilter(categorie))
            .WhereElementIsNotElementType()
            .ToElements())
