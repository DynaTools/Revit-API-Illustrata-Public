# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.1.2  |  Capitolo 7.1 - Lo staffaggio
# Sezione: Passi 1--2 - lettura, calcolo e risultato

# ============================================================
# 0. RIPARTENZA                                 [PY] + [REVIT]
#    blocco autonomo: import, dati e selezione, compressi
# ============================================================
from Autodesk.Revit.UI.Selection import ObjectType

FT_M = 0.3048
PESI = {"FG16 4G95": 4.10, "FG16 5G16": 1.35, "FG16 3G2.5": 0.18}
PESO_PASSERELLA = 5.00

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document
ref   = uidoc.Selection.PickObject(ObjectType.Element,
                                   "Seleziona la passerella")
tray  = doc.GetElement(ref.ElementId)

# ============================================================
# 1. PASSO 1, LA LETTURA                       [REVIT] + [ENG]
#    lunghezza della curva, da piedi a metri (Legge II)
# ============================================================
L_run = tray.Location.Curve.Length * FT_M
print("Tratto: {}   L = {:.2f} m".format(tray.Name, L_run))

# ============================================================
# 2. PASSO 2, IL CALCOLO                       [ENG] + [REVIT]
#    w = passerella + somma (peso x quantita')
# ============================================================
w = PESO_PASSERELLA
for nome, peso in PESI.items():
    par = tray.LookupParameter(nome)
    if par is None:
        print("  {:>11}: PARAMETRO ASSENTE sul tratto".format(nome))
        continue
    n = par.AsInteger()
    w += peso * n
    print("  {:>11}: {:.2f} kg/m  x{}  ->  {:.2f} kg/m".format(
        nome, peso, n, peso * n))

# ============================================================
# 3. IL RISULTATO                                        [OUT]
# ============================================================
print("Peso passerella: {:.2f} kg/m".format(PESO_PASSERELLA))
print("Peso al metro w: {:.2f} kg/m".format(w))
