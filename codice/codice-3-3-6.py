# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 3.3.6  |  Capitolo 3.3 - Il collector fino in fondo
# Sezione: La sequenza mentale

# prima i filtri di Revit...
equip = (FilteredElementCollector(doc)
         .OfCategory(BuiltInCategory.OST_MechanicalEquipment)  # universo
         .WhereElementIsNotElementType()                       # istanze
         .ToElements())                                        # raccolta

# ...poi Python, solo sul residuo
uta = [e for e in equip if "UTA" in e.Symbol.Family.Name]
print("unita' di trattamento ->", len(uta))
