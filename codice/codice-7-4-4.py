# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.4.4  |  Capitolo 7.4 - Distribuire con lo schema L-2L
# Sezione: Lo strumento da cantiere, dal clic alla griglia

# ============================================================
# 0. GLI ATTREZZI                                        [PY]
#    anche le due finestre di serie: InputBox e TaskDialog
# ============================================================
FT_M = 0.3048
import math
import clr
clr.AddReference("Microsoft.VisualBasic")
from Microsoft.VisualBasic import Interaction
from Autodesk.Revit.DB import (XYZ, UV, Transform, RevitLinkInstance,
                               Transaction, ElementId, BuiltInParameter)
from Autodesk.Revit.DB.Structure import StructuralType
from Autodesk.Revit.UI import (TaskDialog, TaskDialogCommonButtons,
                               TaskDialogResult)
from Autodesk.Revit.UI.Selection import ObjectType

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

# ============================================================
# 1. LA LUMINARIA CAMPIONE                             [REVIT]
#    tipo, livello e ORIGINE della famiglia; l'origine deve
#    essere il centro del pannello, e lo strumento avvisa
# ============================================================
r1  = uidoc.Selection.PickObject(ObjectType.Element,
                                 "Clicca la luminaria campione")
lum = doc.GetElement(r1.ElementId)
bb  = lum.get_BoundingBox(None)
print("Luminaria: {} | {}".format(lum.Symbol.Family.Name, lum.Name))
print("Ingombro in pianta: {:.2f} x {:.2f} m".format(
    (bb.Max.X - bb.Min.X) * FT_M, (bb.Max.Y - bb.Min.Y) * FT_M))

scarto = (bb.Min + bb.Max) / 2.0 - lum.Location.Point
sx = abs(scarto.X) * FT_M * 1000
sy = abs(scarto.Y) * FT_M * 1000
if max(sx, sy) > 50:
    print("ATTENZIONE: origine non al centro ({:.0f} x {:.0f} mm);".format(sx, sy))
    print("  correggi la famiglia (Definisce origine sui piani centrali).")
else:
    print("Origine della famiglia al centro (scarto {:.0f} x {:.0f} mm).".format(sx, sy))

lid = lum.LevelId
if lid == ElementId.InvalidElementId:          # non ospitata: Schedule Level
    lid = lum.get_Parameter(
        BuiltInParameter.INSTANCE_SCHEDULE_ONLY_LEVEL_PARAM).AsElementId()
livello = doc.GetElement(lid)

# ============================================================
# 2. LA FACCIA DEL CONTROSOFFITTO               [REVIT]+[ENG]
#    il contorno VERO (EdgeLoops), non il bbox UV; se la
#    faccia vive in un link, la sua Transform riporta tutto
#    nelle coordinate del modello ospite
# ============================================================
r2   = uidoc.Selection.PickObject(ObjectType.Face,
          "Clicca la faccia del controsoffitto")
host = doc.GetElement(r2.ElementId)
trasf, dove = Transform.Identity, "nel modello"
if isinstance(host, RevitLinkInstance):
    trasf = host.GetTotalTransform()
    dove  = "in un link ({})".format(host.Name)
faccia = host.GetGeometryObjectFromReference(r2)
print("Faccia {} | tipo {}".format(dove, type(faccia).__name__))

anello, per_max = None, 0.0
for k in range(faccia.EdgeLoops.Size):
    loop = faccia.EdgeLoops.get_Item(k)
    per  = sum(e.AsCurve().Length for e in loop)
    if per > per_max:
        anello, per_max = loop, per
vertici = []
for e in anello:
    p = trasf.OfPoint(e.AsCurve().GetEndPoint(0))
    if not vertici or (p - vertici[-1]).GetLength() > 0.001:
        vertici.append(p)

A  = vertici[0]
eU = (vertici[1] - A).Normalize()
eV = trasf.OfVector(faccia.ComputeNormal(UV(0.5, 0.5))).CrossProduct(eU)
us = [(p - A).DotProduct(eU) for p in vertici]
vs = [(p - A).DotProduct(eV) for p in vertici]
u0, u1, v0, v1 = min(us), max(us), min(vs), max(vs)
O  = A + eU * u0 + eV * v0
lu, lv = (u1 - u0) * FT_M, (v1 - v0) * FT_M
print("Controsoffitto: {:.2f} x {:.2f} m | quota z {:.3f} m".format(
    lu, lv, O.Z * FT_M))
print("Livello di posa: {}".format(livello.Name))

# ============================================================
# 3. QUANTE, E SU QUANTE COLONNE                         [PY]
#    totale e colonne si scrivono nella finestrella; il tetto
#    decide le file, e l'ultima puo' restare incompleta
# ============================================================
N = int(Interaction.InputBox(
    "Quante luminarie in totale? Per esempio 10", "Griglia L-2L", "10"))
C = int(Interaction.InputBox(
    "Su quante colonne? Per esempio 3", "Griglia L-2L", "3"))

R = int(math.ceil(N / float(C)))
righe, resto = [], N
for j in range(R):
    righe.append(min(C, resto))
    resto -= righe[-1]
print("{} luminarie su {} colonne -> {} file ({})".format(
    N, C, R, "+".join(str(x) for x in righe)))

# ============================================================
# 4. LA GRIGLIA L-2L                                    [ENG]
#    ogni fila distribuisce le SUE luminarie a mezzo passo;
#    la fila incompleta centra da sola cio' che le resta
# ============================================================
print("Passo {:.2f} x {:.2f} m | bordo {:.2f} x {:.2f} m".format(
    lu / C, lv / R, lu / C / 2, lv / R / 2))
posizioni = []
for j, quante in enumerate(righe):
    for i in range(quante):
        posizioni.append(O + eU * (u1 - u0) * (i + 0.5) / quante
                           + eV * (v1 - v0) * (j + 0.5) / R)
for k, p in enumerate(posizioni, 1):
    print("  #{:>2}: x={:.3f}  y={:.3f}  z={:.3f} m".format(
        k, p.X * FT_M, p.Y * FT_M, p.Z * FT_M))

# ============================================================
# 5. LA CONFERMA E LA POSA                            [REVIT]
# ============================================================
esito = TaskDialog.Show("Griglia L-2L",
    "Posare {} luminarie ({} file, {})?".format(
        N, R, "+".join(str(x) for x in righe)),
    TaskDialogCommonButtons.Yes | TaskDialogCommonButtons.No)

if esito == TaskDialogResult.Yes:
    t = Transaction(doc, "Griglia L-2L di luminarie")
    t.Start()
    if not lum.Symbol.IsActive:
        lum.Symbol.Activate()
    for p in posizioni:
        doc.Create.NewFamilyInstance(p, lum.Symbol, livello,
                                     StructuralType.NonStructural)
    t.Commit()
    print("Posate {} luminarie sul livello {}.".format(
        len(posizioni), livello.Name))
else:
    print("Solo analisi, nessuna posa.")
