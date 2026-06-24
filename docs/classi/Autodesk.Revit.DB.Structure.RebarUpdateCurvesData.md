---
title: RebarUpdateCurvesData
classe: Autodesk.Revit.DB.Structure.RebarUpdateCurvesData
namespace: Autodesk.Revit.DB.Structure
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 42
---

# RebarUpdateCurvesData

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `AlignedFreeFormSetOrientationOptions AlignedFreeFormSetOrientationOptions { get; }` | `rebarUpdateCurvesData.AlignedFreeFormSetOrientationOptions` | AlignedFreeFormSetOrientationOptions |
| `Boolean AreOrientationOptionsChanged { get; }` | `rebarUpdateCurvesData.AreOrientationOptionsChanged` | Boolean |
| `Boolean AreWorkshopInstructionsChanged { get; }` | `rebarUpdateCurvesData.AreWorkshopInstructionsChanged` | Boolean |
| `Boolean CycleCounterChanged { get; }` | `rebarUpdateCurvesData.CycleCounterChanged` | Boolean |
| `String ErrorMessage { get; set; }` | `rebarUpdateCurvesData.ErrorMessage` | String |
| `Boolean HostMirrored { get; set; }` | `rebarUpdateCurvesData.HostMirrored` | Boolean |
| `Boolean IsAttachmentTypeChanged { get; }` | `rebarUpdateCurvesData.IsAttachmentTypeChanged` | Boolean |
| `Boolean IsBarsNumberChanged { get; }` | `rebarUpdateCurvesData.IsBarsNumberChanged` | Boolean |
| `Boolean IsBendingRadiusChanged { get; }` | `rebarUpdateCurvesData.IsBendingRadiusChanged` | Boolean |
| `Boolean IsEndConstraintChanged { get; }` | `rebarUpdateCurvesData.IsEndConstraintChanged` | Boolean |
| `Boolean IsLayoutChanged { get; }` | `rebarUpdateCurvesData.IsLayoutChanged` | Boolean |
| `Boolean IsReversed { get; set; }` | `rebarUpdateCurvesData.IsReversed` | Boolean |
| `Boolean IsSpacingChanged { get; }` | `rebarUpdateCurvesData.IsSpacingChanged` | Boolean |
| `Boolean IsStartConstraintChanged { get; }` | `rebarUpdateCurvesData.IsStartConstraintChanged` | Boolean |
| `Boolean IsStyleChanged { get; }` | `rebarUpdateCurvesData.IsStyleChanged` | Boolean |
| `Boolean IsValidObject { get; }` | `rebarUpdateCurvesData.IsValidObject` | Boolean |
| `Double Spacing { get; }` | `rebarUpdateCurvesData.Spacing` | Double |
| `RebarWorkInstructions WorkshopInstructions { get; }` | `rebarUpdateCurvesData.WorkshopInstructions` | RebarWorkInstructions |
| `Void Dispose()` | `rebarUpdateCurvesData.Dispose()` | Void |
| `StirrupTieAttachmentType GetAttachmentType()` | `rebarUpdateCurvesData.GetAttachmentType()` | StirrupTieAttachmentType |
| `IList<Curve> GetBarGeometry(Int32)` | `rebarUpdateCurvesData.GetBarGeometry(barIndex)` | IList<Curve> |
| `Double GetBarModelDiameter()` | `rebarUpdateCurvesData.GetBarModelDiameter()` | Double |
| `Double GetBarNominalDiameter()` | `rebarUpdateCurvesData.GetBarNominalDiameter()` | Double |
| `Int32 GetBarsNumber()` | `rebarUpdateCurvesData.GetBarsNumber()` | Int32 |
| `Double GetBendingRadius()` | `rebarUpdateCurvesData.GetBendingRadius()` | Double |
| `IList<Int32> GetChangedCustomHandles()` | `rebarUpdateCurvesData.GetChangedCustomHandles()` | IList<Int32> |
| `IList<Guid> GetChangedSharedParameterGUIDs()` | `rebarUpdateCurvesData.GetChangedSharedParameterGUIDs()` | IList<Guid> |
| `IList<RebarConstraint> GetCustomConstraints()` | `rebarUpdateCurvesData.GetCustomConstraints()` | IList<RebarConstraint> |
| `Int32 GetCycleCounter()` | `rebarUpdateCurvesData.GetCycleCounter()` | Int32 |
| `Document GetDocument()` | `rebarUpdateCurvesData.GetDocument()` | Document |
| `RebarConstraint GetEndConstraint()` | `rebarUpdateCurvesData.GetEndConstraint()` | RebarConstraint |
| `Double GetHookOrientationAngle(Int32)` | `rebarUpdateCurvesData.GetHookOrientationAngle(end)` | Double |
| `XYZ GetHookPlaneNormalForBarIdx(Int32, Int32)` | `rebarUpdateCurvesData.GetHookPlaneNormalForBarIdx(end, barPositionIndex)` | XYZ |
| `ElementId GetHostId()` | `rebarUpdateCurvesData.GetHostId()` | ElementId |
| `RebarLayoutRule GetLayoutRule()` | `rebarUpdateCurvesData.GetLayoutRule()` | RebarLayoutRule |
| `Int32 GetNumberOfBars()` | `rebarUpdateCurvesData.GetNumberOfBars()` | Int32 |
| `ElementId GetRebarId()` | `rebarUpdateCurvesData.GetRebarId()` | ElementId |
| `RebarStyle GetRebarStyle()` | `rebarUpdateCurvesData.GetRebarStyle()` | RebarStyle |
| `RebarConstraint GetStartConstraint()` | `rebarUpdateCurvesData.GetStartConstraint()` | RebarConstraint |
| `Void SetCycleCounter(Int32)` | `rebarUpdateCurvesData.SetCycleCounter(cycleCounter)` | Void |
| `Void SetHookOrientationAngle(Int32, Double)` | `rebarUpdateCurvesData.SetHookOrientationAngle(end, angle)` | Void |
| `Void SetHookPlaneNormalForBarIdx(Int32, Int32, XYZ)` | `rebarUpdateCurvesData.SetHookPlaneNormalForBarIdx(end, barPositionIndex, hookNormal)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
