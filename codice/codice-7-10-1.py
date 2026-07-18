# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.10.1  |  Capitolo 7.10 - La distanza minima fra due percorsi
# Sezione: Passi 1--2 - leggere i percorsi e calcolare

from Autodesk.Revit.DB import XYZ
from Autodesk.Revit.UI.Selection import ObjectType

FT_M = 0.3048                      # 1 piede = 0.3048 m

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

def clamp01(x):
    return max(0.0, min(1.0, x))

# distanza minima fra i segmenti AB e CD (punti piu' vicini + parametri)
def distanza_segmenti(A, B, C, D):
    u = B - A                      # direzione del primo segmento
    v = D - C                      # direzione del secondo
    r = A - C
    a = u.DotProduct(u)            # |u|^2
    e = v.DotProduct(v)            # |v|^2
    f = v.DotProduct(r)
    c = u.DotProduct(r)
    b = u.DotProduct(v)
    denom = a * e - b * b          # 0 se i percorsi sono paralleli
    s = clamp01((b * f - c * e) / denom) if denom != 0 else 0.0
    t = (b * s + f) / e
    if t < 0.0:                    # oltre l'estremo: torna sull'estremo
        t = 0.0; s = clamp01(-c / a)
    elif t > 1.0:
        t = 1.0; s = clamp01((b - c) / a)
    C1 = A + u.Multiply(s)         # punto piu' vicino sul primo
    C2 = C + v.Multiply(t)         # punto piu' vicino sul secondo
    return C1, C2, s, t

# PASSO 1: clicca i due percorsi e leggi gli estremi
r1 = uidoc.Selection.PickObject(ObjectType.Element, "Primo percorso")
r2 = uidoc.Selection.PickObject(ObjectType.Element, "Secondo percorso")
e1 = doc.GetElement(r1.ElementId)
e2 = doc.GetElement(r2.ElementId)
k1 = e1.Location.Curve
k2 = e2.Location.Curve
A, B = k1.GetEndPoint(0), k1.GetEndPoint(1)
C, D = k2.GetEndPoint(0), k2.GetEndPoint(1)

# PASSO 2: la perpendicolare comune
C1, C2, s, t = distanza_segmenti(A, B, C, D)
d = C1.DistanceTo(C2) * FT_M       # distanza minima in metri

def m(p): return (p.X*FT_M, p.Y*FT_M, p.Z*FT_M)
print("Percorso A: {}".format(e1.Name))
print("Percorso B: {}".format(e2.Name))
print("Punto piu' vicino su A: ({:.2f}, {:.2f}, {:.2f}) m  (s = {:.2f})".format(
    m(C1)[0], m(C1)[1], m(C1)[2], s))
print("Punto piu' vicino su B: ({:.2f}, {:.2f}, {:.2f}) m  (t = {:.2f})".format(
    m(C2)[0], m(C2)[1], m(C2)[2], t))
print("Distanza minima: {:.2f} m".format(d))
