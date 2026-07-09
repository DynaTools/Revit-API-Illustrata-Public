# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.1.2  |  Capitolo 7.1 - Lo staffaggio
# Sezione: Passi 1--2 - lettura, calcolo e risultato (sezioni 3-5)

# ============================================================
# 3. PASSO 1, LA LETTURA                       [REVIT] + [ENG]
#    lunghezza della curva, da piedi a metri (Legge II)
# ============================================================
L_run = tray.Location.Curve.Length * FT_M
print("Tratto: {}   L = {:.2f} m".format(tray.Name, L_run))

# ============================================================
# 4. PASSO 2, IL CALCOLO                       [ENG] + [REVIT]
#    w = passerella + somma (peso x quantita')
# ============================================================
w = PESO_PASSERELLA
for nome, peso in PESI.items():
    par = tray.LookupParameter(nome)
    n = par.AsInteger() if par else 0
    w += peso * n
    print("  {:>11}: {:.2f} kg/m  x{}  ->  {:.2f} kg/m".format(
        nome, peso, n, peso * n))

# ============================================================
# 5. IL RISULTATO                                        [OUT]
# ============================================================
print("Peso passerella: {:.2f} kg/m".format(PESO_PASSERELLA))
print("Peso al metro w: {:.2f} kg/m".format(w))
