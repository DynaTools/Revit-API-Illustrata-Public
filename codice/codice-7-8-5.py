# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.8.5  |  Capitolo 7.8 - L'aria, portata e ricambi
# Sezione: Dalla velocità ai ricambi d'aria

# stesso strumento, sala con occupazione piu' densa
n = 2.5                            # ricambi orari (vol/h)
Q = n * V                         # 2.5 * 72.00 = 180.0 m3/h
N_diff = int(math.ceil(Q / q_diff))

print("Ricambi n: {:.1f} vol/h".format(n))
print("Portata Q = n*V: {:.1f} m3/h".format(Q))
print("Rapporto Q/q_diff: {:.1f}".format(Q / q_diff))
print("Diffusori = ceil({:.1f}) = {}".format(Q / q_diff, N_diff))
