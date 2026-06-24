---
title: NurbSpline
classe: Autodesk.Revit.DB.NurbSpline
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Curve
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# NurbSpline

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `IList<XYZ> CtrlPoints { get; }` | `nurbSpline.CtrlPoints` | IList<XYZ> |
| `Int32 Degree { get; }` | `nurbSpline.Degree` | Int32 |
| `Boolean isRational { get; }` | `nurbSpline.isRational` | Boolean |
| `DoubleArray Knots { get; set; }` | `nurbSpline.Knots` | DoubleArray |
| `DoubleArray Weights { get; }` | `nurbSpline.Weights` | DoubleArray |
| `NurbSpline Create(HermiteSpline)` | `NurbSpline.Create(hermiteSpline)` | NurbSpline |
| `Curve CreateCurve(HermiteSpline)` | `NurbSpline.CreateCurve(hermiteSpline)` | Curve |
| `Curve CreateCurve(IList<XYZ>, IList<Double>)` | `NurbSpline.CreateCurve(controlPoints, weights)` | Curve |
| `Curve CreateCurve(Int32, IList<Double>, IList<XYZ>, IList<Double>)` | `NurbSpline.CreateCurve(degree, knots, controlPoints, weights)` | Curve |
| `Curve CreateCurve(Int32, IList<Double>, IList<XYZ>)` | `NurbSpline.CreateCurve(degree, knots, controlPoints)` | Curve |
| `Void SetControlPointsAndWeights(IList<XYZ>, DoubleArray)` | `nurbSpline.SetControlPointsAndWeights(ctrlPoints, weights)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
