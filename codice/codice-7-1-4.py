# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.1.4  |  Capitolo 7.1 - Lo staffaggio
# Sezione: Passo 4 - scrittura sul modello, in transazione (sezione 8)

# ============================================================
# 8. PASSO 4, LA SCRITTURA SUL MODELLO         [REVIT] + [OUT]
#    Legge I: ogni modifica vive in una Transaction
# ============================================================
from Autodesk.Revit.DB import Transaction

t = Transaction(doc, "Staffaggio EC-01")
t.Start()
tray.LookupParameter("Staffe n").Set(N)
tray.LookupParameter("Staffe interasse").Set(INTERASSE / FT_M)  # piedi
t.Commit()

print("Scritti sul tratto: Staffe n = {}, interasse = {:.2f} m".format(
    N, INTERASSE))
