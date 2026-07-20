# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 5.1.4  |  Capitolo 5.1 - pyRevit, pulsanti e distribuzione
# Sezione: Chiedere all'utente, una finestra in XAML

from pyrevit import forms


class Finestra(forms.WPFWindow):
    def __init__(self):
        # carica il .xaml che sta accanto allo script
        forms.WPFWindow.__init__(self, "Finestra.xaml")
        self.risposta = None

    # metodo agganciato a  Click="ok_click"  nel XAML
    def ok_click(self, sender, args):
        # self.valore = la TextBox  x:Name="valore"
        self.risposta = float(self.valore.Text)
        self.Close()


f = Finestra()
f.show_dialog()              # apre la finestra e aspetta
if f.risposta is not None:
    forms.alert("Interasse: {} m".format(f.risposta))
