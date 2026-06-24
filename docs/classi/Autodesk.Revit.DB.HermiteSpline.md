---
title: HermiteSpline
classe: Autodesk.Revit.DB.HermiteSpline
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Curve
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 6
---

# HermiteSpline

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `IList<XYZ> ControlPoints { get; set; }` | `hermiteSpline.ControlPoints` | IList<XYZ> |
| `Boolean IsPeriodic { get; }` | `hermiteSpline.IsPeriodic` | Boolean |
| `DoubleArray Parameters { get; }` | `hermiteSpline.Parameters` | DoubleArray |
| `IList<XYZ> Tangents { get; }` | `hermiteSpline.Tangents` | IList<XYZ> |
| `HermiteSpline Create(IList<XYZ>, Boolean, HermiteSplineTangents)` | `HermiteSpline.Create(controlPoints, periodic, tangents)` | HermiteSpline |
| `HermiteSpline Create(IList<XYZ>, Boolean)` | `HermiteSpline.Create(controlPoints, periodic)` | HermiteSpline |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
