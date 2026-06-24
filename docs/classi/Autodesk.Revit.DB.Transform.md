---
title: Transform
classe: Autodesk.Revit.DB.Transform
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 23
---

# Transform

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ Basis { get; set; }` | `transform.Basis` | XYZ |
| `XYZ BasisX { get; set; }` | `transform.BasisX` | XYZ |
| `XYZ BasisY { get; set; }` | `transform.BasisY` | XYZ |
| `XYZ BasisZ { get; set; }` | `transform.BasisZ` | XYZ |
| `Double Determinant { get; }` | `transform.Determinant` | Double |
| `Boolean HasReflection { get; }` | `transform.HasReflection` | Boolean |
| `Transform Identity { get; }` | `Transform.Identity` | Transform |
| `Transform Inverse { get; }` | `transform.Inverse` | Transform |
| `Boolean IsConformal { get; }` | `transform.IsConformal` | Boolean |
| `Boolean IsIdentity { get; }` | `transform.IsIdentity` | Boolean |
| `Boolean IsTranslation { get; }` | `transform.IsTranslation` | Boolean |
| `XYZ Origin { get; set; }` | `transform.Origin` | XYZ |
| `Double Scale { get; }` | `transform.Scale` | Double |
| `Boolean AlmostEqual(Transform)` | `transform.AlmostEqual(right)` | Boolean |
| `Transform CreateReflection(Plane)` | `Transform.CreateReflection(plane)` | Transform |
| `Transform CreateRotation(XYZ, Double)` | `Transform.CreateRotation(axis, angle)` | Transform |
| `Transform CreateRotationAtPoint(XYZ, Double, XYZ)` | `Transform.CreateRotationAtPoint(axis, angle, origin)` | Transform |
| `Transform CreateTranslation(XYZ)` | `Transform.CreateTranslation(vector)` | Transform |
| `Transform Multiply(Transform)` | `transform.Multiply(right)` | Transform |
| `XYZ OfPoint(XYZ)` | `transform.OfPoint(point)` | XYZ |
| `XYZ OfVector(XYZ)` | `transform.OfVector(vec)` | XYZ |
| `Transform ScaleBasis(Double)` | `transform.ScaleBasis(scale)` | Transform |
| `Transform ScaleBasisAndOrigin(Double)` | `transform.ScaleBasisAndOrigin(scale)` | Transform |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
