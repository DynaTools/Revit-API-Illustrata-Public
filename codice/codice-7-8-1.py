# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.8.1  |  Capitolo 7.8 - Lo spazio di lavoro davanti al quadro
# Sezione: Passi 1--2 - il quadro e la sua zona

from Autodesk.Revit.DB import (FilteredElementCollector, BuiltInCategory,
    XYZ, Outline)

FT_M = 0.3048                      # 1 piede = 0.3048 m

doc = __revit__.ActiveUIDocument.Document

# PASSO 1: individua il quadro (prima apparecchiatura elettrica)
quadro = (FilteredElementCollector(doc)
          .OfCategory(BuiltInCategory.OST_ElectricalEquipment)
          .WhereElementIsNotElementType()
          .FirstElement())

bb = quadro.get_BoundingBox(None)   # AABB del quadro (in piedi)
n  = quadro.FacingOrientation       # normale: dove "guarda" il quadro

# PASSO 2: costruisci la zona di lavoro davanti alla faccia
p = 0.70 / FT_M                     # profondita' richiesta (piedi)
H = 2.00 / FT_M                     # altezza utile da terra (piedi)

# la faccia frontale e' il lato del bbox dalla parte della normale:
# spingo Min e Max in avanti di p*n e impongo z da 0 a H
avanti = XYZ(n.X * p, n.Y * p, 0.0)
zmin = XYZ(min(bb.Min.X, bb.Min.X + avanti.X),
           min(bb.Min.Y, bb.Min.Y + avanti.Y), 0.0)
zmax = XYZ(max(bb.Max.X, bb.Max.X + avanti.X),
           max(bb.Max.Y, bb.Max.Y + avanti.Y), H)

print("Quadro: {}".format(quadro.Name))
print("Orientamento n: ({:.0f}, {:.0f}, {:.0f})".format(n.X, n.Y, n.Z))
print("Zona min: ({:.2f}, {:.2f}, {:.2f}) m".format(
    zmin.X*FT_M, zmin.Y*FT_M, zmin.Z*FT_M))
print("Zona max: ({:.2f}, {:.2f}, {:.2f}) m".format(
    zmax.X*FT_M, zmax.Y*FT_M, zmax.Z*FT_M))
