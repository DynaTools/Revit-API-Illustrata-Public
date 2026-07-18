# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.9.1  |  Capitolo 7.9 - La pressione dell'acqua fredda in bagno
# Sezione: Passi 1--2 - leggere le quote dal modello

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

FT_M = 0.3048                 # 1 piede = 0.3048 m

uidoc = __revit__.ActiveUIDocument
doc   = uidoc.Document

# Quota del pelo libero del serbatoio (dato di progetto, in metri)
Z_SERBATOIO = 9.60

# Perdite di carico stimate dal serbatoio al bagno (mca):
#   - lungo la colonna e la distribuzione orizzontale
PERDITA_DISTRIB = 3.0     # mca
#   - nel breve stacco verso ogni apparecchio
PERDITA_STACCO  = 1.0     # mca

# 50 kPa ~ 5.1 mca per tutti gli apparecchi domestici (UNI 9182)
P_MIN = 50.0 / 9.81       # 50 kPa convertiti in mca -> ~5.10 mca

# Leggi dal modello gli apparecchi del bagno e la loro quota d'uso:
# la quota d'uso e' la Z del punto d'inserimento (Location.Point), in piedi.
quote = {}
sanitari = FilteredElementCollector(doc)\
    .OfCategory(BuiltInCategory.OST_PlumbingFixtures)\
    .WhereElementIsNotElementType()
for el in sanitari:
    quote[el.Name] = el.Location.Point.Z * FT_M   # quota d'uso in metri

# Apparecchi del bagno: (nome, quota d'uso in m, pressione minima in mca)
apparecchi = [
    ("Lavabo (rubinetto)", quote["Lavabo (rubinetto)"], P_MIN),
    ("Vaso (cassetta)",    quote["Vaso (cassetta)"],    P_MIN),
    ("Bidet",              quote["Bidet"],              P_MIN),
    ("Doccia (soffione)",  quote["Doccia (soffione)"],  P_MIN),
]

print("Pelo libero serbatoio: {:.2f} m".format(Z_SERBATOIO))
print("Pressione minima richiesta: {:.2f} mca (50 kPa)".format(P_MIN))
print("Apparecchi nel bagno: {}".format(len(apparecchi)))
