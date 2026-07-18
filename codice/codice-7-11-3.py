# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.11.3  |  Capitolo 7.11 - La copertura Wi-Fi
# Sezione: Bonus - la mappa di copertura su una griglia

# griglia 2D sul pavimento (passo 1 m), z = 1.20 m (altezza utile)
passo = 1.0 / FT_M
x0, y0 = 0.0, -4.0 / FT_M
nx, ny = 11, 6
z = 1.20 / FT_M

coperti, ombre = 0, 0
for j in range(ny):
    riga = ""
    for i in range(nx):
        p = XYZ(x0 + i*passo, y0 + j*passo, z)
        prx, _, _, _ = livello_ricevuto(origine, p, caster, ATT)
        if prx >= SOGLIA:
            riga += "#"; coperti += 1          # coperto
        elif prx >= SOGLIA - 8.0:
            riga += "+"                        # marginale
        else:
            riga += "."; ombre += 1            # ombra
    print(riga)

tot = nx * ny
print("Coperti: {}/{}  ({:.0f}%)  Ombre: {}".format(
    coperti, tot, 100.0*coperti/tot, ombre))
