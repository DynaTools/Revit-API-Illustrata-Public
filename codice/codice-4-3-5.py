# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 4.3.5  |  Capitolo 4.3 - Parametri in blocco
# Sezione: I None e i sola-lettura

count, skipped = 0, 0

t = Transaction(doc, "Riempire in blocco - difensivo")
t.Start()
for el in targets:
    p = el.LookupParameter("COD_LOCALIZACAO")
    if p and not p.IsReadOnly:        # la riga che salva il blocco
        p.Set(value)
        count += 1
    else:
        skipped += 1
t.Commit()

print(count, "riempiti /", skipped, "saltati")
