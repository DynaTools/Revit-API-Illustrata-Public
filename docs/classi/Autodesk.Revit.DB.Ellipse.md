---
title: Ellipse
classe: Autodesk.Revit.DB.Ellipse
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Curve
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# Ellipse

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ Center { get; }` | `ellipse.Center` | XYZ |
| `XYZ Normal { get; }` | `ellipse.Normal` | XYZ |
| `Double RadiusX { get; }` | `ellipse.RadiusX` | Double |
| `Double RadiusY { get; }` | `ellipse.RadiusY` | Double |
| `XYZ XDirection { get; }` | `ellipse.XDirection` | XYZ |
| `XYZ YDirection { get; }` | `ellipse.YDirection` | XYZ |
| `Curve CreateCurve(XYZ, Double, Double, XYZ, XYZ, Double, Double)` | `Ellipse.CreateCurve(center, xRadius, yRadius, xAxis, yAxis, startParameter, endParameter)` | Curve |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
