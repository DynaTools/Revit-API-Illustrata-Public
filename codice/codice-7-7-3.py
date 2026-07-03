# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.7.3  |  Capitolo 7.7 - La distribuzione delle prese
# Sezione: Passo 4 - inserire le prese orientate

from Autodesk.Revit.DB import (Transaction, Structure, Line,
    ElementTransformUtils, FilteredElementCollector, BuiltInCategory,
    FamilySymbol)

# PASSO 4: recupera il tipo di presa e il livello del muro
symbol = FilteredElementCollector(doc)\
    .OfCategory(BuiltInCategory.OST_ElectricalFixtures)\
    .OfClass(FamilySymbol).FirstElement()    # il primo tipo di presa caricato
level  = doc.GetElement(wall.LevelId)        # il livello del muro

n = wall.Orientation                # normale del muro: verso l'esterno
verso_stanza = -n                   # le prese guardano verso l'interno

if not symbol.IsActive:
    symbol.Activate()

t = Transaction(doc, "Distribuzione prese")
t.Start()
for p in punti:
    inst = doc.Create.NewFamilyInstance(
        p, symbol, level, Structure.StructuralType.NonStructural)
    doc.Regenerate()                        # aggiorna l'orientamento
    attuale = inst.FacingOrientation        # dove guarda la presa adesso
    angolo  = attuale.AngleTo(verso_stanza) # quanto ruotarla
    if attuale.CrossProduct(verso_stanza).Z < 0:
        angolo = -angolo                    # segno della rotazione (asse Z)
    asse = Line.CreateBound(p, p + XYZ.BasisZ)
    ElementTransformUtils.RotateElement(doc, inst.Id, asse, angolo)
t.Commit()

print("Posate {} prese sul muro, orientate verso la stanza.".format(
    len(punti)))
