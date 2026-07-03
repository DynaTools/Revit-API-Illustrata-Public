# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.9.4  |  Capitolo 7.9 - La portata d'aria nei condotti
# Sezione: Bonus - il canale circolare equivalente

import math

# diametro del canale circolare con la stessa area (stessa velocita')
D_eq = math.sqrt(4.0 * A / math.pi)

print("Sezione rettangolare: {:.3f} m2".format(A))
print("Diametro circolare equivalente: {:.0f} mm".format(D_eq * 1000))
print("(stessa area -> stessa velocita': {:.2f} m/s)".format(Q / A))
