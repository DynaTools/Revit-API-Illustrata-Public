# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.7.4  |  Capitolo 7.7 - La pressione dell'acqua fredda in bagno
# Sezione: Bonus - quanta pressione manca, e a chi

# Bonus: l'apparecchio critico e la quota di serbatoio necessaria
critico = min(risultati, key=lambda r: r[3] - r[4])   # min (residua - minimo)
nome_c, z_c, batt_c, pres_c, pmin_c = critico
deficit = pmin_c - pres_c                              # mca mancanti (se >0)

print("Apparecchio critico: {}".format(nome_c))
print("Residua {:.2f} mca, minimo {:.2f} mca".format(pres_c, pmin_c))
if deficit > 0:
    z_nuova = Z_SERBATOIO + deficit
    print("Mancano {:.2f} mca.".format(deficit))
    print("Alza il serbatoio a {:.2f} m (+{:.2f} m).".format(z_nuova, deficit))
else:
    print("Margine {:.2f} mca: nessun intervento.".format(-deficit))
