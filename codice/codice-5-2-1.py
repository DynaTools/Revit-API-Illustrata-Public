# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 5.2.1  |  Capitolo 5.2 - Il cammino verso il C#
# Sezione: Lo stesso script nelle due lingue

# PYTHON (Livello 4)
walls = FilteredElementCollector(doc).OfClass(Wall)

t = Transaction(doc, "Riempire Commenti")
t.Start()
for w in walls:
    p = w.LookupParameter("Commenti")
    if p and not p.IsReadOnly:
        p.Set("Verificato")
t.Commit()
