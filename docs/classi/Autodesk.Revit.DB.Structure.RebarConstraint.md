---
title: RebarConstraint
classe: Autodesk.Revit.DB.Structure.RebarConstraint
namespace: Autodesk.Revit.DB.Structure
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 50
---

# RebarConstraint

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `rebarConstraint.IsValidObject` | Boolean |
| `Int32 NumberOfTargets { get; }` | `rebarConstraint.NumberOfTargets` | Int32 |
| `Boolean ConstrainsRebarEnds()` | `rebarConstraint.ConstrainsRebarEnds()` | Boolean |
| `RebarConstraint Create(RebarConstrainedHandle, IList<Reference>, Boolean, Double)` | `RebarConstraint.Create(handle, targetReferences, isConstraintToCover, offsetValue)` | RebarConstraint |
| `RebarConstraint CreateConstraintToSurface(RebarConstrainedHandle, Surface)` | `RebarConstraint.CreateConstraintToSurface(handle, surface)` | RebarConstraint |
| `Void Dispose()` | `rebarConstraint.Dispose()` | Void |
| `Void FlipHandleOverTarget()` | `rebarConstraint.FlipHandleOverTarget()` | Void |
| `Void FlipSideForClearBarSpacingZeroDistanceConstraint()` | `rebarConstraint.FlipSideForClearBarSpacingZeroDistanceConstraint()` | Void |
| `RebarConstraintType GetConstraintType()` | `rebarConstraint.GetConstraintType()` | RebarConstraintType |
| `Int32 GetCustomHandleTag()` | `rebarConstraint.GetCustomHandleTag()` | Int32 |
| `Double GetDistanceToTargetCover()` | `rebarConstraint.GetDistanceToTargetCover()` | Double |
| `Double GetDistanceToTargetHostFace()` | `rebarConstraint.GetDistanceToTargetHostFace()` | Double |
| `Double GetDistanceToTargetRebar()` | `rebarConstraint.GetDistanceToTargetRebar()` | Double |
| `XYZ GetPositiveOffsetDirectionForToOtherRebarConstraint()` | `rebarConstraint.GetPositiveOffsetDirectionForToOtherRebarConstraint()` | XYZ |
| `RebarConstrainedHandle GetRebarConstrainedHandle()` | `rebarConstraint.GetRebarConstrainedHandle()` | RebarConstrainedHandle |
| `RebarConstraintTargetHostFaceType GetRebarConstraintTargetHostFaceType()` | `rebarConstraint.GetRebarConstraintTargetHostFaceType()` | RebarConstraintTargetHostFaceType |
| `RebarConstraintTargetHostFaceType GetRebarConstraintTargetHostFaceType(Int32)` | `rebarConstraint.GetRebarConstraintTargetHostFaceType(targetIndex)` | RebarConstraintTargetHostFaceType |
| `Surface GetSurfaceForConstraintToSurface()` | `rebarConstraint.GetSurfaceForConstraintToSurface()` | Surface |
| `RebarCoverType GetTargetCoverType(Int32)` | `rebarConstraint.GetTargetCoverType(targetIndex)` | RebarCoverType |
| `Element GetTargetElement()` | `rebarConstraint.GetTargetElement()` | Element |
| `Element GetTargetElement(Int32)` | `rebarConstraint.GetTargetElement(targetIndex)` | Element |
| `Face GetTargetHostFaceAndTransform(Int32, Transform)` | `rebarConstraint.GetTargetHostFaceAndTransform(targetIndex, faceTransform)` | Face |
| `Reference GetTargetHostFaceReference()` | `rebarConstraint.GetTargetHostFaceReference()` | Reference |
| `Reference GetTargetHostFaceReference(Int32)` | `rebarConstraint.GetTargetHostFaceReference(targetIndex)` | Reference |
| `Int32 GetTargetRebarAngleOnBarOrHookBend()` | `rebarConstraint.GetTargetRebarAngleOnBarOrHookBend()` | Int32 |
| `Int32 GetTargetRebarBendNumber()` | `rebarConstraint.GetTargetRebarBendNumber()` | Int32 |
| `TargetRebarConstraintType GetTargetRebarConstraintType()` | `rebarConstraint.GetTargetRebarConstraintType()` | TargetRebarConstraintType |
| `Int32 GetTargetRebarEdgeNumber()` | `rebarConstraint.GetTargetRebarEdgeNumber()` | Int32 |
| `Int32 GetTargetRebarHookBarEnd()` | `rebarConstraint.GetTargetRebarHookBarEnd()` | Int32 |
| `Boolean HasAnEdgeNumber()` | `rebarConstraint.HasAnEdgeNumber()` | Boolean |
| `Boolean IsBindingHandleWithTarget()` | `rebarConstraint.IsBindingHandleWithTarget()` | Boolean |
| `Boolean IsEqual(RebarConstraint)` | `rebarConstraint.IsEqual(other)` | Boolean |
| `Boolean IsFixedDistanceToHostFace()` | `rebarConstraint.IsFixedDistanceToHostFace()` | Boolean |
| `Boolean IsReferenceValidForConstraint(Reference)` | `rebarConstraint.IsReferenceValidForConstraint(targetReference)` | Boolean |
| `Boolean IsToCover()` | `rebarConstraint.IsToCover()` | Boolean |
| `Boolean IsToHostFaceOrCover()` | `rebarConstraint.IsToHostFaceOrCover()` | Boolean |
| `Boolean IsToOtherRebar()` | `rebarConstraint.IsToOtherRebar()` | Boolean |
| `Boolean IsToSurface()` | `rebarConstraint.IsToSurface()` | Boolean |
| `Boolean IsUsingClearBarSpacing()` | `rebarConstraint.IsUsingClearBarSpacing()` | Boolean |
| `Boolean IsValid()` | `rebarConstraint.IsValid()` | Boolean |
| `Boolean IsValidSurfaceToConstraintHandleTo(RebarConstrainedHandle, Surface)` | `RebarConstraint.IsValidSurfaceToConstraintHandleTo(handle, surface)` | Boolean |
| `Void ReplaceReferenceTargets(RebarConstrainedHandle, IList<Reference>, Boolean, Double)` | `rebarConstraint.ReplaceReferenceTargets(handle, targetReferences, isConstraintToCover, offsetValue)` | Void |
| `Void SetDistanceToTargetCover(Double)` | `rebarConstraint.SetDistanceToTargetCover(distanceToTargetCover)` | Void |
| `Void SetDistanceToTargetHostFace(Double)` | `rebarConstraint.SetDistanceToTargetHostFace(offset)` | Void |
| `Void SetDistanceToTargetRebar(Double)` | `rebarConstraint.SetDistanceToTargetRebar(distanceToTargetRebar)` | Void |
| `Void SetToBindHandleWithTarget(Boolean)` | `rebarConstraint.SetToBindHandleWithTarget(bindsHandleWithTarget)` | Void |
| `Void SetToUseClearBarSpacing(Boolean)` | `rebarConstraint.SetToUseClearBarSpacing(useClearBarSpacing)` | Void |
| `Boolean TargetIsBarBend()` | `rebarConstraint.TargetIsBarBend()` | Boolean |
| `Boolean TargetIsHookBend()` | `rebarConstraint.TargetIsHookBend()` | Boolean |
| `Boolean TargetRebarConstraintTypeIsEdge()` | `rebarConstraint.TargetRebarConstraintTypeIsEdge()` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
