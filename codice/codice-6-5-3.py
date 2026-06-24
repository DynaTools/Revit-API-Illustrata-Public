# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.5.3  |  Capitolo 6.5 - Lo schema L-2L
# Sezione: In Revit - leggere la stanza e posare le luci

from Autodesk.Revit.DB import Transaction, Structure

# symbol = FamilySymbol del punto luce (gia' caricato);  level = livello
if not symbol.IsActive:
    symbol.Activate()

t = Transaction(doc, "Griglia luci L-2L")
t.Start()
for p in punti:
    doc.Create.NewFamilyInstance(p, symbol, level,
                                 Structure.StructuralType.NonStructural)
t.Commit()

print("Posati {} apparecchi sulla griglia.".format(len(punti)))
