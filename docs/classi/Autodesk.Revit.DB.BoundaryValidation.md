---
title: BoundaryValidation
classe: Autodesk.Revit.DB.BoundaryValidation
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 5
---

# BoundaryValidation

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `boundaryValidation.IsValidObject` | Boolean |
| `Void Dispose()` | `boundaryValidation.Dispose()` | Void |
| `Boolean IsValidBoundaryOnSketchPlane(SketchPlane, IList<CurveLoop>)` | `BoundaryValidation.IsValidBoundaryOnSketchPlane(sketchPlane, curveLoops)` | Boolean |
| `Boolean IsValidBoundaryOnView(Document, ElementId, IList<CurveLoop>)` | `BoundaryValidation.IsValidBoundaryOnView(document, viewId, curveLoops)` | Boolean |
| `Boolean IsValidHorizontalBoundary(IList<CurveLoop>)` | `BoundaryValidation.IsValidHorizontalBoundary(curveLoops)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
