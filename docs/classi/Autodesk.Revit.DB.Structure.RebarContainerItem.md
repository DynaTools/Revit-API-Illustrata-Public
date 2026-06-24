---
title: RebarContainerItem
classe: Autodesk.Revit.DB.Structure.RebarContainerItem
namespace: Autodesk.Revit.DB.Structure
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 51
---

# RebarContainerItem

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double ArrayLength { get; set; }` | `rebarContainerItem.ArrayLength` | Double |
| `Boolean BarsOnNormalSide { get; set; }` | `rebarContainerItem.BarsOnNormalSide` | Boolean |
| `ElementId BarTypeId { get; }` | `rebarContainerItem.BarTypeId` | ElementId |
| `Int32 BaseFinishingTurns { get; set; }` | `rebarContainerItem.BaseFinishingTurns` | Int32 |
| `Double Height { get; set; }` | `rebarContainerItem.Height` | Double |
| `Boolean IncludeFirstBar { get; set; }` | `rebarContainerItem.IncludeFirstBar` | Boolean |
| `Boolean IncludeLastBar { get; set; }` | `rebarContainerItem.IncludeLastBar` | Boolean |
| `Boolean IsValidObject { get; }` | `rebarContainerItem.IsValidObject` | Boolean |
| `Int32 ItemIndex { get; }` | `rebarContainerItem.ItemIndex` | Int32 |
| `RebarLayoutRule LayoutRule { get; }` | `rebarContainerItem.LayoutRule` | RebarLayoutRule |
| `Double MaxSpacing { get; set; }` | `rebarContainerItem.MaxSpacing` | Double |
| `Double MultiplanarDepth { get; set; }` | `rebarContainerItem.MultiplanarDepth` | Double |
| `XYZ Normal { get; }` | `rebarContainerItem.Normal` | XYZ |
| `Int32 NumberOfBarPositions { get; set; }` | `rebarContainerItem.NumberOfBarPositions` | Int32 |
| `Double Pitch { get; set; }` | `rebarContainerItem.Pitch` | Double |
| `Int32 Quantity { get; }` | `rebarContainerItem.Quantity` | Int32 |
| `ElementId RebarShapeId { get; set; }` | `rebarContainerItem.RebarShapeId` | ElementId |
| `Int32 TopFinishingTurns { get; set; }` | `rebarContainerItem.TopFinishingTurns` | Int32 |
| `Double TotalLength { get; }` | `rebarContainerItem.TotalLength` | Double |
| `Double Volume { get; }` | `rebarContainerItem.Volume` | Double |
| `Boolean CanApplyPresentationMode(View)` | `rebarContainerItem.CanApplyPresentationMode(dBView)` | Boolean |
| `Boolean CanUseHookType(ElementId)` | `rebarContainerItem.CanUseHookType(proposedHookId)` | Boolean |
| `Void ClearPresentationMode(View)` | `rebarContainerItem.ClearPresentationMode(dBView)` | Void |
| `IList<Curve> ComputeDrivingCurves()` | `rebarContainerItem.ComputeDrivingCurves()` | IList<Curve> |
| `Void Dispose()` | `rebarContainerItem.Dispose()` | Void |
| `Boolean DoesBarExistAtPosition(Int32)` | `rebarContainerItem.DoesBarExistAtPosition(barPosition)` | Boolean |
| `RebarPresentationMode FindMatchingPredefinedPresentationMode(View)` | `rebarContainerItem.FindMatchingPredefinedPresentationMode(dBView)` | RebarPresentationMode |
| `Transform GetBarPositionTransform(Int32)` | `rebarContainerItem.GetBarPositionTransform(barPositionIndex)` | Transform |
| `RebarBendData GetBendData()` | `rebarContainerItem.GetBendData()` | RebarBendData |
| `IList<Curve> GetCenterlineCurves(Boolean, Boolean, Boolean, MultiplanarOption)` | `rebarContainerItem.GetCenterlineCurves(adjustForSelfIntersection, suppressHooks, suppressBendRadius, multiplanarOption)` | IList<Curve> |
| `IList<Curve> GetCenterlineCurves(Boolean, Boolean, Boolean)` | `rebarContainerItem.GetCenterlineCurves(adjustForSelfIntersection, suppressHooks, suppressBendRadius)` | IList<Curve> |
| `Line GetDistributionPath()` | `rebarContainerItem.GetDistributionPath()` | Line |
| `RebarHookOrientation GetHookOrientation(Int32)` | `rebarContainerItem.GetHookOrientation(iEnd)` | RebarHookOrientation |
| `ElementId GetHookTypeId(Int32)` | `rebarContainerItem.GetHookTypeId(end)` | ElementId |
| `RebarPresentationMode GetPresentationMode(View)` | `rebarContainerItem.GetPresentationMode(dBView)` | RebarPresentationMode |
| `Boolean HasPresentationOverrides(View)` | `rebarContainerItem.HasPresentationOverrides(dBView)` | Boolean |
| `Boolean IsBarHidden(View, Int32)` | `rebarContainerItem.IsBarHidden(view, barIndex)` | Boolean |
| `Boolean IsRebarInSection(View)` | `rebarContainerItem.IsRebarInSection(dBView)` | Boolean |
| `Void SetBarHiddenStatus(View, Int32, Boolean)` | `rebarContainerItem.SetBarHiddenStatus(view, barIndex, hide)` | Void |
| `Void SetFromCurves(RebarStyle, RebarBarType, RebarHookType, RebarHookType, XYZ, IList<Curve>, RebarHookOrientation, RebarHookOrientation, Boolean, Boolean)` | `rebarContainerItem.SetFromCurves(style, barType, startHook, endHook, norm, curves, startHookOrient, endHookOrient, useExistingShapeIfPossible, createNewShape)` | Void |
| `Void SetFromCurvesAndShape(RebarShape, RebarBarType, RebarHookType, RebarHookType, XYZ, IList<Curve>, RebarHookOrientation, RebarHookOrientation)` | `rebarContainerItem.SetFromCurvesAndShape(rebarShape, barType, startHook, endHook, norm, curves, startHookOrient, endHookOrient)` | Void |
| `Void SetFromRebar(Rebar)` | `rebarContainerItem.SetFromRebar(rebar)` | Void |
| `Void SetFromRebarShape(RebarShape, RebarBarType, XYZ, XYZ, XYZ)` | `rebarContainerItem.SetFromRebarShape(rebarShape, barType, origin, xVec, yVec)` | Void |
| `Void SetHookOrientation(Int32, RebarHookOrientation)` | `rebarContainerItem.SetHookOrientation(iEnd, hookOrientation)` | Void |
| `Void SetHookTypeId(Int32, ElementId)` | `rebarContainerItem.SetHookTypeId(end, hookTypeId)` | Void |
| `Void SetLayoutAsFixedNumber(Int32, Double, Boolean, Boolean, Boolean)` | `rebarContainerItem.SetLayoutAsFixedNumber(numberOfBarPositions, arrayLength, barsOnNormalSide, includeFirstBar, includeLastBar)` | Void |
| `Void SetLayoutAsMaximumSpacing(Double, Double, Boolean, Boolean, Boolean)` | `rebarContainerItem.SetLayoutAsMaximumSpacing(spacing, arrayLength, barsOnNormalSide, includeFirstBar, includeLastBar)` | Void |
| `Void SetLayoutAsMinimumClearSpacing(Double, Double, Boolean, Boolean, Boolean)` | `rebarContainerItem.SetLayoutAsMinimumClearSpacing(spacing, arrayLength, barsOnNormalSide, includeFirstBar, includeLastBar)` | Void |
| `Void SetLayoutAsNumberWithSpacing(Int32, Double, Boolean, Boolean, Boolean)` | `rebarContainerItem.SetLayoutAsNumberWithSpacing(numberOfBarPositions, spacing, barsOnNormalSide, includeFirstBar, includeLastBar)` | Void |
| `Void SetLayoutAsSingle()` | `rebarContainerItem.SetLayoutAsSingle()` | Void |
| `Void SetPresentationMode(View, RebarPresentationMode)` | `rebarContainerItem.SetPresentationMode(dBView, presentationMode)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
