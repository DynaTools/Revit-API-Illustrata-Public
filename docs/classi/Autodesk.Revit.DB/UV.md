---
title: UV
classe: Autodesk.Revit.DB.UV
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 21
---

# UV

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `UV BasisU { get; }` | `UV.BasisU` | UV |
| `UV BasisV { get; }` | `UV.BasisV` | UV |
| `Double Item { get; }` | `uV.Item` | Double |
| `Double U { get; }` | `uV.U` | Double |
| `Double V { get; }` | `uV.V` | Double |
| `UV Zero { get; }` | `UV.Zero` | UV |
| `UV Add(UV)` | `uV.Add(source)` | UV |
| `Double AngleTo(UV)` | `uV.AngleTo(source)` | Double |
| `Double CrossProduct(UV)` | `uV.CrossProduct(source)` | Double |
| `Double DistanceTo(UV)` | `uV.DistanceTo(source)` | Double |
| `UV Divide(Double)` | `uV.Divide(value)` | UV |
| `Double DotProduct(UV)` | `uV.DotProduct(source)` | Double |
| `Double GetLength()` | `uV.GetLength()` | Double |
| `Boolean IsAlmostEqualTo(UV, Double)` | `uV.IsAlmostEqualTo(source, tolerance)` | Boolean |
| `Boolean IsAlmostEqualTo(UV)` | `uV.IsAlmostEqualTo(source)` | Boolean |
| `Boolean IsUnitLength()` | `uV.IsUnitLength()` | Boolean |
| `Boolean IsZeroLength()` | `uV.IsZeroLength()` | Boolean |
| `UV Multiply(Double)` | `uV.Multiply(value)` | UV |
| `UV Negate()` | `uV.Negate()` | UV |
| `UV Normalize()` | `uV.Normalize()` | UV |
| `UV Subtract(UV)` | `uV.Subtract(source)` | UV |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
