---
title: RebarSpliceUtils
classe: Autodesk.Revit.DB.Structure.RebarSpliceUtils
namespace: Autodesk.Revit.DB.Structure
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# RebarSpliceUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `RebarSpliceError CanRebarBeSpliced(Rebar, RebarSpliceOptions, Line, XYZ)` | `RebarSpliceUtils.CanRebarBeSpliced(rebar, spliceOptions, line, linePlaneNormal)` | RebarSpliceError |
| `RebarSpliceError CanRebarBeSpliced(Rebar, RebarSpliceOptions, Line, ElementId)` | `RebarSpliceUtils.CanRebarBeSpliced(rebar, spliceOptions, line, viewId)` | RebarSpliceError |
| `RebarSpliceError CanRebarBeSpliced(Rebar, RebarSpliceOptions, RebarSpliceGeometry)` | `RebarSpliceUtils.CanRebarBeSpliced(rebar, spliceOptions, spliceGeometry)` | RebarSpliceError |
| `XYZ GetLapDirectionForSpliceGeometryAndPosition(Rebar, RebarSpliceGeometry, RebarSplicePosition)` | `RebarSpliceUtils.GetLapDirectionForSpliceGeometryAndPosition(rebar, spliceGeometry, splicePosition)` | XYZ |
| `IList<ElementId> GetSpliceChain(Rebar)` | `RebarSpliceUtils.GetSpliceChain(rebar)` | IList<ElementId> |
| `RebarSpliceByRulesResult GetSpliceGeometries(Document, ElementId, RebarSpliceOptions, RebarSpliceRules)` | `RebarSpliceUtils.GetSpliceGeometries(document, rebarIdToSplit, spliceOptions, spliceRules)` | RebarSpliceByRulesResult |
| `IList<ElementId> SpliceRebar(Document, ElementId, RebarSpliceOptions, Line, XYZ)` | `RebarSpliceUtils.SpliceRebar(document, rebarIdToSplit, spliceOptions, line, linePlaneNormal)` | IList<ElementId> |
| `IList<ElementId> SpliceRebar(Document, ElementId, RebarSpliceOptions, Line, ElementId)` | `RebarSpliceUtils.SpliceRebar(document, rebarIdToSplit, spliceOptions, line, viewId)` | IList<ElementId> |
| `IList<ElementId> SpliceRebar(Document, ElementId, RebarSpliceOptions, IList<RebarSpliceGeometry>)` | `RebarSpliceUtils.SpliceRebar(document, rebarIdToSplit, spliceOptions, spliceGeometries)` | IList<ElementId> |
| `ElementId UnifyRebarsIntoOne(Document, ElementId, ElementId)` | `RebarSpliceUtils.UnifyRebarsIntoOne(document, firstRebarId, secondRebarId)` | ElementId |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
