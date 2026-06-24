---
title: AnalyticalSurfaceBase
classe: Autodesk.Revit.DB.Structure.AnalyticalSurfaceBase
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Structure.AnalyticalElement
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 5
---

# AnalyticalSurfaceBase

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId SketchId { get; }` | `analyticalSurfaceBase.SketchId` | ElementId |
| `CurveLoop GetOuterContour()` | `analyticalSurfaceBase.GetOuterContour()` | CurveLoop |
| `Boolean IsCurveLoopValid(CurveLoop)` | `AnalyticalSurfaceBase.IsCurveLoopValid(profile)` | Boolean |
| `Boolean IsOuterContourValid(CurveLoop)` | `analyticalSurfaceBase.IsOuterContourValid(contour)` | Boolean |
| `Void SetOuterContour(CurveLoop)` | `analyticalSurfaceBase.SetOuterContour(outerContour)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
