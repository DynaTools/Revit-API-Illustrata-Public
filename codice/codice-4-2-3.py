# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 4.2.3  |  Capitolo 4.2 - Il metodo Spy: replicare e generalizzare
# Sezione: Generalizzare: scambiare lo specifico con la variabile

# DOPO (Generalizzare): tutti gli elementi, valore in variabile
value = "Verificato"                        # il fissato e diventato input
targets = FilteredElementCollector(doc)\
    .OfCategory(BuiltInCategory.OST_Walls)\
    .WhereElementIsNotElementType()         # la selezione e diventata domanda

t = Transaction(doc, "Riempire Commenti - muri")
t.Start()
for el in targets:                            # l'"uno" e diventato il for
    p = el.LookupParameter("Comments")
    if p and not p.IsReadOnly:              # il bordo che il blocco richiede
        p.Set(value)
t.Commit()
