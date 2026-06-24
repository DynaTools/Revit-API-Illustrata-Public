---
title: PartUtils
classe: Autodesk.Revit.DB.PartUtils
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 23
---

# PartUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean AreElementsValidForCreateParts(Document, ICollection<ElementId>)` | `PartUtils.AreElementsValidForCreateParts(document, elementIds)` | Boolean |
| `Boolean ArePartsValidForDivide(Document, ICollection<ElementId>)` | `PartUtils.ArePartsValidForDivide(document, elementIdsToDivide)` | Boolean |
| `Boolean ArePartsValidForMerge(Document, ICollection<ElementId>)` | `PartUtils.ArePartsValidForMerge(document, partIds)` | Boolean |
| `PartMaker CreateMergedPart(Document, ICollection<ElementId>)` | `PartUtils.CreateMergedPart(document, partIds)` | PartMaker |
| `Void CreateParts(Document, ICollection<ElementId>)` | `PartUtils.CreateParts(document, elementIds)` | Void |
| `Void CreateParts(Document, ICollection<LinkElementId>)` | `PartUtils.CreateParts(document, hostOrLinkElementIds)` | Void |
| `PartMaker DivideParts(Document, ICollection<ElementId>, ICollection<ElementId>, IList<Curve>, ElementId)` | `PartUtils.DivideParts(document, elementIdsToDivide, intersectingReferenceIds, curveArray, sketchPlaneId)` | PartMaker |
| `IList<ICollection<ElementId>> FindMergeableClusters(Document, ICollection<ElementId>)` | `PartUtils.FindMergeableClusters(doc, partIds)` | IList<ICollection<ElementId>> |
| `PartMaker GetAssociatedPartMaker(Document, ElementId)` | `PartUtils.GetAssociatedPartMaker(hostDocument, elementId)` | PartMaker |
| `PartMaker GetAssociatedPartMaker(Document, LinkElementId)` | `PartUtils.GetAssociatedPartMaker(hostDocument, hostOrLinkElementId)` | PartMaker |
| `ICollection<ElementId> GetAssociatedParts(Document, ElementId, Boolean, Boolean)` | `PartUtils.GetAssociatedParts(hostDocument, elementId, includePartsWithAssociatedParts, includeAllChildren)` | ICollection<ElementId> |
| `ICollection<ElementId> GetAssociatedParts(Document, LinkElementId, Boolean, Boolean)` | `PartUtils.GetAssociatedParts(hostDocument, hostOrLinkElementId, includePartsWithAssociatedParts, includeAllChildren)` | ICollection<ElementId> |
| `Int32 GetChainLengthToOriginal(Part)` | `PartUtils.GetChainLengthToOriginal(part)` | Int32 |
| `ICollection<ElementId> GetMergedParts(Part)` | `PartUtils.GetMergedParts(part)` | ICollection<ElementId> |
| `PartMakerMethodToDivideVolumes GetPartMakerMethodToDivideVolumeFW(PartMaker)` | `PartUtils.GetPartMakerMethodToDivideVolumeFW(partMaker)` | PartMakerMethodToDivideVolumes |
| `IList<Curve> GetSplittingCurves(Document, ElementId, Plane&)` | `PartUtils.GetSplittingCurves(document, partId, sketchPlane)` | IList<Curve> |
| `IList<Curve> GetSplittingCurves(Document, ElementId)` | `PartUtils.GetSplittingCurves(document, partId)` | IList<Curve> |
| `ISet<ElementId> GetSplittingElements(Document, ElementId)` | `PartUtils.GetSplittingElements(document, partId)` | ISet<ElementId> |
| `Boolean HasAssociatedParts(Document, ElementId)` | `PartUtils.HasAssociatedParts(hostDocument, elementId)` | Boolean |
| `Boolean HasAssociatedParts(Document, LinkElementId)` | `PartUtils.HasAssociatedParts(hostDocument, hostOrLinkElementId)` | Boolean |
| `Boolean IsMergedPart(Part)` | `PartUtils.IsMergedPart(part)` | Boolean |
| `Boolean IsPartDerivedFromLink(Part)` | `PartUtils.IsPartDerivedFromLink(dPart)` | Boolean |
| `Boolean IsValidForCreateParts(Document, LinkElementId)` | `PartUtils.IsValidForCreateParts(document, hostOrLinkElementId)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
