# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.1.4  |  Capitolo 7.1 - Lo staffaggio
# Sezione: Passo 4 - scrittura sul modello, in transazione

# ============================================================
# 0. RIPARTENZA                          [PY]+[REVIT]+[ENG]
#    blocco autonomo: ricrea il numero di staffe N
# ============================================================
import math
from Autodesk.Revit.DB import Transaction
from Autodesk.Revit.UI.Selection import ObjectType

FT_M      = 0.3048
INTERASSE = 1.50

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document
ref   = uidoc.Selection.PickObject(ObjectType.Element,
                                   "Seleziona la passerella")
tray  = doc.GetElement(ref.ElementId)

L_run = tray.Location.Curve.Length * FT_M
N     = int(math.ceil(L_run / INTERASSE)) + 1

# ============================================================
# 1. PASSO 4, LA SCRITTURA SUL MODELLO         [REVIT] + [OUT]
#    Legge I: ogni modifica vive in una Transaction
# ============================================================
t = Transaction(doc, "Staffaggio EC-01")
t.Start()
tray.LookupParameter("Staffe n").Set(N)
tray.LookupParameter("Staffe interasse").Set(INTERASSE / FT_M)  # piedi
t.Commit()

print("Scritti sul tratto: Staffe n = {}, interasse = {:.2f} m".format(
    N, INTERASSE))
