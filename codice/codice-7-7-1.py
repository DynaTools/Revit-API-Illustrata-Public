# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.7.1  |  Capitolo 7.7 - La distribuzione delle prese
# Sezione: Passi 1--2 - il muro e i parametri

import math
from Autodesk.Revit.UI.Selection import ObjectType

FT_M = 0.3048                       # 1 piede = 0.3048 m

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

# PASSO 1: clicca il muro e leggi il suo asse
ref   = uidoc.Selection.PickObject(ObjectType.Element, "Seleziona il muro")
wall  = doc.GetElement(ref.ElementId)
curve = wall.Location.Curve         # asse del muro (centerline)
L     = curve.Length * FT_M         # lunghezza dell'asse in metri

# PASSO 2: numero di prese e parametri normalizzati t_i
passo_max = 1.50                    # passo massimo (m)
h         = 0.30                    # altezza di montaggio (m)

N = int(math.ceil(L / passo_max))   # numero di intervalli (e di prese)
s = L / N                           # passo reale (m)

print("Muro lungo: {:.2f} m".format(L))
print("Passo massimo: {:.2f} m  ->  N = {} prese".format(passo_max, N))
print("Passo reale s = L/N: {:.2f} m".format(s))
print("Margine ai bordi (s/2): {:.3f} m".format(s / 2.0))
