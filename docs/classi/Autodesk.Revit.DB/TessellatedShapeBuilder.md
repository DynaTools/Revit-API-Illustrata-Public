---
title: TessellatedShapeBuilder
classe: Autodesk.Revit.DB.TessellatedShapeBuilder
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.ShapeBuilder
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 18
---

# TessellatedShapeBuilder

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `TessellatedShapeBuilderFallback Fallback { get; set; }` | `tessellatedShapeBuilder.Fallback` | TessellatedShapeBuilderFallback |
| `ElementId GraphicsStyleId { get; set; }` | `tessellatedShapeBuilder.GraphicsStyleId` | ElementId |
| `Boolean IsFaceSetOpen { get; }` | `tessellatedShapeBuilder.IsFaceSetOpen` | Boolean |
| `Int32 LogInteger { get; set; }` | `tessellatedShapeBuilder.LogInteger` | Int32 |
| `String LogString { get; set; }` | `tessellatedShapeBuilder.LogString` | String |
| `Int32 NumberOfCompletedFaceSets { get; }` | `tessellatedShapeBuilder.NumberOfCompletedFaceSets` | Int32 |
| `String OwnerInfo { get; set; }` | `tessellatedShapeBuilder.OwnerInfo` | String |
| `TessellatedShapeBuilderTarget Target { get; set; }` | `tessellatedShapeBuilder.Target` | TessellatedShapeBuilderTarget |
| `Void AddFace(TessellatedFace)` | `tessellatedShapeBuilder.AddFace(face)` | Void |
| `Boolean AreTargetAndFallbackCompatible(TessellatedShapeBuilderTarget, TessellatedShapeBuilderFallback)` | `tessellatedShapeBuilder.AreTargetAndFallbackCompatible(target, fallback)` | Boolean |
| `Void Build()` | `tessellatedShapeBuilder.Build()` | Void |
| `Void CancelConnectedFaceSet()` | `tessellatedShapeBuilder.CancelConnectedFaceSet()` | Void |
| `Void Clear()` | `tessellatedShapeBuilder.Clear()` | Void |
| `Void CloseConnectedFaceSet()` | `tessellatedShapeBuilder.CloseConnectedFaceSet()` | Void |
| `MeshFromGeometryOperationResult CreateMeshByExtrusion(IList<CurveLoop>, XYZ, Double, ElementId)` | `TessellatedShapeBuilder.CreateMeshByExtrusion(profileLoops, extrusionDirection, extrusionDistance, materialId)` | MeshFromGeometryOperationResult |
| `Boolean DoesFaceHaveEnoughLoopsAndVertices(TessellatedFace)` | `tessellatedShapeBuilder.DoesFaceHaveEnoughLoopsAndVertices(face)` | Boolean |
| `TessellatedShapeBuilderResult GetBuildResult()` | `tessellatedShapeBuilder.GetBuildResult()` | TessellatedShapeBuilderResult |
| `Void OpenConnectedFaceSet(Boolean)` | `tessellatedShapeBuilder.OpenConnectedFaceSet(isSolid)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
