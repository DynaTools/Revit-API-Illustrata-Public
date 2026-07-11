# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.5.1  |  Capitolo 7.5 - La caduta di tensione
# Sezione: Passo 1 - la lunghezza del cavo dal modello

# ============================================================
# 0. PREPARAZIONE                               [PY] + [REVIT]
#    librerie e documento Revit attivo
# ============================================================
from Autodesk.Revit.UI.Selection import ObjectType

FT_M = 0.3048                      # 1 piede = 0.3048 m

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

# ============================================================
# 1. PASSO 1, I CLIC                                   [REVIT]
#    i tratti del percorso QE-01 -> M-12, come nel cap. 7-2
# ============================================================
refs = uidoc.Selection.PickObjects(ObjectType.Element,
                                   "Seleziona i tratti del percorso")

# ============================================================
# 2. LA SOMMA DELLE LUNGHEZZE                  [REVIT] + [ENG]
#    lunghezza 3D di ogni tratto, da piedi a metri
# ============================================================
L = 0.0
for r in refs:
    el = doc.GetElement(r.ElementId)
    L += el.Location.Curve.Length * FT_M   # lunghezza 3D in metri

# ============================================================
# 3. IL RISULTATO                                        [OUT]
#    nel modello d'esempio QE-01 -> M-12: L = 18.06 m
# ============================================================
print("Lunghezza del cavo L: {:.2f} m".format(L))
