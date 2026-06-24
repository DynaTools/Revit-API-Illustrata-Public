# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 4.4.3  |  Capitolo 4.4 - Gli errori che compaiono nel progetto reale
# Sezione: Sul documento: collegamenti e worksharing

from Autodesk.Revit.DB import WorksharingUtils, CheckoutStatus

if doc.IsLinked:                         # documento di link = sola-lettura
    print("Questo documento e un link; aprilo direttamente per editare.")

st = WorksharingUtils.GetCheckoutStatus(doc, el.Id)
if st == CheckoutStatus.OwnedByOtherUser:    # il proprietario e un'altra persona
    print("L'elemento appartiene a un altro utente; salto.")
