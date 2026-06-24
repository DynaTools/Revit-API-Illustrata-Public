---
title: ElevationMarker
classe: Autodesk.Revit.DB.ElevationMarker
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# ElevationMarker

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 CurrentViewCount { get; }` | `elevationMarker.CurrentViewCount` | Int32 |
| `Boolean IsReference { get; }` | `elevationMarker.IsReference` | Boolean |
| `Int32 MaximumViewCount { get; }` | `elevationMarker.MaximumViewCount` | Int32 |
| `ViewSection CreateElevation(Document, ElementId, Int32)` | `elevationMarker.CreateElevation(document, viewPlanId, index)` | ViewSection |
| `ElevationMarker CreateElevationMarker(Document, ElementId, XYZ, Int32)` | `ElevationMarker.CreateElevationMarker(document, viewFamilyTypeId, origin, initialViewScale)` | ElevationMarker |
| `Void CreateReferenceElevation(Document, Int32, ElementId)` | `elevationMarker.CreateReferenceElevation(document, index, viewIdToReference)` | Void |
| `ElevationMarker CreateReferenceElevationMarker(Document, ElementId, XYZ, ElementId)` | `ElevationMarker.CreateReferenceElevationMarker(document, viewFamilyTypeId, origin, viewPlanId)` | ElevationMarker |
| `ElementId GetViewId(Int32)` | `elevationMarker.GetViewId(index)` | ElementId |
| `Boolean HasElevations()` | `elevationMarker.HasElevations()` | Boolean |
| `Boolean IsAvailableIndex(Int32)` | `elevationMarker.IsAvailableIndex(index)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
