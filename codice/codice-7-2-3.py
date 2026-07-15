# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.2.3  |  Capitolo 7.2 - La lunghezza del circuito
# Sezione: Passo 4 - sfrido e lunghezza totale

# ============================================================
# 0. RIPARTENZA                            [PY]+[REVIT]+[ENG]
#    blocco autonomo: ricrea percorso orizzontale e verticale
# ============================================================
from Autodesk.Revit.UI.Selection import ObjectType

FT_M     = 0.3048
z_quadro = 3.2       # uscita del cavo in cima al quadro QE-01
z_carico = 1.0       # morsettiera del motore M-12

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document
refs  = uidoc.Selection.PickObjects(ObjectType.Element,
                                    "Seleziona i tratti del percorso")

L_orizz = 0.0
for r in refs:
    el = doc.GetElement(r.ElementId)
    L_orizz += el.Location.Curve.Length * FT_M
    z_pass = el.Location.Curve.GetEndPoint(0).Z * FT_M

L_vert = abs(z_pass - z_quadro) + abs(z_pass - z_carico)

# ============================================================
# 1. PASSO 4, SFRIDO E TOTALE                            [ENG]
#    margine per collegamenti, in percentuale
# ============================================================
sfrido_pct = 5.0     # margine per collegamenti e terminazioni (%)

L_geom   = L_orizz + L_vert                  # lunghezza geometrica
L_sfrido = L_geom * sfrido_pct / 100.0
L_cavo   = L_geom + L_sfrido                 # lunghezza del cavo

# ============================================================
# 2. IL RISULTATO                                        [OUT]
# ============================================================
print("Lunghezza geometrica: {:.2f} m".format(L_geom))
print("Sfrido ({:.0f}%): {:.2f} m".format(sfrido_pct, L_sfrido))
print("---")
print("LUNGHEZZA DEL CAVO: {:.2f} m".format(L_cavo))
print("(il solo tratto orizzontale era {:.2f} m: +{:.0f}%)".format(
    L_orizz, (L_cavo / L_orizz - 1.0) * 100))
