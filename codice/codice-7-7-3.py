# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.7.3  |  Capitolo 7.7 - Lo spazio da difendere
# Sezione: Passo 4 - riportare le violazioni

# PASSO 4: verdetto
print("Quadro {}: spazio di lavoro {:.2f} m (CEI 64-8)".format(
    quadro.Name, 0.70))
print("---")
if len(intrusi) == 0:
    print("ESITO: ZONA LIBERA - nessuna violazione")
else:
    print("ESITO: ZONA VIOLATA - {} intruso/i".format(len(intrusi)))
    for e in intrusi:
        print("  violazione: {} '{}'".format(e.Category.Name, e.Name))
