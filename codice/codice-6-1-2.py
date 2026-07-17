# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.1.2  |  Capitolo 6.1 - Le primitive geometriche
# Sezione: I due prodotti e l'angolo

import math
from Autodesk.Revit.DB import XYZ

# Direzione della EC-01 (dal paragrafo Il punto) e asse globale X
u = XYZ(0.866, 0.500, 0.0)
x = XYZ(1.0,   0.0,   0.0)

# Prodotto scalare -> allineamento -> coseno
dot   = u.DotProduct(x)
cos_t = dot / (u.GetLength() * x.GetLength())
print("u . x      = {:.3f}".format(dot))      # 0.866 = cos 30
print("cos(theta) = {:.3f}".format(cos_t))

# Angolo: dalla formula (arccos) e dal metodo nativo -> coincidono
print("arccos  = {:.1f} gradi".format(math.degrees(math.acos(cos_t))))
print("AngleTo = {:.1f} gradi".format(math.degrees(u.AngleTo(x))))

# Prodotto vettoriale -> perpendicolarita -> seno
cross = u.CrossProduct(x)
print("|u x x| = {:.3f}".format(cross.GetLength()))   # 0.500 = sin 30
