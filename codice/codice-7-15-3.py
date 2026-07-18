# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.15.3  |  Capitolo 7.15 - La pendenza dello scarico, dal tratto alla filiera
# Sezione: La filiera - il controllo che Revit non fa

# (stessa sessione: pendenza(), FASCIA_MIN e FASCIA_MAX, uidoc e doc
#  arrivano dai Codici 7.15.1 e 7.15.2)
from Autodesk.Revit.UI.Selection import ObjectType

# PASSO 1: clicca i tratti in ordine di flusso, dal monte alla valle
refs = uidoc.Selection.PickObjects(ObjectType.Element,
                                   "Filiera dal monte alla valle")
tratti = [doc.GetElement(r.ElementId) for r in refs]

# PASSO 2: orienta ogni tratto sul precedente e misura
# (il verso di disegno non e' garantito: il monte e' l'estremo
#  piu' vicino alla valle del tratto precedente)
valle = None
esiti = []
for el in tratti:
    k = el.Location.Curve
    A, B = k.GetEndPoint(0), k.GetEndPoint(1)
    if valle is not None and A.DistanceTo(valle) > B.DistanceTo(valle):
        A, B = B, A                    # A = monte, B = valle
    p, dz, L = pendenza(A, B)          # p e' senza segno (Codice 7.15.1)
    scende = B.Z < A.Z                 # il segno lo rimettiamo qui
    esiti.append((el.Name, p, scende))
    valle = B

# PASSO 3: fascia su ogni tratto, e il fondo mai in risalita
print("{:<8}{:>8}{:>10}".format("tratto", "p (%)", "fondo"))
filiera_ok = True
for nome, p, scende in esiti:
    ok = scende and FASCIA_MIN <= p <= FASCIA_MAX
    filiera_ok = filiera_ok and ok
    print("{:<8}{:>8.2f}{:>10}".format(nome, p if scende else -p,
                                       "scende" if scende else "RISALE"))
print("ESITO: " + ("CONFORME" if filiera_ok
                   else "NON CONFORME - un tratto tradisce la filiera"))
