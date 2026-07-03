# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.5.3  |  Capitolo 7.5 - La caduta di tensione
# Sezione: Passo 3 - calcolare la caduta

# PASSO 3: caduta di tensione trifase
# DeltaU = (sqrt(3) * rho * L * Ib * cosphi) / S
dU  = (math.sqrt(3) * rho * L * Ib * cosphi) / S    # in volt
dU_pct = dU / Un * 100.0                             # in percentuale

print("Caduta di tensione DeltaU: {:.2f} V".format(dU))
print("Caduta percentuale DeltaU%: {:.2f} %".format(dU_pct))
