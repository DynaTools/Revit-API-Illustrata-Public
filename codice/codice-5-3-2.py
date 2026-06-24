# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 5.3.2  |  Capitolo 5.3 - Progetto finale: uno strumento da cima a fondo
# Sezione: La finestra di input

from pyrevit import forms

resposta = forms.ask_for_string(
    default="300",
    prompt="Diametro minimo (mm):",
    title="Evidenzia Canali")

if not resposta:                       # l'utente ha annullato: uscita pulita
    import sys; sys.exit()

try:
    limite_mm = float(resposta)
except ValueError:                     # "trecento" non vale
    forms.alert("Inserisci un numero valido.", exitscript=True)
