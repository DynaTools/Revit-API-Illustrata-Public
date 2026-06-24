---
title: StairsLanding
classe: Autodesk.Revit.DB.Architecture.StairsLanding
namespace: Autodesk.Revit.DB.Architecture
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# StairsLanding

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double BaseElevation { get; set; }` | `stairsLanding.BaseElevation` | Double |
| `Boolean IsAutomaticLanding { get; }` | `stairsLanding.IsAutomaticLanding` | Boolean |
| `Double Thickness { get; }` | `stairsLanding.Thickness` | Double |
| `Boolean CanCreateAutomaticLanding(Document, ElementId, ElementId)` | `StairsLanding.CanCreateAutomaticLanding(document, firstRunId, secondRunId)` | Boolean |
| `IList<ElementId> CreateAutomaticLanding(Document, ElementId, ElementId)` | `StairsLanding.CreateAutomaticLanding(document, firstRunId, secondRunId)` | IList<ElementId> |
| `StairsLanding CreateSketchedLanding(Document, ElementId, CurveLoop, Double)` | `StairsLanding.CreateSketchedLanding(document, stairsId, curveLoop, baseElevation)` | StairsLanding |
| `StairsLanding CreateSketchedLandingWithSlopeData(Document, ElementId, IList<SketchedStairsCurveData>, Double)` | `StairsLanding.CreateSketchedLandingWithSlopeData(document, stairsId, curveLoop, baseElevation)` | StairsLanding |
| `IList<ElementId> GetAllSupports()` | `stairsLanding.GetAllSupports()` | IList<ElementId> |
| `IList<StairsComponentConnection> GetConnections()` | `stairsLanding.GetConnections()` | IList<StairsComponentConnection> |
| `CurveLoop GetFootprintBoundary()` | `stairsLanding.GetFootprintBoundary()` | CurveLoop |
| `Stairs GetStairs()` | `stairsLanding.GetStairs()` | Stairs |
| `CurveLoop GetStairsPath()` | `stairsLanding.GetStairsPath()` | CurveLoop |
| `Void SetSketchedLandingBoundaryAndPath(Document, CurveLoop, CurveLoop)` | `stairsLanding.SetSketchedLandingBoundaryAndPath(document, boundaryCurveLoop, pathCurveLoop)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
