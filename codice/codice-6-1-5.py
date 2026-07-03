# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.1.5  |  Capitolo 6.1 - I primitivi geometrici
# Sezione: Il piano - Planesec:piano

from Autodesk.Revit.DB import Plane, XYZ

FT_M = 0.3048

# Piano orizzontale alla quota +4.00 m (come la EC-01)
normal = XYZ(0, 0, 1)
origin = XYZ(0, 0, 4.00 / FT_M)
piano  = Plane.CreateByNormalAndOrigin(normal, origin)

# Distanza con segno di un punto Q dal piano
# Q leggermente sopra il piano: z = 4.05 m
Q = XYZ(32.40 / FT_M, 18.20 / FT_M, 4.05 / FT_M)
# distanza con segno = proiezione di (Q - origine) sulla normale unitaria
delta_m = piano.Normal.DotProduct(Q - piano.Origin) * FT_M
print("Distanza con segno: {:.3f} m".format(delta_m))
print("Q sopra il piano?", delta_m > 0)

# Piano verticale che passa per la direzione u della EC-01
# n = vettore perpendicolare a u in piano orizzontale = (-0.5, 0.866, 0)
n_vert = XYZ(-0.5, 0.866, 0)
P_asse = XYZ(32.40 / FT_M, 18.20 / FT_M, 4.00 / FT_M)  # centro EC-01
piano_v = Plane.CreateByNormalAndOrigin(n_vert, P_asse)
print("Piano verticale creato. Normale: ({:.3f}, {:.3f}, {:.3f})".format(
    piano_v.Normal.X, piano_v.Normal.Y, piano_v.Normal.Z))
