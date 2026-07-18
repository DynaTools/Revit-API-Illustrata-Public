# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.7.6  |  Capitolo 7.7 - Lo spazio da difendere
# Sezione: Il caso verticale, l'altezza libera

# PASSO 4: confronto con l'altezza libera minima di norma
H_MIN = 2.40                       # altezza libera minima richiesta (m)
conforme = h_libera >= H_MIN

print("Altezza libera minima richiesta: {:.2f} m".format(H_MIN))
print("Altezza libera reale: {:.2f} m".format(h_libera))
print("---")
if conforme:
    print("ESITO: CONFORME (margine {:.2f} m)".format(h_libera - H_MIN))
else:
    print("ESITO: NON CONFORME - manca {:.2f} m".format(H_MIN - h_libera))
    print("  ostacolo critico: {} a {:.2f} m".format(nome_basso, z_basso))
