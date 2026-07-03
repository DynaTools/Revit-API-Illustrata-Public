# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.2.1  |  Capitolo 7.2 - La lunghezza del circuito
# Sezione: Passi 1--2 - il percorso dal modello

import math
from Autodesk.Revit.UI.Selection import ObjectType

FT_M = 0.3048                      # 1 piede = 0.3048 m

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

# PASSO 1: clicca i tratti del percorso (uno o piu')
refs = uidoc.Selection.PickObjects(ObjectType.Element,
                                   "Seleziona i tratti del percorso")

# PASSO 2: somma le lunghezze 3D
L_orizz = 0.0
for r in refs:
    el = doc.GetElement(r.ElementId)
    L_orizz += el.Location.Curve.Length * FT_M
    # quota della passerella (la leggo dal modello)
    z_pass = el.Location.Curve.GetEndPoint(0).Z * FT_M

print("Tratti selezionati: {}".format(len(refs)))
print("Percorso orizzontale: {:.2f} m".format(L_orizz))
print("Quota passerella: {:.2f} m".format(z_pass))
