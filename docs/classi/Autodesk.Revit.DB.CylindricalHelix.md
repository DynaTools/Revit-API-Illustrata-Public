---
title: CylindricalHelix
classe: Autodesk.Revit.DB.CylindricalHelix
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Curve
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# CylindricalHelix

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ BasePoint { get; }` | `cylindricalHelix.BasePoint` | XYZ |
| `Double Height { get; }` | `cylindricalHelix.Height` | Double |
| `Boolean IsRightHanded { get; }` | `cylindricalHelix.IsRightHanded` | Boolean |
| `Double Pitch { get; }` | `cylindricalHelix.Pitch` | Double |
| `Double Radius { get; }` | `cylindricalHelix.Radius` | Double |
| `XYZ XVector { get; }` | `cylindricalHelix.XVector` | XYZ |
| `XYZ YVector { get; }` | `cylindricalHelix.YVector` | XYZ |
| `XYZ ZVector { get; }` | `cylindricalHelix.ZVector` | XYZ |
| `CylindricalHelix Create(XYZ, Double, XYZ, XYZ, Double, Double, Double)` | `CylindricalHelix.Create(basePoint, radius, xVector, zVector, pitch, startAngle, endAngle)` | CylindricalHelix |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
