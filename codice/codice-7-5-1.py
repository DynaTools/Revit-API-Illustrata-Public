# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.5.1  |  Capitolo 7.5 - La caduta di tensione
# Sezione: Passi 1--2 - lunghezza dal modello e dati elettrici

import math
from Autodesk.Revit.UI.Selection import ObjectType

FT_M = 0.3048                      # 1 piede = 0.3048 m

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

# PASSO 1: leggi la lunghezza del cavo dal modello (come nel cap. 7-2)
refs = uidoc.Selection.PickObjects(ObjectType.Element,
                                   "Seleziona i tratti del percorso")

L = 0.0
for r in refs:
    el = doc.GetElement(r.ElementId)
    L += el.Location.Curve.Length * FT_M   # lunghezza 3D in metri

# L e' la lunghezza reale del cavo letta dal modello: sommando i tratti 3D
# (discese e risalite comprese, come nel cap. 7-2) si ottiene il numero che
# usa il calcolo. Nel modello d'esempio QE-01 -> M-12 vale L = 18.06 m
print("Lunghezza del cavo L: {:.2f} m".format(L))
