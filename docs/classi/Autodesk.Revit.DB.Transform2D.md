---
title: Transform2D
classe: Autodesk.Revit.DB.Transform2D
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 22
---

# Transform2D

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `UV BasisU { get; set; }` | `transform2D.BasisU` | UV |
| `UV BasisV { get; set; }` | `transform2D.BasisV` | UV |
| `Double Determinant { get; }` | `transform2D.Determinant` | Double |
| `Boolean HasReflection { get; }` | `transform2D.HasReflection` | Boolean |
| `Boolean IsConformal { get; }` | `transform2D.IsConformal` | Boolean |
| `Boolean IsIdentity { get; }` | `transform2D.IsIdentity` | Boolean |
| `Boolean IsTranslation { get; }` | `transform2D.IsTranslation` | Boolean |
| `Boolean IsValidObject { get; }` | `transform2D.IsValidObject` | Boolean |
| `UV Origin { get; set; }` | `transform2D.Origin` | UV |
| `Double Scale { get; }` | `transform2D.Scale` | Double |
| `Boolean AlmostEqual(Transform2D)` | `transform2D.AlmostEqual(right)` | Boolean |
| `Void Assign(Transform2D)` | `transform2D.Assign(from)` | Void |
| `Transform2D CreateIdentity()` | `Transform2D.CreateIdentity()` | Transform2D |
| `Void Dispose()` | `transform2D.Dispose()` | Void |
| `Transform2D GetInverse()` | `transform2D.GetInverse()` | Transform2D |
| `Transform2D Multiply(Transform2D)` | `transform2D.Multiply(right)` | Transform2D |
| `UV OfPoint(UV)` | `transform2D.OfPoint(point)` | UV |
| `UV OfVector(UV)` | `transform2D.OfVector(vector)` | UV |
| `Transform2D PostScale(Double)` | `transform2D.PostScale(scale)` | Transform2D |
| `Transform2D PreScale(Double)` | `transform2D.PreScale(scale)` | Transform2D |
| `Transform2D SetToIdentity()` | `transform2D.SetToIdentity()` | Transform2D |
| `BoundingBoxUV TransformUVDomainIfPossible(BoundingBoxUV)` | `transform2D.TransformUVDomainIfPossible(uvDomain)` | BoundingBoxUV |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
