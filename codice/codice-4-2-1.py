# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 4.2.1  |  Capitolo 4.2 - Il metodo Spy: replicare e generalizzare
# Sezione: Replicare: il caso più semplice che funziona

target = uidoc.Selection.GetElementIds()      # l'elemento selezionato
el = doc.GetElement(list(target)[0])          # prende il primo (e unico)

t = Transaction(doc, "Replicare - test")    # LEGGE I
t.Start()
el.LookupParameter("Comments").Set("TEST-REPLICARE")
t.Commit()
