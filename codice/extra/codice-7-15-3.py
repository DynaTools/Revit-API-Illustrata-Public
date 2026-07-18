# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.15.3  |  Capitolo 7.15 - Il campo visivo di una telecamera
# Sezione: Bonus - la mappa di copertura

# BONUS: copertura su una griglia di punti a pavimento
PASSO = 1.0 / FT_M                 # griglia da 1 m (in piedi)
visti = 0
totali = 0
for i in range(0, 18):             # x da 0 a 17 m
    for j in range(-8, 9):         # y da -8 a +8 m
        q = XYZ(i * PASSO, j * PASSO, 0.0)
        totali += 1
        dentro, alfa, dist = dentro_cono(cam, w, q, THETA)
        if not dentro or dist > R:
            continue               # fuori cono o oltre R
        if not linea_libera(cam, q, ri):
            continue               # occluso da muro/pilastro
        visti += 1

copertura = 100.0 * visti / totali
print("Punti visibili e riconoscibili: {} su {}".format(visti, totali))
print("Copertura utile: {:.1f}%".format(copertura))
