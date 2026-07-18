# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 3.3.4  |  Capitolo 3.3 - Il collector fino in fondo
# Sezione: Il filtro su parametro, pezzo per pezzo

from Autodesk.Revit.DB import (
    FilteredElementCollector, BuiltInCategory, BuiltInParameter,
    ElementId, ParameterValueProvider, FilterStringRule,
    FilterStringEquals, ElementParameterFilter)

# 1. quale colonna dello schedario (il parametro Mark)
p_id = ElementId(BuiltInParameter.ALL_MODEL_MARK)
# 2. chi va a leggerla, elemento per elemento
fornitore = ParameterValueProvider(p_id)
# 3. la regola del confronto
regola = FilterStringRule(fornitore, FilterStringEquals(), "MEP-001")
# 4. la regola diventa un filtro
filtro = ElementParameterFilter(regola)

trovati = (FilteredElementCollector(doc)
           .OfCategory(BuiltInCategory.OST_MechanicalEquipment)
           .WhereElementIsNotElementType()   # rapidi, prima
           .WherePasses(filtro)              # lento, per ultimo
           .ToElements())

print("trovati ->", len(trovati))
for e in trovati:
    print(e.Name)
