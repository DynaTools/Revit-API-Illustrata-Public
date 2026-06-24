---
title: DividedSurface
classe: Autodesk.Revit.DB.DividedSurface
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 29
---

# DividedSurface

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double AllGridRotation { get; set; }` | `dividedSurface.AllGridRotation` | Double |
| `BorderTile BorderTile { get; set; }` | `dividedSurface.BorderTile` | BorderTile |
| `ComponentRotation ComponentRotation { get; set; }` | `dividedSurface.ComponentRotation` | ComponentRotation |
| `Element Host { get; }` | `dividedSurface.Host` | Element |
| `Reference HostReference { get; }` | `dividedSurface.HostReference` | Reference |
| `Boolean IsComponentFlipped { get; set; }` | `dividedSurface.IsComponentFlipped` | Boolean |
| `Boolean IsComponentMirrored { get; set; }` | `dividedSurface.IsComponentMirrored` | Boolean |
| `Int32 NumberOfUGridlines { get; }` | `dividedSurface.NumberOfUGridlines` | Int32 |
| `Int32 NumberOfVGridlines { get; }` | `dividedSurface.NumberOfVGridlines` | Int32 |
| `Int32 UPatternIndent { get; set; }` | `dividedSurface.UPatternIndent` | Int32 |
| `SpacingRule USpacingRule { get; }` | `dividedSurface.USpacingRule` | SpacingRule |
| `Int32 VPatternIndent { get; set; }` | `dividedSurface.VPatternIndent` | Int32 |
| `SpacingRule VSpacingRule { get; }` | `dividedSurface.VSpacingRule` | SpacingRule |
| `Void AddIntersectionElement(ElementId)` | `dividedSurface.AddIntersectionElement(newIntersectionElemId)` | Void |
| `Boolean CanBeDivided(Document, Reference)` | `DividedSurface.CanBeDivided(document, reference)` | Boolean |
| `Boolean CanBeIntersectionElement(ElementId)` | `dividedSurface.CanBeIntersectionElement(id)` | Boolean |
| `DividedSurface Create(Document, Reference)` | `DividedSurface.Create(document, faceReference)` | DividedSurface |
| `ICollection<ElementId> GetAllIntersectionElements()` | `dividedSurface.GetAllIntersectionElements()` | ICollection<ElementId> |
| `DividedSurface GetDividedSurfaceForReference(Document, Reference)` | `DividedSurface.GetDividedSurfaceForReference(document, faceReference)` | DividedSurface |
| `GridNodeLocation GetGridNodeLocation(GridNode)` | `dividedSurface.GetGridNodeLocation(gridNode)` | GridNodeLocation |
| `Reference GetGridNodeReference(GridNode)` | `dividedSurface.GetGridNodeReference(gridNode)` | Reference |
| `UV GetGridNodeUV(GridNode)` | `dividedSurface.GetGridNodeUV(gridNode)` | UV |
| `Reference GetGridSegmentReference(GridNode, GridSegmentDirection)` | `dividedSurface.GetGridSegmentReference(gridNode, gridSegmentDirection)` | Reference |
| `IList<Reference> GetReferencesWithDividedSurfaces(Element)` | `DividedSurface.GetReferencesWithDividedSurfaces(host)` | IList<Reference> |
| `FamilyInstance GetTileFamilyInstance(GridNode, Int32)` | `dividedSurface.GetTileFamilyInstance(gridNode, tileIndex)` | FamilyInstance |
| `Reference GetTileReference(GridNode, Int32)` | `dividedSurface.GetTileReference(gridNode, tileIndex)` | Reference |
| `Boolean IsSeedNode(GridNode)` | `dividedSurface.IsSeedNode(gridNode)` | Boolean |
| `Void RemoveAllIntersectionElements()` | `dividedSurface.RemoveAllIntersectionElements()` | Void |
| `Void RemoveIntersectionElement(ElementId)` | `dividedSurface.RemoveIntersectionElement(referenceElemIdToRemove)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
