# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.1.2  |  Capitolo 7.1 - Lo staffaggio
# Sezione: Passi 3--4 - staffe, verifica e scrittura sul modello

# PASSO 3: staffe e verifica
G           = 9.81   # m/s^2
INTERASSE   = 1.50   # m, prassi di catalogo
PORTATA     = 80.0   # kg, mensola B300: 784 N (CEI EN 61537)
CAMPATA_MAX = 2.00   # m, dal diagramma di carico della passerella

F   = w * INTERASSE                        # carico per staffa (kg)
F_N = F * G                                # in newton
N   = int(math.ceil(L_run / INTERASSE)) + 1

i_max_staffa = PORTATA / w                 # vincolo della mensola
i_ammesso    = min(i_max_staffa, CAMPATA_MAX)
conforme     = (F <= PORTATA) and (INTERASSE <= CAMPATA_MAX)

print("Peso del tratto: {:.1f} kg".format(w * L_run))
print("Carico per staffa: {:.1f} kg  ({:.0f} N)".format(F, F_N))
print("Numero di staffe: {}".format(N))
print("Interasse ammesso: {:.2f} m  (mensola {:.2f} / campata {:.2f})".format(
    i_ammesso, i_max_staffa, CAMPATA_MAX))
print("ESITO: {}".format("CONFORME (margine {:.1f} kg)".format(PORTATA - F)
                         if conforme else "NON CONFORME"))

# PASSO 4: scrivi il risultato sul tratto (LEGGE I: in transazione)
t = Transaction(doc, "Staffaggio EC-01")
t.Start()
tray.LookupParameter("Staffe n").Set(N)
tray.LookupParameter("Staffe interasse").Set(INTERASSE / FT_M)  # in piedi
t.Commit()
print("Scritti sul tratto: Staffe n = {}, interasse = {:.2f} m".format(
    N, INTERASSE))
