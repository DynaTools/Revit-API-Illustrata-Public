---
title: ViewCropRegionShapeManager
classe: Autodesk.Revit.DB.ViewCropRegionShapeManager
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 26
---

# ViewCropRegionShapeManager

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double BottomAnnotationCropOffset { get; set; }` | `viewCropRegionShapeManager.BottomAnnotationCropOffset` | Double |
| `Boolean CanBeSplit { get; }` | `viewCropRegionShapeManager.CanBeSplit` | Boolean |
| `Boolean CanHaveAnnotationCrop { get; }` | `viewCropRegionShapeManager.CanHaveAnnotationCrop` | Boolean |
| `Boolean CanHaveShape { get; }` | `viewCropRegionShapeManager.CanHaveShape` | Boolean |
| `Boolean IsSplitHorizontally { get; }` | `viewCropRegionShapeManager.IsSplitHorizontally` | Boolean |
| `Boolean IsSplitVertically { get; }` | `viewCropRegionShapeManager.IsSplitVertically` | Boolean |
| `Boolean IsValidObject { get; }` | `viewCropRegionShapeManager.IsValidObject` | Boolean |
| `Double LeftAnnotationCropOffset { get; set; }` | `viewCropRegionShapeManager.LeftAnnotationCropOffset` | Double |
| `Int32 NumberOfSplitRegions { get; }` | `viewCropRegionShapeManager.NumberOfSplitRegions` | Int32 |
| `Double RightAnnotationCropOffset { get; set; }` | `viewCropRegionShapeManager.RightAnnotationCropOffset` | Double |
| `Boolean ShapeSet { get; }` | `viewCropRegionShapeManager.ShapeSet` | Boolean |
| `Boolean Split { get; }` | `viewCropRegionShapeManager.Split` | Boolean |
| `Double TopAnnotationCropOffset { get; set; }` | `viewCropRegionShapeManager.TopAnnotationCropOffset` | Double |
| `Void Dispose()` | `viewCropRegionShapeManager.Dispose()` | Void |
| `CurveLoop GetAnnotationCropShape()` | `viewCropRegionShapeManager.GetAnnotationCropShape()` | CurveLoop |
| `IList<CurveLoop> GetCropShape()` | `viewCropRegionShapeManager.GetCropShape()` | IList<CurveLoop> |
| `Double GetSplitRegionMaximum(Int32)` | `viewCropRegionShapeManager.GetSplitRegionMaximum(regionIndex)` | Double |
| `Double GetSplitRegionMinimum(Int32)` | `viewCropRegionShapeManager.GetSplitRegionMinimum(regionIndex)` | Double |
| `XYZ GetSplitRegionOffset(Int32)` | `viewCropRegionShapeManager.GetSplitRegionOffset(regionIndex)` | XYZ |
| `Boolean IsCropRegionShapeValid(CurveLoop)` | `viewCropRegionShapeManager.IsCropRegionShapeValid(boundary)` | Boolean |
| `Void RemoveCropRegionShape()` | `viewCropRegionShapeManager.RemoveCropRegionShape()` | Void |
| `Void RemoveSplit()` | `viewCropRegionShapeManager.RemoveSplit()` | Void |
| `Void RemoveSplitRegion(Int32)` | `viewCropRegionShapeManager.RemoveSplitRegion(regionIndex)` | Void |
| `Void SetCropShape(CurveLoop)` | `viewCropRegionShapeManager.SetCropShape(boundary)` | Void |
| `Void SplitRegionHorizontally(Int32, Double, Double)` | `viewCropRegionShapeManager.SplitRegionHorizontally(regionIndex, leftPart, rightPart)` | Void |
| `Void SplitRegionVertically(Int32, Double, Double)` | `viewCropRegionShapeManager.SplitRegionVertically(regionIndex, topPart, bottomPart)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
