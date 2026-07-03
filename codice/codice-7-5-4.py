# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.5.4  |  Capitolo 7.5 - La caduta di tensione
# Sezione: Passo 4 - verificare contro il 4%

# PASSO 4: verifica contro il limite CEI 64-8
LIMITE = 4.0        # caduta massima ammessa (%) - CEI 64-8
conforme = dU_pct <= LIMITE

print("DeltaU% = {:.2f} %   limite = {:.0f} %".format(dU_pct, LIMITE))
print("---")
if conforme:
    print("ESITO: CONFORME (margine {:.2f} punti)".format(LIMITE - dU_pct))
else:
    print("ESITO: NON CONFORME - serve una sezione maggiore")
