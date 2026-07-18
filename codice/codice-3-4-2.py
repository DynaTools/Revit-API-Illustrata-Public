# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 3.4.2  |  Capitolo 3.4 - Il Python del mestiere
# Sezione: La ricetta che scrivi tu, def

def in_metri(piedi):
    return piedi * 0.3048     # la conversione della Legge II

print(in_metri(10))
print("{:.2f} m".format(in_metri(32.8)))
