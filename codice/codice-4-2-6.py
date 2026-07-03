# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 4.2.6  |  Capitolo 4.2 - Il metodo Spy → Replicare → Generalizzare
# Sezione: Un caso completo, da cima a fondo

panels = FilteredElementCollector(doc)\
    .OfCategory(BuiltInCategory.OST_ElectricalEquipment)\
    .WhereElementIsNotElementType()         # LEGGE III

t = Transaction(doc, "COD_LOCALIZACAO - quadri elettrici")
t.Start()
for q in panels:                           # R7
    level = doc.GetElement(q.LevelId)       # domino via Id
    code = level.Name[:3] + "-EL"         # P02-EL, P03-EL...
    p = q.LookupParameter("COD_LOCALIZACAO")
    if p and not p.IsReadOnly:
        p.Set(code)
t.Commit()
