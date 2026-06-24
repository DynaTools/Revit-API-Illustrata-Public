---
title: Face
classe: Autodesk.Revit.DB.Face
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.GeometryObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 26
---

# Face

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double Area { get; }` | `face.Area` | Double |
| `EdgeArrayArray EdgeLoops { get; }` | `face.EdgeLoops` | EdgeArrayArray |
| `Boolean HasRegions { get; }` | `face.HasRegions` | Boolean |
| `Boolean IsCyclic { get; }` | `face.IsCyclic` | Boolean |
| `Boolean IsTwoSided { get; }` | `face.IsTwoSided` | Boolean |
| `ElementId MaterialElementId { get; }` | `face.MaterialElementId` | ElementId |
| `Boolean OrientationMatchesSurfaceOrientation { get; }` | `face.OrientationMatchesSurfaceOrientation` | Boolean |
| `Double Period { get; }` | `face.Period` | Double |
| `Reference Reference { get; }` | `face.Reference` | Reference |
| `Transform ComputeDerivatives(UV)` | `face.ComputeDerivatives(point)` | Transform |
| `XYZ ComputeNormal(UV)` | `face.ComputeNormal(point)` | XYZ |
| `FaceSecondDerivatives ComputeSecondDerivatives(UV)` | `face.ComputeSecondDerivatives(point)` | FaceSecondDerivatives |
| `XYZ Evaluate(UV)` | `face.Evaluate(params)` | XYZ |
| `BoundingBoxUV GetBoundingBox()` | `face.GetBoundingBox()` | BoundingBoxUV |
| `IList<CurveLoop> GetEdgesAsCurveLoops()` | `face.GetEdgesAsCurveLoops()` | IList<CurveLoop> |
| `IList<Face> GetRegions()` | `face.GetRegions()` | IList<Face> |
| `Surface GetSurface()` | `face.GetSurface()` | Surface |
| `FaceIntersectionFaceResult Intersect(Face, Curve&)` | `face.Intersect(face, result)` | FaceIntersectionFaceResult |
| `FaceIntersectionFaceResult Intersect(Face)` | `face.Intersect(face)` | FaceIntersectionFaceResult |
| `SetComparisonResult Intersect(Curve, IntersectionResultArray&)` | `face.Intersect(curve, results)` | SetComparisonResult |
| `SetComparisonResult Intersect(Curve)` | `face.Intersect(curve)` | SetComparisonResult |
| `Boolean IsInside(UV, IntersectionResult&)` | `face.IsInside(point, result)` | Boolean |
| `Boolean IsInside(UV)` | `face.IsInside(point)` | Boolean |
| `IntersectionResult Project(XYZ)` | `face.Project(point)` | IntersectionResult |
| `Mesh Triangulate(Double)` | `face.Triangulate(levelOfDetail)` | Mesh |
| `Mesh Triangulate()` | `face.Triangulate()` | Mesh |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
