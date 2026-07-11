# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.4.3  |  Capitolo 7.4 - Lo schema L--2L
# Sezione: In Revit - posare gli apparecchi in transazione

# ============================================================
# 0. RIPARTENZA                            [PY]+[REVIT]+[ENG]
#    blocco autonomo: rilegge la stanza, rifa' passo e bordo
# ============================================================
from Autodesk.Revit.DB import (XYZ, Transaction, Structure,
    FilteredElementCollector, BuiltInCategory, FamilySymbol, Level)
from Autodesk.Revit.UI.Selection import ObjectType

FT_M  = 0.3048
uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

ref = uidoc.Selection.PickObject(ObjectType.Element,
                                 "Seleziona la stanza")
bb  = doc.GetElement(ref.ElementId).get_BoundingBox(None)

x0 = bb.Min.X * FT_M;  A = (bb.Max.X - bb.Min.X) * FT_M
y0 = bb.Min.Y * FT_M;  B = (bb.Max.Y - bb.Min.Y) * FT_M
z  = bb.Max.Z * FT_M                       # quota soffitto

nx, ny = 4, 3
sx = A / nx;  sy = B / ny

# ============================================================
# 1. I PUNTI, RIGENERATI                         [PY] + [ENG]
#    la formula del centro, in forma compressa
# ============================================================
punti = []
for i in range(nx):
    for j in range(ny):
        punti.append(XYZ((x0 + (i + 0.5) * sx) / FT_M,
                         (y0 + (j + 0.5) * sy) / FT_M, z / FT_M))

# ============================================================
# 2. TIPO E LIVELLO                                    [REVIT]
#    il primo tipo di apparecchio luce e il primo livello
# ============================================================
symbol = FilteredElementCollector(doc)\
    .OfCategory(BuiltInCategory.OST_LightingFixtures)\
    .OfClass(FamilySymbol).FirstElement()   # il primo tipo di punto luce
level  = FilteredElementCollector(doc).OfClass(Level).FirstElement()

# ============================================================
# 3. LA POSA, IN TRANSAZIONE                   [REVIT] + [OUT]
#    FirstElement -> None se manca il tipo o il livello
# ============================================================
if symbol is None or level is None:
    print("ERRORE: nel modello manca un tipo di apparecchio")
    print("luce (o un livello). Carica una famiglia della")
    print("categoria Lighting Fixtures e riprova.")
else:
    if not symbol.IsActive:
        symbol.Activate()
    t = Transaction(doc, "Griglia luci L-2L")
    t.Start()
    for p in punti:
        doc.Create.NewFamilyInstance(
            p, symbol, level, Structure.StructuralType.NonStructural)
    t.Commit()
    print("Posati {} apparecchi sulla griglia.".format(len(punti)))
