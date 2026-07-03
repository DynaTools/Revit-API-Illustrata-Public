# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.17.2  |  Capitolo 7.17 - Le pendenze: scarico e rampa
# Sezione: Passo 3 - il verdetto, col verso giusto

# PASSO 3: confronto col verso giusto e verdetto
def verdetto(p, soglia, e_minimo):
    if e_minimo:
        ok = p >= soglia               # scarico: serve almeno la minima
        verso = ">="
    else:
        ok = p <= soglia               # rampa: non oltre la massima
        verso = "<="
    print("Pendenza {:.2f} %  {}  soglia {:.2f} %".format(p, verso, soglia))
    print("ESITO: {}".format("CONFORME" if ok else "NON CONFORME"))
    return ok

# caso SCARICO: soglia MINIMA 1%
verdetto(p, 1.0, e_minimo=True)
