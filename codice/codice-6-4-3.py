# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.4.3  |  Capitolo 6.4 - Il riempimento dei cavidotti
# Sezione: Passo 4 - calcolare e verificare

# Riempimento percentuale: K = area cavi / area tubo
K = A_cavi / A_tubo

# Diametro equivalente del fascio e verifica CEI 64-8
Dt     = math.sqrt(somma_d2)         # diametro del fascio (mm)
De_min = 1.3 * Dt                    # diametro minimo richiesto
conforme = De >= De_min

print("Riempimento: {:.1f} %".format(K * 100))
print("Diametro fascio Dt: {:.1f} mm".format(Dt))
print("Diametro minimo del tubo (1.3 x Dt): {:.1f} mm".format(De_min))
print("Diametro reale del tubo De: {:.1f} mm".format(De))
print("---")
if conforme:
    print("ESITO: CONFORME (margine {:.1f} mm)".format(De - De_min))
else:
    print("ESITO: NON CONFORME - serve un tubo piu' grande")
