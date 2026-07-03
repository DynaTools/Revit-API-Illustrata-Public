# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.17.1  |  Capitolo 7.17 - Le pendenze: scarico e rampa
# Sezione: Passi 1--2 - leggere il tratto e calcolare

import math
from Autodesk.Revit.UI.Selection import ObjectType

FT_M = 0.3048                      # 1 piede = 0.3048 m

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

# pendenza (%) di un tratto dai suoi due estremi
def pendenza(P0, P1):
    dz = abs(P1.Z - P0.Z)                      # dislivello (verticale)
    dx = P1.X - P0.X
    dy = P1.Y - P0.Y
    L_orizz = math.sqrt(dx * dx + dy * dy)     # sviluppo in pianta
    p = dz / L_orizz * 100.0                   # rapporto, in %
    return p, dz * FT_M, L_orizz * FT_M        # % , dz (m), L (m)

# PASSO 1: clicca il tratto e leggi gli estremi
ref = uidoc.Selection.PickObject(ObjectType.Element, "Tratto da verificare")
el  = doc.GetElement(ref.ElementId)
k   = el.Location.Curve
P0, P1 = k.GetEndPoint(0), k.GetEndPoint(1)

# PASSO 2: la pendenza
p, dz, L = pendenza(P0, P1)

print("Tratto: {}".format(el.Name))
print("Dislivello dz: {:.2f} m".format(dz))
print("Sviluppo orizzontale L: {:.2f} m".format(L))
print("Pendenza: {:.2f} %  ({:.2f} cm/m)".format(p, p))
