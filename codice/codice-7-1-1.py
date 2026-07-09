# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.1.1  |  Capitolo 7.1 - Lo staffaggio
# Sezione: Passi 1--2 - preparazione, dati di progetto e selezione

# ============================================================
# 0. PREPARAZIONE                               [PY] + [REVIT]
#    librerie e documento Revit attivo
# ============================================================
from Autodesk.Revit.UI.Selection import ObjectType

FT_M = 0.3048                      # 1 piede = 0.3048 m

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

# ============================================================
# 1. DATI DI PROGETTO                                    [ENG]
#    pesi al metro dalle schede tecniche (kg/m)
# ============================================================
PESI = {
    "FG16 4G95":  4.10,
    "FG16 5G16":  1.35,
    "FG16 3G2.5": 0.18,
}
PESO_PASSERELLA = 5.00             # kg/m, catalogo (450 x 100)

# ============================================================
# 2. PASSO 1, IL CLIC                          [REVIT] + [OUT]
#    l'utente seleziona il tratto nel modello
# ============================================================
ref  = uidoc.Selection.PickObject(ObjectType.Element,
                                  "Seleziona la passerella")
tray = doc.GetElement(ref.ElementId)
print("Selezionato: {}".format(tray.Name))
