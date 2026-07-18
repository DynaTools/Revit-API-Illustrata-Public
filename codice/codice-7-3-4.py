# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.3.4  |  Capitolo 7.3 - Il riempimento dei cavidotti
# Sezione: Bonus - scrivere l'esito nel modello

# ============================================================
# 0. RIPARTENZA                            [PY]+[REVIT]+[ENG]
#    blocco autonomo: ricrea K e l'esito della verifica
# ============================================================
import math
from Autodesk.Revit.DB import BuiltInParameter
from Autodesk.Revit.UI.Selection import ObjectType

FT_MM = 304.8
catalogo = [("FG16OR16 3G6 mm²", 14.0),
            ("FG16OR16 3G4 mm²", 12.5)]

uidoc   = __revit__.ActiveUIDocument
doc     = uidoc.Document
ref     = uidoc.Selection.PickObject(ObjectType.Element,
                                     "Seleziona il cavidotto")
conduit = doc.GetElement(ref.ElementId)
De      = conduit.get_Parameter(
    BuiltInParameter.RBS_CONDUIT_INNER_DIAM_PARAM).AsDouble() * FT_MM

cavi = [(n, d, conduit.LookupParameter(n).AsInteger())
        for n, d in catalogo if conduit.LookupParameter(n)]
somma_d2 = sum(d**2 * q for nome, d, q in cavi)
K        = somma_d2 / De**2        # il pi/4 si semplifica
conforme = De >= 1.3 * math.sqrt(somma_d2)

# ============================================================
# 1. BONUS, LA SCRITTURA SUL MODELLO           [REVIT] + [OUT]
#    Legge I: ogni modifica vive in una Transaction.
#    get_Parameter -> None se il parametro manca;
#    Set -> False se esiste ma non si puo' scrivere.
# ============================================================
from Autodesk.Revit.DB import Transaction

testo = "Riempimento {:.0f}% - {}".format(
    K * 100, "CONFORME" if conforme else "NON CONFORME")

p_note = conduit.get_Parameter(
    BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)

if p_note is None or p_note.IsReadOnly:
    print("ERRORE: il parametro Commenti manca o e' di sola")
    print("lettura su questo elemento: niente da scrivere.")
else:
    t = Transaction(doc, "Riempimento cavidotto")
    t.Start()
    ok = p_note.Set(testo)
    t.Commit()
    if ok:
        print("Scritto nei Commenti del cavidotto: "
              "'{}'".format(testo))
    else:
        print("ERRORE: scrittura rifiutata (Set = False),")
        print("controlla il tipo del parametro Commenti.")
