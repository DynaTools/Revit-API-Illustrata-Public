---
title: RevolvedSurface
classe: Autodesk.Revit.DB.RevolvedSurface
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Surface
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 12
---

# RevolvedSurface

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ Axis { get; }` | `revolvedSurface.Axis` | XYZ |
| `XYZ Origin { get; }` | `revolvedSurface.Origin` | XYZ |
| `XYZ XDir { get; }` | `revolvedSurface.XDir` | XYZ |
| `XYZ YDir { get; }` | `revolvedSurface.YDir` | XYZ |
| `Surface Create(Frame, Curve, Double, Double)` | `RevolvedSurface.Create(frameOfReference, profileCurve, startAngle, endAngle)` | Surface |
| `Surface Create(Frame, Curve)` | `RevolvedSurface.Create(frameOfReference, profileCurve)` | Surface |
| `Surface Create(XYZ, XYZ, Curve, Double, Double)` | `RevolvedSurface.Create(axisBasePoint, axisDirection, profileCurve, startAngle, endAngle)` | Surface |
| `Surface Create(XYZ, XYZ, Curve)` | `RevolvedSurface.Create(axisBasePoint, axisDirection, profileCurve)` | Surface |
| `Curve GetProfileCurve()` | `revolvedSurface.GetProfileCurve()` | Curve |
| `Curve GetProfileCurveInWorldCoordinates()` | `revolvedSurface.GetProfileCurveInWorldCoordinates()` | Curve |
| `Boolean IsValidProfileCurve(Frame, Curve)` | `RevolvedSurface.IsValidProfileCurve(frameOfReference, profileCurve)` | Boolean |
| `Boolean IsValidProfileCurve(XYZ, XYZ, Curve)` | `RevolvedSurface.IsValidProfileCurve(axisBasePoint, axisDirection, profileCurve)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
