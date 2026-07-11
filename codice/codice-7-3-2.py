# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.3.2  |  Capitolo 7.3 - Il riempimento dei cavidotti
# Sezione: Passo 3 - aggiungere i cavi

# ============================================================
# 0. RIPARTENZA                                           [PY]
#    blocco autonomo: qui basta la matematica, un import
# ============================================================
import math

# ============================================================
# 1. PASSO 3, I CAVI                                     [ENG]
#    i cavi da infilare: nome, diametro esterno, quantita'
# ============================================================
cavi = [
    ("FG16OR16 3G2.5", 11.5, 2),
    ("N07V-K 1x4",      4.4, 3),
]

# ============================================================
# 2. LA SOMMA DELLE AREE                          [PY] + [ENG]
#    area di ogni famiglia e somma dei quadrati dei diametri
# ============================================================
A_cavi = 0.0      # somma delle aree dei cavi (mm^2)
somma_d2 = 0.0    # somma dei d^2 (serve per il fascio)
n_cavi = 0

for nome, d, q in cavi:
    area_singolo = math.pi / 4.0 * d**2
    A_cavi   += area_singolo * q
    somma_d2 += d**2 * q
    n_cavi   += q
    print("{:>16}: d={:.1f} mm  x{}  ->  {:.0f} mm2".format(
        nome, d, q, area_singolo * q))

# ============================================================
# 3. IL RISULTATO                                        [OUT]
# ============================================================
print("---")
print("Cavi totali: {}".format(n_cavi))
print("Area occupata dai cavi: {:.0f} mm2".format(A_cavi))
