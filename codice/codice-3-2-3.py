# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 3.2.3  |  Capitolo 3.2 - Il primo script
# Sezione: Sezionando, riga per riga

total = 0
walls = FilteredElementCollector(doc)\
    .OfClass(Wall)\
    .WhereElementIsNotElementType()      # LEGGE III

for w in walls:                        # R7
    curve  = w.Location.Curve            # R1 - domino
    total += curve.Length                # R1 - in piedi! (LEGGE II)

metri = UnitUtils.ConvertFromInternalUnits(total, UnitTypeId.Meters)
print(round(metri, 2), "m")
