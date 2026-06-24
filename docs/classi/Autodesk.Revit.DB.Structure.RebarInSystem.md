---
title: RebarInSystem
classe: Autodesk.Revit.DB.Structure.RebarInSystem
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 38
---

# RebarInSystem

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double ArrayLength { get; }` | `rebarInSystem.ArrayLength` | Double |
| `Boolean BarsOnNormalSide { get; }` | `rebarInSystem.BarsOnNormalSide` | Boolean |
| `RebarLayoutRule LayoutRule { get; }` | `rebarInSystem.LayoutRule` | RebarLayoutRule |
| `Double MaxSpacing { get; }` | `rebarInSystem.MaxSpacing` | Double |
| `XYZ Normal { get; }` | `rebarInSystem.Normal` | XYZ |
| `Int32 NumberOfBarPositions { get; }` | `rebarInSystem.NumberOfBarPositions` | Int32 |
| `Int32 Quantity { get; }` | `rebarInSystem.Quantity` | Int32 |
| `ElementId RebarShapeId { get; }` | `rebarInSystem.RebarShapeId` | ElementId |
| `String ScheduleMark { get; set; }` | `rebarInSystem.ScheduleMark` | String |
| `ElementId SystemId { get; }` | `rebarInSystem.SystemId` | ElementId |
| `Double TotalLength { get; }` | `rebarInSystem.TotalLength` | Double |
| `Double Volume { get; }` | `rebarInSystem.Volume` | Double |
| `Boolean CanApplyPresentationMode(View)` | `rebarInSystem.CanApplyPresentationMode(dBView)` | Boolean |
| `Boolean CanEditIndividualBars()` | `rebarInSystem.CanEditIndividualBars()` | Boolean |
| `Void ClearPresentationMode(View)` | `rebarInSystem.ClearPresentationMode(dBView)` | Void |
| `Boolean DoesBarExistAtPosition(Int32)` | `rebarInSystem.DoesBarExistAtPosition(barPosition)` | Boolean |
| `RebarPresentationMode FindMatchingPredefinedPresentationMode(View)` | `rebarInSystem.FindMatchingPredefinedPresentationMode(dBView)` | RebarPresentationMode |
| `Int32 GetBarIndexFromReference(Reference)` | `rebarInSystem.GetBarIndexFromReference(barReference)` | Int32 |
| `Transform GetBarPositionTransform(Int32)` | `rebarInSystem.GetBarPositionTransform(barPositionIndex)` | Transform |
| `RebarBendData GetBendData()` | `rebarInSystem.GetBendData()` | RebarBendData |
| `IList<Curve> GetCenterlineCurves(Boolean, Boolean, Boolean)` | `rebarInSystem.GetCenterlineCurves(adjustForSelfIntersection, suppressHooks, suppressBendRadius)` | IList<Curve> |
| `Line GetDistributionPath()` | `rebarInSystem.GetDistributionPath()` | Line |
| `ElementId GetHookTypeId(Int32)` | `rebarInSystem.GetHookTypeId(end)` | ElementId |
| `ElementId GetHostId()` | `rebarInSystem.GetHostId()` | ElementId |
| `Transform GetMovedBarTransform(Int32)` | `rebarInSystem.GetMovedBarTransform(barPositionIndex)` | Transform |
| `RebarPresentationMode GetPresentationMode(View)` | `rebarInSystem.GetPresentationMode(dBView)` | RebarPresentationMode |
| `RebarRoundingManager GetReinforcementRoundingManager()` | `rebarInSystem.GetReinforcementRoundingManager()` | RebarRoundingManager |
| `IList<Curve> GetTransformedCenterlineCurves(Boolean, Boolean, Boolean, Int32)` | `rebarInSystem.GetTransformedCenterlineCurves(adjustForSelfIntersection, suppressHooks, suppressBendRadius, barPositionIndex)` | IList<Curve> |
| `Boolean HasPresentationOverrides(View)` | `rebarInSystem.HasPresentationOverrides(dBView)` | Boolean |
| `Boolean IsBarHidden(View, Int32)` | `rebarInSystem.IsBarHidden(view, barIndex)` | Boolean |
| `Boolean IsRebarInSection(View)` | `rebarInSystem.IsRebarInSection(dBView)` | Boolean |
| `Boolean IsUnobscuredInView(View)` | `rebarInSystem.IsUnobscuredInView(view)` | Boolean |
| `Void MoveBarInSet(Int32, Transform)` | `rebarInSystem.MoveBarInSet(barPositionIndex, moveTransform)` | Void |
| `Void ResetMovedBarTransform(Int32)` | `rebarInSystem.ResetMovedBarTransform(barPositionIndex)` | Void |
| `Void SetBarHiddenStatus(View, Int32, Boolean)` | `rebarInSystem.SetBarHiddenStatus(view, barIndex, hide)` | Void |
| `Void SetBarIncluded(Boolean, Int32)` | `rebarInSystem.SetBarIncluded(include, barPositionIndex)` | Void |
| `Void SetPresentationMode(View, RebarPresentationMode)` | `rebarInSystem.SetPresentationMode(dBView, presentationMode)` | Void |
| `Void SetUnobscuredInView(View, Boolean)` | `rebarInSystem.SetUnobscuredInView(view, unobscured)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
