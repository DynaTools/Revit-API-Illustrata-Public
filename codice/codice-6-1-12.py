# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.1.12  |  Capitolo 6.1 - I primitivi geometrici
# Sezione: I primitivi applicati alle categorie Revit

from Autodesk.Revit.DB import (Outline, BoundingBoxIntersectsFilter,
    ElementIntersectsElementFilter)

def centro_raggio(elem):
    bb = elem.get_BoundingBox(None)
    C  = bb.Min + (bb.Max - bb.Min) * 0.5
    r  = C.DistanceTo(bb.Max)         # semidiagonale = raggio sfera
    return C, r, bb

Cd, rd, bbd = centro_raggio(duct)
Cb, rb, bbb = centro_raggio(beam)

# FASE 1 - sfera: 1 confronto
sfera_ok = Cd.DistanceTo(Cb) <= (rd + rb)
print("1) sfera: {}".format("possibile" if sfera_ok else "escluso"))

# FASE 2 - AABB: 6 confronti (solo se la sfera non ha escluso)
aabb_ok = False
if sfera_ok:
    f = BoundingBoxIntersectsFilter(Outline(bbd.Min, bbd.Max))
    aabb_ok = f.PassesFilter(doc, beam.Id)
    print("2) AABB: {}".format("possibile" if aabb_ok else "escluso"))

# FASE 3 - solido esatto (solo se l'AABB non ha escluso)
if aabb_ok:
    f = ElementIntersectsElementFilter(beam)
    clash = f.PassesFilter(doc, duct.Id)
    print("3) solido: {}".format("CLASH CONFERMATO" if clash else "nessun clash"))
