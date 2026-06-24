---
title: Application
classe: Autodesk.Revit.ApplicationServices.Application
namespace: Autodesk.Revit.ApplicationServices
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 83
---

# Application

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `AddInId ActiveAddInId { get; }` | `application.ActiveAddInId` | AddInId |
| `Boolean AllowNavigationDuringRedraw { get; set; }` | `application.AllowNavigationDuringRedraw` | Boolean |
| `String AllUsersAddinsLocation { get; }` | `application.AllUsersAddinsLocation` | String |
| `Double AngleTolerance { get; }` | `application.AngleTolerance` | Double |
| `Color BackgroundColor { get; set; }` | `application.BackgroundColor` | Color |
| `CitySet Cities { get; }` | `application.Cities` | CitySet |
| `Application Create { get; }` | `application.Create` | Application |
| `String CurrentRevitServerAccelerator { get; set; }` | `application.CurrentRevitServerAccelerator` | String |
| `String CurrentUserAddinsLocation { get; }` | `application.CurrentUserAddinsLocation` | String |
| `String CurrentUsersAddinsDataFolderPath { get; }` | `application.CurrentUsersAddinsDataFolderPath` | String |
| `String CurrentUsersDataFolderPath { get; }` | `application.CurrentUsersDataFolderPath` | String |
| `String DefaultIFCProjectTemplate { get; }` | `application.DefaultIFCProjectTemplate` | String |
| `String DefaultProjectTemplate { get; }` | `application.DefaultProjectTemplate` | String |
| `ViewDiscipline DefaultViewDiscipline { get; set; }` | `application.DefaultViewDiscipline` | ViewDiscipline |
| `DocumentSet Documents { get; }` | `application.Documents` | DocumentSet |
| `String ExportIFCCategoryTable { get; }` | `application.ExportIFCCategoryTable` | String |
| `String FamilyTemplatePath { get; }` | `application.FamilyTemplatePath` | String |
| `String ImportIFCCategoryTable { get; }` | `application.ImportIFCCategoryTable` | String |
| `Boolean IsArchitectureEnabled { get; set; }` | `application.IsArchitectureEnabled` | Boolean |
| `Boolean IsElectricalAnalysisEnabled { get; set; }` | `application.IsElectricalAnalysisEnabled` | Boolean |
| `Boolean IsElectricalEnabled { get; set; }` | `application.IsElectricalEnabled` | Boolean |
| `Boolean IsEnergyAnalysisEnabled { get; set; }` | `application.IsEnergyAnalysisEnabled` | Boolean |
| `Boolean IsInfrastructureEnabled { get; set; }` | `application.IsInfrastructureEnabled` | Boolean |
| `Boolean IsLoggedIn { get; }` | `Application.IsLoggedIn` | Boolean |
| `Boolean IsMassingEnabled { get; set; }` | `application.IsMassingEnabled` | Boolean |
| `Boolean IsMechanicalAnalysisEnabled { get; set; }` | `application.IsMechanicalAnalysisEnabled` | Boolean |
| `Boolean IsMechanicalEnabled { get; set; }` | `application.IsMechanicalEnabled` | Boolean |
| `Boolean IsPipingAnalysisEnabled { get; set; }` | `application.IsPipingAnalysisEnabled` | Boolean |
| `Boolean IsPipingEnabled { get; set; }` | `application.IsPipingEnabled` | Boolean |
| `Boolean IsRouteAnalysisEnabled { get; set; }` | `application.IsRouteAnalysisEnabled` | Boolean |
| `Boolean IsStructuralAnalysisEnabled { get; set; }` | `application.IsStructuralAnalysisEnabled` | Boolean |
| `Boolean IsStructureEnabled { get; set; }` | `application.IsStructureEnabled` | Boolean |
| `Boolean IsSystemsEnabled { get; }` | `application.IsSystemsEnabled` | Boolean |
| `Boolean IsValidObject { get; }` | `application.IsValidObject` | Boolean |
| `LanguageType Language { get; }` | `application.Language` | LanguageType |
| `String LoginUserId { get; }` | `application.LoginUserId` | String |
| `Double MinimumThickness { get; }` | `Application.MinimumThickness` | Double |
| `String PointCloudsRootPath { get; }` | `application.PointCloudsRootPath` | String |
| `ProductType Product { get; }` | `application.Product` | ProductType |
| `String RecordingJournalFilename { get; }` | `application.RecordingJournalFilename` | String |
| `String SharedParametersFilename { get; set; }` | `application.SharedParametersFilename` | String |
| `Double ShortCurveTolerance { get; }` | `application.ShortCurveTolerance` | Double |
| `Boolean ShowGraphicalOpenEndsAreaBasedLoadBoundaryDisconnects { get; set; }` | `application.ShowGraphicalOpenEndsAreaBasedLoadBoundaryDisconnects` | Boolean |
| `Boolean ShowGraphicalWarningCableTrayConduitDisconnects { get; set; }` | `application.ShowGraphicalWarningCableTrayConduitDisconnects` | Boolean |
| `Boolean ShowGraphicalWarningDuctDisconnects { get; set; }` | `application.ShowGraphicalWarningDuctDisconnects` | Boolean |
| `Boolean ShowGraphicalWarningElectricalDisconnects { get; set; }` | `application.ShowGraphicalWarningElectricalDisconnects` | Boolean |
| `Boolean ShowGraphicalWarningHangerDisconnects { get; set; }` | `application.ShowGraphicalWarningHangerDisconnects` | Boolean |
| `Boolean ShowGraphicalWarningPipeDisconnects { get; set; }` | `application.ShowGraphicalWarningPipeDisconnects` | Boolean |
| `String SubVersionNumber { get; }` | `application.SubVersionNumber` | String |
| `String SystemsAnalysisWorkfilesRootPath { get; }` | `application.SystemsAnalysisWorkfilesRootPath` | String |
| `String Username { get; }` | `application.Username` | String |
| `String VersionBuild { get; }` | `application.VersionBuild` | String |
| `String VersionName { get; }` | `application.VersionName` | String |
| `String VersionNumber { get; }` | `application.VersionNumber` | String |
| `Double VertexTolerance { get; }` | `application.VertexTolerance` | Double |
| `Void CopyModel(ModelPath, String, Boolean)` | `application.CopyModel(sourceModelPath, destFilePath, overwrite)` | Void |
| `Void Dispose()` | `application.Dispose()` | Void |
| `Void ExtractPartAtomFromFamilyFile(String, String)` | `application.ExtractPartAtomFromFamilyFile(familyFilePath, xmlFilePath)` | Void |
| `IList<Asset> GetAssets(AssetType)` | `application.GetAssets(assetType)` | IList<Asset> |
| `FailureDefinitionRegistry GetFailureDefinitionRegistry()` | `Application.GetFailureDefinitionRegistry()` | FailureDefinitionRegistry |
| `IDictionary<String, String> GetLibraryPaths()` | `application.GetLibraryPaths()` | IDictionary<String, String> |
| `IList<String> GetRevitServerNetworkHosts()` | `application.GetRevitServerNetworkHosts()` | IList<String> |
| `IList<String> GetSystemsAnalysisWorkflowNames()` | `application.GetSystemsAnalysisWorkflowNames()` | IList<String> |
| `IDictionary<String, String> GetSystemsAnalysisWorkflows()` | `application.GetSystemsAnalysisWorkflows()` | IDictionary<String, String> |
| `Guid GetWorksharingCentralGUID(ServerPath)` | `application.GetWorksharingCentralGUID(serverModelPath)` | Guid |
| `Boolean IsJournalPlaying()` | `application.IsJournalPlaying()` | Boolean |
| `Boolean IsValidThickness(Double)` | `Application.IsValidThickness(thickness)` | Boolean |
| `Document NewFamilyDocument(String)` | `application.NewFamilyDocument(templateFileName)` | Document |
| `Document NewProjectDocument(UnitSystem)` | `application.NewProjectDocument(unitSystem)` | Document |
| `Document NewProjectDocument(String)` | `application.NewProjectDocument(templateFileName)` | Document |
| `Document NewProjectTemplateDocument(String)` | `application.NewProjectTemplateDocument(templateFilename)` | Document |
| `Document OpenDocumentFile(String)` | `application.OpenDocumentFile(fileName)` | Document |
| `Document OpenDocumentFile(ModelPath, OpenOptions, IOpenFromCloudCallback)` | `application.OpenDocumentFile(modelPath, openOptions, openFromCloudCallback)` | Document |
| `Document OpenDocumentFile(ModelPath, OpenOptions)` | `application.OpenDocumentFile(modelPath, openOptions)` | Document |
| `Document OpenIFCDocument(String, IFCImportOptions)` | `application.OpenIFCDocument(fileName, importOptions)` | Document |
| `Document OpenIFCDocument(String)` | `application.OpenIFCDocument(fileName)` | Document |
| `DefinitionFile OpenSharedParameterFile()` | `application.OpenSharedParameterFile()` | DefinitionFile |
| `Void PurgeReleasedAPIObjects()` | `application.PurgeReleasedAPIObjects()` | Void |
| `Void RegisterFailuresProcessor(IFailuresProcessor)` | `Application.RegisterFailuresProcessor(processor)` | Void |
| `Void SetLibraryPaths(IDictionary<String, String>)` | `application.SetLibraryPaths(paths)` | Void |
| `Void SetSystemsAnalysisWorkflows(IDictionary<String, String>)` | `application.SetSystemsAnalysisWorkflows(paths)` | Void |
| `Void UpdateRenderAppearanceLibrary()` | `application.UpdateRenderAppearanceLibrary()` | Void |
| `Void WriteJournalComment(String, Boolean)` | `application.WriteJournalComment(comment, timeStamp)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
