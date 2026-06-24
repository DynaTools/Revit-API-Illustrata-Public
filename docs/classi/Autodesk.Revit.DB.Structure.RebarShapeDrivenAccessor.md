---
title: RebarShapeDrivenAccessor
classe: Autodesk.Revit.DB.Structure.RebarShapeDrivenAccessor
namespace: Autodesk.Revit.DB.Structure
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 23
---

# RebarShapeDrivenAccessor

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double ArrayLength { get; set; }` | `rebarShapeDrivenAccessor.ArrayLength` | Double |
| `Boolean BarsOnNormalSide { get; set; }` | `rebarShapeDrivenAccessor.BarsOnNormalSide` | Boolean |
| `Int32 BaseFinishingTurns { get; set; }` | `rebarShapeDrivenAccessor.BaseFinishingTurns` | Int32 |
| `Double Height { get; set; }` | `rebarShapeDrivenAccessor.Height` | Double |
| `Boolean IsValidObject { get; }` | `rebarShapeDrivenAccessor.IsValidObject` | Boolean |
| `Double MultiplanarDepth { get; set; }` | `rebarShapeDrivenAccessor.MultiplanarDepth` | Double |
| `XYZ Normal { get; }` | `rebarShapeDrivenAccessor.Normal` | XYZ |
| `Double Pitch { get; set; }` | `rebarShapeDrivenAccessor.Pitch` | Double |
| `Int32 TopFinishingTurns { get; set; }` | `rebarShapeDrivenAccessor.TopFinishingTurns` | Int32 |
| `Boolean UseRebarConstraintsToProduceVaryingBars { get; set; }` | `rebarShapeDrivenAccessor.UseRebarConstraintsToProduceVaryingBars` | Boolean |
| `IList<Curve> ComputeDrivingCurves()` | `rebarShapeDrivenAccessor.ComputeDrivingCurves()` | IList<Curve> |
| `Void Dispose()` | `rebarShapeDrivenAccessor.Dispose()` | Void |
| `Void FlipRebarSet()` | `rebarShapeDrivenAccessor.FlipRebarSet()` | Void |
| `Transform GetBarPositionTransform(Int32)` | `rebarShapeDrivenAccessor.GetBarPositionTransform(barPositionIndex)` | Transform |
| `Line GetDistributionPath()` | `rebarShapeDrivenAccessor.GetDistributionPath()` | Line |
| `Void ScaleToBox(XYZ, XYZ, XYZ)` | `rebarShapeDrivenAccessor.ScaleToBox(origin, xVec, yVec)` | Void |
| `Void ScaleToBoxFor3D(XYZ, XYZ, XYZ, Double)` | `rebarShapeDrivenAccessor.ScaleToBoxFor3D(origin, xVec, yVec, height)` | Void |
| `Void SetLayoutAsFixedNumber(Int32, Double, Boolean, Boolean, Boolean)` | `rebarShapeDrivenAccessor.SetLayoutAsFixedNumber(numberOfBarPositions, arrayLength, barsOnNormalSide, includeFirstBar, includeLastBar)` | Void |
| `Void SetLayoutAsMaximumSpacing(Double, Double, Boolean, Boolean, Boolean)` | `rebarShapeDrivenAccessor.SetLayoutAsMaximumSpacing(spacing, arrayLength, barsOnNormalSide, includeFirstBar, includeLastBar)` | Void |
| `Void SetLayoutAsMinimumClearSpacing(Double, Double, Boolean, Boolean, Boolean)` | `rebarShapeDrivenAccessor.SetLayoutAsMinimumClearSpacing(spacing, arrayLength, barsOnNormalSide, includeFirstBar, includeLastBar)` | Void |
| `Void SetLayoutAsNumberWithSpacing(Int32, Double, Boolean, Boolean, Boolean)` | `rebarShapeDrivenAccessor.SetLayoutAsNumberWithSpacing(numberOfBarPositions, spacing, barsOnNormalSide, includeFirstBar, includeLastBar)` | Void |
| `Void SetLayoutAsSingle()` | `rebarShapeDrivenAccessor.SetLayoutAsSingle()` | Void |
| `Void SetRebarShapeId(ElementId)` | `rebarShapeDrivenAccessor.SetRebarShapeId(shapeId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
