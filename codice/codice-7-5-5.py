# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.5.5  |  Capitolo 7.5 - La caduta di tensione
# Sezione: Due casi a confronto

# CASO 2: alimentatore lungo (trifase 400 V)
def caduta(L, Ib, cosphi, S, Un=400.0, rho=0.0225):
    dU  = (math.sqrt(3) * rho * L * Ib * cosphi) / S
    return dU, dU / Un * 100.0

# prima scelta: S = 10 mm2
dU10, p10 = caduta(140.0, 40.0, 0.85, 10.0)
print("S=10 mm2 -> DeltaU = {:.2f} V  ({:.2f} %)".format(dU10, p10))

# upgrade: S = 16 mm2
dU16, p16 = caduta(140.0, 40.0, 0.85, 16.0)
print("S=16 mm2 -> DeltaU = {:.2f} V  ({:.2f} %)".format(dU16, p16))
