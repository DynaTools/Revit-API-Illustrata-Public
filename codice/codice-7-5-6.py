# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.5.6  |  Capitolo 7.5 - La caduta di tensione
# Sezione: Bonus - scrivere la caduta nel modello

# ============================================================
# 0. RIPARTENZA                            [PY]+[REVIT]+[ENG]
#    blocco autonomo: ricrea caduta, esito e tratti scelti
# ============================================================
import math
from Autodesk.Revit.UI.Selection import ObjectType

FT_M   = 0.3048
LIMITE = 4.0
# dati del passo 2: V, A, cosphi, mm2, ohm*mm2/m
Un, Ib, cosphi, S, rho = 400.0, 28.0, 0.85, 6.0, 0.0225

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document
refs  = uidoc.Selection.PickObjects(ObjectType.Element,
                                    "Seleziona i tratti del percorso")

L = 0.0
for r in refs:
    L += doc.GetElement(r.ElementId).Location.Curve.Length * FT_M

dU_pct   = (math.sqrt(3) * rho * L * Ib * cosphi) / S / Un * 100.0
conforme = dU_pct <= LIMITE

# ============================================================
# 1. IL TESTO E IL PARAMETRO                    [PY] + [REVIT]
#    l'esito da scrivere e il parametro Commenti del target
# ============================================================
from Autodesk.Revit.DB import Transaction, BuiltInParameter

# l'elemento su cui scrivere (es. il primo tratto selezionato)
target = doc.GetElement(refs[0].ElementId)

testo = "DeltaU {:.2f}% - {}".format(
    dU_pct, "CONFORME" if conforme else "NON CONFORME")

p_note = target.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)

# ============================================================
# 2. LA SCRITTURA, IN TRANSAZIONE              [REVIT] + [OUT]
#    parametro assente o bloccato? ERRORE, non finto successo
# ============================================================
if p_note is None or p_note.IsReadOnly:
    print("ERRORE: il parametro Commenti manca o e' di sola")
    print("lettura su questo elemento: niente da scrivere.")
else:
    t = Transaction(doc, "Caduta di tensione")
    t.Start()
    ok = p_note.Set(testo)
    t.Commit()
    if ok:
        print("Scritto nei Commenti: '{}'".format(testo))
    else:
        print("ERRORE: scrittura rifiutata (Set = False),")
        print("controlla il tipo del parametro Commenti.")
