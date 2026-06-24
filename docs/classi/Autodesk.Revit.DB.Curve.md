---
title: Curve
classe: Autodesk.Revit.DB.Curve
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.GeometryObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 29
---

# Curve

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double ApproximateLength { get; }` | `curve.ApproximateLength` | Double |
| `Boolean IsBound { get; }` | `curve.IsBound` | Boolean |
| `Boolean IsClosed { get; }` | `curve.IsClosed` | Boolean |
| `Boolean IsCyclic { get; }` | `curve.IsCyclic` | Boolean |
| `Double Length { get; }` | `curve.Length` | Double |
| `Double Period { get; }` | `curve.Period` | Double |
| `Reference Reference { get; }` | `curve.Reference` | Reference |
| `Curve Clone()` | `curve.Clone()` | Curve |
| `Void ComputeClosestPoints(Curve, Boolean, Boolean, Boolean, IList<ClosestPointsPairBetweenTwoCurves>&)` | `curve.ComputeClosestPoints(otherCurve, withinThisCurveBounds, withinOtherCurveBounds, returnAllCriticalPnts, resultList)` | Void |
| `Transform ComputeDerivatives(Double, Boolean)` | `curve.ComputeDerivatives(parameter, normalized)` | Transform |
| `Double ComputeNormalizedParameter(Double)` | `curve.ComputeNormalizedParameter(rawParameter)` | Double |
| `Double ComputeRawParameter(Double)` | `curve.ComputeRawParameter(normalizedParameter)` | Double |
| `Curve CreateOffset(Double, XYZ)` | `curve.CreateOffset(offsetDist, referenceVector)` | Curve |
| `Curve CreateReversed()` | `curve.CreateReversed()` | Curve |
| `Curve CreateTransformed(Transform)` | `curve.CreateTransformed(transform)` | Curve |
| `Double Distance(XYZ)` | `curve.Distance(point)` | Double |
| `XYZ Evaluate(Double, Boolean)` | `curve.Evaluate(parameter, normalized)` | XYZ |
| `Double GetEndParameter(Int32)` | `curve.GetEndParameter(index)` | Double |
| `XYZ GetEndPoint(Int32)` | `curve.GetEndPoint(index)` | XYZ |
| `Reference GetEndPointReference(Int32)` | `curve.GetEndPointReference(index)` | Reference |
| `SetComparisonResult Intersect(Curve, IntersectionResultArray&)` | `curve.Intersect(curve, resultArray)` | SetComparisonResult |
| `SetComparisonResult Intersect(Curve)` | `curve.Intersect(curve)` | SetComparisonResult |
| `Boolean IsInside(Double, Int32&)` | `curve.IsInside(parameter, end)` | Boolean |
| `Boolean IsInside(Double)` | `curve.IsInside(parameter)` | Boolean |
| `Void MakeBound(Double, Double)` | `curve.MakeBound(startParameter, endParameter)` | Void |
| `Void MakeUnbound()` | `curve.MakeUnbound()` | Void |
| `IntersectionResult Project(XYZ)` | `curve.Project(point)` | IntersectionResult |
| `Void SetGraphicsStyleId(ElementId)` | `curve.SetGraphicsStyleId(id)` | Void |
| `IList<XYZ> Tessellate()` | `curve.Tessellate()` | IList<XYZ> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
