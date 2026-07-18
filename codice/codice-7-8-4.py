# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.8.4  |  Capitolo 7.8 - L'aria, portata e ricambi
# Sezione: Dalla velocità ai ricambi d'aria

import math
from Autodesk.Revit.DB import (FilteredElementCollector, BuiltInCategory,
    SpatialElement)

FT_M = 0.3048                      # 1 piede = 0.3048 m
FT3_M3 = FT_M ** 3                 # 1 piede cubo = 0.3048^3 m3

doc = __revit__.ActiveUIDocument.Document

# PASSO 1: leggi il volume della prima stanza (Room)
stanza = (FilteredElementCollector(doc)
          .OfCategory(BuiltInCategory.OST_Rooms)
          .WhereElementIsNotElementType()
          .FirstElement())

V = stanza.Volume * FT3_M3         # volume in m3 (Room.Volume e' in piedi cubi)

# PASSO 2: la portata richiesta dai ricambi della norma
n = 2.0                            # ricambi orari (regola pratica; UNI 10339 ragiona per persona)
Q = n * V                          # portata richiesta in m3/h

# PASSO 3: il numero di diffusori
q_diff = 72.0                      # portata per diffusore (m3/h)
N_diff = int(math.ceil(Q / q_diff))

print("Stanza: {}".format(stanza.Name))
print("Volume V: {:.2f} m3".format(V))
print("Ricambi n: {:.1f} vol/h".format(n))
print("Portata Q = n*V: {:.1f} m3/h".format(Q))
print("Diffusori = ceil({:.1f} / {:.0f}) = {}".format(Q, q_diff, N_diff))
