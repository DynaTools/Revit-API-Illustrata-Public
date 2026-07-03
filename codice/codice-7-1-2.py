# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.1.2  |  Capitolo 7.1 - Lo staffaggio
# Sezione: Passo 2 - sommare i pesi al metro

# PASSO 2: pesi al metro (dati di progetto, in kg/m)
peso_passerella = 5.0      # peso proprio della passerella

cavi = [
    ("FG16OR16 4G25", 1.75,  4),
    ("FG16OR16 3G6",  0.55, 20),
]

peso_cavi = 0.0
for nome, p, q in cavi:
    peso_cavi += p * q
    print("{:>16}: {:.2f} kg/m  x{:>2}  ->  {:.2f} kg/m".format(
        nome, p, q, p * q))

w = peso_passerella + peso_cavi    # peso al metro totale

print("---")
print("Peso passerella: {:.2f} kg/m".format(peso_passerella))
print("Peso cavi:       {:.2f} kg/m".format(peso_cavi))
print("Peso al metro w: {:.2f} kg/m".format(w))
