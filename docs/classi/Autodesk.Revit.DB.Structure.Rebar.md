---
title: Rebar
classe: Autodesk.Revit.DB.Structure.Rebar
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 77
---

# Rebar

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean CanHaveVaryingLengthBars { get; }` | `rebar.CanHaveVaryingLengthBars` | Boolean |
| `DistributionType DistributionType { get; set; }` | `rebar.DistributionType` | DistributionType |
| `Boolean HasVariableLengthBars { get; }` | `rebar.HasVariableLengthBars` | Boolean |
| `Boolean IncludeFirstBar { get; set; }` | `rebar.IncludeFirstBar` | Boolean |
| `Boolean IncludeLastBar { get; set; }` | `rebar.IncludeLastBar` | Boolean |
| `RebarLayoutRule LayoutRule { get; }` | `rebar.LayoutRule` | RebarLayoutRule |
| `Double MaxSpacing { get; set; }` | `rebar.MaxSpacing` | Double |
| `Int32 NumberOfBarPositions { get; set; }` | `rebar.NumberOfBarPositions` | Int32 |
| `Int32 Quantity { get; }` | `rebar.Quantity` | Int32 |
| `Boolean ReadOnlyParameters { get; set; }` | `rebar.ReadOnlyParameters` | Boolean |
| `String ScheduleMark { get; set; }` | `rebar.ScheduleMark` | String |
| `Double TotalLength { get; }` | `rebar.TotalLength` | Double |
| `Double Volume { get; }` | `rebar.Volume` | Double |
| `Boolean CanApplyPresentationMode(View)` | `rebar.CanApplyPresentationMode(dBView)` | Boolean |
| `Boolean CanBeMatchedWithMultipleShapes()` | `rebar.CanBeMatchedWithMultipleShapes()` | Boolean |
| `Boolean CanSuppressFirstOrLastBar(View, Int32)` | `rebar.CanSuppressFirstOrLastBar(dBView, end)` | Boolean |
| `Boolean CanUseHookType(ElementId)` | `rebar.CanUseHookType(proposedHookId)` | Boolean |
| `Void ClearPresentationMode(View)` | `rebar.ClearPresentationMode(dBView)` | Void |
| `Boolean ConstraintsCanBeEdited()` | `rebar.ConstraintsCanBeEdited()` | Boolean |
| `Boolean ContainsValidArcRadiiForStyleAndBarType(IList<Curve>, RebarStyle, RebarBarType)` | `Rebar.ContainsValidArcRadiiForStyleAndBarType(curves, style, barType)` | Boolean |
| `Rebar CreateFreeForm(Document, RebarBarType, Element, IList<CurveLoop>, RebarFreeFormValidationResult&)` | `Rebar.CreateFreeForm(doc, barType, host, curves, error)` | Rebar |
| `Rebar CreateFreeForm(Document, RebarBarType, Element, IList<IList<Curve>>, RebarFreeFormValidationResult&)` | `Rebar.CreateFreeForm(doc, barType, host, curves, error)` | Rebar |
| `Rebar CreateFreeForm(Document, Guid, RebarBarType, Element)` | `Rebar.CreateFreeForm(doc, serverGUID, barType, host)` | Rebar |
| `Rebar CreateFromCurves(Document, RebarStyle, RebarBarType, RebarHookType, RebarHookType, Element, XYZ, IList<Curve>, RebarHookOrientation, RebarHookOrientation, Double, Double, ElementId, ElementId, Boolean, Boolean)` | `Rebar.CreateFromCurves(doc, style, barType, startHook, endHook, host, norm, curves, startHookOrient, endHookOrient, hookRotationAngleAtStart, hookRotationAngleAtEnd, endTreatmentTypeIdAtStart, endTreatmentTypeIdAtEnd, useExistingShapeIfPossible, createNewShape)` | Rebar |
| `Rebar CreateFromCurves(Document, RebarStyle, RebarBarType, RebarHookType, RebarHookType, Element, XYZ, IList<Curve>, RebarHookOrientation, RebarHookOrientation, Boolean, Boolean)` | `Rebar.CreateFromCurves(doc, style, barType, startHook, endHook, host, norm, curves, startHookOrient, endHookOrient, useExistingShapeIfPossible, createNewShape)` | Rebar |
| `Rebar CreateFromCurvesAndShape(Document, RebarShape, RebarBarType, RebarHookType, RebarHookType, Element, XYZ, IList<Curve>, RebarHookOrientation, RebarHookOrientation, Double, Double, ElementId, ElementId)` | `Rebar.CreateFromCurvesAndShape(doc, rebarShape, barType, startHook, endHook, host, norm, curves, startHookOrient, endHookOrient, hookRotationAngleAtStart, hookRotationAngleAtEnd, endTreatmentTypeIdAtStart, endTreatmentTypeIdAtEnd)` | Rebar |
| `Rebar CreateFromCurvesAndShape(Document, RebarShape, RebarBarType, RebarHookType, RebarHookType, Element, XYZ, IList<Curve>, RebarHookOrientation, RebarHookOrientation)` | `Rebar.CreateFromCurvesAndShape(doc, rebarShape, barType, startHook, endHook, host, norm, curves, startHookOrient, endHookOrient)` | Rebar |
| `Rebar CreateFromRebarShape(Document, RebarShape, RebarBarType, Element, XYZ, XYZ, XYZ)` | `Rebar.CreateFromRebarShape(doc, rebarShape, barType, host, origin, xVec, yVec)` | Rebar |
| `Boolean DoesBarExistAtPosition(Int32)` | `rebar.DoesBarExistAtPosition(barPosition)` | Boolean |
| `Void EnableHookLengthOverride(Boolean)` | `rebar.EnableHookLengthOverride(enable)` | Void |
| `RebarPresentationMode FindMatchingPredefinedPresentationMode(View)` | `rebar.FindMatchingPredefinedPresentationMode(dBView)` | RebarPresentationMode |
| `IList<ElementId> GetAllRebarShapeIds()` | `rebar.GetAllRebarShapeIds()` | IList<ElementId> |
| `Int32 GetBarIndexFromReference(Reference)` | `rebar.GetBarIndexFromReference(barReference)` | Int32 |
| `RebarBendData GetBendData()` | `rebar.GetBendData()` | RebarBendData |
| `IList<Curve> GetCenterlineCurves(Boolean, Boolean, Boolean, MultiplanarOption, Int32)` | `rebar.GetCenterlineCurves(adjustForSelfIntersection, suppressHooks, suppressBendRadius, multiplanarOption, barPositionIndex)` | IList<Curve> |
| `ElementId GetCouplerId(Int32)` | `rebar.GetCouplerId(end)` | ElementId |
| `ElementId GetEndTreatmentTypeId(Int32)` | `rebar.GetEndTreatmentTypeId(end)` | ElementId |
| `RebarFreeFormAccessor GetFreeFormAccessor()` | `rebar.GetFreeFormAccessor()` | RebarFreeFormAccessor |
| `GeometryElement GetFullGeometryForView(View)` | `rebar.GetFullGeometryForView(view)` | GeometryElement |
| `RebarHookOrientation GetHookOrientation(Int32)` | `rebar.GetHookOrientation(iEnd)` | RebarHookOrientation |
| `Double GetHookRotationAngle(Int32)` | `rebar.GetHookRotationAngle(iEnd)` | Double |
| `ElementId GetHookTypeId(Int32)` | `rebar.GetHookTypeId(end)` | ElementId |
| `ElementId GetHostId()` | `rebar.GetHostId()` | ElementId |
| `Double GetLapLength(Int32)` | `rebar.GetLapLength(barEnd)` | Double |
| `Transform GetMovedBarTransform(Int32)` | `rebar.GetMovedBarTransform(barPositionIndex)` | Transform |
| `Void GetOverridableHookParameters(ISet<ElementId>&, ISet<ElementId>&, ISet<ElementId>&, ISet<ElementId>&)` | `rebar.GetOverridableHookParameters(startHookLengthPrameters, startHookTangentLengthParameters, endHookLengthParameters, endHookTangentLengthParameters)` | Void |
| `ParameterValue GetParameterValueAtIndex(ElementId, Int32)` | `rebar.GetParameterValueAtIndex(paramId, barPositionIndex)` | ParameterValue |
| `RebarPresentationMode GetPresentationMode(View)` | `rebar.GetPresentationMode(dBView)` | RebarPresentationMode |
| `RebarConstraintsManager GetRebarConstraintsManager()` | `rebar.GetRebarConstraintsManager()` | RebarConstraintsManager |
| `RebarSplice GetRebarSplice(Int32)` | `rebar.GetRebarSplice(barEnd)` | RebarSplice |
| `RebarRoundingManager GetReinforcementRoundingManager()` | `rebar.GetReinforcementRoundingManager()` | RebarRoundingManager |
| `RebarShapeDrivenAccessor GetShapeDrivenAccessor()` | `rebar.GetShapeDrivenAccessor()` | RebarShapeDrivenAccessor |
| `ElementId GetShapeId()` | `rebar.GetShapeId()` | ElementId |
| `Double GetSpliceStaggerLength(Int32)` | `rebar.GetSpliceStaggerLength(barEnd)` | Double |
| `IList<Curve> GetTransformedCenterlineCurves(Boolean, Boolean, Boolean, MultiplanarOption, Int32)` | `rebar.GetTransformedCenterlineCurves(adjustForSelfIntersection, suppressHooks, suppressBendRadius, multiplanarOption, barPositionIndex)` | IList<Curve> |
| `Boolean HasPresentationOverrides(View)` | `rebar.HasPresentationOverrides(dBView)` | Boolean |
| `Boolean HookAngleMatchesRebarShapeDefinition(Int32, ElementId)` | `rebar.HookAngleMatchesRebarShapeDefinition(iEnd, proposedHookId)` | Boolean |
| `Boolean IsBarHidden(View, Int32)` | `rebar.IsBarHidden(view, barIndex)` | Boolean |
| `Boolean IsHookLengthOverrideEnabled()` | `rebar.IsHookLengthOverrideEnabled()` | Boolean |
| `Boolean IsRebarFreeForm()` | `rebar.IsRebarFreeForm()` | Boolean |
| `Boolean IsRebarInSection(View)` | `rebar.IsRebarInSection(dBView)` | Boolean |
| `Boolean IsRebarShapeDriven()` | `rebar.IsRebarShapeDriven()` | Boolean |
| `Boolean IsUnobscuredInView(View)` | `rebar.IsUnobscuredInView(view)` | Boolean |
| `Void MoveBarInSet(Int32, Transform)` | `rebar.MoveBarInSet(barPositionIndex, moveTransform)` | Void |
| `Boolean RebarShapeMatchesCurvesAndHooks(RebarShape, RebarBarType, XYZ, IList<Curve>, RebarHookType, RebarHookType, RebarHookOrientation, RebarHookOrientation)` | `Rebar.RebarShapeMatchesCurvesAndHooks(rebarShape, barType, norm, curves, startHook, endHook, startHookOrient, endHookOrient)` | Boolean |
| `Boolean RebarShapeMatchesCurvesHooksAndEndTreatment(RebarShape, RebarBarType, XYZ, IList<Curve>, RebarHookType, RebarHookType, RebarHookOrientation, RebarHookOrientation, Double, Double, ElementId, ElementId)` | `Rebar.RebarShapeMatchesCurvesHooksAndEndTreatment(rebarShape, barType, norm, curves, startHook, endHook, startHookOrient, endHookOrient, hookRotationAngleAtStart, hookRotationAngleAtEnd, endTreatmentTypeIdAtStart, endTreatmentTypeIdAtEnd)` | Boolean |
| `Void RemoveSplice(Int32)` | `rebar.RemoveSplice(barEnd)` | Void |
| `Void ResetMovedBarTransform(Int32)` | `rebar.ResetMovedBarTransform(barPositionIndex)` | Void |
| `Void SetBarHiddenStatus(View, Int32, Boolean)` | `rebar.SetBarHiddenStatus(view, barIndex, hide)` | Void |
| `Void SetBarIncluded(Boolean, Int32)` | `rebar.SetBarIncluded(include, barPositionIndex)` | Void |
| `Void SetEndTreatmentTypeId(Int32, ElementId)` | `rebar.SetEndTreatmentTypeId(end, endTreatmentTypeId)` | Void |
| `Void SetHookOrientation(Int32, RebarHookOrientation)` | `rebar.SetHookOrientation(iEnd, hookOrientation)` | Void |
| `Void SetHookRotationAngle(Double, Int32)` | `rebar.SetHookRotationAngle(hookRotationAngle, iEnd)` | Void |
| `Void SetHookTypeId(Int32, ElementId)` | `rebar.SetHookTypeId(end, hookTypeId)` | Void |
| `Void SetHostId(Document, ElementId)` | `rebar.SetHostId(doc, hostId)` | Void |
| `Void SetPresentationMode(View, RebarPresentationMode)` | `rebar.SetPresentationMode(dBView, presentationMode)` | Void |
| `Void SetUnobscuredInView(View, Boolean)` | `rebar.SetUnobscuredInView(view, unobscured)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
