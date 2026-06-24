# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 4.4.1  |  Capitolo 4.4 - Gli errori che compaiono nel progetto reale
# Sezione: Sul parametro: quattro silenzi

from Autodesk.Revit.DB import StorageType, BuiltInParameter

def set_texto(el, bip, value):
    p = el.get_Parameter(bip)            # 4) per BuiltInParameter, non per nome
    if p is None:                        # 1) non esiste su questo elemento
        return "assente"
    if p.IsReadOnly:                     # 2) sola-lettura
        return "bloccato"
    if p.StorageType != StorageType.String:  # 3) tipo sbagliato
        return "tipo incompatibile"
    p.Set(value)                         # (dentro una Transaction)
    return "ok"

# invece di LookupParameter("Comments"):
set_texto(el, BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS, "Verificato")
