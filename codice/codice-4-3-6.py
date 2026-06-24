# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 4.3.6  |  Capitolo 4.3 - Parametri in blocco
# Sezione: Parametri condivisi e di progetto

from System import Guid

guid = Guid("a1b2c3d4-0000-0000-0000-00000000beba")  # il GUID del tuo .txt
p = el.get_Parameter(guid)        # trova col passaporto, non col soprannome
if p and not p.IsReadOnly:
    p.Set(value)
