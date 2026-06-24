# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 4.1.1  |  Capitolo 4.1 - Transazioni: il contratto prima di mettere mano
# Sezione: Perché esiste il contratto

walls = FilteredElementCollector(doc).OfClass(Wall)  # R4 + R2

t = Transaction(doc, "Riempire Commenti")    # LEGGE I - il contratto
t.Start()
for w in walls:                            # R7 - for diretto
    p = w.LookupParameter("Commenti")        # R2 - prende la scheda
    if p and not p.IsReadOnly:               # solo se esiste ed e modificabile
        p.Set("Verificato")
t.Commit()                                   # LEGGE I - firmare
