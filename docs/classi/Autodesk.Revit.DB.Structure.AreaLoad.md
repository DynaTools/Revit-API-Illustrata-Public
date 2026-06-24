---
title: AreaLoad
classe: Autodesk.Revit.DB.Structure.AreaLoad
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Structure.LoadBase
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 15
---

# AreaLoad

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double Area { get; }` | `areaLoad.Area` | Double |
| `XYZ ForceVector1 { get; set; }` | `areaLoad.ForceVector1` | XYZ |
| `XYZ ForceVector2 { get; set; }` | `areaLoad.ForceVector2` | XYZ |
| `XYZ ForceVector3 { get; set; }` | `areaLoad.ForceVector3` | XYZ |
| `Boolean IsProjected { get; set; }` | `areaLoad.IsProjected` | Boolean |
| `Int32 NumRefPoints { get; }` | `areaLoad.NumRefPoints` | Int32 |
| `Boolean AreCurveLoopsValid(IList<CurveLoop>)` | `AreaLoad.AreCurveLoopsValid(loops)` | Boolean |
| `AreaLoad Create(Document, ElementId, IList<CurveLoop>, IList<XYZ>, IList<Int32>, IList<Int32>, AreaLoadType)` | `AreaLoad.Create(document, hostElemId, loops, forceVectors, refPointCurveIndexes, refPointCurveEnds, symbol)` | AreaLoad |
| `AreaLoad Create(Document, ElementId, IList<CurveLoop>, XYZ, AreaLoadType)` | `AreaLoad.Create(document, hostElemId, loops, forceVector, symbol)` | AreaLoad |
| `AreaLoad Create(Document, ElementId, XYZ, AreaLoadType)` | `AreaLoad.Create(document, hostElemId, forceVector, symbol)` | AreaLoad |
| `IList<CurveLoop> GetLoops()` | `areaLoad.GetLoops()` | IList<CurveLoop> |
| `XYZ GetRefPoint(Int32)` | `areaLoad.GetRefPoint(index)` | XYZ |
| `Boolean IsCurveLoopsInsideHostBoundaries(Document, ElementId, IList<CurveLoop>)` | `AreaLoad.IsCurveLoopsInsideHostBoundaries(doc, hostId, loops)` | Boolean |
| `Boolean IsValidHostId(Document, ElementId)` | `AreaLoad.IsValidHostId(pDoc, hostId)` | Boolean |
| `Boolean SetLoops(Document, IList<CurveLoop>)` | `areaLoad.SetLoops(doc, newLoops)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
