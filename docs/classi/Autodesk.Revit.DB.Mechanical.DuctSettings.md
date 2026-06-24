---
title: DuctSettings
classe: Autodesk.Revit.DB.Mechanical.DuctSettings
namespace: Autodesk.Revit.DB.Mechanical
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 30
---

# DuctSettings

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double AirDensity { get; set; }` | `ductSettings.AirDensity` | Double |
| `Double AirDynamicViscosity { get; set; }` | `ductSettings.AirDynamicViscosity` | Double |
| `Double AirViscosity { get; set; }` | `ductSettings.AirViscosity` | Double |
| `String Centerline { get; set; }` | `ductSettings.Centerline` | String |
| `String ConnectorSeparator { get; set; }` | `ductSettings.ConnectorSeparator` | String |
| `FittingAngleUsage FittingAngleUsage { get; set; }` | `ductSettings.FittingAngleUsage` | FittingAngleUsage |
| `Double FittingAnnotationSize { get; set; }` | `ductSettings.FittingAnnotationSize` | Double |
| `String FlatOnBottom { get; set; }` | `ductSettings.FlatOnBottom` | String |
| `String FlatOnTop { get; set; }` | `ductSettings.FlatOnTop` | String |
| `Boolean NetworkBasedCalculations { get; set; }` | `ductSettings.NetworkBasedCalculations` | Boolean |
| `String OvalDuctSizeSeparator { get; set; }` | `ductSettings.OvalDuctSizeSeparator` | String |
| `String OvalDuctSizeSuffix { get; set; }` | `ductSettings.OvalDuctSizeSuffix` | String |
| `String RectangularDuctSizeSeparator { get; set; }` | `ductSettings.RectangularDuctSizeSeparator` | String |
| `String RectangularDuctSizeSuffix { get; set; }` | `ductSettings.RectangularDuctSizeSuffix` | String |
| `Double RiseDropAnnotationSize { get; set; }` | `ductSettings.RiseDropAnnotationSize` | Double |
| `String RoundDuctSizePrefix { get; set; }` | `ductSettings.RoundDuctSizePrefix` | String |
| `String RoundDuctSizeSuffix { get; set; }` | `ductSettings.RoundDuctSizeSuffix` | String |
| `String SetDown { get; set; }` | `ductSettings.SetDown` | String |
| `String SetDownFromBottom { get; set; }` | `ductSettings.SetDownFromBottom` | String |
| `String SetUp { get; set; }` | `ductSettings.SetUp` | String |
| `String SetUpFromBottom { get; set; }` | `ductSettings.SetUpFromBottom` | String |
| `Boolean UseAnnotationScaleForSingleLineFittings { get; set; }` | `ductSettings.UseAnnotationScaleForSingleLineFittings` | Boolean |
| `DuctSettings GetDuctSettings(Document)` | `DuctSettings.GetDuctSettings(document)` | DuctSettings |
| `MEPCalculationServerInfo GetPressLossCalculationServerInfo()` | `ductSettings.GetPressLossCalculationServerInfo()` | MEPCalculationServerInfo |
| `IList<Double> GetSpecificFittingAngles()` | `ductSettings.GetSpecificFittingAngles()` | IList<Double> |
| `Boolean GetSpecificFittingAngleStatus(Double)` | `ductSettings.GetSpecificFittingAngleStatus(angle)` | Boolean |
| `Boolean IsNetworkBasedCalculationsEnabled(Document)` | `DuctSettings.IsNetworkBasedCalculationsEnabled(document)` | Boolean |
| `Boolean IsValidSpecificFittingAngle(Double)` | `ductSettings.IsValidSpecificFittingAngle(angle)` | Boolean |
| `Void SetPressLossCalculationServerInfo(MEPCalculationServerInfo)` | `ductSettings.SetPressLossCalculationServerInfo(serverInfo)` | Void |
| `Void SetSpecificFittingAngleStatus(Double, Boolean)` | `ductSettings.SetSpecificFittingAngleStatus(angle, useInLayout)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
