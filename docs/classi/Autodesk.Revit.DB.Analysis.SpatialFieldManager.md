---
title: SpatialFieldManager
classe: Autodesk.Revit.DB.Analysis.SpatialFieldManager
namespace: Autodesk.Revit.DB.Analysis
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 30
---

# SpatialFieldManager

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean AllowInteractiveSettings { get; set; }` | `spatialFieldManager.AllowInteractiveSettings` | Boolean |
| `Int32 CurrentMeasurement { get; set; }` | `spatialFieldManager.CurrentMeasurement` | Int32 |
| `XYZ LegendPosition { get; set; }` | `spatialFieldManager.LegendPosition` | XYZ |
| `Boolean LegendShowConfigurationName { get; set; }` | `spatialFieldManager.LegendShowConfigurationName` | Boolean |
| `Boolean LegendShowDescription { get; set; }` | `spatialFieldManager.LegendShowDescription` | Boolean |
| `ElementId LegendTextTypeId { get; set; }` | `spatialFieldManager.LegendTextTypeId` | ElementId |
| `Int32 NumberOfMeasurements { get; }` | `spatialFieldManager.NumberOfMeasurements` | Int32 |
| `Boolean ResultsVisibleInView { get; set; }` | `spatialFieldManager.ResultsVisibleInView` | Boolean |
| `Boolean UseRangeForAllMeasurements { get; set; }` | `spatialFieldManager.UseRangeForAllMeasurements` | Boolean |
| `Int32 AddSpatialFieldPrimitive(Curve, Transform)` | `spatialFieldManager.AddSpatialFieldPrimitive(curve, trf)` | Int32 |
| `Int32 AddSpatialFieldPrimitive(Face, Transform)` | `spatialFieldManager.AddSpatialFieldPrimitive(face, trf)` | Int32 |
| `Int32 AddSpatialFieldPrimitive(Reference, SpatialFieldPrimitiveHideMode)` | `spatialFieldManager.AddSpatialFieldPrimitive(reference, hidingMode)` | Int32 |
| `Int32 AddSpatialFieldPrimitive(Reference)` | `spatialFieldManager.AddSpatialFieldPrimitive(reference)` | Int32 |
| `Int32 AddSpatialFieldPrimitive()` | `spatialFieldManager.AddSpatialFieldPrimitive()` | Int32 |
| `Void Clear()` | `spatialFieldManager.Clear()` | Void |
| `SpatialFieldManager CreateSpatialFieldManager(View, Int32)` | `SpatialFieldManager.CreateSpatialFieldManager(view, numberOfMeasurements)` | SpatialFieldManager |
| `AnalysisDisplayLegend GetLegend()` | `spatialFieldManager.GetLegend()` | AnalysisDisplayLegend |
| `Double GetMaximum(Int32, Boolean)` | `spatialFieldManager.GetMaximum(resultIndex, rawValue)` | Double |
| `Double GetMinimum(Int32, Boolean)` | `spatialFieldManager.GetMinimum(resultIndex, rawValue)` | Double |
| `IList<Int32> GetRegisteredResults()` | `spatialFieldManager.GetRegisteredResults()` | IList<Int32> |
| `AnalysisResultSchema GetResultSchema(Int32)` | `spatialFieldManager.GetResultSchema(idx)` | AnalysisResultSchema |
| `SpatialFieldManager GetSpatialFieldManager(View)` | `SpatialFieldManager.GetSpatialFieldManager(view)` | SpatialFieldManager |
| `Boolean IsResultSchemaNameUnique(String, Int32)` | `spatialFieldManager.IsResultSchemaNameUnique(name, resultIndexToSkip)` | Boolean |
| `Boolean IsTextTypeIdValid(ElementId, Document)` | `SpatialFieldManager.IsTextTypeIdValid(textTypeId, doc)` | Boolean |
| `Int32 RegisterResult(AnalysisResultSchema)` | `spatialFieldManager.RegisterResult(resultSchema)` | Int32 |
| `Void RemoveSpatialFieldPrimitive(Int32)` | `spatialFieldManager.RemoveSpatialFieldPrimitive(idx)` | Void |
| `Void SetMeasurementDescriptions(IList<String>)` | `spatialFieldManager.SetMeasurementDescriptions(measurementDescriptions)` | Void |
| `Void SetMeasurementNames(IList<String>)` | `spatialFieldManager.SetMeasurementNames(measurementNames)` | Void |
| `Void SetResultSchema(Int32, AnalysisResultSchema)` | `spatialFieldManager.SetResultSchema(idx, resultSchema)` | Void |
| `Void UpdateSpatialFieldPrimitive(Int32, FieldDomainPoints, FieldValues, Int32)` | `spatialFieldManager.UpdateSpatialFieldPrimitive(idx, fieldDomainPoints, fieldValues, resultIndex)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
