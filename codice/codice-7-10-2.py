# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.10.2  |  Capitolo 7.10 - La pressione dell'acqua fredda in bagno
# Sezione: Passo 3 - calcolare la pressione residua

# PASSO 3: pressione residua a ogni apparecchio (in mca)
perdite = PERDITA_DISTRIB + PERDITA_STACCO     # mca totali

risultati = []
for nome, z_app, p_min in apparecchi:
    battente = Z_SERBATOIO - z_app             # dislivello geodetico
    p_res    = battente - perdite              # pressione residua (mca)
    risultati.append((nome, z_app, battente, p_res, p_min))
    print("{:<20} quota {:.2f} m  battente {:.2f} mca  ->  "
          "residua {:.2f} mca ({:.0f} kPa)".format(
              nome, z_app, battente, p_res, p_res * 9.81))
