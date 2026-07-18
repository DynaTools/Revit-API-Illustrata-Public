# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.7.5  |  Capitolo 7.7 - Lo spazio da difendere
# Sezione: Il caso verticale, l'altezza libera

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

FT_M = 0.3048                      # 1 piede = 0.3048 m

doc = __revit__.ActiveUIDocument.Document

# PASSO 1: raccogli gli impianti del corridoio (condotti, tubi, passerelle)
cats = [BuiltInCategory.OST_DuctCurves,    # canali dell'aria
        BuiltInCategory.OST_PipeCurves,    # tubi
        BuiltInCategory.OST_CableTray]     # passerelle portacavi

impianti = []
for cat in cats:
    impianti += list(FilteredElementCollector(doc).OfCategory(cat)
                     .WhereElementIsNotElementType())

Z_PAV = 0.00                       # quota del pavimento finito (m)

# PASSO 2: leggi l'intradosso (bottom z del bounding box) di ciascuno
intradossi = []
for e in impianti:
    bb = e.get_BoundingBox(None)   # AABB dell'elemento (in piedi)
    if bb is None:
        continue
    z_bottom = bb.Min.Z * FT_M     # intradosso in metri
    intradossi.append((e.Name, z_bottom))
    print("  {}: intradosso {:.2f} m".format(e.Name, z_bottom))

# PASSO 3: l'altezza libera e' il minimo degli intradossi meno il pavimento
nome_basso, z_basso = min(intradossi, key=lambda p: p[1])
h_libera = z_basso - Z_PAV

print("---")
print("Intradosso piu' basso: {} a {:.2f} m".format(nome_basso, z_basso))
print("Altezza libera: {:.2f} m".format(h_libera))
