# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.15.3  |  Capitolo 7.15 - Le pendenze: scarico e rampa
# Sezione: Scarico o rampa? Due casi a confronto

# stesso strumento, caso RAMPA: dz=0,80 m su L=12,00 m
# (qui i valori a scopo di confronto; nel modello verrebbero dal click)
p_rampa = 0.80 / 12.00 * 100.0     # = 6.6667 %

print("--- RAMPA RP-01 ---")
verdetto(p_rampa, 8.0, e_minimo=False)      # massimo di legge
if p_rampa > 5.0:
    print("NOTA: sopra il 5% preferibile (conforme ma faticosa)")
