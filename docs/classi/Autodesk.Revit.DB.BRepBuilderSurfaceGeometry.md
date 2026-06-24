---
title: BRepBuilderSurfaceGeometry
classe: Autodesk.Revit.DB.BRepBuilderSurfaceGeometry
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 5
---

# BRepBuilderSurfaceGeometry

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `bRepBuilderSurfaceGeometry.IsValidObject` | Boolean |
| `BRepBuilderSurfaceGeometry Create(Surface, BoundingBoxUV)` | `BRepBuilderSurfaceGeometry.Create(surface, surfaceEnvelope)` | BRepBuilderSurfaceGeometry |
| `BRepBuilderSurfaceGeometry CreateNURBSSurface(Int32, Int32, IList<Double>, IList<Double>, IList<XYZ>, IList<Double>, Boolean, BoundingBoxUV)` | `BRepBuilderSurfaceGeometry.CreateNURBSSurface(degreeU, degreeV, knotsU, knotsV, controlPoints, weights, bReverseOrientation, surfaceEnvelope)` | BRepBuilderSurfaceGeometry |
| `BRepBuilderSurfaceGeometry CreateNURBSSurface(Int32, Int32, IList<Double>, IList<Double>, IList<XYZ>, Boolean, BoundingBoxUV)` | `BRepBuilderSurfaceGeometry.CreateNURBSSurface(degreeU, degreeV, knotsU, knotsV, controlPoints, bReverseOrientation, surfaceEnvelope)` | BRepBuilderSurfaceGeometry |
| `Void Dispose()` | `bRepBuilderSurfaceGeometry.Dispose()` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
