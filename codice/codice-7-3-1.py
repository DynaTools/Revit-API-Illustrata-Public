# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.3.1  |  Capitolo 7.3 - Il riempimento dei cavidotti
# Sezione: Passi 1--2 - raccogliere il cavidotto

# ============================================================
# 0. PREPARAZIONE                               [PY] + [REVIT]
#    librerie, conversione e documento Revit attivo
# ============================================================
import math
from Autodesk.Revit.DB import BuiltInParameter
from Autodesk.Revit.UI.Selection import ObjectType

FT_MM = 304.8                      # 1 piede = 304.8 mm

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

# ============================================================
# 1. PASSO 1, IL CLIC                                  [REVIT]
#    l'utente seleziona il cavidotto nel modello
# ============================================================
ref     = uidoc.Selection.PickObject(ObjectType.Element,
                                     "Seleziona il cavidotto")
conduit = doc.GetElement(ref.ElementId)

# ============================================================
# 2. PASSO 2, IL DIAMETRO                      [REVIT] + [ENG]
#    diametro interno (la API restituisce piedi -> mm)
# ============================================================
p_int = conduit.get_Parameter(
    BuiltInParameter.RBS_CONDUIT_INNER_DIAM_PARAM)
De    = p_int.AsDouble() * FT_MM   # diametro interno in mm

A_tubo = math.pi / 4.0 * De**2     # area interna in mm^2

# ============================================================
# 3. IL RISULTATO                                        [OUT]
# ============================================================
print("Cavidotto CD-01")
print("Diametro interno De: {:.1f} mm".format(De))
print("Area interna del tubo: {:.0f} mm2".format(A_tubo))
