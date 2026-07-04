# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.1.3  |  Capitolo 7.1 - Lo staffaggio
# Sezione: Bonus - tutto il modello, e l'abaco fa il totale

# BONUS: staffaggio di tutte le passerelle del modello
from Autodesk.Revit.DB import (FilteredElementCollector,
                               BuiltInCategory)

tratti = (FilteredElementCollector(doc)
          .OfCategory(BuiltInCategory.OST_CableTray)
          .WhereElementIsNotElementType())

tot = 0
t = Transaction(doc, "Staffaggio del modello")
t.Start()
for tr in tratti:
    L = tr.Location.Curve.Length * FT_M
    w_t = PESO_PASSERELLA
    for nome, peso in PESI.items():
        par = tr.LookupParameter(nome)
        w_t += peso * (par.AsInteger() if par else 0)
    n_t = int(math.ceil(L / INTERASSE)) + 1
    tr.LookupParameter("Staffe n").Set(n_t)
    tr.LookupParameter("Staffe interasse").Set(INTERASSE / FT_M)
    tot += n_t
    print("{}: L = {:5.2f} m  w = {:5.2f} kg/m  ->  {} staffe".format(
        tr.Name, L, w_t, n_t))
t.Commit()

print("---")
print("Totale staffe nel modello: {}".format(tot))
