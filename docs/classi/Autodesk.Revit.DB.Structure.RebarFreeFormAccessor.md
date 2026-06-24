---
title: RebarFreeFormAccessor
classe: Autodesk.Revit.DB.Structure.RebarFreeFormAccessor
namespace: Autodesk.Revit.DB.Structure
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 36
---

# RebarFreeFormAccessor

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `AlignedFreeFormSetOrientationOptions AlignedFreeFormSetOrientationOptions { get; set; }` | `rebarFreeFormAccessor.AlignedFreeFormSetOrientationOptions` | AlignedFreeFormSetOrientationOptions |
| `Int32 CycleCounter { get; set; }` | `rebarFreeFormAccessor.CycleCounter` | Int32 |
| `Boolean IsValidObject { get; }` | `rebarFreeFormAccessor.IsValidObject` | Boolean |
| `RebarStyle RebarStyle { get; set; }` | `rebarFreeFormAccessor.RebarStyle` | RebarStyle |
| `StirrupTieAttachmentType StirrupTieAttachmentType { get; set; }` | `rebarFreeFormAccessor.StirrupTieAttachmentType` | StirrupTieAttachmentType |
| `RebarWorkInstructions WorkshopInstructions { get; set; }` | `rebarFreeFormAccessor.WorkshopInstructions` | RebarWorkInstructions |
| `Void AddUpdatingSharedParameter(ElementId)` | `rebarFreeFormAccessor.AddUpdatingSharedParameter(parameterId)` | Void |
| `Boolean CanBeHookNormal(Int32, Int32, XYZ)` | `rebarFreeFormAccessor.CanBeHookNormal(barIndex, end, normal)` | Boolean |
| `Void DisconnectFromServer()` | `rebarFreeFormAccessor.DisconnectFromServer()` | Void |
| `Void Dispose()` | `rebarFreeFormAccessor.Dispose()` | Void |
| `ElementId GetCouplerIdAtIndex(Int32, Int32)` | `rebarFreeFormAccessor.GetCouplerIdAtIndex(barPositionIndex, end)` | ElementId |
| `IList<Curve> GetCustomDistributionPath()` | `rebarFreeFormAccessor.GetCustomDistributionPath()` | IList<Curve> |
| `ElementId GetEndTreatmentTypeIdAtIndex(Int32, Int32)` | `rebarFreeFormAccessor.GetEndTreatmentTypeIdAtIndex(barPositionIndex, end)` | ElementId |
| `Double GetHookOrientationAngle(Int32)` | `rebarFreeFormAccessor.GetHookOrientationAngle(end)` | Double |
| `Double GetHookOrientationAngleAtIndex(Int32, Int32)` | `rebarFreeFormAccessor.GetHookOrientationAngleAtIndex(barPositionIndex, end)` | Double |
| `RebarHookOrientation GetHookOrientationAtIndex(Int32, Int32)` | `rebarFreeFormAccessor.GetHookOrientationAtIndex(barPositionIndex, end)` | RebarHookOrientation |
| `XYZ GetHookPlaneNormalForBarIdx(Int32, Int32)` | `rebarFreeFormAccessor.GetHookPlaneNormalForBarIdx(end, barPositionIndex)` | XYZ |
| `ElementId GetHookTypeIdAtIndex(Int32, Int32)` | `rebarFreeFormAccessor.GetHookTypeIdAtIndex(barPositionIndex, end)` | ElementId |
| `Guid GetServerGUID()` | `rebarFreeFormAccessor.GetServerGUID()` | Guid |
| `ElementId GetShapeIdAtIndex(Int32)` | `rebarFreeFormAccessor.GetShapeIdAtIndex(barPositionIndex)` | ElementId |
| `IList<ElementId> GetUpdatingSharedParameters()` | `rebarFreeFormAccessor.GetUpdatingSharedParameters()` | IList<ElementId> |
| `Boolean HasValidAlignedServer()` | `rebarFreeFormAccessor.HasValidAlignedServer()` | Boolean |
| `Boolean HasValidServer()` | `rebarFreeFormAccessor.HasValidServer()` | Boolean |
| `Boolean IsBarMatchedWithShapeInReverseOrder(Int32)` | `rebarFreeFormAccessor.IsBarMatchedWithShapeInReverseOrder(barPositionIndex)` | Boolean |
| `Boolean IsUnconstrained()` | `rebarFreeFormAccessor.IsUnconstrained()` | Boolean |
| `Void RemoveUpdatingSharedParameter(ElementId)` | `rebarFreeFormAccessor.RemoveUpdatingSharedParameter(parameterId)` | Void |
| `RebarFreeFormValidationResult SetCurves(IList<CurveLoop>)` | `rebarFreeFormAccessor.SetCurves(curves)` | RebarFreeFormValidationResult |
| `RebarFreeFormValidationResult SetCurves(IList<IList<Curve>>)` | `rebarFreeFormAccessor.SetCurves(curves)` | RebarFreeFormValidationResult |
| `Void SetHookOrientationAngle(Int32, Double)` | `rebarFreeFormAccessor.SetHookOrientationAngle(end, angle)` | Void |
| `Void SetHookPlaneNormalForBarIdx(Int32, Int32, XYZ)` | `rebarFreeFormAccessor.SetHookPlaneNormalForBarIdx(end, barPositionIndex, hookNormal)` | Void |
| `Void SetLayoutAsFixedNumber(Int32)` | `rebarFreeFormAccessor.SetLayoutAsFixedNumber(numberOfBars)` | Void |
| `Void SetLayoutAsMaximumSpacing(Double)` | `rebarFreeFormAccessor.SetLayoutAsMaximumSpacing(spacing)` | Void |
| `Void SetLayoutAsMinimumClearSpacing(Double)` | `rebarFreeFormAccessor.SetLayoutAsMinimumClearSpacing(spacing)` | Void |
| `Void SetLayoutAsNumberWithSpacing(Int32, Double)` | `rebarFreeFormAccessor.SetLayoutAsNumberWithSpacing(numberOfBars, spacing)` | Void |
| `Void SetLayoutAsSingle()` | `rebarFreeFormAccessor.SetLayoutAsSingle()` | Void |
| `Void SetReportedShape(ElementId)` | `rebarFreeFormAccessor.SetReportedShape(rebarShapeId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
