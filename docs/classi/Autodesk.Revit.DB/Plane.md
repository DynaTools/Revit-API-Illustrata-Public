---
title: Plane
classe: Autodesk.Revit.DB.Plane
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Surface
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# Plane

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ Normal { get; }` | `plane.Normal` | XYZ |
| `XYZ Origin { get; }` | `plane.Origin` | XYZ |
| `XYZ XVec { get; }` | `plane.XVec` | XYZ |
| `XYZ YVec { get; }` | `plane.YVec` | XYZ |
| `Plane Create(Frame)` | `Plane.Create(frameOfReference)` | Plane |
| `Plane CreateByNormalAndOrigin(XYZ, XYZ)` | `Plane.CreateByNormalAndOrigin(normal, origin)` | Plane |
| `Plane CreateByOriginAndBasis(XYZ, XYZ, XYZ)` | `Plane.CreateByOriginAndBasis(origin, basisX, basisY)` | Plane |
| `Plane CreateByThreePoints(XYZ, XYZ, XYZ)` | `Plane.CreateByThreePoints(point1, point2, point3)` | Plane |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
