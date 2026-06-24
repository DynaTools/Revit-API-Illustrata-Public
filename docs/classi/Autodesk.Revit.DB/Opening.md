---
title: Opening
classe: Autodesk.Revit.DB.Opening
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# Opening

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `CurveArray BoundaryCurves { get; }` | `opening.BoundaryCurves` | CurveArray |
| `IList<XYZ> BoundaryRect { get; }` | `opening.BoundaryRect` | IList<XYZ> |
| `Element Host { get; }` | `opening.Host` | Element |
| `Boolean IsRectBoundary { get; }` | `opening.IsRectBoundary` | Boolean |
| `Boolean IsTransparentIn3D { get; set; }` | `opening.IsTransparentIn3D` | Boolean |
| `Boolean IsTransparentInElevation { get; set; }` | `opening.IsTransparentInElevation` | Boolean |
| `ElementId SketchId { get; }` | `opening.SketchId` | ElementId |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
