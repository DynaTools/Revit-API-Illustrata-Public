# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.5.2  |  Capitolo 6.5 - Lo schema L-2L
# Sezione: In Revit - leggere la stanza e posare le luci

# genera i punti con la formula del centro
punti = []
for i in range(nx):
    for j in range(ny):
        x = x0 + (i + 0.5) * sx        # centro cella lungo x
        y = y0 + (j + 0.5) * sy        # centro cella lungo y
        punti.append(XYZ(x / FT_M, y / FT_M, z / FT_M))   # XYZ in piedi

print("Punti generati: {}".format(len(punti)))
for p in punti[:4]:
    print("  ({:.2f}, {:.2f}) m".format(p.X * FT_M, p.Y * FT_M))
print("  ...")
