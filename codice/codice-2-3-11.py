# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 2.3.11  |  Capitolo 2.3 - RevitPythonShell: il playground
# Sezione: Ripetere: for, il nastro trasportatore

total = 0
for wall in walls:
    total = total + 1   # +1 a ogni giro
print(total)            # FUORI dal for: solo alla fine
