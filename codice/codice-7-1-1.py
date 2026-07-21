# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.1.1  |  Capitolo 7.1 - La lunghezza del circuito
# Sezione: Passi 1--2 - misurare il percorso dal modello

# ============================================================
# 0. PREPARAZIONE                               [PY] + [REVIT]
#    librerie e documento Revit attivo
# ============================================================
from Autodesk.Revit.DB import LocationCurve
from Autodesk.Revit.UI.Selection import ObjectType

FT_M = 0.3048                      # 1 piede = 0.3048 m

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

# ============================================================
# 1. PASSO 1, I CLIC                                   [REVIT]
#    l'utente seleziona TUTTO il percorso: tratti e raccordi
# ============================================================
refs = uidoc.Selection.PickObjects(ObjectType.Element,
                                   "Seleziona tutto il percorso, poi Finish")

# ============================================================
# 2. PASSO 2, LA SOMMA 3D                      [REVIT] + [ENG]
#    tratti dritti -> la loro curva; raccordi -> l'arco
# ============================================================
L_ft     = 0.0
n_tratti = 0
n_curve  = 0

for r in refs:
    # un passo per riga, cosi' si vede tutto
    elem_id = r.ElementId                 # 1) l'id dell'elemento
    elem    = doc.GetElement(elem_id)     # 2) l'elemento vero e proprio
    loc     = elem.Location               # 3) la sua posizione

    if isinstance(loc, LocationCurve):
        # tratto dritto: ha una curva d'asse
        curva = loc.Curve
        L_ft += curva.Length              # lunghezza 3D, in piedi
        n_tratti += 1
    else:
        # raccordo (gomito): la sua lunghezza e' l'ARCO
        # arco = raggio x angolo  (l'angolo e' gia' in radianti, Legge II)
        p_raggio = elem.LookupParameter("Bend Radius")
        p_angolo = elem.LookupParameter("Angle")
        if p_raggio and p_angolo:
            raggio = p_raggio.AsDouble()  # raggio di curvatura, in piedi
            angolo = p_angolo.AsDouble()  # angolo della piega, in radianti
            L_ft += raggio * angolo       # lunghezza dell'arco, in piedi
        n_curve += 1

L_mod = L_ft * FT_M                    # lunghezza modellata, in metri

# ============================================================
# 3. IL RISULTATO                                        [OUT]
# ============================================================
print("Elementi selezionati: {}".format(len(refs)))
print("  tratti dritti:    {}".format(n_tratti))
print("  raccordi (archi): {}".format(n_curve))
print("Lunghezza modellata (3D): {:.2f} m".format(L_mod))
