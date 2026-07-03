# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 2.3.12  |  Capitolo 2.3 - RevitPythonShell: il playground
# Sezione: Ripetere: for, il nastro trasportatore

for wall in walls:
    if wall.Width > 0.2:
        print(wall.Name)
