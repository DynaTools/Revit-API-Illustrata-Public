# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 3.4.1  |  Capitolo 3.4 - Il Python del mestiere
# Sezione: L'etichetta con le finestrelle, format

n = 42
larghezza = 0.4572

print("muri trovati -> " + str(n))        # concatenare stanca
print("muri trovati -> {}".format(n))     # la finestrella
print("{} muri, il piu' spesso {:.2f} m".format(n, larghezza))
