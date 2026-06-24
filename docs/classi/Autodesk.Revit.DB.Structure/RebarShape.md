---
title: RebarShape
classe: Autodesk.Revit.DB.Structure.RebarShape
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.ElementType
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 21
---

# RebarShape

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 HigherEnd { get; }` | `rebarShape.HigherEnd` | Int32 |
| `RebarStyle RebarStyle { get; }` | `rebarShape.RebarStyle` | RebarStyle |
| `ElementId ShapeFamilyId { get; }` | `rebarShape.ShapeFamilyId` | ElementId |
| `Boolean SimpleArc { get; }` | `rebarShape.SimpleArc` | Boolean |
| `Boolean SimpleLine { get; }` | `rebarShape.SimpleLine` | Boolean |
| `StirrupTieAttachmentType StirrupTieAttachment { get; }` | `rebarShape.StirrupTieAttachment` | StirrupTieAttachmentType |
| `RebarShape Create(Document, RebarShapeDefinition, RebarShapeMultiplanarDefinition, RebarStyle, StirrupTieAttachmentType, Int32, RebarHookOrientation, Int32, RebarHookOrientation, Int32, Double, Double, ElementId, ElementId)` | `RebarShape.Create(doc, definition, multiplanarDefinition, style, attachmentType, startHookAngle, startHookOrientation, endHookAngle, endHookOrientation, higherEnd, hookRotationAngleAtStart, hookRotationAngleAtEnd, endTreatmentTypeIdAtStart, endTreatmentTypeIdAtEnd)` | RebarShape |
| `RebarShape Create(Document, RebarShapeDefinition, RebarShapeMultiplanarDefinition, RebarStyle, StirrupTieAttachmentType, Int32, RebarHookOrientation, Int32, RebarHookOrientation, Int32)` | `RebarShape.Create(doc, definition, multiplanarDefinition, style, attachmentType, startHookAngle, startHookOrientation, endHookAngle, endHookOrientation, higherEnd)` | RebarShape |
| `Boolean GetAllowed(RebarBarType)` | `rebarShape.GetAllowed(barType)` | Boolean |
| `IList<Curve> GetCurvesForBrowser()` | `rebarShape.GetCurvesForBrowser()` | IList<Curve> |
| `Int32 GetDefaultHookAngle(Int32)` | `rebarShape.GetDefaultHookAngle(index)` | Int32 |
| `RebarHookOrientation GetDefaultHookOrientation(Int32)` | `rebarShape.GetDefaultHookOrientation(index)` | RebarHookOrientation |
| `ElementId GetEndTreatmentTypeId(Int32)` | `rebarShape.GetEndTreatmentTypeId(iEnd)` | ElementId |
| `Double GetHookRotationAngle(Int32)` | `rebarShape.GetHookRotationAngle(iEnd)` | Double |
| `RebarShapeMultiplanarDefinition GetMultiplanarDefinition()` | `rebarShape.GetMultiplanarDefinition()` | RebarShapeMultiplanarDefinition |
| `RebarShapeDefinition GetRebarShapeDefinition()` | `rebarShape.GetRebarShapeDefinition()` | RebarShapeDefinition |
| `Boolean HasEndTreatment()` | `rebarShape.HasEndTreatment()` | Boolean |
| `Boolean IsSameShapeIgnoringHooks(RebarShape)` | `rebarShape.IsSameShapeIgnoringHooks(otherShape)` | Boolean |
| `Void SetAllowed(RebarBarType, Boolean)` | `rebarShape.SetAllowed(barType, allowed)` | Void |
| `Void SetEndTreatmentTypeId(ElementId, Int32)` | `rebarShape.SetEndTreatmentTypeId(endTreatmentId, iEnd)` | Void |
| `Void SetHookRotationAngle(Double, Int32)` | `rebarShape.SetHookRotationAngle(hookRotationAngle, iEnd)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
