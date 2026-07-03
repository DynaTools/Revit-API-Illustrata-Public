# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.4.3  |  Capitolo 7.4 - Lo schema L--2L
# Sezione: In Revit - leggere la stanza e posare le luci

from Autodesk.Revit.DB import (Transaction, Structure,
    FilteredElementCollector, BuiltInCategory, FamilySymbol, Level)

# symbol = tipo di apparecchio luce (gia' caricato); level = livello su cui posare
symbol = FilteredElementCollector(doc)\
    .OfCategory(BuiltInCategory.OST_LightingFixtures)\
    .OfClass(FamilySymbol).FirstElement()   # il primo tipo di punto luce
level  = FilteredElementCollector(doc).OfClass(Level).FirstElement()

if not symbol.IsActive:
    symbol.Activate()

t = Transaction(doc, "Griglia luci L-2L")
t.Start()
for p in punti:
    doc.Create.NewFamilyInstance(p, symbol, level,
                                 Structure.StructuralType.NonStructural)
t.Commit()

print("Posati {} apparecchi sulla griglia.".format(len(punti)))
