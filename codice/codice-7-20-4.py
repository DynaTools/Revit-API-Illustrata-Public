# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.20.4  |  Capitolo 7.20 - Area e perimetro di una stanza irregolare
# Sezione: Leggere il contorno dalla stanza

from Autodesk.Revit.DB import (FilteredElementCollector, BuiltInCategory,
    SpatialElementBoundaryOptions)

FT_M = 0.3048                      # 1 piede = 0.3048 m

doc = __revit__.ActiveUIDocument.Document

# PASSO 1: prendi la stanza e i suoi segmenti di contorno
room = (FilteredElementCollector(doc)
        .OfCategory(BuiltInCategory.OST_Rooms)
        .WhereElementIsNotElementType()
        .FirstElement())

opt = SpatialElementBoundaryOptions()
anelli = room.GetBoundarySegments(opt)     # lista di anelli (il primo: esterno)

vertici = []
P = 0.0
for seg in anelli[0]:                       # anello esterno della stanza
    c = seg.GetCurve()
    p0 = c.GetEndPoint(0)                    # punto iniziale del segmento
    vertici.append((p0.X * FT_M, p0.Y * FT_M))
    P += c.Length * FT_M                     # lunghezza del lato (perimetro)

A = area_poligono(vertici)                  # nostra area (shoelace)
A_revit = room.Area * FT_M * FT_M           # area della Room (controprova)

print("Stanza: {}".format(room.Name))
print("Vertici del contorno: {}".format(len(vertici)))
print("Area (shoelace):  {:.1f} m2".format(A))
print("Area (Room.Area): {:.1f} m2".format(A_revit))
print("Perimetro:        {:.1f} m".format(P))
