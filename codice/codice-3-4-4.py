# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 3.4.4  |  Capitolo 3.4 - Il Python del mestiere
# Sezione: Il nastro in una riga, la comprehension

larghezze = [0.20, 0.45, 0.10, 0.30]

spessi = [w for w in larghezze if w > 0.25]      # filtrare
centimetri = [w * 100 for w in larghezze]        # trasformare

print(spessi)
print(centimetri)
