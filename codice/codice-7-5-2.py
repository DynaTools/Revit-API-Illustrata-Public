# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.5.2  |  Capitolo 7.5 - La caduta di tensione
# Sezione: Passo 2 - i dati elettrici del circuito

# ============================================================
# 0. RIPARTENZA                                           [PY]
#    blocco autonomo: questo passo non tocca il modello
# ============================================================
# niente import e niente selezione: solo dati di progetto

# ============================================================
# 1. PASSO 2, I DATI ELETTRICI                           [ENG]
#    tensione, corrente, cos(phi), sezione, resistivita'
# ============================================================
Un     = 400.0      # tensione nominale trifase (V)
Ib     = 28.0       # corrente d'impiego del motore M-12 (A)
cosphi = 0.85       # fattore di potenza
S      = 6.0        # sezione del conduttore di rame (mm2)
rho    = 0.0225     # resistivita' rame a 70 C (ohm*mm2/m, valore CEI)

# ============================================================
# 2. LA CARTA DEL CIRCUITO                               [OUT]
# ============================================================
print("Motore M-12: 15 kW, trifase {:.0f} V".format(Un))
print("Ib = {:.0f} A   cosphi = {:.2f}   S = {:.0f} mm2".format(
    Ib, cosphi, S))
