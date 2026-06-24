# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 4.3.4  |  Capitolo 4.3 - Parametri in blocco
# Sezione: Scrivere con criterio: il filtro nel mezzo

    state = el.LookupParameter("Stato").AsString()
    if state == "Da verificare":
        el.LookupParameter("Comments").Set("In sospeso")
