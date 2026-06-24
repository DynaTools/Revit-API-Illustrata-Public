---
title: EnergyAnalysisDetailModel
classe: Autodesk.Revit.DB.Analysis.EnergyAnalysisDetailModel
namespace: Autodesk.Revit.DB.Analysis
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# EnergyAnalysisDetailModel

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId BuildingTypeId { get; set; }` | `energyAnalysisDetailModel.BuildingTypeId` | ElementId |
| `ElementId ExportCategory { get; set; }` | `energyAnalysisDetailModel.ExportCategory` | ElementId |
| `Boolean ExportMullions { get; }` | `energyAnalysisDetailModel.ExportMullions` | Boolean |
| `Boolean IncludeShadingSurfaces { get; }` | `energyAnalysisDetailModel.IncludeShadingSurfaces` | Boolean |
| `Boolean SimplifyCurtainSystems { get; }` | `energyAnalysisDetailModel.SimplifyCurtainSystems` | Boolean |
| `EnergyAnalysisDetailModelTier Tier { get; }` | `energyAnalysisDetailModel.Tier` | EnergyAnalysisDetailModelTier |
| `EnergyAnalysisDetailModel Create(Document, EnergyAnalysisDetailModelOptions)` | `EnergyAnalysisDetailModel.Create(document, options)` | EnergyAnalysisDetailModel |
| `IList<EnergyAnalysisOpening> GetAnalyticalOpenings()` | `energyAnalysisDetailModel.GetAnalyticalOpenings()` | IList<EnergyAnalysisOpening> |
| `IList<EnergyAnalysisSurface> GetAnalyticalShadingSurfaces()` | `energyAnalysisDetailModel.GetAnalyticalShadingSurfaces()` | IList<EnergyAnalysisSurface> |
| `IList<EnergyAnalysisSpace> GetAnalyticalSpaces()` | `energyAnalysisDetailModel.GetAnalyticalSpaces()` | IList<EnergyAnalysisSpace> |
| `IList<EnergyAnalysisSurface> GetAnalyticalSurfaces()` | `energyAnalysisDetailModel.GetAnalyticalSurfaces()` | IList<EnergyAnalysisSurface> |
| `EnergyAnalysisDetailModel GetMainEnergyAnalysisDetailModel(Document)` | `EnergyAnalysisDetailModel.GetMainEnergyAnalysisDetailModel(document)` | EnergyAnalysisDetailModel |
| `Void TransformModel()` | `energyAnalysisDetailModel.TransformModel()` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
