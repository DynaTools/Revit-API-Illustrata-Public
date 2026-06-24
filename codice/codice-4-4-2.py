# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 4.4.2  |  Capitolo 4.4 - Gli errori che compaiono nel progetto reale
# Sezione: Nelle unità: il piede nascosto

from Autodesk.Revit.DB import UnitUtils, UnitTypeId

larg_ft = p.AsDouble()                                  # PIEDI (interno)
larg_mm = UnitUtils.ConvertFromInternalUnits(larg_ft, UnitTypeId.Millimeters)
