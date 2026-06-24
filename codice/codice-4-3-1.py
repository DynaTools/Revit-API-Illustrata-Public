# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 4.3.1  |  Capitolo 4.3 - Parametri in blocco
# Sezione: Scrivere con criterio: il filtro nel mezzo

t = Transaction(doc, "Scrivere con criterio")
t.Start()
for el in targets:
    if <criterio>:                # DECIDERE: solo chi passa, cambia
        el.LookupParameter("...").Set(value)
t.Commit()
