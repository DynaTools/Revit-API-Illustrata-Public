# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.6.1  |  Capitolo 7.6 - Il calcolo illuminotecnico punto per punto
# Sezione: Passi 1--2 - apparecchi e griglia dal modello

import math
from Autodesk.Revit.DB import (FilteredElementCollector, BuiltInCategory,
    XYZ)

FT_M = 0.3048                      # 1 piede = 0.3048 m

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

# PASSO 1: leggi gli apparecchi illuminanti dal modello
apparecchi = (FilteredElementCollector(doc)
              .OfCategory(BuiltInCategory.OST_LightingFixtures)
              .WhereElementIsNotElementType()
              .ToElements())

sorgenti = []                      # lista di (x, y, z) in metri
for ap in apparecchi:
    p = ap.Location.Point          # XYZ in piedi
    sorgenti.append(XYZ(p.X * FT_M, p.Y * FT_M, p.Z * FT_M))

# PASSO 2: bounding box del locale (un Room) -> griglia sul piano di lavoro
room   = uidoc.Selection.PickElementsByRectangle()[0]  # o un Room scelto
bb     = room.get_BoundingBox(None)
x0, x1 = bb.Min.X * FT_M, bb.Max.X * FT_M    # confini in metri
y0, y1 = bb.Min.Y * FT_M, bb.Max.Y * FT_M

z_piano = 0.80                     # piano di lavoro a 0,80 m
passo   = 1.00                     # maglia della griglia: 1,0 m
griglia = []
gx = x0 + passo / 2.0
while gx < x1:
    gy = y0 + passo / 2.0
    while gy < y1:
        griglia.append((gx, gy, z_piano))
        gy += passo
    gx += passo

print("Apparecchi trovati: {}".format(len(sorgenti)))
print("Locale: {:.1f} x {:.1f} m".format(x1 - x0, y1 - y0))
print("Punti di griglia: {}".format(len(griglia)))
