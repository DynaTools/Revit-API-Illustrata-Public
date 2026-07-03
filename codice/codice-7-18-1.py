# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.18.1  |  Capitolo 7.18 - Le unità di scarico e il diametro della colonna
# Sezione: Passi 1--2 - apparecchi e somma delle Unità di Scarico

import math
from Autodesk.Revit.DB import (FilteredElementCollector, BuiltInCategory)

doc = __revit__.ActiveUIDocument.Document

# tabella di ripiego: Unita' di Scarico tipiche (UNI EN 12056-2)
DU_TIPICHE = {"lavabo": 0.5, "bidet": 0.5, "doccia": 0.6, "wc": 2.0}

def du_tipica(nome):
    n = nome.lower()
    for chiave, val in DU_TIPICHE.items():
        if chiave in n:
            return val
    return 0.0

# PASSO 1: raccogli gli apparecchi sanitari del modello
apparecchi = (FilteredElementCollector(doc)
              .OfCategory(BuiltInCategory.OST_PlumbingFixtures)
              .WhereElementIsNotElementType()
              .ToElements())

# PASSO 2: leggi e somma le Unita' di Scarico
somma_du = 0.0
for ap in apparecchi:
    nome = ap.Name
    par = ap.LookupParameter("DU")          # parametro condiviso, se c'e'
    if par and par.HasValue:
        du = par.AsDouble()
    else:
        du = du_tipica(nome)                 # ripiego sui valori tipici
    somma_du += du
    print("{:>22}: DU = {:.1f}".format(nome, du))

print("---")
print("Apparecchi: {}".format(len(apparecchi)))
print("Somma DU: {:.1f}".format(somma_du))
