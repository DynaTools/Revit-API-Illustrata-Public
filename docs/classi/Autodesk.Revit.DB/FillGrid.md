---
title: FillGrid
classe: Autodesk.Revit.DB.FillGrid
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 16
---

# FillGrid

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double Angle { get; set; }` | `fillGrid.Angle` | Double |
| `Boolean IsValidObject { get; }` | `fillGrid.IsValidObject` | Boolean |
| `Double Offset { get; set; }` | `fillGrid.Offset` | Double |
| `UV Origin { get; set; }` | `fillGrid.Origin` | UV |
| `Double Shift { get; set; }` | `fillGrid.Shift` | Double |
| `Double CalculateLengthPerArea()` | `fillGrid.CalculateLengthPerArea()` | Double |
| `Double CalculateLinesPerLength()` | `fillGrid.CalculateLinesPerLength()` | Double |
| `Double CalculateStrokesPerArea()` | `fillGrid.CalculateStrokesPerArea()` | Double |
| `Void Dispose()` | `fillGrid.Dispose()` | Void |
| `UV GetHatchingDirection()` | `fillGrid.GetHatchingDirection()` | UV |
| `Int32 GetPointLineZone(UV, UV&)` | `fillGrid.GetPointLineZone(point, nearestPoint)` | Int32 |
| `Int32 GetPointLineZone(UV)` | `fillGrid.GetPointLineZone(point)` | Int32 |
| `UV GetSegmentDirection()` | `fillGrid.GetSegmentDirection()` | UV |
| `IList<Double> GetSegments()` | `fillGrid.GetSegments()` | IList<Double> |
| `Boolean IsEqual(FillGrid)` | `fillGrid.IsEqual(other)` | Boolean |
| `Void SetSegments(IList<Double>)` | `fillGrid.SetSegments(segArr)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
