---
title: PointLoad
classe: Autodesk.Revit.DB.Structure.PointLoad
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Structure.LoadBase
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# PointLoad

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ ForceVector { get; set; }` | `pointLoad.ForceVector` | XYZ |
| `XYZ MomentVector { get; set; }` | `pointLoad.MomentVector` | XYZ |
| `XYZ Point { get; set; }` | `pointLoad.Point` | XYZ |
| `PointLoad Create(Document, ElementId, XYZ, XYZ, XYZ, PointLoadType)` | `PointLoad.Create(document, hostElemId, point, forceVector, momentVector, symbol)` | PointLoad |
| `PointLoad Create(Document, ElementId, AnalyticalElementSelector, XYZ, XYZ, PointLoadType)` | `PointLoad.Create(document, hostElemId, selector, forceVector, momentVector, symbol)` | PointLoad |
| `Boolean IsPointInsideHostBoundaries(Document, ElementId, XYZ)` | `PointLoad.IsPointInsideHostBoundaries(pDoc, hostId, point)` | Boolean |
| `Boolean IsValidHostId(Document, ElementId)` | `PointLoad.IsValidHostId(pDoc, hostId)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
