---
title: AnalysisDisplayColorSettings
classe: Autodesk.Revit.DB.Analysis.AnalysisDisplayColorSettings
namespace: Autodesk.Revit.DB.Analysis
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# AnalysisDisplayColorSettings

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `AnalysisDisplayStyleColorSettingsType ColorSettingsType { get; set; }` | `analysisDisplayColorSettings.ColorSettingsType` | AnalysisDisplayStyleColorSettingsType |
| `Boolean IsValidObject { get; }` | `analysisDisplayColorSettings.IsValidObject` | Boolean |
| `Color MaxColor { get; set; }` | `analysisDisplayColorSettings.MaxColor` | Color |
| `Color MinColor { get; set; }` | `analysisDisplayColorSettings.MinColor` | Color |
| `Boolean AreIntermediateColorsValid(IList<AnalysisDisplayColorEntry>)` | `analysisDisplayColorSettings.AreIntermediateColorsValid(map)` | Boolean |
| `Int32 Colors()` | `analysisDisplayColorSettings.Colors()` | Int32 |
| `Void Dispose()` | `analysisDisplayColorSettings.Dispose()` | Void |
| `IList<AnalysisDisplayColorEntry> GetIntermediateColors()` | `analysisDisplayColorSettings.GetIntermediateColors()` | IList<AnalysisDisplayColorEntry> |
| `Boolean IsEqual(AnalysisDisplayColorSettings)` | `analysisDisplayColorSettings.IsEqual(other)` | Boolean |
| `Void SetIntermediateColors(IList<AnalysisDisplayColorEntry>)` | `analysisDisplayColorSettings.SetIntermediateColors(map)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
