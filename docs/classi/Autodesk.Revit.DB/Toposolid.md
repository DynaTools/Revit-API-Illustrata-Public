---
title: Toposolid
classe: Autodesk.Revit.DB.Toposolid
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.CeilingAndFloor
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 17
---

# Toposolid

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId HostTopoId { get; }` | `toposolid.HostTopoId` | ElementId |
| `ElementId SketchId { get; }` | `toposolid.SketchId` | ElementId |
| `Boolean CanBeExcavatedBy(ElementId)` | `toposolid.CanBeExcavatedBy(elementId)` | Boolean |
| `Toposolid Create(Document, IList<CurveLoop>, IList<XYZ>, ElementId, ElementId)` | `Toposolid.Create(document, profiles, points, topoTypeId, levelId)` | Toposolid |
| `Toposolid Create(Document, IList<XYZ>, ElementId, ElementId)` | `Toposolid.Create(document, points, topoTypeId, levelId)` | Toposolid |
| `Toposolid Create(Document, IList<CurveLoop>, ElementId, ElementId)` | `Toposolid.Create(document, profiles, topoTypeId, levelId)` | Toposolid |
| `Toposolid CreateFromTopographySurface(Document, ElementId, ElementId, ElementId)` | `Toposolid.CreateFromTopographySurface(document, hostSurfaceId, topoTypeId, levelId)` | Toposolid |
| `Toposolid CreateSubDivision(Document, IList<CurveLoop>)` | `toposolid.CreateSubDivision(document, profiles)` | Toposolid |
| `Void ExcavateBy(ElementId)` | `toposolid.ExcavateBy(elementId)` | Void |
| `IList<IntersectingElementData> GetIntersectingElementData()` | `toposolid.GetIntersectingElementData()` | IList<IntersectingElementData> |
| `SlabShapeEditor GetSlabShapeEditor()` | `toposolid.GetSlabShapeEditor()` | SlabShapeEditor |
| `IList<ElementId> GetSubDivisionIds()` | `toposolid.GetSubDivisionIds()` | IList<ElementId> |
| `Boolean IsSmoothedSurfaceEnabled(Document)` | `Toposolid.IsSmoothedSurfaceEnabled(document)` | Boolean |
| `Void RemoveExcavationBy(ElementId)` | `toposolid.RemoveExcavationBy(elementId)` | Void |
| `Void SetSmoothedSurface(Document, Boolean)` | `Toposolid.SetSmoothedSurface(document, enable)` | Void |
| `Void Simplify(Double)` | `toposolid.Simplify(percentage)` | Void |
| `IList<ElementId> Split(IList<CurveLoop>)` | `toposolid.Split(splitCurveLoops)` | IList<ElementId> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
