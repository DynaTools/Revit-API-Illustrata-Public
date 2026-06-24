---
title: Transform1D
classe: Autodesk.Revit.DB.Transform1D
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 14
---

# Transform1D

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double Determinant { get; }` | `transform1D.Determinant` | Double |
| `Boolean IsIdentity { get; }` | `transform1D.IsIdentity` | Boolean |
| `Boolean IsValidObject { get; }` | `transform1D.IsValidObject` | Boolean |
| `Double Scale { get; set; }` | `transform1D.Scale` | Double |
| `Double Translation { get; set; }` | `transform1D.Translation` | Double |
| `Boolean AlmostEqual(Transform1D)` | `transform1D.AlmostEqual(right)` | Boolean |
| `Void Assign(Transform1D)` | `transform1D.Assign(from)` | Void |
| `Void Dispose()` | `transform1D.Dispose()` | Void |
| `Transform1D GetInverse()` | `transform1D.GetInverse()` | Transform1D |
| `Transform1D Multiply(Transform1D)` | `transform1D.Multiply(right)` | Transform1D |
| `Double OfPoint(Double)` | `transform1D.OfPoint(point)` | Double |
| `Double OfVector(Double)` | `transform1D.OfVector(vector)` | Double |
| `Transform1D SetToIdentity()` | `transform1D.SetToIdentity()` | Transform1D |
| `IList<Double> TransformParameterDomain(Double, Double)` | `transform1D.TransformParameterDomain(domainStart, domainEnd)` | IList<Double> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
