# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.2.2  |  Capitolo 7.2 - La lunghezza del circuito
# Sezione: Passo 3 - discese e risalite

# PASSO 3: discese e risalite (quote in metri)
z_quadro = 2.0       # punto di partenza del cavo nel quadro QE-01
z_carico = 0.8       # morsettiera del motore M-12

risalita = z_pass - z_quadro     # dal quadro su alla passerella
discesa  = z_pass - z_carico     # dalla passerella giu' al motore
L_vert   = risalita + discesa

print("Risalita al quadro: {:.2f} m".format(risalita))
print("Discesa al motore:  {:.2f} m".format(discesa))
print("Totale verticale:   {:.2f} m".format(L_vert))
