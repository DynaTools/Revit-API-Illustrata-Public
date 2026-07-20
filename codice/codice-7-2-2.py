# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.2.2  |  Capitolo 7.2 - Il riempimento dei cavidotti
# Sezione: Passo 4 - la distinta letta dal modello

# ============================================================
# 0. RIPARTENZA                                  [PY]+[REVIT]
#    blocco autonomo: si riclicca il cavidotto del passo 2
# ============================================================
import math
from Autodesk.Revit.UI.Selection import ObjectType

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document
ref   = uidoc.Selection.PickObject(ObjectType.Element,
                                   "Seleziona il cavidotto")
cavidotto = doc.GetElement(ref.ElementId)

# ============================================================
# 1. PASSO 4, LA DISTINTA DAL MODELLO           [ENG]+[REVIT]
#    catalogo (schede tecniche) + quantita' dai parametri
# ============================================================
catalogo = [("FG16OR16 3G6 mm²", 14.0),
            ("FG16OR16 3G4 mm²", 12.5)]

cavi = []
for nome, d in catalogo:
    p = cavidotto.LookupParameter(nome)
    q = p.AsInteger() if p else 0
    if q > 0:
        cavi.append((nome, d, q))

# ============================================================
# 2. LA SOMMA DELLE AREE                          [PY]+[ENG]
#    area di ogni famiglia e somma dei quadrati dei diametri
# ============================================================
A_cavi = 0.0      # somma delle aree dei cavi (mm^2)
somma_d2 = 0.0    # somma dei d^2 (serve per il fascio)
n_cavi = 0

for nome, d, q in cavi:
    area_singolo = math.pi / 4.0 * d**2
    A_cavi   += area_singolo * q
    somma_d2 += d**2 * q
    n_cavi   += q
    print("{:>17}: d={:.1f} mm  x{}  ->  {:.0f} mm2".format(
        nome, d, q, area_singolo * q))

# ============================================================
# 3. IL RISULTATO                                        [OUT]
# ============================================================
print("---")
print("Cavi totali: {}".format(n_cavi))
print("Area occupata dai cavi: {:.0f} mm2".format(A_cavi))
