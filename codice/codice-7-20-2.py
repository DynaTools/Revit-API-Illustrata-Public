# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.20.2  |  Capitolo 7.20 - Area e perimetro di una stanza irregolare
# Sezione: Passo 3 - il perimetro come somma dei lati

import math

# PASSO 3: perimetro = somma delle lunghezze dei lati
def perimetro_poligono(vertici):
    n = len(vertici)
    P = 0.0
    for i in range(n):
        x1, y1 = vertici[i]
        x2, y2 = vertici[(i + 1) % n]      # vertice consecutivo (l'ultimo chiude)
        P += math.hypot(x2 - x1, y2 - y1)  # distanza fra i due estremi
    return P

P = perimetro_poligono(stanza)

print("Perimetro stanza: {:.1f} m".format(P))
