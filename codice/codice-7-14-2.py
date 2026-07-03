# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.14.2  |  Capitolo 7.14 - Il volume di scavo di una trincea
# Sezione: Passi 3--4 - il volume lungo la trincea

from Autodesk.Revit.DB import (FilteredElementCollector, BuiltInCategory)

FT_M = 0.3048                      # 1 piede = 0.3048 m

doc = __revit__.ActiveUIDocument.Document

# PASSO 4: volume per stazioni (regola trapezoidale; A*L se sezione costante)
def volume_trincea(aree, lunghezze):
    V = 0.0
    for i in range(len(lunghezze)):
        V += (aree[i] + aree[i + 1]) / 2.0 * lunghezze[i]   # area media * tratto
    return V

# PASSO 3: leggi il percorso della canaletta interrata e la sua lunghezza
cana = (FilteredElementCollector(doc)
        .OfCategory(BuiltInCategory.OST_Conduit)
        .WhereElementIsNotElementType()
        .FirstElement())
L = cana.Location.Curve.Length * FT_M      # lunghezza del percorso (m)

# sezione costante per tutta la trincea: due stazioni con la stessa area A
V = volume_trincea([A, A], [L])            # = A * L

print("Canaletta: {}".format(cana.Name))
print("Lunghezza trincea: {:.2f} m".format(L))
print("Area sezione: {:.2f} m2".format(A))
print("Volume di sterro: {:.2f} m3".format(V))
