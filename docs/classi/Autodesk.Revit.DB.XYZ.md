---
title: XYZ
classe: Autodesk.Revit.DB.XYZ
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 26
---

# XYZ

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ BasisX { get; }` | `XYZ.BasisX` | XYZ |
| `XYZ BasisY { get; }` | `XYZ.BasisY` | XYZ |
| `XYZ BasisZ { get; }` | `XYZ.BasisZ` | XYZ |
| `Double Item { get; }` | `xYZ.Item` | Double |
| `Double X { get; }` | `xYZ.X` | Double |
| `Double Y { get; }` | `xYZ.Y` | Double |
| `Double Z { get; }` | `xYZ.Z` | Double |
| `XYZ Zero { get; }` | `XYZ.Zero` | XYZ |
| `XYZ Add(XYZ)` | `xYZ.Add(source)` | XYZ |
| `Double AngleOnPlaneTo(XYZ, XYZ)` | `xYZ.AngleOnPlaneTo(right, normal)` | Double |
| `Double AngleTo(XYZ)` | `xYZ.AngleTo(source)` | Double |
| `XYZ CrossProduct(XYZ)` | `xYZ.CrossProduct(source)` | XYZ |
| `Double DistanceTo(XYZ)` | `xYZ.DistanceTo(source)` | Double |
| `XYZ Divide(Double)` | `xYZ.Divide(value)` | XYZ |
| `Double DotProduct(XYZ)` | `xYZ.DotProduct(source)` | Double |
| `Double GetLength()` | `xYZ.GetLength()` | Double |
| `Boolean IsAlmostEqualTo(XYZ, Double)` | `xYZ.IsAlmostEqualTo(source, tolerance)` | Boolean |
| `Boolean IsAlmostEqualTo(XYZ)` | `xYZ.IsAlmostEqualTo(source)` | Boolean |
| `Boolean IsUnitLength()` | `xYZ.IsUnitLength()` | Boolean |
| `Boolean IsWithinLengthLimits(XYZ)` | `XYZ.IsWithinLengthLimits(point)` | Boolean |
| `Boolean IsZeroLength()` | `xYZ.IsZeroLength()` | Boolean |
| `XYZ Multiply(Double)` | `xYZ.Multiply(value)` | XYZ |
| `XYZ Negate()` | `xYZ.Negate()` | XYZ |
| `XYZ Normalize()` | `xYZ.Normalize()` | XYZ |
| `XYZ Subtract(XYZ)` | `xYZ.Subtract(source)` | XYZ |
| `Double TripleProduct(XYZ, XYZ)` | `xYZ.TripleProduct(middle, right)` | Double |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
