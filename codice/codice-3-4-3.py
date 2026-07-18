# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 3.4.3  |  Capitolo 3.4 - Il Python del mestiere
# Sezione: Lo schedario tascabile, il dizionario

quota = {"lavabo": 0.85, "vaso": 0.40, "doccia": 2.10}

print(quota["doccia"])        # si cerca per chiave, non per posizione

quota["bidet"] = 0.40         # una scheda nuova, al volo

for nome in quota:
    print(nome, "->", quota[nome])
