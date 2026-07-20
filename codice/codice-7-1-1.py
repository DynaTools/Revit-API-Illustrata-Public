# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.1.1  |  Capitolo 7.1 - La lunghezza del circuito
# Sezione: Passi 1--2 - misurare il percorso dal modello

# ============================================================
# 0. PREPARAZIONE                               [PY] + [REVIT]
#    librerie e documento Revit attivo
# ============================================================
from Autodesk.Revit.DB import LocationCurve
from Autodesk.Revit.UI.Selection import ObjectType

FT_M = 0.3048                      # 1 piede = 0.3048 m

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

# ============================================================
# 1. PASSO 1, I CLIC                                   [REVIT]
#    l'utente seleziona TUTTO il percorso: tratti e curve
# ============================================================
refs = uidoc.Selection.PickObjects(ObjectType.Element,
                                   "Seleziona tutto il percorso, poi Finish")

# ============================================================
# 2. PASSO 2, LA SOMMA 3D                      [REVIT] + [ENG]
#    lunghezza 3D di ogni tratto; le curve (raccordi) sono
#    punti, non hanno una curva-linea: si contano e si saltano
# ============================================================
L_ft     = 0.0
n_tratti = 0
n_curve  = 0
for r in refs:
    loc = doc.GetElement(r.ElementId).Location
    if isinstance(loc, LocationCurve):
        L_ft += loc.Curve.Length       # lunghezza 3D, in piedi
        n_tratti += 1
    else:
        n_curve += 1                   # raccordo: nessuna curva-linea

L_mod = L_ft * FT_M                    # lunghezza modellata, in metri

# ============================================================
# 3. IL RISULTATO                                        [OUT]
# ============================================================
print("Elementi selezionati: {}".format(len(refs)))
print("  tratti con curva: {}".format(n_tratti))
print("  raccordi (curve): {}".format(n_curve))
print("Lunghezza modellata (3D): {:.2f} m".format(L_mod))
