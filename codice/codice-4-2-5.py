# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 4.2.5  |  Capitolo 4.2 - Il metodo Spy: replicare e generalizzare
# Sezione: Un caso completo, da cima a fondo

el = doc.GetElement(list(uidoc.Selection.GetElementIds())[0])

t = Transaction(doc, "COD - test su un quadro")
t.Start()
el.LookupParameter("COD_LOCALIZACAO").Set("P02-EL")  # fissato!
t.Commit()
