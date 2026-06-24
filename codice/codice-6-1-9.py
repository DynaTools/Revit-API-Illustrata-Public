# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.1.9  |  Capitolo 6.1 - I primitivi geometrici
# Sezione: I primitivi applicati alle categorie Revit

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

FT_M = 0.3048

# Solaio (Floor) di riferimento
floor = (FilteredElementCollector(doc)
         .OfCategory(BuiltInCategory.OST_Floors)
         .WhereElementIsNotElementType().FirstElement())
z_top = floor.get_BoundingBox(None).Max.Z * FT_M   # faccia superiore

# Passerella EC-01 (categoria OST_CableTray)
z_bottom = element.get_BoundingBox(None).Min.Z * FT_M   # faccia inferiore

# Altezza libera e verifica
h_libera = z_bottom - z_top
h_min    = 2.70
margine  = h_libera - h_min

print("Faccia sup. solaio: {:.2f} m".format(z_top))
print("Faccia inf. EC-01:  {:.2f} m".format(z_bottom))
print("Altezza libera: {:.2f} m  (minimo {:.2f} m)".format(h_libera, h_min))
print("Verifica: {}".format(
    "OK, margine {:.2f} m".format(margine) if margine >= 0 else "VIOLATA"))
