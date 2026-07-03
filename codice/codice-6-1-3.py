# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.1.3  |  Capitolo 6.1 - I primitivi geometrici
# Sezione: I due prodotti e l'angolo

import math
from Autodesk.Revit.DB import XYZ

# Tubo di scarico: 5,00 m in orizzontale, 0,10 m di dislivello
P0 = XYZ(0.0, 0.0, 0.00)
P1 = XYZ(5.0, 0.0, 0.10)
u  = (P1 - P0).Normalize()

# u.Z e' il seno dell'angolo con il piano orizzontale
alpha = math.degrees(math.asin(u.Z))
print("Pendenza: {:.1f} gradi".format(alpha))
print("Pendenza: {:.1f} %".format(100.0 * math.tan(math.radians(alpha))))
