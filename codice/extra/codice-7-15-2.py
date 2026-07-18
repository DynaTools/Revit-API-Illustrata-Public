# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.15.2  |  Capitolo 7.15 - Il campo visivo di una telecamera
# Sezione: Passo 4 - la linea di vista (ray casting)

from Autodesk.Revit.DB import (FilteredElementCollector, View3D,
    ElementCategoryFilter, BuiltInCategory, LogicalOrFilter,
    ReferenceIntersector, FindReferenceTarget)

doc = __revit__.ActiveUIDocument.Document

# una vista 3D non template (serve al ReferenceIntersector)
vista3d = next(v for v in FilteredElementCollector(doc).OfClass(View3D)
               if not v.IsTemplate)

# il raggio "vede" muri e pilastri: sono i nostri ostacoli
ostacoli = LogicalOrFilter(
    ElementCategoryFilter(BuiltInCategory.OST_Walls),
    ElementCategoryFilter(BuiltInCategory.OST_StructuralColumns))
ri = ReferenceIntersector(ostacoli, FindReferenceTarget.Element, vista3d)

# la linea di vista cam->p e' libera? (nessun ostacolo PIU' VICINO del punto)
def linea_libera(cam, p, intersector):
    d = p - cam
    L = d.GetLength()
    if L == 0.0:
        return True
    hit = intersector.FindNearest(cam, d.Normalize())   # prima intersezione
    if hit is None:
        return True                                     # niente di mezzo
    d_occ = hit.Proximity                               # distanza dell'ostacolo (piedi)
    return d_occ >= L - 1e-6                             # libera se l'ostacolo e' OLTRE p

# PASSO 4: esito completo per ogni punto
for nome in ("P1", "P2", "P3"):
    dentro, alfa, dist = dentro_cono(cam, w, P[nome], THETA)
    if not dentro:
        esito = "FUORI CONO"
    elif dist > R:
        esito = "RILEVATO ma NON RICONOSCIBILE (oltre R)"
    elif not linea_libera(cam, P[nome], ri):
        esito = "OCCLUSO"
    else:
        esito = "VISIBILE e RICONOSCIBILE"
    print("{}: angolo {:.2f} gradi, dist {:.2f} m  ->  {}".format(
        nome, alfa, dist, esito))
