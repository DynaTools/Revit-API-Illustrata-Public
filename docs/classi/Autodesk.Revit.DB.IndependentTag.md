---
title: IndependentTag
classe: Autodesk.Revit.DB.IndependentTag
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 32
---

# IndependentTag

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean HasLeader { get; set; }` | `independentTag.HasLeader` | Boolean |
| `Boolean IsMaterialTag { get; }` | `independentTag.IsMaterialTag` | Boolean |
| `Boolean IsMulticategoryTag { get; }` | `independentTag.IsMulticategoryTag` | Boolean |
| `Boolean IsOrphaned { get; }` | `independentTag.IsOrphaned` | Boolean |
| `LeaderEndCondition LeaderEndCondition { get; set; }` | `independentTag.LeaderEndCondition` | LeaderEndCondition |
| `LeadersPresentationMode LeadersPresentationMode { get; set; }` | `independentTag.LeadersPresentationMode` | LeadersPresentationMode |
| `Boolean MergeElbows { get; set; }` | `independentTag.MergeElbows` | Boolean |
| `Boolean MultiLeader { get; }` | `independentTag.MultiLeader` | Boolean |
| `ElementId MultiReferenceAnnotationId { get; }` | `independentTag.MultiReferenceAnnotationId` | ElementId |
| `Double RotationAngle { get; set; }` | `independentTag.RotationAngle` | Double |
| `XYZ TagHeadPosition { get; set; }` | `independentTag.TagHeadPosition` | XYZ |
| `TagOrientation TagOrientation { get; set; }` | `independentTag.TagOrientation` | TagOrientation |
| `String TagText { get; }` | `independentTag.TagText` | String |
| `Void AddReferences(IList<Reference>)` | `independentTag.AddReferences(referencesToTag)` | Void |
| `Boolean CanLeaderEndConditionBeAssigned(LeaderEndCondition)` | `independentTag.CanLeaderEndConditionBeAssigned(leaderEndCondition)` | Boolean |
| `IndependentTag Create(Document, ElementId, ElementId, Reference, Boolean, TagOrientation, XYZ)` | `IndependentTag.Create(document, symId, ownerDBViewId, referenceToTag, addLeader, tagOrientation, pnt)` | IndependentTag |
| `IndependentTag Create(Document, ElementId, Reference, Boolean, TagMode, TagOrientation, XYZ)` | `IndependentTag.Create(document, ownerDBViewId, referenceToTag, addLeader, tagMode, tagOrientation, pnt)` | IndependentTag |
| `XYZ GetLeaderElbow(Reference)` | `independentTag.GetLeaderElbow(referenceTagged)` | XYZ |
| `XYZ GetLeaderEnd(Reference)` | `independentTag.GetLeaderEnd(referenceTagged)` | XYZ |
| `ICollection<LinkElementId> GetTaggedElementIds()` | `independentTag.GetTaggedElementIds()` | ICollection<LinkElementId> |
| `ISet<ElementId> GetTaggedLocalElementIds()` | `independentTag.GetTaggedLocalElementIds()` | ISet<ElementId> |
| `ICollection<Element> GetTaggedLocalElements()` | `independentTag.GetTaggedLocalElements()` | ICollection<Element> |
| `IList<Reference> GetTaggedReferences()` | `independentTag.GetTaggedReferences()` | IList<Reference> |
| `Boolean HasLeaderElbow(Reference)` | `independentTag.HasLeaderElbow(referenceTagged)` | Boolean |
| `Boolean HasTagBehavior()` | `independentTag.HasTagBehavior()` | Boolean |
| `Boolean HasTagText()` | `independentTag.HasTagText()` | Boolean |
| `Boolean IsLeaderVisible(Reference)` | `independentTag.IsLeaderVisible(referenceTagged)` | Boolean |
| `Boolean IsTaggedOnSubelement()` | `independentTag.IsTaggedOnSubelement()` | Boolean |
| `Void RemoveReferences(IList<Reference>)` | `independentTag.RemoveReferences(referencesToRemove)` | Void |
| `Void SetIsLeaderVisible(Reference, Boolean)` | `independentTag.SetIsLeaderVisible(referenceTagged, visible)` | Void |
| `Void SetLeaderElbow(Reference, XYZ)` | `independentTag.SetLeaderElbow(referenceTagged, elbowPosition)` | Void |
| `Void SetLeaderEnd(Reference, XYZ)` | `independentTag.SetLeaderEnd(referenceTagged, pointEnd)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
