# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.1.1  |  Capitolo 7.1 - Lo staffaggio
# Sezione: Passo 1 - cliccare la passerella

import math
from Autodesk.Revit.UI.Selection import ObjectType

FT_M = 0.3048                      # 1 piede = 0.3048 m

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

# PASSO 1: clicca la passerella nel modello
ref  = uidoc.Selection.PickObject(ObjectType.Element,
                                  "Seleziona la passerella")
tray = doc.GetElement(ref.ElementId)

# Lunghezza del tratto (la API lavora in piedi -> converto in metri)
L_run = tray.Location.Curve.Length * FT_M

print("Passerella EC-01")
print("Lunghezza del tratto: {:.2f} m".format(L_run))
