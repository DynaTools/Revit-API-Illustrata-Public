---
title: Document
classe: Autodesk.Revit.DB.Document
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 162
---

# Document

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ProjectLocation ActiveProjectLocation { get; set; }` | `document.ActiveProjectLocation` | ProjectLocation |
| `View ActiveView { get; }` | `document.ActiveView` | View |
| `Application Application { get; }` | `document.Application` | Application |
| `Document Create { get; }` | `document.Create` | Document |
| `Guid CreationGUID { get; }` | `document.CreationGUID` | Guid |
| `DisplayUnit DisplayUnitSystem { get; }` | `document.DisplayUnitSystem` | DisplayUnit |
| `FamilyItemFactory FamilyCreate { get; }` | `document.FamilyCreate` | FamilyItemFactory |
| `FamilyManager FamilyManager { get; }` | `document.FamilyManager` | FamilyManager |
| `Boolean IsDetached { get; }` | `document.IsDetached` | Boolean |
| `Boolean IsFamilyDocument { get; }` | `document.IsFamilyDocument` | Boolean |
| `Boolean IsLinked { get; }` | `document.IsLinked` | Boolean |
| `Boolean IsModelInCloud { get; }` | `document.IsModelInCloud` | Boolean |
| `Boolean IsModifiable { get; }` | `document.IsModifiable` | Boolean |
| `Boolean IsModified { get; }` | `document.IsModified` | Boolean |
| `Boolean IsReadOnly { get; }` | `document.IsReadOnly` | Boolean |
| `Boolean IsReadOnlyFile { get; }` | `document.IsReadOnlyFile` | Boolean |
| `Boolean IsValidObject { get; }` | `document.IsValidObject` | Boolean |
| `Boolean IsWorkshared { get; }` | `document.IsWorkshared` | Boolean |
| `MassDisplayTemporaryOverrideType MassDisplayTemporaryOverride { get; set; }` | `document.MassDisplayTemporaryOverride` | MassDisplayTemporaryOverrideType |
| `MullionTypeSet MullionTypes { get; }` | `document.MullionTypes` | MullionTypeSet |
| `Family OwnerFamily { get; }` | `document.OwnerFamily` | Family |
| `PanelTypeSet PanelTypes { get; }` | `document.PanelTypes` | PanelTypeSet |
| `BindingMap ParameterBindings { get; }` | `document.ParameterBindings` | BindingMap |
| `String PathName { get; }` | `document.PathName` | String |
| `PhaseArray Phases { get; }` | `document.Phases` | PhaseArray |
| `PlanTopologySet PlanTopologies { get; }` | `document.PlanTopologies` | PlanTopologySet |
| `PlanTopologySet PlanTopologies { get; }` | `document.PlanTopologies` | PlanTopologySet |
| `PlanTopology PlanTopology { get; }` | `document.PlanTopology` | PlanTopology |
| `PlanTopology PlanTopology { get; }` | `document.PlanTopology` | PlanTopology |
| `PrintManager PrintManager { get; }` | `document.PrintManager` | PrintManager |
| `ProjectInfo ProjectInformation { get; }` | `document.ProjectInformation` | ProjectInfo |
| `ProjectLocationSet ProjectLocations { get; }` | `document.ProjectLocations` | ProjectLocationSet |
| `Boolean ReactionsAreUpToDate { get; }` | `document.ReactionsAreUpToDate` | Boolean |
| `Settings Settings { get; }` | `document.Settings` | Settings |
| `SiteLocation SiteLocation { get; }` | `document.SiteLocation` | SiteLocation |
| `String Title { get; }` | `document.Title` | String |
| `StorageType TypeOfStorage { get; }` | `document.TypeOfStorage` | StorageType |
| `Guid WorksharingCentralGUID { get; }` | `document.WorksharingCentralGUID` | Guid |
| `Void AcquireCoordinates(ElementId)` | `document.AcquireCoordinates(linkInstanceId)` | Void |
| `Void AutoJoinElements()` | `document.AutoJoinElements()` | Void |
| `Boolean CanEnableCloudWorksharing()` | `document.CanEnableCloudWorksharing()` | Boolean |
| `Boolean CanEnableWorksharing()` | `document.CanEnableWorksharing()` | Boolean |
| `Boolean Close()` | `document.Close()` | Boolean |
| `Boolean Close(Boolean)` | `document.Close(saveModified)` | Boolean |
| `GeomCombination CombineElements(CombinableElementArray)` | `document.CombineElements(members)` | GeomCombination |
| `ModelCurveArray ConvertDetailToModelCurves(View, DetailCurveArray)` | `document.ConvertDetailToModelCurves(view, detailCurves)` | ModelCurveArray |
| `DetailCurveArray ConvertModelToDetailCurves(View, ModelCurveArray)` | `document.ConvertModelToDetailCurves(view, modelCurves)` | DetailCurveArray |
| `SymbolicCurveArray ConvertModelToSymbolicCurves(View, ModelCurveArray)` | `document.ConvertModelToSymbolicCurves(view, modelCurves)` | SymbolicCurveArray |
| `ModelCurveArray ConvertSymbolicToModelCurves(View, SymbolicCurveArray)` | `document.ConvertSymbolicToModelCurves(view, symbolicCurve)` | ModelCurveArray |
| `ICollection<ElementId> Delete(ICollection<ElementId>)` | `document.Delete(elementIds)` | ICollection<ElementId> |
| `ICollection<ElementId> Delete(ElementId)` | `document.Delete(elementId)` | ICollection<ElementId> |
| `Void Dispose()` | `document.Dispose()` | Void |
| `Document EditFamily(Family)` | `document.EditFamily(loadedFamily)` | Document |
| `Void EnableCloudWorksharing()` | `document.EnableCloudWorksharing()` | Void |
| `Void EnableWorksharing(String, String)` | `document.EnableWorksharing(worksetNameGridLevel, worksetName)` | Void |
| `Void EraseSchemaAndAllEntities(Schema)` | `document.EraseSchemaAndAllEntities(schema)` | Void |
| `Boolean Export(String, String, GBXMLExportOptions)` | `document.Export(folder, name, options)` | Boolean |
| `Boolean Export(String, IList<ElementId>, PDFExportOptions)` | `document.Export(folder, viewIds, options)` | Boolean |
| `Void Export(String, String, NavisworksExportOptions)` | `document.Export(folder, name, options)` | Void |
| `Boolean Export(String, String, OBJExportOptions)` | `document.Export(folder, name, options)` | Boolean |
| `Boolean Export(String, String, STEPExportOptions)` | `document.Export(folder, name, options)` | Boolean |
| `Boolean Export(String, String, STLExportOptions)` | `document.Export(folder, name, options)` | Boolean |
| `Boolean Export(String, String, IFCExportOptions)` | `document.Export(folder, name, options)` | Boolean |
| `Boolean Export(String, String, ICollection<ElementId>, SATExportOptions)` | `document.Export(folder, name, views, options)` | Boolean |
| `Boolean Export(String, String, ICollection<ElementId>, DGNExportOptions)` | `document.Export(folder, name, views, options)` | Boolean |
| `Boolean Export(String, String, ICollection<ElementId>, DXFExportOptions)` | `document.Export(folder, name, views, options)` | Boolean |
| `Boolean Export(String, String, ICollection<ElementId>, DWGExportOptions)` | `document.Export(folder, name, views, options)` | Boolean |
| `Boolean Export(String, String, ViewSet, FBXExportOptions)` | `document.Export(folder, name, views, options)` | Boolean |
| `Boolean Export(String, String, ViewSet, DWFXExportOptions)` | `document.Export(folder, name, views, options)` | Boolean |
| `Boolean Export(String, String, ViewSet, DWFExportOptions)` | `document.Export(folder, name, views, options)` | Boolean |
| `Void ExportImage(ImageExportOptions)` | `document.ExportImage(options)` | Void |
| `ISet<ElementId> GetAllUnusedElements(ISet<ElementId>)` | `document.GetAllUnusedElements(categories)` | ISet<ElementId> |
| `DocumentDifference GetChangedElements(Guid)` | `document.GetChangedElements(baseVersionGUID)` | DocumentDifference |
| `String GetCloudFolderId(Boolean)` | `document.GetCloudFolderId(forceRefresh)` | String |
| `ModelPath GetCloudModelPath()` | `document.GetCloudModelPath()` | ModelPath |
| `String GetCloudModelUrn()` | `document.GetCloudModelUrn()` | String |
| `ElementId GetDefaultElementTypeId(ElementTypeGroup)` | `document.GetDefaultElementTypeId(defaultTypeId)` | ElementId |
| `ElementId GetDefaultFamilyTypeId(ElementId)` | `document.GetDefaultFamilyTypeId(familyCategoryId)` | ElementId |
| `DocumentPreviewSettings GetDocumentPreviewSettings()` | `document.GetDocumentPreviewSettings()` | DocumentPreviewSettings |
| `DocumentVersion GetDocumentVersion(Document)` | `Document.GetDocumentVersion(doc)` | DocumentVersion |
| `Element GetElement(ElementId)` | `document.GetElement(id)` | Element |
| `Element GetElement(String)` | `document.GetElement(uniqueId)` | Element |
| `Element GetElement(Reference)` | `document.GetElement(reference)` | Element |
| `String GetHubId()` | `document.GetHubId()` | String |
| `ElementId GetPaintedMaterial(ElementId, Face)` | `document.GetPaintedMaterial(elementId, face)` | ElementId |
| `ICollection<ElementId> GetPrintSettingIds()` | `document.GetPrintSettingIds()` | ICollection<ElementId> |
| `String GetProjectId()` | `document.GetProjectId()` | String |
| `Room GetRoomAtPoint(XYZ)` | `document.GetRoomAtPoint(point)` | Room |
| `Room GetRoomAtPoint(XYZ, Phase)` | `document.GetRoomAtPoint(point, phase)` | Room |
| `Space GetSpaceAtPoint(XYZ)` | `document.GetSpaceAtPoint(point)` | Space |
| `Space GetSpaceAtPoint(XYZ, Phase)` | `document.GetSpaceAtPoint(point, phase)` | Space |
| `Subelement GetSubelement(ElementId, Int32)` | `document.GetSubelement(id, subId)` | Subelement |
| `Subelement GetSubelement(String)` | `document.GetSubelement(uniqueId)` | Subelement |
| `Subelement GetSubelement(Reference)` | `document.GetSubelement(reference)` | Subelement |
| `StorageType GetTypeOfStorage(ForgeTypeId)` | `document.GetTypeOfStorage(parameterTypeId)` | StorageType |
| `Units GetUnits()` | `document.GetUnits()` | Units |
| `ISet<ElementId> GetUnusedElements(ISet<ElementId>)` | `document.GetUnusedElements(categories)` | ISet<ElementId> |
| `IList<FailureMessage> GetWarnings()` | `document.GetWarnings()` | IList<FailureMessage> |
| `WorksetId GetWorksetId(ElementId)` | `document.GetWorksetId(id)` | WorksetId |
| `WorksetTable GetWorksetTable()` | `document.GetWorksetTable()` | WorksetTable |
| `ModelPath GetWorksharingCentralModelPath()` | `document.GetWorksharingCentralModelPath()` | ModelPath |
| `Boolean HasAllChangesFromCentral()` | `document.HasAllChangesFromCentral()` | Boolean |
| `ElementId Import(String, AXMImportOptions, View)` | `document.Import(file, options, pDBView)` | ElementId |
| `Boolean Import(String, DGNImportOptions, View, ElementId&)` | `document.Import(file, options, pDBView, elementId)` | Boolean |
| `ElementId Import(String, ImportOptions3DM, View)` | `document.Import(file, options, pDBView)` | ElementId |
| `ElementId Import(String, STLImportOptions, View)` | `document.Import(file, options, pDBView)` | ElementId |
| `ElementId Import(String, STEPImportOptions, View)` | `document.Import(file, options, pDBView)` | ElementId |
| `ElementId Import(String, OBJImportOptions, View)` | `document.Import(file, options, pDBView)` | ElementId |
| `ElementId Import(String, SKPImportOptions, View)` | `document.Import(file, options, pDBView)` | ElementId |
| `ElementId Import(String, SATImportOptions, View)` | `document.Import(file, options, pDBView)` | ElementId |
| `Boolean Import(String, DWGImportOptions, View, ElementId&)` | `document.Import(file, options, pDBView, elementId)` | Boolean |
| `Boolean Import(String, GBXMLImportOptions)` | `document.Import(file, options)` | Boolean |
| `Boolean IsBackgroundCalculationInProgress()` | `document.IsBackgroundCalculationInProgress()` | Boolean |
| `Boolean IsDefaultElementTypeIdValid(ElementTypeGroup, ElementId)` | `document.IsDefaultElementTypeIdValid(defaultTypeId, typeId)` | Boolean |
| `Boolean IsDefaultFamilyTypeIdValid(ElementId, ElementId)` | `document.IsDefaultFamilyTypeIdValid(familyCategoryId, familyTypeId)` | Boolean |
| `Boolean IsInEditMode()` | `document.IsInEditMode()` | Boolean |
| `Boolean IsPainted(ElementId, Face)` | `document.IsPainted(elementId, face)` | Boolean |
| `Boolean IsValidVersionGUID(Document, Guid)` | `Document.IsValidVersionGUID(document, versionGUID)` | Boolean |
| `IList<ElementId> Link(String, DWFImportOptions)` | `document.Link(file, options)` | IList<ElementId> |
| `Boolean Link(String, DGNImportOptions, View, ElementId&)` | `document.Link(file, options, pDBView, elementId)` | Boolean |
| `ElementId Link(String, ImportOptions3DM, View)` | `document.Link(file, options, pDBView)` | ElementId |
| `ElementId Link(String, STLImportOptions, View)` | `document.Link(file, options, pDBView)` | ElementId |
| `ElementId Link(String, STEPImportOptions, View)` | `document.Link(file, options, pDBView)` | ElementId |
| `ElementId Link(String, OBJImportOptions, View)` | `document.Link(file, options, pDBView)` | ElementId |
| `ElementId Link(String, SKPImportOptions, View)` | `document.Link(file, options, pDBView)` | ElementId |
| `ElementId Link(String, SATImportOptions, View)` | `document.Link(file, options, pDBView)` | ElementId |
| `Boolean Link(String, DWGImportOptions, View, ElementId&)` | `document.Link(file, options, pDBView, elementId)` | Boolean |
| `Family LoadFamily(Document, IFamilyLoadOptions)` | `document.LoadFamily(targetDocument, familyLoadOptions)` | Family |
| `Family LoadFamily(Document)` | `document.LoadFamily(targetDocument)` | Family |
| `Boolean LoadFamily(String, IFamilyLoadOptions, Family&)` | `document.LoadFamily(filename, familyLoadOptions, family)` | Boolean |
| `Boolean LoadFamily(String, Family&)` | `document.LoadFamily(filename, family)` | Boolean |
| `Boolean LoadFamily(String)` | `document.LoadFamily(filename)` | Boolean |
| `Boolean LoadFamilySymbol(String, String, IFamilyLoadOptions, FamilySymbol&)` | `document.LoadFamilySymbol(filename, name, familyLoadOptions, symbol)` | Boolean |
| `Boolean LoadFamilySymbol(String, String, FamilySymbol&)` | `document.LoadFamilySymbol(filename, name, symbol)` | Boolean |
| `Boolean LoadFamilySymbol(String, String)` | `document.LoadFamilySymbol(filename, name)` | Boolean |
| `Void MakeTransientElements(ITransientElementMaker)` | `document.MakeTransientElements(maker)` | Void |
| `Void Paint(ElementId, Face, ElementId)` | `document.Paint(elementId, face, materialId)` | Void |
| `Void Paint(ElementId, Face, FamilyParameter)` | `document.Paint(elementId, face, familyParameter)` | Void |
| `FailureMessageKey PostFailure(FailureMessage)` | `document.PostFailure(failure)` | FailureMessageKey |
| `Void Print(ViewSet, View, Boolean)` | `document.Print(views, viewTemplate, useCurrentPrintSettings)` | Void |
| `Void Print(ViewSet, View)` | `document.Print(views, viewTemplate)` | Void |
| `Void Print(ViewSet, Boolean)` | `document.Print(views, useCurrentPrintSettings)` | Void |
| `Void Print(ViewSet)` | `document.Print(views)` | Void |
| `Void PublishCoordinates(LinkElementId)` | `document.PublishCoordinates(locationId)` | Void |
| `Void Regenerate()` | `document.Regenerate()` | Void |
| `Void ReloadLatest(ReloadLatestOptions)` | `document.ReloadLatest(reloadOptions)` | Void |
| `Void RemovePaint(ElementId, Face)` | `document.RemovePaint(elementId, face)` | Void |
| `Void ResetSharedCoordinates()` | `document.ResetSharedCoordinates()` | Void |
| `Void Save(SaveOptions)` | `document.Save(options)` | Void |
| `Void Save()` | `document.Save()` | Void |
| `Void SaveAs(ModelPath, SaveAsOptions)` | `document.SaveAs(path, options)` | Void |
| `Void SaveAs(String, SaveAsOptions)` | `document.SaveAs(filepath, options)` | Void |
| `Void SaveAs(String)` | `document.SaveAs(filepath)` | Void |
| `Void SaveAsCloudModel(Guid, Guid, String, String)` | `document.SaveAsCloudModel(accountId, projectId, folderId, modelName)` | Void |
| `Void SaveCloudModel()` | `document.SaveCloudModel()` | Void |
| `ElementId SaveToProjectAsImage(ImageExportOptions)` | `document.SaveToProjectAsImage(options)` | ElementId |
| `Void SeparateElements(CombinableElementArray)` | `document.SeparateElements(members)` | Void |
| `Void SetDefaultElementTypeId(ElementTypeGroup, ElementId)` | `document.SetDefaultElementTypeId(defaultTypeId, typeId)` | Void |
| `Void SetDefaultFamilyTypeId(ElementId, ElementId)` | `document.SetDefaultFamilyTypeId(familyCategoryId, familyTypeId)` | Void |
| `Void SetUnits(Units)` | `document.SetUnits(units)` | Void |
| `Void SynchronizeWithCentral(TransactWithCentralOptions, SynchronizeWithCentralOptions)` | `document.SynchronizeWithCentral(transactOptions, syncOptions)` | Void |
| `Void UnpostFailure(FailureMessageKey)` | `document.UnpostFailure(messageKey)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
