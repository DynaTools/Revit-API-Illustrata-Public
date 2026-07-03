# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.9.3  |  Capitolo 7.9 - La portata d'aria nei condotti
# Sezione: Passo 4 - verificare i limiti di comfort

# PASSO 4: verifica contro la fascia raccomandata (ramo derivato)
V_MIN = 3.0      # m/s - sotto: canale sovradimensionato
V_MAX = 5.0      # m/s - sopra: rumore e perdite di carico

if v < V_MIN:
    esito = "SOTTO LA FASCIA - canale sovradimensionato"
elif v > V_MAX:
    esito = "SOPRA LA FASCIA - rischio rumore e perdite"
else:
    esito = "NELLA FASCIA - OK"

print("Velocita': {:.2f} m/s   (fascia consigliata {:.0f}-{:.0f} m/s)".format(
    v, V_MIN, V_MAX))
print("ESITO: {}".format(esito))
