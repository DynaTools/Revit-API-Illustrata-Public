# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.8.2  |  Capitolo 7.8 - Il percorso minimo nella rete
# Sezione: Passi 1--2 - costruire il grafo dalla rete Revit

from Autodesk.Revit.DB import (FilteredElementCollector, BuiltInCategory)

FT_M = 0.3048                      # 1 piede = 0.3048 m
EPS  = 0.01                        # tolleranza di prossimita' (m)

doc = __revit__.ActiveUIDocument.Document

# PASSO 1: raccogli i tratti della rete (canalette + cavidotti)
cats = [BuiltInCategory.OST_Conduit, BuiltInCategory.OST_CableTray]
tratti = []
for cat in cats:
    tratti += list(FilteredElementCollector(doc).OfCategory(cat)
                   .WhereElementIsNotElementType())

# estremi e lunghezza di ogni tratto (in metri)
segmenti = []
for el in tratti:
    k = el.Location.Curve
    p0, p1 = k.GetEndPoint(0), k.GetEndPoint(1)
    L = k.Length * FT_M
    segmenti.append((el, p0, p1, L))

# PASSO 2: nodi per prossimita' degli estremi (DistanceTo < EPS)
nodi = []                          # lista dei punti-rappresentante dei nodi
def id_nodo(p):                    # indice del nodo cui appartiene il punto p
    for i, q in enumerate(nodi):
        if p.DistanceTo(q) * FT_M < EPS:   # prossimita': Cap. 7.11
            return i
    nodi.append(p)                 # nuovo nodo
    return len(nodi) - 1

# costruisci la lista di adiacenza (grafo non orientato, pesi in metri)
adj = {}
def aggiungi(u, v, w):
    adj.setdefault(u, []).append((v, w))
    adj.setdefault(v, []).append((u, w))

for el, p0, p1, L in segmenti:
    a, b = id_nodo(p0), id_nodo(p1)
    if a != b:
        aggiungi(a, b, L)

print("Tratti letti: {}".format(len(segmenti)))
print("Nodi (raccordi): {}".format(len(nodi)))
print("Archi nel grafo: {}".format(sum(len(v) for v in adj.values()) // 2))
