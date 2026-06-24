# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.2.3  |  Capitolo 6.2 - Lo staffaggio
# Sezione: Passi 3--4 - carico, verifica e numero di staffe

# PASSO 3-4: staffaggio
G         = 9.81     # accelerazione di gravita' (m/s^2)
interasse = 2.0      # m, passo scelto fra le staffe
portata   = 60.0     # kg, portata di una staffa (da catalogo)

# Carico su ogni staffa = peso di una campata
F = w * interasse                              # kg
F_N = F * G                                    # newton

# Numero di staffe lungo il tratto (estremi inclusi)
N = int(math.ceil(L_run / interasse)) + 1

# Interasse massimo consentito dalla portata della staffa
i_max = portata / w

conforme = F <= portata

print("Peso totale del tratto: {:.1f} kg".format(w * L_run))
print("Interasse scelto: {:.2f} m".format(interasse))
print("Carico per staffa: {:.1f} kg  ({:.0f} N)".format(F, F_N))
print("Portata staffa: {:.1f} kg".format(portata))
print("Numero di staffe: {}".format(N))
print("Interasse massimo ammesso: {:.2f} m".format(i_max))
print("---")
if conforme:
    print("ESITO: CONFORME (margine {:.1f} kg)".format(portata - F))
else:
    print("ESITO: NON CONFORME - avvicinare le staffe")
