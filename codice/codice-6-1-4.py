# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.1.4  |  Capitolo 6.1 - Le primitive geometriche
# Sezione: Retta, segmento e raggio - Line

from Autodesk.Revit.DB import XYZ

FT_M = 0.3048

# element = il tuo elemento lineare (es. uidoc.Selection.PickObject(...))
# Asse dell'elemento dal LocationCurve
curve = element.Location.Curve
P0    = curve.GetEndPoint(0)           # inizio (XYZ in piedi)
P1    = curve.GetEndPoint(1)           # fine
L_ft  = P0.DistanceTo(P1)
u     = (P1 - P0).Normalize()         # direzione unitaria

# Centro geometrico: P(t = L/2)
C = P0 + u * (L_ft / 2.0)

# Punto al terzo metro: P(t = 3 m)
t = 3.0 / FT_M                        # t in piedi
Pt = P0 + u * t

print("Centro: ({:.3f}, {:.3f}, {:.3f}) m".format(
    C.X*FT_M, C.Y*FT_M, C.Z*FT_M))
print("P(3 m): ({:.3f}, {:.3f}, {:.3f}) m".format(
    Pt.X*FT_M, Pt.Y*FT_M, Pt.Z*FT_M))
