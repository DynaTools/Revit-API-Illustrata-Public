# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.3.3  |  Capitolo 6.3 - La lunghezza del circuito
# Sezione: Passo 4 - sfrido e lunghezza totale

# PASSO 4: sfrido e lunghezza totale
sfrido_pct = 5.0     # margine per collegamenti e terminazioni (%)

L_geom   = L_orizz + L_vert                  # lunghezza geometrica
L_sfrido = L_geom * sfrido_pct / 100.0
L_cavo   = L_geom + L_sfrido                  # lunghezza del cavo

print("Lunghezza geometrica: {:.2f} m".format(L_geom))
print("Sfrido ({:.0f}%): {:.2f} m".format(sfrido_pct, L_sfrido))
print("---")
print("LUNGHEZZA DEL CAVO: {:.2f} m".format(L_cavo))
print("(il solo tratto orizzontale era {:.2f} m: +{:.0f}%)".format(
    L_orizz, (L_cavo / L_orizz - 1.0) * 100))
