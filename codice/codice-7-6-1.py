# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.6.1  |  Capitolo 7.6 - La copertura Wi-Fi
# Sezione: Passi 1--2 - l'antenna e i muri sul raggio

import math
from Autodesk.Revit.DB import (FilteredElementCollector, BuiltInCategory,
    XYZ, View3D, ReferenceIntersector, FindReferenceTarget)

FT_M = 0.3048                       # 1 piede = 0.3048 m

doc = __revit__.ActiveUIDocument.Document

# tabella materiale -> attenuazione (dB) a 2.4 GHz
ATT = {"cartongesso": 3.0, "vetro": 2.0, "mattone": 6.0, "cemento": 12.0}

# PASSO 1: individua l'access point e prepara il ray caster
ap = (FilteredElementCollector(doc)
      .OfCategory(BuiltInCategory.OST_CommunicationDevices)
      .WhereElementIsNotElementType()
      .FirstElement())

origine = ap.Location.Point          # posizione dell'antenna (piedi)

vista3d = (FilteredElementCollector(doc).OfClass(View3D)
           .WhereElementIsNotElementType().FirstElement())
caster = ReferenceIntersector(vista3d)
caster.TargetType = FindReferenceTarget.Element

# PASSO 2: conta i muri attraversati dal raggio AP -> punto
def attenuazione_ostacoli(ap_pt, p, caster, tabella):
    direzione = (p - ap_pt).Normalize()
    colpiti = caster.Find(ap_pt, direzione)
    dmax = ap_pt.DistanceTo(p)        # non guardare oltre il punto
    perdita = 0.0
    for ref in colpiti:
        if ref.Proximity > dmax:
            continue
        muro = doc.GetElement(ref.GetReference())
        nome = (muro.Name or "").lower()
        for chiave, db in tabella.items():
            if chiave in nome:
                perdita += db
                break
    return perdita

print("Access point: {}".format(ap.Name))
print("Posizione AP: ({:.2f}, {:.2f}, {:.2f}) m".format(
    origine.X*FT_M, origine.Y*FT_M, origine.Z*FT_M))
