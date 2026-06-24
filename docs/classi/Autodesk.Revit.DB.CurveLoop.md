---
title: CurveLoop
classe: Autodesk.Revit.DB.CurveLoop
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 23
---

# CurveLoop

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `curveLoop.IsValidObject` | Boolean |
| `Void Append(Curve)` | `curveLoop.Append(curve)` | Void |
| `CurveLoop Create(IList<Curve>)` | `CurveLoop.Create(curves)` | CurveLoop |
| `CurveLoop CreateViaCopy(CurveLoop)` | `CurveLoop.CreateViaCopy(original)` | CurveLoop |
| `CurveLoop CreateViaOffset(CurveLoop, IList<Double>, XYZ)` | `CurveLoop.CreateViaOffset(original, offsetDists, normal)` | CurveLoop |
| `CurveLoop CreateViaOffset(CurveLoop, Double, XYZ)` | `CurveLoop.CreateViaOffset(original, offsetDist, normal)` | CurveLoop |
| `CurveLoop CreateViaThicken(CurveLoop, Double, XYZ)` | `CurveLoop.CreateViaThicken(curveLoop, thickness, normal)` | CurveLoop |
| `CurveLoop CreateViaThicken(Curve, Double, XYZ)` | `CurveLoop.CreateViaThicken(pCurve, thickness, normal)` | CurveLoop |
| `CurveLoop CreateViaTransform(CurveLoop, Transform)` | `CurveLoop.CreateViaTransform(curveLoop, transform)` | CurveLoop |
| `Void Dispose()` | `curveLoop.Dispose()` | Void |
| `Void Flip()` | `curveLoop.Flip()` | Void |
| `CurveLoopIterator GetCurveLoopIterator()` | `curveLoop.GetCurveLoopIterator()` | CurveLoopIterator |
| `IEnumerator<Curve> GetEnumerator()` | `curveLoop.GetEnumerator()` | IEnumerator<Curve> |
| `Double GetExactLength()` | `curveLoop.GetExactLength()` | Double |
| `Plane GetPlane()` | `curveLoop.GetPlane()` | Plane |
| `Double GetRectangularHeight(Plane)` | `curveLoop.GetRectangularHeight(plane)` | Double |
| `Double GetRectangularWidth(Plane)` | `curveLoop.GetRectangularWidth(plane)` | Double |
| `Boolean HasPlane()` | `curveLoop.HasPlane()` | Boolean |
| `Boolean IsCounterclockwise(XYZ)` | `curveLoop.IsCounterclockwise(normal)` | Boolean |
| `Boolean IsOpen()` | `curveLoop.IsOpen()` | Boolean |
| `Boolean IsRectangular(Plane)` | `curveLoop.IsRectangular(plane)` | Boolean |
| `Int32 NumberOfCurves()` | `curveLoop.NumberOfCurves()` | Int32 |
| `Void Transform(Transform)` | `curveLoop.Transform(transform)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
