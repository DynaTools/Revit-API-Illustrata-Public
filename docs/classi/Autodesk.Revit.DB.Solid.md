---
title: Solid
classe: Autodesk.Revit.DB.Solid
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.GeometryObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# Solid

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `EdgeArray Edges { get; }` | `solid.Edges` | EdgeArray |
| `FaceArray Faces { get; }` | `solid.Faces` | FaceArray |
| `Double SurfaceArea { get; }` | `solid.SurfaceArea` | Double |
| `Double Volume { get; }` | `solid.Volume` | Double |
| `XYZ ComputeCentroid()` | `solid.ComputeCentroid()` | XYZ |
| `BoundingBoxXYZ GetBoundingBox()` | `solid.GetBoundingBox()` | BoundingBoxXYZ |
| `SolidCurveIntersection IntersectWithCurve(Curve, SolidCurveIntersectionOptions)` | `solid.IntersectWithCurve(curve, options)` | SolidCurveIntersection |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
