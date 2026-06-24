---
title: DefaultDivideSettings
classe: Autodesk.Revit.DB.DefaultDivideSettings
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# DefaultDivideSettings

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double PathDistance { get; set; }` | `defaultDivideSettings.PathDistance` | Double |
| `SpacingRuleLayout PathLayout { get; set; }` | `defaultDivideSettings.PathLayout` | SpacingRuleLayout |
| `DividedPathMeasurementType PathMeasurementType { get; set; }` | `defaultDivideSettings.PathMeasurementType` | DividedPathMeasurementType |
| `Int32 PathNumber { get; set; }` | `defaultDivideSettings.PathNumber` | Int32 |
| `DefaultDivideSettings GetDefaultDivideSettings(Document)` | `DefaultDivideSettings.GetDefaultDivideSettings(cda)` | DefaultDivideSettings |
| `Double GetSurfaceDistance(UVGridlineType)` | `defaultDivideSettings.GetSurfaceDistance(gridlines)` | Double |
| `SpacingRuleLayout GetSurfaceLayout(UVGridlineType)` | `defaultDivideSettings.GetSurfaceLayout(gridlines)` | SpacingRuleLayout |
| `Int32 GetSurfaceNumber(UVGridlineType)` | `defaultDivideSettings.GetSurfaceNumber(gridlines)` | Int32 |
| `Void SetSurfaceDistance(UVGridlineType, Double)` | `defaultDivideSettings.SetSurfaceDistance(gridlines, distance)` | Void |
| `Void SetSurfaceLayout(UVGridlineType, SpacingRuleLayout)` | `defaultDivideSettings.SetSurfaceLayout(gridlines, layout)` | Void |
| `Void SetSurfaceNumber(UVGridlineType, Int32)` | `defaultDivideSettings.SetSurfaceNumber(gridlines, number)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
