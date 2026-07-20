# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.3.3  |  Capitolo 7.3 - Lo staffaggio
# Sezione: Passo 3 - soglie e verifica

# ============================================================
# 0. RIPARTENZA                          [PY]+[REVIT]+[ENG]
#    blocco autonomo: ricrea lunghezza e peso al metro
# ============================================================
import math
from Autodesk.Revit.UI.Selection import ObjectType

FT_M = 0.3048
PESI = {"FG16 4G95": 4.10, "FG16 5G16": 1.35, "FG16 3G2.5": 0.18}
PESO_PASSERELLA = 5.00

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document
ref   = uidoc.Selection.PickObject(ObjectType.Element,
                                   "Seleziona la passerella")
tray  = doc.GetElement(ref.ElementId)

L_run = tray.Location.Curve.Length * FT_M
w = PESO_PASSERELLA
for nome, peso in PESI.items():
    par = tray.LookupParameter(nome)
    w += peso * (par.AsInteger() if par else 0)

# ============================================================
# 1. PASSO 3, SOGLIE E VERIFICA                          [ENG]
#    carico per staffa, numero di staffe, interasse
# ============================================================
G           = 9.81   # m/s^2
INTERASSE   = 1.50   # m, prassi di catalogo
PORTATA     = 152.9  # kg, staffa 41/600: 1500 N (CEI EN 61537)
CAMPATA_MAX = 2.00   # m, dal diagramma di carico

F   = w * INTERASSE                        # carico per staffa (kg)
F_N = F * G                                # in newton
N   = int(math.ceil(L_run / INTERASSE)) + 1

i_max_staffa = PORTATA / w                 # vincolo della mensola
i_ammesso    = min(i_max_staffa, CAMPATA_MAX)
conforme     = (F <= PORTATA) and (INTERASSE <= CAMPATA_MAX)

# ============================================================
# 2. L'ESITO                                             [OUT]
# ============================================================
print("Peso del tratto: {:.1f} kg".format(w * L_run))
print("Carico per staffa: {:.1f} kg  ({:.0f} N)".format(F, F_N))
print("Numero di staffe: {}".format(N))
print("Interasse ammesso: {:.2f} m  (mensola {:.2f} / campata {:.2f})".format(
    i_ammesso, i_max_staffa, CAMPATA_MAX))
print("ESITO: {}".format("CONFORME (margine {:.1f} kg)".format(PORTATA - F)
                         if conforme else "NON CONFORME"))
