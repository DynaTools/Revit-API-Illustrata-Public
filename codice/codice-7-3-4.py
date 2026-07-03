# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.3.4  |  Capitolo 7.3 - Il riempimento dei cavidotti
# Sezione: Bonus - scrivere l'esito nel modello

from Autodesk.Revit.DB import Transaction, BuiltInParameter

testo = "Riempimento {:.0f}% - {}".format(
    K * 100, "CONFORME" if conforme else "NON CONFORME")

t = Transaction(doc, "Riempimento cavidotto")
t.Start()
p_note = conduit.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
if p_note and not p_note.IsReadOnly:
    p_note.Set(testo)
t.Commit()

print("Scritto nei Commenti del cavidotto: '{}'".format(testo))
