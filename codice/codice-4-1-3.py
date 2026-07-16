# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 4.1.3  |  Capitolo 4.1 - Transazioni, il contratto prima di mettere mano
# Sezione: Anatomia del contratto - Start, Commit, RollBack

level = FilteredElementCollector(doc).OfClass(Level).FirstElement()

length = UnitUtils.ConvertToInternalUnits(6, UnitTypeId.Meters)
                                         # R3 + LEGGE II - 6 m -> piedi
t = Transaction(doc, "Creare muro")      # LEGGE I
t.Start()
line  = Line.CreateBound(XYZ(0,0,0), XYZ(length,0,0))  # R3 + R4
wall = Wall.Create(doc, line, level.Id, False)     # R3 static
t.Commit()
