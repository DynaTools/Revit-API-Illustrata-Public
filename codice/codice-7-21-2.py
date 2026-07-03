# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.21.2  |  Capitolo 7.21 - Il numero di alzate di una scala
# Sezione: Passi 3--4 - alzata reale, pedata e verifica

# PASSI 3-4: alzata reale, pedata (Blondel), verifica
a = H / n_alzate                   # alzata reale (m): H spartito esatto
BLONDEL = 0.63                     # 2a + p = 63 cm (valore centrale)
p = BLONDEL - 2 * a                # pedata da Blondel (m)
n_pedate = n_alzate - 1            # una in meno delle alzate

A_MIN, A_MAX = 0.16, 0.18          # alzata di norma (m)
ok = A_MIN <= a <= A_MAX

print("Alzata reale a: {:.1f} cm".format(a * 100))
print("Pedata p (Blondel): {:.1f} cm".format(p * 100))
print("Numero di pedate: {}".format(n_pedate))
print("Controllo 2a+p: {:.1f} cm".format((2 * a + p) * 100))
print("---")
if ok:
    print("ESITO: ALZATA A NORMA ({:.0f} <= {:.1f} <= {:.0f} cm)".format(
        A_MIN * 100, a * 100, A_MAX * 100))
else:
    print("ESITO: ALZATA FUORI NORMA")
