---
title: EnergyDataSettings
classe: Autodesk.Revit.DB.Analysis.EnergyDataSettings
namespace: Autodesk.Revit.DB.Analysis
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 64
---

# EnergyDataSettings

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `AnalysisMode AnalysisType { get; set; }` | `energyDataSettings.AnalysisType` | AnalysisMode |
| `Double AnalyticalGridCellSize { get; set; }` | `energyDataSettings.AnalyticalGridCellSize` | Double |
| `HVACLoadConstructionClass BuildingConstructionClass { get; set; }` | `energyDataSettings.BuildingConstructionClass` | HVACLoadConstructionClass |
| `gbXMLExportBuildingEnvelope BuildingEnvelopeDeterminationMethod { get; set; }` | `energyDataSettings.BuildingEnvelopeDeterminationMethod` | gbXMLExportBuildingEnvelope |
| `gbXMLBuildingHVACSystem BuildingHVACSystem { get; set; }` | `energyDataSettings.BuildingHVACSystem` | gbXMLBuildingHVACSystem |
| `gbXMLBuildingOperatingSchedule BuildingOperatingSchedule { get; set; }` | `energyDataSettings.BuildingOperatingSchedule` | gbXMLBuildingOperatingSchedule |
| `gbXMLBuildingType BuildingType { get; set; }` | `energyDataSettings.BuildingType` | gbXMLBuildingType |
| `ElementId BuildingTypeId { get; set; }` | `energyDataSettings.BuildingTypeId` | ElementId |
| `Double CoreOffset { get; set; }` | `energyDataSettings.CoreOffset` | Double |
| `Boolean CreateAnalyticalModel { get; }` | `energyDataSettings.CreateAnalyticalModel` | Boolean |
| `Boolean DividePerimeter { get; set; }` | `energyDataSettings.DividePerimeter` | Boolean |
| `Boolean EnergyModel { get; set; }` | `energyDataSettings.EnergyModel` | Boolean |
| `ElementId ExportCategory { get; set; }` | `energyDataSettings.ExportCategory` | ElementId |
| `gbXMLExportComplexity ExportComplexity { get; set; }` | `energyDataSettings.ExportComplexity` | gbXMLExportComplexity |
| `Boolean ExportDefaults { get; set; }` | `energyDataSettings.ExportDefaults` | Boolean |
| `ElementId GroundPlane { get; set; }` | `energyDataSettings.GroundPlane` | ElementId |
| `Boolean IncludeThermalProperties { get; set; }` | `energyDataSettings.IncludeThermalProperties` | Boolean |
| `Boolean IsExportMullionsEnabled { get; }` | `energyDataSettings.IsExportMullionsEnabled` | Boolean |
| `Boolean IsExportShadingSurfacesEnabled { get; }` | `energyDataSettings.IsExportShadingSurfacesEnabled` | Boolean |
| `Boolean IsExportSimplifiedCurtainSystemsEnabled { get; }` | `energyDataSettings.IsExportSimplifiedCurtainSystemsEnabled` | Boolean |
| `Boolean IsGlazingShaded { get; set; }` | `energyDataSettings.IsGlazingShaded` | Boolean |
| `Double OutsideAirChangesRatePerHour { get; set; }` | `energyDataSettings.OutsideAirChangesRatePerHour` | Double |
| `Double OutsideAirPerArea { get; set; }` | `energyDataSettings.OutsideAirPerArea` | Double |
| `Double OutsideAirPerPerson { get; set; }` | `energyDataSettings.OutsideAirPerPerson` | Double |
| `Double PercentageGlazing { get; set; }` | `energyDataSettings.PercentageGlazing` | Double |
| `Double PercentageSkylights { get; set; }` | `energyDataSettings.PercentageSkylights` | Double |
| `ElementId ProjectPhase { get; set; }` | `energyDataSettings.ProjectPhase` | ElementId |
| `HVACLoadLoadsReportType ProjectReportType { get; set; }` | `energyDataSettings.ProjectReportType` | HVACLoadLoadsReportType |
| `String ReportsFolder { get; }` | `energyDataSettings.ReportsFolder` | String |
| `gbXMLServiceType ServiceType { get; set; }` | `energyDataSettings.ServiceType` | gbXMLServiceType |
| `Double ShadeDepth { get; set; }` | `energyDataSettings.ShadeDepth` | Double |
| `Double SillHeight { get; set; }` | `energyDataSettings.SillHeight` | Double |
| `Double SkylightWidth { get; set; }` | `energyDataSettings.SkylightWidth` | Double |
| `Double SliverSpaceTolerance { get; set; }` | `energyDataSettings.SliverSpaceTolerance` | Double |
| `Boolean UseAirChangesPerHour { get; set; }` | `energyDataSettings.UseAirChangesPerHour` | Boolean |
| `Boolean UseCurrentViewOnly { get; set; }` | `energyDataSettings.UseCurrentViewOnly` | Boolean |
| `Boolean UseHeatingCredits { get; set; }` | `energyDataSettings.UseHeatingCredits` | Boolean |
| `Boolean UseOutsideAirPerArea { get; set; }` | `energyDataSettings.UseOutsideAirPerArea` | Boolean |
| `Boolean UseOutsideAirPerPerson { get; set; }` | `energyDataSettings.UseOutsideAirPerPerson` | Boolean |
| `Boolean CheckAnalysisType(AnalysisMode)` | `EnergyDataSettings.CheckAnalysisType(analysisType)` | Boolean |
| `Boolean CheckBuildingConstructionClass(HVACLoadConstructionClass)` | `EnergyDataSettings.CheckBuildingConstructionClass(buildingConstructionClass)` | Boolean |
| `Boolean CheckBuildingEnvelope(gbXMLExportBuildingEnvelope)` | `EnergyDataSettings.CheckBuildingEnvelope(determinationMethod)` | Boolean |
| `Boolean CheckBuildingHVACSystem(gbXMLBuildingHVACSystem)` | `EnergyDataSettings.CheckBuildingHVACSystem(buildingHVACSystem)` | Boolean |
| `Boolean CheckBuildingOperatingSchedule(gbXMLBuildingOperatingSchedule)` | `EnergyDataSettings.CheckBuildingOperatingSchedule(buildingOperatingSchedule)` | Boolean |
| `Boolean CheckBuildingType(gbXMLBuildingType)` | `EnergyDataSettings.CheckBuildingType(buildingType)` | Boolean |
| `Boolean CheckConstructionSetElement(ElementId)` | `energyDataSettings.CheckConstructionSetElement(constructionSetElementId)` | Boolean |
| `Boolean CheckExportCategory(ElementId)` | `EnergyDataSettings.CheckExportCategory(exportCategoryId)` | Boolean |
| `Boolean CheckExportComplexity(gbXMLExportComplexity)` | `EnergyDataSettings.CheckExportComplexity(exportComplexity)` | Boolean |
| `Boolean CheckGroundPlane(Document, ElementId)` | `EnergyDataSettings.CheckGroundPlane(ccda, groundPlaneId)` | Boolean |
| `Boolean CheckGroundPlane(ElementId)` | `energyDataSettings.CheckGroundPlane(groundPlaneId)` | Boolean |
| `Boolean CheckProjectPhase(ElementId)` | `energyDataSettings.CheckProjectPhase(projectPhaseId)` | Boolean |
| `Boolean CheckProjectReportType(HVACLoadLoadsReportType)` | `EnergyDataSettings.CheckProjectReportType(projectReportType)` | Boolean |
| `Boolean CheckRangeOfPercentageGlazing(Double)` | `EnergyDataSettings.CheckRangeOfPercentageGlazing(percentageGlazing)` | Boolean |
| `Boolean CheckRangeOfPercentageSkylights(Double)` | `EnergyDataSettings.CheckRangeOfPercentageSkylights(percentageSkylights)` | Boolean |
| `Boolean CheckRangeOfShadeDepth(Double)` | `EnergyDataSettings.CheckRangeOfShadeDepth(shadeDepth)` | Boolean |
| `Boolean CheckRangeOfSillHeight(Double)` | `EnergyDataSettings.CheckRangeOfSillHeight(sillHeight)` | Boolean |
| `Boolean CheckRangeOfSkylightWidth(Double)` | `EnergyDataSettings.CheckRangeOfSkylightWidth(skylightWidth)` | Boolean |
| `Boolean CheckRangeOfSliverSpaceTolerance(Double)` | `EnergyDataSettings.CheckRangeOfSliverSpaceTolerance(silverSpaceTolerance)` | Boolean |
| `Boolean CheckServiceType(gbXMLServiceType)` | `EnergyDataSettings.CheckServiceType(serviceType)` | Boolean |
| `ElementId GetBuildingConstructionSetElementId(Document)` | `EnergyDataSettings.GetBuildingConstructionSetElementId(ccda)` | ElementId |
| `EnergyDataSettings GetFromDocument(Document)` | `EnergyDataSettings.GetFromDocument(cda)` | EnergyDataSettings |
| `String GetReportsFolderParsed()` | `energyDataSettings.GetReportsFolderParsed()` | String |
| `Boolean IsDocumentUsingEnergyDataAnalyticalModel(Document)` | `EnergyDataSettings.IsDocumentUsingEnergyDataAnalyticalModel(ccda)` | Boolean |
| `Void SetReportsFolder(String)` | `energyDataSettings.SetReportsFolder(folderPath)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
