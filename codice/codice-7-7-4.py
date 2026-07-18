# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.7.4  |  Capitolo 7.7 - Lo spazio da difendere
# Sezione: Bonus - disegnare la zona nel modello

from Autodesk.Revit.DB import (Transaction, DirectShape, ElementId,
    BuiltInCategory, GeometryCreationUtilities, CurveLoop, Line)

# rettangolo di base della zona (a z=0) -> estruso fino a H
P0 = XYZ(zmin.X, zmin.Y, 0.0)
P1 = XYZ(zmax.X, zmin.Y, 0.0)
P2 = XYZ(zmax.X, zmax.Y, 0.0)
P3 = XYZ(zmin.X, zmax.Y, 0.0)

loop = CurveLoop()
for a, b in [(P0, P1), (P1, P2), (P2, P3), (P3, P0)]:
    loop.Append(Line.CreateBound(a, b))

solido = GeometryCreationUtilities.CreateExtrusionGeometry(
    [loop], XYZ.BasisZ, H)            # estrudo verso l'alto fino ad H

t = Transaction(doc, "Zona di lavoro QE-01")
t.Start()
ds = DirectShape.CreateElement(
    doc, ElementId(BuiltInCategory.OST_GenericModel))
ds.SetShape([solido])
ds.Name = "Zona lavoro QE-01"
t.Commit()

print("Creata la zona di lavoro come DirectShape nel modello.")
