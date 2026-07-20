# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.5.3  |  Capitolo 7.5 - Il calcolo illuminotecnico punto per punto
# Sezione: Passo 4 - media, minimo, uniformità e verifica

# PASSO 4: valuta la griglia, calcola media / minimo / uniformita'
griglia_m = [XYZ(x, y, 0.80) for (x, y) in
             [(gx, gy) for gx in (0.5,1.5,2.5,3.5,4.5,5.5)
                       for gy in (0.5,1.5,2.5,3.5)]]

valori = [illuminamento(P, S_m) for P in griglia_m]

E_media = sum(valori) / len(valori)
E_min   = min(valori)
E_max   = max(valori)
U0      = E_min / E_media

# verifica norma: ufficio (UNI EN 12464-1)
Em_norma = 500.0
U0_norma = 0.60
conforme = (E_media >= Em_norma) and (U0 >= U0_norma)

print("E media: {:.0f} lux".format(E_media))
print("E min:   {:.0f} lux   E max: {:.0f} lux".format(E_min, E_max))
print("Uniformita U0: {:.2f}".format(U0))
print("---")
print("Richiesto (ufficio): Em >= {:.0f} lux, U0 >= {:.2f}".format(
    Em_norma, U0_norma))
if conforme:
    print("ESITO: CONFORME")
else:
    print("ESITO: NON CONFORME")
