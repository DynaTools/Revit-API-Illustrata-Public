# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.15.2  |  Capitolo 7.15 - La pendenza dello scarico, dal tratto alla filiera
# Sezione: Passo 3 - il verdetto di fascia

# PASSO 3: il verdetto, una fascia con due versi (UNI EN 12056)
FASCIA_MIN = 1.0        # % - almeno, perche' l'acqua corra
FASCIA_MAX = 5.0        # % - al piu', perche' i solidi la seguano

def verdetto_fascia(p):
    print("Pendenza {:.2f} %  |  fascia [{:.2f}, {:.2f}] %".format(
        p, FASCIA_MIN, FASCIA_MAX))
    if p < FASCIA_MIN:
        print("ESITO: NON CONFORME - sotto la minima, l'acqua ristagna")
    elif p > FASCIA_MAX:
        print("ESITO: NON CONFORME - oltre la massima, la vena si separa")
    else:
        print("ESITO: CONFORME - dentro la fascia")

verdetto_fascia(p)                     # p dal Codice 7.15.1
