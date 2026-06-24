---
title: PipeSettings
classe: Autodesk.Revit.DB.Plumbing.PipeSettings
namespace: Autodesk.Revit.DB.Plumbing
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 26
---

# PipeSettings

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean AnalysisForClosedLoopHydronicPipingNetworks { get; set; }` | `pipeSettings.AnalysisForClosedLoopHydronicPipingNetworks` | Boolean |
| `String Centerline { get; set; }` | `pipeSettings.Centerline` | String |
| `String ConnectorSeparator { get; set; }` | `pipeSettings.ConnectorSeparator` | String |
| `Double ConnectorTolerance { get; set; }` | `pipeSettings.ConnectorTolerance` | Double |
| `FittingAngleUsage FittingAngleUsage { get; set; }` | `pipeSettings.FittingAngleUsage` | FittingAngleUsage |
| `Double FittingAnnotationSize { get; set; }` | `pipeSettings.FittingAnnotationSize` | Double |
| `String FlatOnBottom { get; set; }` | `pipeSettings.FlatOnBottom` | String |
| `String FlatOnTop { get; set; }` | `pipeSettings.FlatOnTop` | String |
| `String SetDown { get; set; }` | `pipeSettings.SetDown` | String |
| `String SetDownFromBottom { get; set; }` | `pipeSettings.SetDownFromBottom` | String |
| `String SetUp { get; set; }` | `pipeSettings.SetUp` | String |
| `String SetUpFromBottom { get; set; }` | `pipeSettings.SetUpFromBottom` | String |
| `String SizePrefix { get; set; }` | `pipeSettings.SizePrefix` | String |
| `String SizeSuffix { get; set; }` | `pipeSettings.SizeSuffix` | String |
| `Boolean UseAnnotationScaleForSingleLineFittings { get; set; }` | `pipeSettings.UseAnnotationScaleForSingleLineFittings` | Boolean |
| `Void AddPipeSlope(Double)` | `pipeSettings.AddPipeSlope(slope)` | Void |
| `MEPCalculationServerInfo GetFlowConvertionServerInfo()` | `pipeSettings.GetFlowConvertionServerInfo()` | MEPCalculationServerInfo |
| `PipeSettings GetPipeSettings(Document)` | `PipeSettings.GetPipeSettings(document)` | PipeSettings |
| `IList<Double> GetPipeSlopes()` | `pipeSettings.GetPipeSlopes()` | IList<Double> |
| `IList<Double> GetSpecificFittingAngles()` | `pipeSettings.GetSpecificFittingAngles()` | IList<Double> |
| `Boolean GetSpecificFittingAngleStatus(Double)` | `pipeSettings.GetSpecificFittingAngleStatus(angle)` | Boolean |
| `Boolean IsAnalysisForClosedLoopHydronicPipingNetworksEnabled(Document)` | `PipeSettings.IsAnalysisForClosedLoopHydronicPipingNetworksEnabled(ccda)` | Boolean |
| `Boolean IsValidSpecificFittingAngle(Double)` | `pipeSettings.IsValidSpecificFittingAngle(angle)` | Boolean |
| `Void SetFlowConvertionServerInfo(MEPCalculationServerInfo)` | `pipeSettings.SetFlowConvertionServerInfo(serverInfo)` | Void |
| `Void SetPipeSlopes(IList<Double>)` | `pipeSettings.SetPipeSlopes(slopes)` | Void |
| `Void SetSpecificFittingAngleStatus(Double, Boolean)` | `pipeSettings.SetSpecificFittingAngleStatus(angle, bStatus)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
