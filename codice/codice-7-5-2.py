# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.5.2  |  Capitolo 7.5 - Il calcolo illuminotecnico punto per punto
# Sezione: Passo 3 - sommare i contributi

# PASSO 3: illuminamento in ogni punto = somma dei contributi
I_cd  = 1200.0                     # intensita' luminosa (cd), verso il basso
n_hat = XYZ(0, 0, 1)               # normale del piano di lavoro (orizzontale)

def illuminamento(P, sorgenti):
    """E nel punto P (in metri) sommando inverso-quadrato * coseno."""
    E = 0.0
    for S in sorgenti:
        d_vec  = S - P                 # vettore P -> S
        d      = d_vec.GetLength()     # distanza (m)
        cos_eps = n_hat.DotProduct(d_vec) / d   # prodotto scalare / d = coseno
        E += I_cd * cos_eps / d**2     # inverso del quadrato per coseno
    return E

# le sorgenti vanno in metri (qui simuliamo la lettura del modello)
S_m = [XYZ(x, y, 3.00) for (x, y) in
       [(1.0,1.0),(3.0,1.0),(5.0,1.0),(1.0,3.0),(3.0,3.0),(5.0,3.0)]]

# verifica su un singolo apparecchio: sotto, e a 1,5 m di offset
P_sotto = XYZ(1.0, 1.0, 0.80)
P_off   = XYZ(2.5, 1.0, 0.80)      # 1,5 m a lato dell'apparecchio (1.0,1.0)
print("1 apparecchio - sotto:        {:.1f} lux".format(
    illuminamento(P_sotto, [S_m[0]])))
print("1 apparecchio - offset 1,5 m: {:.1f} lux".format(
    illuminamento(P_off, [S_m[0]])))
