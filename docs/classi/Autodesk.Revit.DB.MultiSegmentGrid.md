---
title: MultiSegmentGrid
classe: Autodesk.Revit.DB.MultiSegmentGrid
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# MultiSegmentGrid

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String Text { get; set; }` | `multiSegmentGrid.Text` | String |
| `Boolean AreGridsInSameMultiSegmentGrid(Grid, Grid)` | `MultiSegmentGrid.AreGridsInSameMultiSegmentGrid(grid1, grid2)` | Boolean |
| `ElementId Create(Document, ElementId, CurveLoop, ElementId)` | `MultiSegmentGrid.Create(document, typeId, curveLoop, sketchPlaneId)` | ElementId |
| `ICollection<ElementId> GetGridIds()` | `multiSegmentGrid.GetGridIds()` | ICollection<ElementId> |
| `ElementId GetMultiSegementGridId(Grid)` | `MultiSegmentGrid.GetMultiSegementGridId(grid)` | ElementId |
| `Boolean IsValidCurveLoop(CurveLoop)` | `MultiSegmentGrid.IsValidCurveLoop(curveLoop)` | Boolean |
| `Boolean IsValidSketchPlaneId(Document, ElementId)` | `MultiSegmentGrid.IsValidSketchPlaneId(document, elemId)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
