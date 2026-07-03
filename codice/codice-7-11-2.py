# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.11.2  |  Capitolo 7.11 - La distanza minima fra due percorsi
# Sezione: Passi 3--4 - confronto e verdetto

# PASSI 3-4: confronto col franco minimo e verdetto
FRANCO = 0.20                      # franco minimo richiesto (m) -- da norma
conforme = d >= FRANCO

print("Franco minimo richiesto: {:.2f} m".format(FRANCO))
print("Distanza reale: {:.2f} m".format(d))
print("---")
if conforme:
    print("ESITO: CONFORME (margine {:.2f} m)".format(d - FRANCO))
else:
    print("ESITO: NON CONFORME - i due percorsi sono troppo vicini")
