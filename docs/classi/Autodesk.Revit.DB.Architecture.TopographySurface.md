---
title: TopographySurface
classe: Autodesk.Revit.DB.Architecture.TopographySurface
namespace: Autodesk.Revit.DB.Architecture
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 24
---

# TopographySurface

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean ArePointsEditable { get; }` | `topographySurface.ArePointsEditable` | Boolean |
| `ElementId AssociatedBuildingPadId { get; }` | `topographySurface.AssociatedBuildingPadId` | ElementId |
| `Boolean IsAssociatedWithBuildingPad { get; }` | `topographySurface.IsAssociatedWithBuildingPad` | Boolean |
| `Boolean IsSiteSubRegion { get; }` | `topographySurface.IsSiteSubRegion` | Boolean |
| `ElementId MaterialId { get; set; }` | `topographySurface.MaterialId` | ElementId |
| `Void AddPoints(IList<XYZ>)` | `topographySurface.AddPoints(points)` | Void |
| `Boolean ArePointsDistinct(IList<XYZ>)` | `TopographySurface.ArePointsDistinct(points)` | Boolean |
| `SiteSubRegion AsSiteSubRegion()` | `topographySurface.AsSiteSubRegion()` | SiteSubRegion |
| `Void ChangePointElevation(XYZ, Double)` | `topographySurface.ChangePointElevation(point, elevationValue)` | Void |
| `Void ChangePointsElevation(IList<XYZ>, Double)` | `topographySurface.ChangePointsElevation(points, elevationValue)` | Void |
| `Boolean ContainsPoint(XYZ)` | `topographySurface.ContainsPoint(point)` | Boolean |
| `TopographySurface Create(Document, IList<XYZ>, IList<PolymeshFacet>)` | `TopographySurface.Create(document, points, facets)` | TopographySurface |
| `TopographySurface Create(Document, IList<XYZ>)` | `TopographySurface.Create(document, points)` | TopographySurface |
| `Void DeletePoints(IList<XYZ>)` | `topographySurface.DeletePoints(points)` | Void |
| `IList<XYZ> FindPoints(Outline)` | `topographySurface.FindPoints(boundingBox)` | IList<XYZ> |
| `IList<XYZ> GetBoundaryPoints()` | `topographySurface.GetBoundaryPoints()` | IList<XYZ> |
| `IList<ElementId> GetHostedSubRegionIds()` | `topographySurface.GetHostedSubRegionIds()` | IList<ElementId> |
| `IList<XYZ> GetInteriorPoints()` | `topographySurface.GetInteriorPoints()` | IList<XYZ> |
| `IList<XYZ> GetPoints()` | `topographySurface.GetPoints()` | IList<XYZ> |
| `Boolean IsBoundaryPoint(XYZ)` | `topographySurface.IsBoundaryPoint(point)` | Boolean |
| `Boolean IsValidFaceSet(IList<PolymeshFacet>, IList<XYZ>)` | `TopographySurface.IsValidFaceSet(facets, points)` | Boolean |
| `Boolean IsValidRegion(IList<XYZ>)` | `TopographySurface.IsValidRegion(points)` | Boolean |
| `Void MovePoint(XYZ, XYZ)` | `topographySurface.MovePoint(movedPoint, targetPoint)` | Void |
| `Void MovePoints(IList<XYZ>, XYZ)` | `topographySurface.MovePoints(movedPoints, moveVector)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
