# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 4.2.4  |  Capitolo 4.2 - Il metodo Spy → Replicare → Generalizzare
# Sezione: Generalizzare: scambiare lo specifico con la variabile

ids = list(uidoc.Selection.GetElementIds())
if not ids:                          # 1) niente selezionato?
    print("Seleziona prima un elemento.")
else:
    el = doc.GetElement(ids[0])
    p = el.LookupParameter("Commenti")   # 2) puo essere None
    if p and not p.IsReadOnly:           # 3) puo essere sola-lettura
        # ... dentro la Transaction ...
        p.Set("Verificato")
