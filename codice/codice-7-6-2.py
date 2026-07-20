# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.6.2  |  Capitolo 7.6 - La copertura Wi-Fi
# Sezione: Passi 3--4 - il livello ricevuto e il verdetto

P_TX  = 20.0                        # potenza trasmessa (dBm)
PL0   = 40.0                        # path loss a d0 = 1 m (dB)
D0    = 1.0                         # distanza di riferimento (m)
N_ENV = 3.0                         # esponente d'ambiente (interni)
SOGLIA = -67.0                      # copertura voce/streaming (dBm)

def perdita_percorso(d):
    return PL0 + 10.0 * N_ENV * math.log10(d / D0)

def livello_ricevuto(ap_pt, p, caster, tabella):
    d = ap_pt.DistanceTo(p) * FT_M  # distanza in metri
    pl = perdita_percorso(d)
    att = attenuazione_ostacoli(ap_pt, p, caster, tabella)
    return P_TX - pl - att, d, pl, att

# PASSO 3-4: due punti da verificare (in piedi)
punti = {"P1": XYZ(6.80/FT_M, -2.20/FT_M, 2.50/FT_M),    # 8 m, 1 cartongesso
         "P2": XYZ(14.00/FT_M, -4.80/FT_M, 2.50/FT_M)}   # 15 m, oltre cemento

for nome, p in punti.items():
    prx, d, pl, att = livello_ricevuto(origine, p, caster, ATT)
    esito = "COPERTO" if prx >= SOGLIA else "OMBRA (non coperto)"
    print("{}: d={:.0f} m  PL={:.1f} dB  att={:.1f} dB  "
          "Prx={:.1f} dBm -> {}".format(nome, d, pl, att, prx, esito))
