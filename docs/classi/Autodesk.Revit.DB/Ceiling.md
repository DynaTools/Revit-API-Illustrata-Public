---
title: Ceiling
classe: Autodesk.Revit.DB.Ceiling
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.CeilingAndFloor
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 4
---

# Ceiling

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId SketchId { get; }` | `ceiling.SketchId` | ElementId |
| `Ceiling Create(Document, IList<CurveLoop>, ElementId, ElementId)` | `Ceiling.Create(document, curveLoops, ceilingTypeId, levelId)` | Ceiling |
| `Ceiling Create(Document, IList<CurveLoop>, ElementId, ElementId, Line, Double)` | `Ceiling.Create(document, curveLoops, ceilingTypeId, levelId, slopeArrow, slope)` | Ceiling |
| `IList<Curve> GetCeilingGridLines(Boolean)` | `ceiling.GetCeilingGridLines(includeBoundary)` | IList<Curve> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
