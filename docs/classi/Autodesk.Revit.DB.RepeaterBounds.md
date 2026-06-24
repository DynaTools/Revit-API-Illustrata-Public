---
title: RepeaterBounds
classe: Autodesk.Revit.DB.RepeaterBounds
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# RepeaterBounds

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 DimensionCount { get; }` | `repeaterBounds.DimensionCount` | Int32 |
| `Boolean IsValidObject { get; }` | `repeaterBounds.IsValidObject` | Boolean |
| `RepeaterCoordinates AdjustForCyclicalBounds(RepeaterCoordinates)` | `repeaterBounds.AdjustForCyclicalBounds(coordinates)` | RepeaterCoordinates |
| `Boolean AreCoordinatesInBounds(RepeaterCoordinates, Boolean)` | `repeaterBounds.AreCoordinatesInBounds(coordinates, treatCyclicalBoundsAsInfinite)` | Boolean |
| `Void Dispose()` | `repeaterBounds.Dispose()` | Void |
| `Int32 GetLowerBound(Int32)` | `repeaterBounds.GetLowerBound(dimension)` | Int32 |
| `Int32 GetUpperBound(Int32)` | `repeaterBounds.GetUpperBound(dimension)` | Int32 |
| `Boolean IsCyclical(Int32)` | `repeaterBounds.IsCyclical(dimension)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
