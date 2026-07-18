# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 3.4.5  |  Capitolo 3.4 - Il Python del mestiere
# Sezione: Il criterio come argomento, lambda

larghezze = [0.20, 0.45, 0.10, 0.30]
print(max(larghezze))          # il criterio ovvio

quota = {"lavabo": 0.85, "vaso": 0.40, "doccia": 2.10}

# il criterio lo decidi tu, con key=
print(max(quota, key=lambda nome: quota[nome]))
print(sorted(quota, key=lambda nome: quota[nome]))
