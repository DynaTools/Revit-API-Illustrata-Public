# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.2.3  |  Capitolo 7.2 - La lunghezza del circuito
# Sezione: Passo 4 - sfrido e lunghezza totale

# ============================================================
# 0. RIPARTENZA                            [PY]+[REVIT]+[ENG]
#    blocco autonomo: riclicca e risomma il percorso 3D
# ============================================================
from Autodesk.Revit.DB import LocationCurve
from Autodesk.Revit.UI.Selection import ObjectType

FT_M  = 0.3048
uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document
refs  = uidoc.Selection.PickObjects(ObjectType.Element,
                                    "Seleziona tutto il percorso, poi Finish")

L_ft = 0.0
for r in refs:
    loc = doc.GetElement(r.ElementId).Location
    if isinstance(loc, LocationCurve):
        L_ft += loc.Curve.Length
L_mod = L_ft * FT_M

# ============================================================
# 1. PASSO 4, SFRIDO E TOTALE                            [ENG]
#    margine di posa: raccordi, terminazioni, scorta (%)
# ============================================================
sfrido_pct = 5.0
L_sfrido   = L_mod * sfrido_pct / 100.0
L_cavo     = L_mod + L_sfrido

# ============================================================
# 2. IL RISULTATO                                        [OUT]
# ============================================================
print("Lunghezza modellata: {:.2f} m".format(L_mod))
print("Sfrido ({:.0f}%): {:.2f} m".format(sfrido_pct, L_sfrido))
print("---")
print("LUNGHEZZA DEL CAVO: {:.2f} m".format(L_cavo))
