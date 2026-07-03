# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.5.6  |  Capitolo 7.5 - La caduta di tensione
# Sezione: Bonus - scrivere la caduta nel modello

from Autodesk.Revit.DB import Transaction, BuiltInParameter

# l'elemento su cui scrivere (es. il primo tratto selezionato)
target = doc.GetElement(refs[0].ElementId)

testo = "DeltaU {:.2f}% - {}".format(
    dU_pct, "CONFORME" if conforme else "NON CONFORME")

t = Transaction(doc, "Caduta di tensione")
t.Start()
p_note = target.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
if p_note and not p_note.IsReadOnly:
    p_note.Set(testo)
t.Commit()

print("Scritto nei Commenti: '{}'".format(testo))
