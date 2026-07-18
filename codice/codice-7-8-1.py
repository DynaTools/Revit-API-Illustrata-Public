# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.8.1  |  Capitolo 7.8 - L'aria, portata e ricambi
# Sezione: Passi 1--2 - raccogliere il condotto

from Autodesk.Revit.DB import (BuiltInParameter, UnitUtils, UnitTypeId)
from Autodesk.Revit.UI.Selection import ObjectType

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

# PASSO 1: clicca il condotto nel modello
ref      = uidoc.Selection.PickObject(ObjectType.Element,
                                      "Seleziona il condotto")
condotto = doc.GetElement(ref.ElementId)

# PASSO 2: leggi la sezione (rettangolare) e la portata
p_larg = condotto.get_Parameter(BuiltInParameter.RBS_CURVE_WIDTH_PARAM)
p_alt  = condotto.get_Parameter(BuiltInParameter.RBS_CURVE_HEIGHT_PARAM)
p_q    = condotto.get_Parameter(BuiltInParameter.RBS_DUCT_FLOW_PARAM)

# dai piedi ai metri, dai piedi cubi/s ai m3/s (Legge II)
larg = UnitUtils.ConvertFromInternalUnits(p_larg.AsDouble(), UnitTypeId.Meters)
alt  = UnitUtils.ConvertFromInternalUnits(p_alt.AsDouble(),  UnitTypeId.Meters)
Q    = UnitUtils.ConvertFromInternalUnits(p_q.AsDouble(),
                                          UnitTypeId.CubicMetersPerSecond)

A = larg * alt                       # area della sezione in m2

print("Condotto DA-01")
print("Sezione: {:.0f} x {:.0f} mm".format(larg * 1000, alt * 1000))
print("Area della sezione: {:.3f} m2".format(A))
print("Portata: {:.3f} m3/s  ({:.0f} L/s = {:.0f} m3/h)".format(
    Q, Q * 1000, Q * 3600))
