# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.16.3  |  Capitolo 7.16 - Il bilanciamento delle fasi su un quadro
# Sezione: Bonus - scrivere la fase assegnata sul modello

from Autodesk.Revit.DB import Transaction

# rifaccio la mappa carico -> fase con LPT, tenendo il riferimento al circuito
def assegna_circuiti(coppie):       # coppie = lista di (carico_kW, circuito)
    somme = [0.0, 0.0, 0.0]
    mappa = []
    for carico, sis in sorted(coppie, key=lambda p: p[0], reverse=True):
        k = min(range(3), key=lambda j: somme[j])
        somme[k] += carico
        mappa.append((sis, NOMI[k]))
    return mappa, somme

coppie = []
for sis in circuiti:
    try:
        coppie.append((sis.ApparentLoad / 1000.0, sis))
    except:
        pass

mappa, somme = assegna_circuiti(coppie)

t = Transaction(doc, "Bilanciamento fasi QE-01")
t.Start()
for sis, fase in mappa:
    p = sis.LookupParameter("Fase assegnata")
    if p and not p.IsReadOnly:
        p.Set(fase)                 # scrive R, S o T sul circuito
t.Commit()

print("Fase scritta su {} circuiti.".format(len(mappa)))
print("Somme finali R/S/T: {} kW".format([round(s, 1) for s in somme]))
