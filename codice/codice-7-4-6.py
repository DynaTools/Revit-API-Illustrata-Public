# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.4.6  |  Capitolo 7.4 - Distribuire con lo schema L-2L
# Sezione: La stessa musica sul muro, le prese

from Autodesk.Revit.DB import XYZ

# PASSO 3: valuta i punti P(t_i) e alzali all'altezza di montaggio
punti = []
for i in range(N):
    t  = (i + 0.5) / N              # parametro normalizzato t_i
    pt = curve.Evaluate(t, True)    # punto sull'asse (XYZ in piedi)
    pt = XYZ(pt.X, pt.Y, pt.Z + h / FT_M)   # alza a h (h in metri -> piedi)
    punti.append(pt)
    print("presa {}: t={:.3f}  d={:.3f} m  ({:.2f}, {:.2f}) m".format(
        i, t, t * L, pt.X * FT_M, pt.Y * FT_M))

print("---")
print("Punti generati: {}".format(len(punti)))
