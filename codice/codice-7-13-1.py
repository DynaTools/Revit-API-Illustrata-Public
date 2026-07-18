# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.13.1  |  Capitolo 7.13 - Il volume di scavo di una trincea
# Sezione: Passi 1--2 - la sezione e la sua area

# PASSO 2: area di un poligono qualsiasi (formula di Gauss / shoelace)
def area_poligono(vertici):
    n = len(vertici)
    s = 0.0
    for i in range(n):
        x1, y1 = vertici[i]
        x2, y2 = vertici[(i + 1) % n]   # il vertice dopo, l'ultimo torna al primo
        s += x1 * y2 - x2 * y1          # prodotto incrociato
    return abs(s) / 2.0

# PASSO 1: i vertici della sezione dai parametri di progetto
b = 0.40            # larghezza di fondo (m)
h = 1.00            # profondita' (m)
scarpata = 0.50     # coefficiente m = 0,5 -> 0,5 m di allargamento per metro

top = b + 2.0 * h * scarpata           # larghezza in sommita'
sezione = [(-b/2.0, 0.0), (b/2.0, 0.0),    # fondo: P1, P2
           (top/2.0, h), (-top/2.0, h)]    # sommita': P3, P4

A = area_poligono(sezione)             # area con la shoelace
A_trap = (b + top) / 2.0 * h           # verifica: formula del trapezio
A_rett = b * h                         # ipotesi rettangolare "a occhio"

print("Larghezza in sommita' (top): {:.2f} m".format(top))
print("Area sezione (shoelace): {:.2f} m2".format(A))
print("Area sezione (trapezio): {:.2f} m2".format(A_trap))
print("Ipotesi rettangolare b*h: {:.2f} m2".format(A_rett))
print("Errore ipotesi rettangolare: {:.2f} %".format(
    (A - A_rett) / A * 100.0))
