# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.13.3  |  Capitolo 7.13 - Il volume di scavo di una trincea
# Sezione: Quando la sezione cambia

# tre stazioni lungo i 20 m: profondita' crescente (la canaletta scende)
def sezione_da(b, h, scarpata):
    top = b + 2.0 * h * scarpata
    return [(-b/2.0, 0.0), (b/2.0, 0.0), (top/2.0, h), (-top/2.0, h)]

A0 = area_poligono(sezione_da(0.40, 1.00, 0.50))   # stazione a 0 m
A1 = area_poligono(sezione_da(0.40, 1.20, 0.50))   # stazione a 10 m
A2 = area_poligono(sezione_da(0.40, 1.40, 0.50))   # stazione a 20 m

V = volume_trincea([A0, A1, A2], [10.0, 10.0])     # due tratti da 10 m

print("Aree alle stazioni: {:.2f}, {:.2f}, {:.2f} m2".format(A0, A1, A2))
print("Volume con sezione variabile: {:.2f} m3".format(V))
