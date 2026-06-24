---
title: PathOfTravel
classe: Autodesk.Revit.DB.Analysis.PathOfTravel
namespace: Autodesk.Revit.DB.Analysis
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 23
---

# PathOfTravel

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId LineStyle { get; set; }` | `pathOfTravel.LineStyle` | ElementId |
| `XYZ PathEnd { get; set; }` | `pathOfTravel.PathEnd` | XYZ |
| `XYZ PathMidpoint { get; }` | `pathOfTravel.PathMidpoint` | XYZ |
| `XYZ PathStart { get; set; }` | `pathOfTravel.PathStart` | XYZ |
| `PathOfTravel Create(View, XYZ, XYZ)` | `PathOfTravel.Create(DBView, pathStart, pathEnd)` | PathOfTravel |
| `PathOfTravel Create(View, XYZ, XYZ, PathOfTravelCalculationStatus&)` | `PathOfTravel.Create(DBView, pathStart, pathEnd, resultStatus)` | PathOfTravel |
| `IList<PathOfTravel> CreateMapped(View, IList<XYZ>, IList<XYZ>)` | `PathOfTravel.CreateMapped(DBView, pathStarts, pathEnds)` | IList<PathOfTravel> |
| `IList<PathOfTravel> CreateMapped(View, IList<XYZ>, IList<XYZ>, IList<PathOfTravelCalculationStatus>&)` | `PathOfTravel.CreateMapped(DBView, pathStarts, pathEnds, resultStatus)` | IList<PathOfTravel> |
| `IList<PathOfTravel> CreateMultiple(View, IList<XYZ>, IList<XYZ>, IList<PathOfTravelCalculationStatus>&)` | `PathOfTravel.CreateMultiple(DBView, pathStarts, pathEnds, resultStatus)` | IList<PathOfTravel> |
| `IList<PathOfTravel> CreateMultiple(View, IList<XYZ>, IList<XYZ>)` | `PathOfTravel.CreateMultiple(DBView, pathStarts, pathEnds)` | IList<PathOfTravel> |
| `IList<XYZ> FindEndsOfShortestPaths(View, IList<XYZ>, IList<XYZ>)` | `PathOfTravel.FindEndsOfShortestPaths(DBView, destinationPoints, startPoints)` | IList<XYZ> |
| `IList<IList<XYZ>> FindShortestPaths(View, IList<XYZ>, IList<XYZ>)` | `PathOfTravel.FindShortestPaths(DBView, destinationPoints, startPoints)` | IList<IList<XYZ>> |
| `IList<XYZ> FindStartsOfLongestPathsFromRooms(View, IList<XYZ>)` | `PathOfTravel.FindStartsOfLongestPathsFromRooms(DBView, destinationPoints)` | IList<XYZ> |
| `IList<Curve> GetCurves()` | `pathOfTravel.GetCurves()` | IList<Curve> |
| `IList<XYZ> GetWaypoints()` | `pathOfTravel.GetWaypoints()` | IList<XYZ> |
| `Void InsertWaypoint(XYZ, Int32)` | `pathOfTravel.InsertWaypoint(waypoint, index)` | Void |
| `Boolean IsInRevealObstaclesMode(View)` | `PathOfTravel.IsInRevealObstaclesMode(DBView)` | Boolean |
| `Void RemoveWaypoint(Int32)` | `pathOfTravel.RemoveWaypoint(index)` | Void |
| `PathOfTravelCalculationStatus SetRevealObstaclesMode(View, Boolean)` | `PathOfTravel.SetRevealObstaclesMode(DBView, newState)` | PathOfTravelCalculationStatus |
| `Void SetWaypoint(XYZ, Int32)` | `pathOfTravel.SetWaypoint(waypoint, index)` | Void |
| `PathOfTravelCalculationStatus Update()` | `pathOfTravel.Update()` | PathOfTravelCalculationStatus |
| `Int32 UpdateMultiple(Document, IList<ElementId>, IList<PathOfTravelCalculationStatus>&)` | `PathOfTravel.UpdateMultiple(adoc, elementsToUpdate, resultStatus)` | Int32 |
| `Int32 UpdateMultiple(Document, IList<ElementId>)` | `PathOfTravel.UpdateMultiple(adoc, elementsToUpdate)` | Int32 |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
