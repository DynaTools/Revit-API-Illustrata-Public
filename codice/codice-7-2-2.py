# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.2.2  |  Capitolo 7.2 - La lunghezza del circuito
# Sezione: Passo 3 - discese e risalite

# ============================================================
# 0. RIPARTENZA                                 [PY] + [REVIT]
#    blocco autonomo: rilegge dal modello la quota z_pass
# ============================================================
from Autodesk.Revit.UI.Selection import ObjectType

FT_M  = 0.3048
uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

ref    = uidoc.Selection.PickObject(ObjectType.Element,
                                    "Seleziona un tratto del percorso")
tratto = doc.GetElement(ref.ElementId)
z_pass = tratto.Location.Curve.GetEndPoint(0).Z * FT_M

# ============================================================
# 1. PASSO 3, DISCESE E RISALITE                         [ENG]
#    differenze di quota (quote di progetto, in metri)
# ============================================================
z_quadro = 3.2       # uscita del cavo in cima al quadro QE-01
z_carico = 1.0       # morsettiera del motore M-12

risalita = z_pass - z_quadro     # dal quadro su alla passerella
discesa  = z_pass - z_carico     # dalla passerella giu' al motore
L_vert   = risalita + discesa

# ============================================================
# 2. L'ESITO                                             [OUT]
# ============================================================
print("Risalita al quadro: {:.2f} m".format(risalita))
print("Discesa al motore:  {:.2f} m".format(discesa))
print("Totale verticale:   {:.2f} m".format(L_vert))
