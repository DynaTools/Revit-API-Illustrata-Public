# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.16.2  |  Capitolo 7.16 - Il bilanciamento delle fasi su un quadro
# Sezione: Passo 4 - il confronto: sequenziale contro LPT

# PASSO 4: confronto NAIVE (round-robin, senza ordinare) contro LPT

# naive: assegna in sequenza R,S,T,R,S,T... cosi' come capitano i carichi
def assegna_naive(carichi):
    fasi = [[], [], []]
    for i, c in enumerate(carichi):
        fasi[i % 3].append(c)
    return fasi

fasi_n = assegna_naive(carichi)
sq_n, somme_n = squilibrio(fasi_n)

fasi_l = assegna_lpt(carichi)
sq_l, somme_l = squilibrio(fasi_l)

SOGLIA = 15.0                      # squilibrio massimo ammesso (%)

print("NAIVE  somme R/S/T: {} kW".format([round(s, 1) for s in somme_n]))
print("NAIVE  squilibrio: {:.1f}%".format(sq_n))
print("---")
print("LPT    somme R/S/T: {} kW".format([round(s, 1) for s in somme_l]))
print("LPT    squilibrio: {:.1f}%".format(sq_l))
print("---")
print("Soglia ammessa: {:.0f}%".format(SOGLIA))
if sq_l <= SOGLIA:
    print("ESITO: CONFORME con LPT (margine {:.1f} punti)".format(SOGLIA - sq_l))
else:
    print("ESITO: NON CONFORME - fasi ancora troppo squilibrate")
