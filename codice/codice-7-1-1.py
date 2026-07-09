# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.1.1  |  Capitolo 7.1 - Lo staffaggio
# Sezione: Passi 1--2 - leggere il tratto e sommare i pesi

# -*- coding: utf-8 -*-
import math
from Autodesk.Revit.DB import Transaction
from Autodesk.Revit.UI.Selection import ObjectType

FT_M = 0.3048                      # 1 piede = 0.3048 m

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

# tabella di progetto: peso al metro dei cavi (kg/m, da scheda tecnica)
PESI = {
    "FG16 4G95":  4.10,
    "FG16 5G16":  1.35,
    "FG16 3G2.5": 0.18,
}
PESO_PASSERELLA = 5.00            # kg/m, dal catalogo (base 300 mm)

# PASSO 1: clicca il tratto e leggi lunghezza + parametri dei cavi
ref  = uidoc.Selection.PickObject(ObjectType.Element,
                                  "Seleziona la passerella")
tray = doc.GetElement(ref.ElementId)
L_run = tray.Location.Curve.Length * FT_M

print("Tratto: {}   L = {:.2f} m".format(tray.Name, L_run))

# PASSO 2: peso al metro = passerella + somma (peso x quantita')
w = PESO_PASSERELLA
for nome, peso in PESI.items():
    par = tray.LookupParameter(nome)
    n = par.AsInteger() if par else 0
    w += peso * n
    print("  {:>11}: {:.2f} kg/m  x{}  ->  {:.2f} kg/m".format(
        nome, peso, n, peso * n))

print("Peso passerella: {:.2f} kg/m".format(PESO_PASSERELLA))
print("Peso al metro w: {:.2f} kg/m".format(w))
