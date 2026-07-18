# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.16.3  |  Capitolo 7.16 - Le unità di scarico e il diametro della colonna
# Sezione: Bonus - la radice all'opera su più bagni

# BONUS: simultaneita' -- piu' bagni completi sulla stessa colonna
K = 0.5
def scegli_dn(q):
    if q <= 0.8: return "DN50"
    elif q <= 1.5: return "DN75"
    else: return "DN100"

DU_BAGNO = 3.6                          # un bagno completo
for n in [1, 2, 3, 4]:
    sdu = DU_BAGNO * n
    qww = K * math.sqrt(sdu)
    nome = "bagno" if n == 1 else "bagni"
    print("{} {}: somma DU = {:.1f}  ->  Qww = {:.2f} L/s  ->  {}".format(
        n, nome, sdu, qww, scegli_dn(qww)))
