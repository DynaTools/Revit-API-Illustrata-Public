---
title: FillPattern
classe: Autodesk.Revit.DB.FillPattern
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 17
---

# FillPattern

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 GridCount { get; }` | `fillPattern.GridCount` | Int32 |
| `FillPatternHostOrientation HostOrientation { get; set; }` | `fillPattern.HostOrientation` | FillPatternHostOrientation |
| `Boolean IsSolidFill { get; }` | `fillPattern.IsSolidFill` | Boolean |
| `Boolean IsValidObject { get; }` | `fillPattern.IsValidObject` | Boolean |
| `Double LengthPerArea { get; }` | `fillPattern.LengthPerArea` | Double |
| `Double LinesPerLength { get; }` | `fillPattern.LinesPerLength` | Double |
| `String Name { get; set; }` | `fillPattern.Name` | String |
| `Double StrokesPerArea { get; }` | `fillPattern.StrokesPerArea` | Double |
| `FillPatternTarget Target { get; set; }` | `fillPattern.Target` | FillPatternTarget |
| `Void Dispose()` | `fillPattern.Dispose()` | Void |
| `Boolean ExpandDots()` | `fillPattern.ExpandDots()` | Boolean |
| `Boolean ExportToPAT(IList<FillPattern>, String)` | `FillPattern.ExportToPAT(fillPatterns, filename)` | Boolean |
| `FillGrid GetFillGrid(Int32)` | `fillPattern.GetFillGrid(gridIdx)` | FillGrid |
| `IList<FillGrid> GetFillGrids()` | `fillPattern.GetFillGrids()` | IList<FillGrid> |
| `Boolean IsEqual(FillPattern)` | `fillPattern.IsEqual(other)` | Boolean |
| `Void SetFillGrid(Int32, FillGrid)` | `fillPattern.SetFillGrid(gridIdx, fillGrid)` | Void |
| `Void SetFillGrids(IList<FillGrid>)` | `fillPattern.SetFillGrids(fillGrids)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
