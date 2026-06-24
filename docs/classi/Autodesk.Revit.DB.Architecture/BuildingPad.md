---
title: BuildingPad
classe: Autodesk.Revit.DB.Architecture.BuildingPad
namespace: Autodesk.Revit.DB.Architecture
eredita: Autodesk.Revit.DB.CeilingAndFloor
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 5
---

# BuildingPad

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId AssociatedTopographySurfaceId { get; }` | `buildingPad.AssociatedTopographySurfaceId` | ElementId |
| `ElementId HostId { get; }` | `buildingPad.HostId` | ElementId |
| `BuildingPad Create(Document, ElementId, ElementId, IList<CurveLoop>)` | `BuildingPad.Create(document, buildingPadTypeId, levelId, curveLoops)` | BuildingPad |
| `IList<CurveLoop> GetBoundary()` | `buildingPad.GetBoundary()` | IList<CurveLoop> |
| `Void SetBoundary(IList<CurveLoop>)` | `buildingPad.SetBoundary(curveLoops)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
