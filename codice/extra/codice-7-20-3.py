# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.20.3  |  Capitolo 7.20 - Area e perimetro di una stanza irregolare
# Sezione: Passo 4 - il battiscopa, meno le porte

# PASSO 4: battiscopa = perimetro meno le luci delle porte
luci_porte = [0.90, 0.90]                 # due porte da 0,90 m

L_porte = sum(luci_porte)
L_battiscopa = P - L_porte                # contorno meno i vani porta

print("Perimetro:        {:.1f} m".format(P))
print("Luci porte:       {:.1f} m ({} porte)".format(L_porte, len(luci_porte)))
print("---")
print("BATTISCOPA:       {:.1f} m".format(L_battiscopa))
