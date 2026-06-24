---
title: Wall
classe: Autodesk.Revit.DB.Wall
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.HostObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 33
---

# Wall

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `WallCrossSection CrossSection { get; set; }` | `wall.CrossSection` | WallCrossSection |
| `CurtainGrid CurtainGrid { get; }` | `wall.CurtainGrid` | CurtainGrid |
| `Boolean Flipped { get; }` | `wall.Flipped` | Boolean |
| `Boolean IsStackedWall { get; }` | `wall.IsStackedWall` | Boolean |
| `Boolean IsStackedWallMember { get; }` | `wall.IsStackedWallMember` | Boolean |
| `XYZ Orientation { get; }` | `wall.Orientation` | XYZ |
| `ElementId SketchId { get; }` | `wall.SketchId` | ElementId |
| `ElementId StackedWallOwnerId { get; }` | `wall.StackedWallOwnerId` | ElementId |
| `StructuralWallUsage StructuralUsage { get; set; }` | `wall.StructuralUsage` | StructuralWallUsage |
| `WallType WallType { get; set; }` | `wall.WallType` | WallType |
| `Double Width { get; }` | `wall.Width` | Double |
| `Void AddAttachment(ElementId, AttachmentLocation)` | `wall.AddAttachment(targetId, attachmentLocation)` | Void |
| `Void AllowWrappingAtLocation(Int32)` | `wall.AllowWrappingAtLocation(locationIndex)` | Void |
| `Boolean CanHaveProfileSketch()` | `wall.CanHaveProfileSketch()` | Boolean |
| `Wall Create(Document, IList<Curve>, ElementId, ElementId, Boolean, XYZ)` | `Wall.Create(document, profile, wallTypeId, levelId, structural, normal)` | Wall |
| `Wall Create(Document, IList<Curve>, ElementId, ElementId, Boolean)` | `Wall.Create(document, profile, wallTypeId, levelId, structural)` | Wall |
| `Wall Create(Document, IList<Curve>, Boolean)` | `Wall.Create(document, profile, structural)` | Wall |
| `Wall Create(Document, Curve, ElementId, ElementId, Double, Double, Boolean, Boolean)` | `Wall.Create(document, curve, wallTypeId, levelId, height, offset, flip, structural)` | Wall |
| `Wall Create(Document, Curve, ElementId, Boolean)` | `Wall.Create(document, curve, levelId, structural)` | Wall |
| `Sketch CreateProfileSketch()` | `wall.CreateProfileSketch()` | Sketch |
| `Void DisallowWrappingAtLocation(Int32)` | `wall.DisallowWrappingAtLocation(locationIndex)` | Void |
| `Void Flip()` | `wall.Flip()` | Void |
| `IList<ElementId> GetAttachmentIds(AttachmentLocation)` | `wall.GetAttachmentIds(attachmentLocation)` | IList<ElementId> |
| `IList<ElementId> GetStackedWallMemberIds()` | `wall.GetStackedWallMemberIds()` | IList<ElementId> |
| `IList<Int32> GetValidWrappingLocationIndices()` | `wall.GetValidWrappingLocationIndices()` | IList<Int32> |
| `Double GetWrappingLocationAsCurveParameter(Int32)` | `wall.GetWrappingLocationAsCurveParameter(locationIndex)` | Double |
| `IList<Reference> GetWrappingLocationAsReferences(Int32)` | `wall.GetWrappingLocationAsReferences(locationIndex)` | IList<Reference> |
| `Boolean IsValidTargetAttachment(Document, ElementId)` | `Wall.IsValidTargetAttachment(doc, targetId)` | Boolean |
| `Boolean IsWallCrossSectionValid(WallCrossSection)` | `wall.IsWallCrossSectionValid(wallCrossSection)` | Boolean |
| `Boolean IsWrappingAtLocationAllowed(Int32)` | `wall.IsWrappingAtLocationAllowed(locationIndex)` | Boolean |
| `Void RemoveAttachment(ElementId)` | `wall.RemoveAttachment(targetId)` | Void |
| `Void RemoveAttachment(ElementId, AttachmentLocation)` | `wall.RemoveAttachment(targetId, attachmentLocation)` | Void |
| `Void RemoveProfileSketch()` | `wall.RemoveProfileSketch()` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
