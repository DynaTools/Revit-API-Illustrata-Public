# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 4.2.2  |  Capitolo 4.2 - Il metodo Spy: replicare e generalizzare
# Sezione: Generalizzare: scambiare lo specifico con la variabile

# PRIMA (Replicare): un elemento, valore fissato
target = uidoc.Selection.GetElementIds()
el = doc.GetElement(list(target)[0])

t = Transaction(doc, "Replicare - test")
t.Start()
el.LookupParameter("Comments").Set("TEST-REPLICARE")
t.Commit()
