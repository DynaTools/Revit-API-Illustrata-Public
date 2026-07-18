# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.20.1  |  Capitolo 7.20 - Area e perimetro di una stanza irregolare
# Sezione: Passo 2 - l'area con la shoelace

# PASSO 2: area di un poligono qualsiasi (formula di Gauss / shoelace)
def area_poligono(vertici):
    n = len(vertici)
    s = 0.0
    for i in range(n):
        x1, y1 = vertici[i]
        x2, y2 = vertici[(i + 1) % n]   # il vertice dopo, l'ultimo torna al primo
        s += x1 * y2 - x2 * y1          # prodotto incrociato
    return abs(s) / 2.0

# i sei vertici della pianta a L (in metri, antiorario)
stanza = [(0.0, 0.0), (6.0, 0.0), (6.0, 3.0),
          (3.0, 3.0), (3.0, 5.0), (0.0, 5.0)]

A = area_poligono(stanza)                 # area con la shoelace
A_box = 6.0 * 5.0                          # rettangolo che racchiude tutto

print("Area stanza (shoelace): {:.1f} m2".format(A))
print("Rettangolo che racchiude: {:.1f} m2".format(A_box))
print("Area del rientro (non pavimento): {:.1f} m2".format(A_box - A))
