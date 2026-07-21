# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.1.3  |  Capitolo 7.1 - La lunghezza del circuito
# Sezione: Passo 4 - sfrido e lunghezza totale

# ============================================================
# 0. RIPARTENZA                            [PY]+[REVIT]+[ENG]
#    blocco autonomo: riclicca e risomma il percorso
# ============================================================
from Autodesk.Revit.DB import LocationCurve
from Autodesk.Revit.UI.Selection import ObjectType

FT_M  = 0.3048
uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document
refs  = uidoc.Selection.PickObjects(ObjectType.Element,
                                    "Seleziona tutto il percorso, poi Finish")

# somma: tratti dritti (curva) + raccordi (arco = raggio x angolo)
L_ft = 0.0
for r in refs:
    elem_id = r.ElementId
    elem    = doc.GetElement(elem_id)
    loc     = elem.Location

    if isinstance(loc, LocationCurve):
        L_ft += loc.Curve.Length
    else:
        p_raggio = elem.LookupParameter("Bend Radius")
        p_angolo = elem.LookupParameter("Angle")
        if p_raggio and p_angolo:
            L_ft += p_raggio.AsDouble() * p_angolo.AsDouble()

L_mod = L_ft * FT_M

# ============================================================
# 1. PASSO 4, SFRIDO E TOTALE                            [ENG]
#    margine di posa: terminazioni, scorta (%)
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
