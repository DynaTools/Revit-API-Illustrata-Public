# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.10.3  |  Capitolo 7.10 - La pressione dell'acqua fredda in bagno
# Sezione: Passo 4 - verificare il minimo di ognuno

# PASSO 4: verifica apparecchio per apparecchio
print("--- VERIFICA BAGNO BA-01 ---")
tutti_ok = True
for nome, z_app, battente, p_res, p_min in risultati:
    ok = p_res >= p_min
    tutti_ok = tutti_ok and ok
    esito = "OK" if ok else "INSUFFICIENTE"
    print("{:<20} {:.2f} mca  (min {:.2f})  {}".format(
        nome, p_res, p_min, esito))

print("---")
if tutti_ok:
    print("ESITO: bagno CONFORME - tutti gli apparecchi alimentati")
else:
    print("ESITO: NON CONFORME - serve piu' battente (serbatoio piu'")
    print("       alto) o una pompa di rilancio / autoclave")
