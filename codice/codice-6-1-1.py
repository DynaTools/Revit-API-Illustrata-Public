# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.1.1  |  Capitolo 6.1 - I primitivi geometrici
# Sezione: Il punto - XYZ

from Autodesk.Revit.DB import XYZ

FT_M = 0.3048         # Revit usa i piedi; 1 piede = 0.3048 m

# Estremi dell'asse della passerella EC-01
P0 = XYZ(27.204 / FT_M, 15.200 / FT_M, 4.00 / FT_M)
P1 = XYZ(37.596 / FT_M, 21.200 / FT_M, 4.00 / FT_M)

# Vettore direzione e lunghezza
v = P1 - P0
print("Vettore: ({:.3f}, {:.3f}, {:.3f}) ft".format(v.X, v.Y, v.Z))
print("Distanza: {:.3f} m".format(P0.DistanceTo(P1) * FT_M))

# Vettore unitario (la direzione senza la lunghezza)
u = v.Normalize()
print("Direzione: ({:.3f}, {:.3f}, {:.3f})".format(u.X, u.Y, u.Z))
