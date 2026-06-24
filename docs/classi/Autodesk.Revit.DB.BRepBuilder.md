---
title: BRepBuilder
classe: Autodesk.Revit.DB.BRepBuilder
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.ShapeBuilder
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 20
---

# BRepBuilder

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `BRepBuilderGeometryId AddCoEdge(BRepBuilderGeometryId, BRepBuilderGeometryId, Boolean)` | `bRepBuilder.AddCoEdge(loopId, edgeId, bCoEdgeIsReversed)` | BRepBuilderGeometryId |
| `BRepBuilderGeometryId AddEdge(BRepBuilderEdgeGeometry)` | `bRepBuilder.AddEdge(edgeGeom)` | BRepBuilderGeometryId |
| `BRepBuilderGeometryId AddFace(BRepBuilderSurfaceGeometry, Boolean)` | `bRepBuilder.AddFace(surfaceGeom, bFaceIsReversed)` | BRepBuilderGeometryId |
| `BRepBuilderGeometryId AddLoop(BRepBuilderGeometryId)` | `bRepBuilder.AddLoop(faceId)` | BRepBuilderGeometryId |
| `Void AllowRemovalOfProblematicFaces()` | `bRepBuilder.AllowRemovalOfProblematicFaces()` | Void |
| `Boolean CanAddGeometry()` | `bRepBuilder.CanAddGeometry()` | Boolean |
| `BRepBuilderOutcome Finish()` | `bRepBuilder.Finish()` | BRepBuilderOutcome |
| `Void FinishFace(BRepBuilderGeometryId)` | `bRepBuilder.FinishFace(faceId)` | Void |
| `Void FinishLoop(BRepBuilderGeometryId)` | `bRepBuilder.FinishLoop(loopId)` | Void |
| `ExternallyTaggedBRep GetResult(ExternalGeometryId, BRepBuilderPersistentIds)` | `bRepBuilder.GetResult(externalId, brepPersistentIds)` | ExternallyTaggedBRep |
| `Solid GetResult()` | `bRepBuilder.GetResult()` | Solid |
| `Boolean IsPermittedSurfaceType(Surface)` | `BRepBuilder.IsPermittedSurfaceType(surface)` | Boolean |
| `Boolean IsResultAvailable()` | `bRepBuilder.IsResultAvailable()` | Boolean |
| `Boolean IsValidEdgeId(BRepBuilderGeometryId)` | `bRepBuilder.IsValidEdgeId(edgeId)` | Boolean |
| `Boolean IsValidFaceId(BRepBuilderGeometryId)` | `bRepBuilder.IsValidFaceId(faceId)` | Boolean |
| `Boolean IsValidLoopId(BRepBuilderGeometryId)` | `bRepBuilder.IsValidLoopId(loopId)` | Boolean |
| `Boolean IsValidPersistentIdsMap(BRepBuilderPersistentIds)` | `bRepBuilder.IsValidPersistentIdsMap(brepPersistentIds)` | Boolean |
| `Boolean RemovedSomeFaces()` | `bRepBuilder.RemovedSomeFaces()` | Boolean |
| `Void SetAllowShortEdges()` | `bRepBuilder.SetAllowShortEdges()` | Void |
| `Void SetFaceMaterialId(BRepBuilderGeometryId, ElementId)` | `bRepBuilder.SetFaceMaterialId(faceId, materialId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
