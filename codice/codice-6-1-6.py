# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.1.6  |  Capitolo 6.1 - I primitivi geometrici
# Sezione: La sfera di contenimento

import math
from Autodesk.Revit.DB import XYZ

FT_M = 0.3048

bb   = element.get_BoundingBox(None)
C    = bb.Min + (bb.Max - bb.Min) * 0.5   # centro
r_ft = C.DistanceTo(bb.Max)               # raggio in piedi (semidiagonale)
r_m  = r_ft * FT_M

# Test rapido: il punto Q e' nella sfera di contenimento?
Q = XYZ(35.0 / FT_M, 19.0 / FT_M, 4.0 / FT_M)
in_sfera = C.DistanceTo(Q) <= r_ft

print("Centro: ({:.2f}, {:.2f}, {:.2f}) m".format(
    C.X*FT_M, C.Y*FT_M, C.Z*FT_M))
print("Raggio: {:.3f} m".format(r_m))
print("Q nella sfera?", in_sfera)
