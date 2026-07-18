# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.15.1  |  Capitolo 7.15 - Il campo visivo di una telecamera
# Sezione: Passi 1--3 - telecamera, cono e distanza

import math
from Autodesk.Revit.DB import XYZ

FT_M = 0.3048                      # 1 piede = 0.3048 m

# il punto p e' dentro il cono (cam, asse w unitario, semiapertura theta)?
def dentro_cono(cam, w, p, theta_gradi):
    d = p - cam                    # direzione verso il punto
    L = d.GetLength()
    if L == 0.0:
        return True, 0.0, 0.0
    coseno = d.DotProduct(w.Normalize()) / L   # cos dell'angolo asse-punto
    coseno = max(-1.0, min(1.0, coseno))
    alfa = math.degrees(math.acos(coseno))     # angolo effettivo (solo per il report)
    dentro = coseno >= math.cos(math.radians(theta_gradi))
    return dentro, alfa, L * FT_M  # esito, angolo in gradi, distanza in metri

# --- dati della telecamera (in piedi) ---
cam   = XYZ(0.0, 0.0, 0.0)
w     = XYZ(1.0, 0.0, 0.0)         # asse di vista: guarda verso +x
THETA = 45.0                       # semiapertura (FOV totale 90 gradi)
R     = 12.0                       # distanza di riconoscimento (m) -- DORI

# tre punti di prova (in piedi)
P = {"P1": XYZ(7.0/FT_M,  4.0/FT_M, 0.0),
     "P2": XYZ(9.0/FT_M,  3.0/FT_M, 0.0),
     "P3": XYZ(13.5/FT_M, 7.0/FT_M, 0.0)}

# PASSI 2-3: cono + distanza per ogni punto
for nome in ("P1", "P2", "P3"):
    dentro, alfa, dist = dentro_cono(cam, w, P[nome], THETA)
    entro_R = dist <= R
    print("{}: angolo = {:.2f} gradi, dist = {:.2f} m  ->  cono={}, entro R={}".format(
        nome, alfa, dist, dentro, entro_R))
