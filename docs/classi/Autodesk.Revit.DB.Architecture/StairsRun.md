---
title: StairsRun
classe: Autodesk.Revit.DB.Architecture.StairsRun
namespace: Autodesk.Revit.DB.Architecture
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 26
---

# StairsRun

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 ActualRisersNumber { get; }` | `stairsRun.ActualRisersNumber` | Int32 |
| `Double ActualRunWidth { get; set; }` | `stairsRun.ActualRunWidth` | Double |
| `Int32 ActualTreadsNumber { get; }` | `stairsRun.ActualTreadsNumber` | Int32 |
| `Double BaseElevation { get; set; }` | `stairsRun.BaseElevation` | Double |
| `Boolean BeginsWithRiser { get; set; }` | `stairsRun.BeginsWithRiser` | Boolean |
| `Boolean EndsWithRiser { get; set; }` | `stairsRun.EndsWithRiser` | Boolean |
| `Double ExtensionBelowRiserBase { get; set; }` | `stairsRun.ExtensionBelowRiserBase` | Double |
| `Double ExtensionBelowTreadBase { get; set; }` | `stairsRun.ExtensionBelowTreadBase` | Double |
| `Double Height { get; }` | `stairsRun.Height` | Double |
| `StairsRunJustification LocationLineJustification { get; set; }` | `stairsRun.LocationLineJustification` | StairsRunJustification |
| `StairsRunStyle StairsRunStyle { get; }` | `stairsRun.StairsRunStyle` | StairsRunStyle |
| `Double TopElevation { get; set; }` | `stairsRun.TopElevation` | Double |
| `StairsRun CreateSketchedRun(Document, ElementId, Double, IList<Curve>, IList<Curve>, IList<Curve>)` | `StairsRun.CreateSketchedRun(document, stairsId, baseElevation, boundaryCurves, riserCurves, stairsPath)` | StairsRun |
| `StairsRun CreateSketchedRunWithSlopeData(Document, ElementId, Double, IList<SketchedStairsCurveData>, IList<Curve>, IList<Curve>)` | `StairsRun.CreateSketchedRunWithSlopeData(document, stairsId, baseElevation, boundaryCurves, riserCurves, stairsPath)` | StairsRun |
| `StairsRun CreateSpiralRun(Document, ElementId, XYZ, Double, Double, Double, Boolean, StairsRunJustification)` | `StairsRun.CreateSpiralRun(document, stairsId, center, radius, startAngle, includedAngle, clockwise, justification)` | StairsRun |
| `StairsRun CreateStraightRun(Document, ElementId, Line, StairsRunJustification)` | `StairsRun.CreateStraightRun(document, stairsId, locationPath, justification)` | StairsRun |
| `IList<ElementId> GetAllSupports()` | `stairsRun.GetAllSupports()` | IList<ElementId> |
| `IList<StairsComponentConnection> GetConnections()` | `stairsRun.GetConnections()` | IList<StairsComponentConnection> |
| `CurveLoop GetFootprintBoundary()` | `stairsRun.GetFootprintBoundary()` | CurveLoop |
| `IList<ElementId> GetLeftSupports()` | `stairsRun.GetLeftSupports()` | IList<ElementId> |
| `Reference GetNumberSystemReference(StairsNumberSystemReferenceOption)` | `stairsRun.GetNumberSystemReference(referenceOption)` | Reference |
| `IList<ElementId> GetRightSupports()` | `stairsRun.GetRightSupports()` | IList<ElementId> |
| `Stairs GetStairs()` | `stairsRun.GetStairs()` | Stairs |
| `CurveLoop GetStairsPath()` | `stairsRun.GetStairsPath()` | CurveLoop |
| `Boolean SetLocationPathForSpiralRun(StairsRun, XYZ, Double, Double, Double, Boolean, StairsRunJustification)` | `StairsRun.SetLocationPathForSpiralRun(stairsRun, center, radius, startAngle, includedAngle, clockwise, justification)` | Boolean |
| `Boolean SetLocationPathForStraightRun(StairsRun, Line)` | `StairsRun.SetLocationPathForStraightRun(stairsRun, locationPath)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
