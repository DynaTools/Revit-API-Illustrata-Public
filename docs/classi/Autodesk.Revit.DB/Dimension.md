---
title: Dimension
classe: Autodesk.Revit.DB.Dimension
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 27
---

# Dimension

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String Above { get; set; }` | `dimension.Above` | String |
| `Boolean AreReferencesAvailable { get; }` | `dimension.AreReferencesAvailable` | Boolean |
| `Boolean AreSegmentsEqual { get; set; }` | `dimension.AreSegmentsEqual` | Boolean |
| `String Below { get; set; }` | `dimension.Below` | String |
| `Curve Curve { get; }` | `dimension.Curve` | Curve |
| `DimensionShape DimensionShape { get; }` | `dimension.DimensionShape` | DimensionShape |
| `DimensionType DimensionType { get; set; }` | `dimension.DimensionType` | DimensionType |
| `FamilyParameter FamilyLabel { get; set; }` | `dimension.FamilyLabel` | FamilyParameter |
| `Boolean HasLeader { get; set; }` | `dimension.HasLeader` | Boolean |
| `Boolean IsLocked { get; set; }` | `dimension.IsLocked` | Boolean |
| `Boolean IsValid { get; }` | `dimension.IsValid` | Boolean |
| `XYZ LeaderEndPosition { get; set; }` | `dimension.LeaderEndPosition` | XYZ |
| `String Name { get; set; }` | `dimension.Name` | String |
| `Int32 NumberOfSegments { get; }` | `dimension.NumberOfSegments` | Int32 |
| `XYZ Origin { get; }` | `dimension.Origin` | XYZ |
| `String Prefix { get; set; }` | `dimension.Prefix` | String |
| `ReferenceArray References { get; }` | `dimension.References` | ReferenceArray |
| `DimensionSegmentArray Segments { get; }` | `dimension.Segments` | DimensionSegmentArray |
| `String Suffix { get; set; }` | `dimension.Suffix` | String |
| `XYZ TextPosition { get; set; }` | `dimension.TextPosition` | XYZ |
| `Nullable<Double> Value { get; }` | `dimension.Value` | Nullable<Double> |
| `String ValueOverride { get; set; }` | `dimension.ValueOverride` | String |
| `String ValueString { get; }` | `dimension.ValueString` | String |
| `View View { get; }` | `dimension.View` | View |
| `Boolean HasOneSegment()` | `dimension.HasOneSegment()` | Boolean |
| `Boolean IsTextPositionAdjustable()` | `dimension.IsTextPositionAdjustable()` | Boolean |
| `Void ResetTextPosition()` | `dimension.ResetTextPosition()` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
