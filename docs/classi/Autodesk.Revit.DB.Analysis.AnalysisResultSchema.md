---
title: AnalysisResultSchema
classe: Autodesk.Revit.DB.Analysis.AnalysisResultSchema
namespace: Autodesk.Revit.DB.Analysis
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# AnalysisResultSchema

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId AnalysisDisplayStyleId { get; set; }` | `analysisResultSchema.AnalysisDisplayStyleId` | ElementId |
| `Int32 CurrentUnits { get; set; }` | `analysisResultSchema.CurrentUnits` | Int32 |
| `String Description { get; set; }` | `analysisResultSchema.Description` | String |
| `Boolean IsValidObject { get; }` | `analysisResultSchema.IsValidObject` | Boolean |
| `Boolean IsVisible { get; set; }` | `analysisResultSchema.IsVisible` | Boolean |
| `String Name { get; set; }` | `analysisResultSchema.Name` | String |
| `Double Scale { get; set; }` | `analysisResultSchema.Scale` | Double |
| `Void Dispose()` | `analysisResultSchema.Dispose()` | Void |
| `Int32 GetNumberOfUnits()` | `analysisResultSchema.GetNumberOfUnits()` | Int32 |
| `Double GetUnitsMultiplier(Int32)` | `analysisResultSchema.GetUnitsMultiplier(index)` | Double |
| `String GetUnitsName(Int32)` | `analysisResultSchema.GetUnitsName(index)` | String |
| `Boolean IsEqual(AnalysisResultSchema)` | `analysisResultSchema.IsEqual(other)` | Boolean |
| `Void SetUnits(IList<String>, IList<Double>)` | `analysisResultSchema.SetUnits(names, multipliers)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
