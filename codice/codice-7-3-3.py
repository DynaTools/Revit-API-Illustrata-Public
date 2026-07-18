# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.3.3  |  Capitolo 7.3 - Il riempimento dei cavidotti
# Sezione: Passo 4 - calcolare e verificare

# ============================================================
# 0. RIPARTENZA                            [PY]+[REVIT]+[ENG]
#    blocco autonomo: riclic, De, parametri e aree dei cavi
# ============================================================
import math
from Autodesk.Revit.DB import BuiltInParameter
from Autodesk.Revit.UI.Selection import ObjectType

FT_MM = 304.8
catalogo = [("FG16OR16 3G6 mm²", 13.0),
            ("FG16OR16 3G4 mm²", 11.5)]

uidoc   = __revit__.ActiveUIDocument
doc     = uidoc.Document
ref     = uidoc.Selection.PickObject(ObjectType.Element,
                                     "Seleziona il cavidotto")
conduit = doc.GetElement(ref.ElementId)
De      = conduit.get_Parameter(
    BuiltInParameter.RBS_CONDUIT_INNER_DIAM_PARAM).AsDouble() * FT_MM
A_tubo  = math.pi / 4.0 * De**2

cavi = [(n, d, conduit.LookupParameter(n).AsInteger())
        for n, d in catalogo if conduit.LookupParameter(n)]

A_cavi = somma_d2 = 0.0
for nome, d, q in cavi:
    A_cavi   += math.pi / 4.0 * d**2 * q
    somma_d2 += d**2 * q

# ============================================================
# 1. PASSO 4, RIEMPIMENTO E VERIFICA                     [ENG]
#    K = area cavi / area tubo; CEI 64-8: De >= 1.3 x Dt
# ============================================================
K = A_cavi / A_tubo                # riempimento (0..1)

Dt     = math.sqrt(somma_d2)       # diametro del fascio (mm)
De_min = 1.3 * Dt                  # diametro minimo richiesto
conforme = De >= De_min

# ============================================================
# 2. L'ESITO                                             [OUT]
# ============================================================
print("Riempimento: {:.1f} %".format(K * 100))
print("Diametro fascio Dt: {:.1f} mm".format(Dt))
print("Diametro minimo del tubo (1.3 x Dt): {:.1f} mm".format(De_min))
print("Diametro reale del tubo De: {:.1f} mm".format(De))
print("---")
if conforme:
    print("ESITO: CONFORME (margine {:.1f} mm)".format(De - De_min))
else:
    print("ESITO: NON CONFORME - serve un tubo piu' grande")
