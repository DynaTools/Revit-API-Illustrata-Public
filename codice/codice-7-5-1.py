# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.5.1  |  Capitolo 7.5 - La caduta di tensione
# Sezione: Passo 1 - la lunghezza del cavo dal modello

# ============================================================
# 0. PREPARAZIONE                               [PY] + [REVIT]
#    librerie e documento Revit attivo
# ============================================================
from Autodesk.Revit.DB import LocationCurve
from Autodesk.Revit.UI.Selection import ObjectType

FT_M   = 0.3048                    # 1 piede = 0.3048 m
SFRIDO = 0.05                      # 5% di margine di posa (sfrido)

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

# ============================================================
# 1. PASSO 1, I CLIC                                   [REVIT]
#    tutto il percorso QE-01 -> M-12, come nel cap. 7-2
# ============================================================
refs = uidoc.Selection.PickObjects(ObjectType.Element,
                                   "Seleziona tutto il percorso, poi Finish")

# ============================================================
# 2. LA SOMMA DELLE LUNGHEZZE                  [REVIT] + [ENG]
#    lunghezza 3D dei tratti; i raccordi non hanno una curva
# ============================================================
L_mod = 0.0
for r in refs:
    loc = doc.GetElement(r.ElementId).Location
    if isinstance(loc, LocationCurve):
        L_mod += loc.Curve.Length * FT_M   # lunghezza 3D in metri

L = L_mod * (1 + SFRIDO)               # lunghezza del cavo (+ sfrido)

# ============================================================
# 3. IL RISULTATO                                        [OUT]
#    nel modello d'esempio QE-01 -> M-12: L = 12.75 m
# ============================================================
print("Lunghezza del cavo L: {:.2f} m".format(L))
