# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 5.1.3  |  Capitolo 5.1 - pyRevit, pulsanti e distribuzione
# Sezione: pyRevit al posto dell'RPS

from pyrevit import revit, script
from Autodesk.Revit.DB import FilteredElementCollector, Wall

doc = revit.doc                      # lo stesso doc dell'RPS
out = script.get_output()            # la finestra pyRevit Output

muri = list(FilteredElementCollector(doc).OfClass(Wall)
            .WhereElementIsNotElementType())

out.print_md("**Muri nel modello** -- {} istanze".format(len(muri)))

piu_lungo = max(muri, key=lambda m: m.Location.Curve.Length)
out.print_md("Il piu lungo -- {}".format(out.linkify(piu_lungo.Id)))
