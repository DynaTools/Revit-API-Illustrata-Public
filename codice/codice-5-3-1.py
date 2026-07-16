# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 5.3.1  |  Capitolo 5.3 - Progetto finale: uno strumento da cima a fondo
# Sezione: Dalla missione allo strumento

rosso = Color(255, 0, 0)                 # R4 - senza new
ogs = OverrideGraphicSettings()          # R4
ogs.SetProjectionLineColor(rosso)        # R2

limite = UnitUtils.ConvertToInternalUnits(300, UnitTypeId.Millimeters)
                                         # R3 + LEGGE II
ducts = (
    FilteredElementCollector(doc, doc.ActiveView.Id)
    .OfCategory(BuiltInCategory.OST_DuctCurves)   # R6
    .WhereElementIsNotElementType()               # LEGGE III
)

t = Transaction(doc, "Evidenziare canali > 300 mm")  # LEGGE I
t.Start()
for d in ducts:                          # R7
    diam = d.LookupParameter("Diametro") # R2 - nome del nostro modello (IT)
    if diam and diam.AsDouble() > limite:    # confronta piedi con piedi
        doc.ActiveView.SetElementOverrides(d.Id, ogs)  # R1 + R2
t.Commit()
