---
title: PartMakerMethodToDivideVolumes
classe: Autodesk.Revit.DB.PartMakerMethodToDivideVolumes
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 28
---

# PartMakerMethodToDivideVolumes

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double DivisionGap { get; set; }` | `partMakerMethodToDivideVolumes.DivisionGap` | Double |
| `Boolean DivisionPatternMirror { get; set; }` | `partMakerMethodToDivideVolumes.DivisionPatternMirror` | Boolean |
| `Double DivisionRotationAngle { get; set; }` | `partMakerMethodToDivideVolumes.DivisionRotationAngle` | Double |
| `ElementId DivisionRuleId { get; set; }` | `partMakerMethodToDivideVolumes.DivisionRuleId` | ElementId |
| `Boolean IsValidObject { get; }` | `partMakerMethodToDivideVolumes.IsValidObject` | Boolean |
| `Boolean ProfileFlipAcross { get; set; }` | `partMakerMethodToDivideVolumes.ProfileFlipAcross` | Boolean |
| `Boolean ProfileFlipAlong { get; set; }` | `partMakerMethodToDivideVolumes.ProfileFlipAlong` | Boolean |
| `PartEdgeConditionOrientation ProfileMatch { get; set; }` | `partMakerMethodToDivideVolumes.ProfileMatch` | PartEdgeConditionOrientation |
| `Double ProfileOffset { get; set; }` | `partMakerMethodToDivideVolumes.ProfileOffset` | Double |
| `ElementId ProfileType { get; set; }` | `partMakerMethodToDivideVolumes.ProfileType` | ElementId |
| `Int32 UConstDivisionIndent { get; set; }` | `partMakerMethodToDivideVolumes.UConstDivisionIndent` | Int32 |
| `Int32 VConstDivisionIndent { get; set; }` | `partMakerMethodToDivideVolumes.VConstDivisionIndent` | Int32 |
| `Boolean AddIntersectingReference(ElementId, Double)` | `partMakerMethodToDivideVolumes.AddIntersectingReference(intersectingReference, offset)` | Boolean |
| `Boolean AreElementsValidIntersectingReferences(Document, ICollection<ElementId>)` | `PartMakerMethodToDivideVolumes.AreElementsValidIntersectingReferences(document, elementIds)` | Boolean |
| `Boolean AreElementsValidIntersectingReferences(ICollection<ElementId>)` | `partMakerMethodToDivideVolumes.AreElementsValidIntersectingReferences(elementIds)` | Boolean |
| `Boolean CanBeDivisionProfile(ElementId)` | `partMakerMethodToDivideVolumes.CanBeDivisionProfile(familyId)` | Boolean |
| `Boolean CanBeDivisionProfile(ElementId, Document)` | `PartMakerMethodToDivideVolumes.CanBeDivisionProfile(familyId, familyDocument)` | Boolean |
| `Void Dispose()` | `partMakerMethodToDivideVolumes.Dispose()` | Void |
| `Double GetOffsetForIntersectingReference(ElementId)` | `partMakerMethodToDivideVolumes.GetOffsetForIntersectingReference(intersectingReference)` | Double |
| `Plane GetPlaneOfSketch()` | `partMakerMethodToDivideVolumes.GetPlaneOfSketch()` | Plane |
| `Void GetSketchCurves(IList<Curve>&)` | `partMakerMethodToDivideVolumes.GetSketchCurves(curveArray)` | Void |
| `IDictionary<ElementId, Double> GetSplitRefsOffsets()` | `partMakerMethodToDivideVolumes.GetSplitRefsOffsets()` | IDictionary<ElementId, Double> |
| `Boolean IsElementValidIntersectingReference(Document, ElementId)` | `PartMakerMethodToDivideVolumes.IsElementValidIntersectingReference(document, elementId)` | Boolean |
| `Boolean IsElementValidIntersectingReference(ElementId)` | `partMakerMethodToDivideVolumes.IsElementValidIntersectingReference(elementId)` | Boolean |
| `Boolean IsValidSketchPlane(Document, ElementId)` | `PartMakerMethodToDivideVolumes.IsValidSketchPlane(document, sketchPlaneId)` | Boolean |
| `Boolean RemoveIntersectingReference(ElementId)` | `partMakerMethodToDivideVolumes.RemoveIntersectingReference(intersectingReference)` | Boolean |
| `Void SetOffsetForIntersectingReference(ElementId, Double)` | `partMakerMethodToDivideVolumes.SetOffsetForIntersectingReference(intersectingReference, offset)` | Void |
| `Boolean UsesReference(ElementId)` | `partMakerMethodToDivideVolumes.UsesReference(intersectingReference)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
