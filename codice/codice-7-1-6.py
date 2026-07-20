# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.1.6  |  Capitolo 7.1 - Lo staffaggio
# Sezione: In pyRevit - il pulsante "Staffaggio"

# ============================================================
# 0. PREPARAZIONE                             [PY] + [REVIT]
# ============================================================
import math
from pyrevit import revit, forms, script
from Autodesk.Revit.UI.Selection import ObjectType
from Autodesk.Revit.DB import (FilteredElementCollector,
    FillPatternElement, OverrideGraphicSettings, Color)
from System.Windows.Controls import (StackPanel, TextBlock,
    TextBox, Orientation)

doc, uidoc = revit.doc, revit.uidoc
out  = script.get_output()
FT_M = 0.3048

# ============================================================
# 1. CATALOGO DEI CAVI E SOGLIE                        [ENG]
# ============================================================
CAVI = [("FG16OR16 3G1.5", 0.12),
        ("FG16OR16 3G2.5", 0.18),
        ("FG16OR16 5G2.5", 0.28),
        ("FG16OR16 3G4",   0.26),
        ("FG16OR16 5G6",   0.55),
        ("FG16OR16 3G10",  0.62),
        ("FG16OR16 4G16",  1.10),
        ("FG16OR16 5G16",  1.35),
        ("FG16OR16 3G50",  2.10),
        ("FG16OR16 4G95",  4.10)]
PESO_PASSERELLA = 5.00      # kg/m, catalogo
INTERASSE       = 1.50      # m, passo di progetto
P_MENSOLA       = 152.9     # kg eq. (1500 N / 9,81)
CAMPATA_MAX     = 2.00      # m, campata massima

# ============================================================
# 2. LA FINESTRA, una riga per cavo           [PY] + [REVIT]
# ============================================================
class Staffaggio(forms.WPFWindow):
    def __init__(self):
        forms.WPFWindow.__init__(
            self, "StaffaggioWindow.xaml")
        self.caselle = {}
        for nome, _peso in CAVI:
            riga = StackPanel(
                Orientation=Orientation.Horizontal)
            riga.Children.Add(
                TextBlock(Text=nome, Width=150))
            box = TextBox(Text="0", Width=60)
            riga.Children.Add(box)
            self.righe.Children.Add(riga)
            self.caselle[nome] = box
        self.quantita = None

    def verifica_click(self, sender, args):
        self.quantita = {
            n: int(b.Text)
            for n, b in self.caselle.items()
            if b.Text.isdigit() and int(b.Text) > 0}
        self.Close()

# ============================================================
# 3. IL CLIC, LA FINESTRA E IL CONTO          [REVIT]+[ENG]
# ============================================================
ref  = uidoc.Selection.PickObject(
    ObjectType.Element, "Seleziona la passerella")
tray = doc.GetElement(ref.ElementId)
L    = tray.Location.Curve.Length * FT_M

f = Staffaggio()
f.show_dialog()               # apre e aspetta l'utente
if not f.quantita:
    script.exit()             # nessun cavo: si esce

pesi = dict(CAVI)
w = PESO_PASSERELLA + sum(pesi[n] * q
                         for n, q in f.quantita.items())
F     = w * INTERASSE
i_max = min(P_MENSOLA / w, CAMPATA_MAX)
N     = int(math.ceil(L / INTERASSE)) + 1
ok    = (F <= P_MENSOLA) and (INTERASSE <= i_max)

# ============================================================
# 4. VERDE O ROSSO SUL MODELLO                [REVIT]+[OUT]
# ============================================================
solido = next(fp for fp in FilteredElementCollector(doc)
              .OfClass(FillPatternElement)
              if fp.GetFillPattern().IsSolidFill)
tinta = Color(0, 158, 61) if ok else Color(207, 0, 0)
ogs = OverrideGraphicSettings()
ogs.SetSurfaceForegroundPatternId(solido.Id)
ogs.SetSurfaceForegroundPatternColor(tinta)
ogs.SetProjectionLineColor(tinta)

with revit.Transaction("Staffaggio"):
    doc.ActiveView.SetElementOverrides(tray.Id, ogs)

esito = "CONFORME" if ok else "NON CONFORME"
out.print_md("### Staffaggio " + out.linkify(tray.Id))
out.print_md("- w **{:.2f} kg/m** - F **{:.1f} kg** "
             "- {} staffe - **{}**".format(w, F, N, esito))
