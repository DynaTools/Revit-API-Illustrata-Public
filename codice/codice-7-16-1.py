# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.16.1  |  Capitolo 7.16 - Il bilanciamento delle fasi su un quadro
# Sezione: Passi 1--3 - leggere i carichi e assegnarli

from Autodesk.Revit.DB import (FilteredElementCollector, BuiltInCategory,
    Electrical)

doc = __revit__.ActiveUIDocument.Document

NOMI = ("R", "S", "T")             # le tre fasi del quadro

# assegna i carichi alle 3 fasi con l'euristica LPT (Longest Processing
# Time first): ordina decrescente, poi mette ognuno sulla fase meno carica
def assegna_lpt(carichi):
    fasi = [[], [], []]            # liste di carichi per R, S, T
    for c in sorted(carichi, reverse=True):
        k = min(range(3), key=lambda j: sum(fasi[j]))   # fase meno carica
        fasi[k].append(c)
    return fasi

# squilibrio % = (Pmax - Pmin) / Pmedia
def squilibrio(fasi):
    somme = [sum(f) for f in fasi]
    media = sum(somme) / 3.0
    if media == 0.0:
        return 0.0, somme
    return (max(somme) - min(somme)) / media * 100.0, somme

# PASSO 1: leggi i carichi dei circuiti del quadro (potenza apparente)
# ApparentLoad e' in VA; /1000 -> kW. Se l'API differisce sul vostro
# modello, leggete qui il parametro numerico di carico del circuito.
circuiti = (FilteredElementCollector(doc)
            .OfCategory(BuiltInCategory.OST_ElectricalCircuit)
            .WhereElementIsNotElementType()
            .ToElements())

carichi = []
for sis in circuiti:
    try:
        carichi.append(sis.ApparentLoad / 1000.0)   # VA -> kW
    except:
        pass

# se il modello non ha circuiti leggibili, usa la lista guida del capitolo
if not carichi:
    carichi = [4.0, 3.5, 3.0, 2.5, 2.2, 2.0, 1.5, 1.2, 0.8, 0.6]

# PASSI 2-3: ordina (dentro assegna_lpt) e assegna alla fase minima
fasi = assegna_lpt(carichi)
sq, somme = squilibrio(fasi)

print("Carichi (kW): {}".format(sorted(carichi, reverse=True)))
for nome, f, s in zip(NOMI, fasi, somme):
    print("Fase {}: {} = {:.1f} kW".format(nome, [round(x, 1) for x in f], s))
print("Squilibrio LPT: {:.1f}%".format(sq))
