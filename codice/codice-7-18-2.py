# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.18.2  |  Capitolo 7.18 - Le unità di scarico e il diametro della colonna
# Sezione: Passi 3--4 - la portata e il diametro

# PASSO 3: portata di acque reflue  Qww = K * sqrt(somma_du)
K   = 0.5                              # uso intermittente (abitazioni)
Qww = K * math.sqrt(somma_du)          # L/s

# PASSO 4: scegli il DN dalla tabella di soglie (UNI EN 12056-2)
def scegli_dn(q):
    if q <= 0.8:
        return "DN50"
    elif q <= 1.5:
        return "DN75"
    else:
        return "DN100"

DN = scegli_dn(Qww)

print("Somma DU: {:.1f}".format(somma_du))
print("Portata Qww = {:.1f} * sqrt({:.1f}) = {:.2f} L/s".format(
    K, somma_du, Qww))
print("---")
print("Diametro della colonna: {}".format(DN))
