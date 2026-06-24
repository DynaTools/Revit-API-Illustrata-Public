---
title: Element
classe: Autodesk.Revit.DB.Element
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 86
---

# Element

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId AssemblyInstanceId { get; }` | `element.AssemblyInstanceId` | ElementId |
| `BoundingBoxXYZ BoundingBox { get; }` | `element.BoundingBox` | BoundingBoxXYZ |
| `Category Category { get; }` | `element.Category` | Category |
| `ElementId CreatedPhaseId { get; set; }` | `element.CreatedPhaseId` | ElementId |
| `ElementId DemolishedPhaseId { get; set; }` | `element.DemolishedPhaseId` | ElementId |
| `DesignOption DesignOption { get; }` | `element.DesignOption` | DesignOption |
| `Document Document { get; }` | `element.Document` | Document |
| `GeometryElement Geometry { get; }` | `element.Geometry` | GeometryElement |
| `ElementId GroupId { get; }` | `element.GroupId` | ElementId |
| `ElementId Id { get; }` | `element.Id` | ElementId |
| `Boolean IsModifiable { get; }` | `element.IsModifiable` | Boolean |
| `Boolean IsTransient { get; }` | `element.IsTransient` | Boolean |
| `Boolean IsValidObject { get; }` | `element.IsValidObject` | Boolean |
| `ElementId LevelId { get; }` | `element.LevelId` | ElementId |
| `Location Location { get; }` | `element.Location` | Location |
| `String Name { get; set; }` | `element.Name` | String |
| `ElementId OwnerViewId { get; }` | `element.OwnerViewId` | ElementId |
| `Parameter Parameter { get; }` | `element.Parameter` | Parameter |
| `Parameter Parameter { get; }` | `element.Parameter` | Parameter |
| `Parameter Parameter { get; }` | `element.Parameter` | Parameter |
| `ParameterSet Parameters { get; }` | `element.Parameters` | ParameterSet |
| `ParameterMap ParametersMap { get; }` | `element.ParametersMap` | ParameterMap |
| `Boolean Pinned { get; set; }` | `element.Pinned` | Boolean |
| `String UniqueId { get; }` | `element.UniqueId` | String |
| `Guid VersionGuid { get; }` | `element.VersionGuid` | Guid |
| `Boolean ViewSpecific { get; }` | `element.ViewSpecific` | Boolean |
| `WorksetId WorksetId { get; }` | `element.WorksetId` | WorksetId |
| `Boolean ArePhasesModifiable()` | `element.ArePhasesModifiable()` | Boolean |
| `Boolean CanBeHidden(View)` | `element.CanBeHidden(pView)` | Boolean |
| `Boolean CanBeLocked()` | `element.CanBeLocked()` | Boolean |
| `Boolean CanDeleteSubelement(Subelement)` | `element.CanDeleteSubelement(subelem)` | Boolean |
| `Boolean CanHaveTypeAssigned(Document, ICollection<ElementId>)` | `Element.CanHaveTypeAssigned(document, elementIds)` | Boolean |
| `Boolean CanHaveTypeAssigned()` | `element.CanHaveTypeAssigned()` | Boolean |
| `IDictionary<ElementId, ElementId> ChangeTypeId(Document, ICollection<ElementId>, ElementId)` | `Element.ChangeTypeId(document, elementIds, typeId)` | IDictionary<ElementId, ElementId> |
| `ElementId ChangeTypeId(ElementId)` | `element.ChangeTypeId(typeId)` | ElementId |
| `Boolean DeleteEntity(Schema)` | `element.DeleteEntity(schema)` | Boolean |
| `Boolean DeleteSubelement(Subelement)` | `element.DeleteSubelement(subelem)` | Boolean |
| `Boolean DeleteSubelements(IList<Subelement>)` | `element.DeleteSubelements(subelems)` | Boolean |
| `Void Dispose()` | `element.Dispose()` | Void |
| `IList<EvaluatedParameter> EvaluateAllParameterValues()` | `element.EvaluateAllParameterValues()` | IList<EvaluatedParameter> |
| `IList<EvaluatedParameter> EvaluateParameterValues(ISet<ElementId>)` | `element.EvaluateParameterValues(parameterIds)` | IList<EvaluatedParameter> |
| `ChangeType GetChangeTypeAny()` | `Element.GetChangeTypeAny()` | ChangeType |
| `ChangeType GetChangeTypeElementAddition()` | `Element.GetChangeTypeElementAddition()` | ChangeType |
| `ChangeType GetChangeTypeElementDeletion()` | `Element.GetChangeTypeElementDeletion()` | ChangeType |
| `ChangeType GetChangeTypeGeometry()` | `Element.GetChangeTypeGeometry()` | ChangeType |
| `ChangeType GetChangeTypeParameter(ElementId)` | `Element.GetChangeTypeParameter(parameterId)` | ChangeType |
| `ChangeType GetChangeTypeParameter(Parameter)` | `Element.GetChangeTypeParameter(param)` | ChangeType |
| `IList<ElementId> GetDependentElements(ElementFilter)` | `element.GetDependentElements(filter)` | IList<ElementId> |
| `Entity GetEntity(Schema)` | `element.GetEntity(schema)` | Entity |
| `IList<Guid> GetEntitySchemaGuids()` | `element.GetEntitySchemaGuids()` | IList<Guid> |
| `ExternalFileReference GetExternalFileReference()` | `element.GetExternalFileReference()` | ExternalFileReference |
| `ExternalResourceReference GetExternalResourceReference(ExternalResourceType)` | `element.GetExternalResourceReference(resourceType)` | ExternalResourceReference |
| `IList<ExternalResourceReference> GetExternalResourceReferenceExpanded(ExternalResourceType)` | `element.GetExternalResourceReferenceExpanded(resourceType)` | IList<ExternalResourceReference> |
| `IDictionary<ExternalResourceType, ExternalResourceReference> GetExternalResourceReferences()` | `element.GetExternalResourceReferences()` | IDictionary<ExternalResourceType, ExternalResourceReference> |
| `IDictionary<ExternalResourceType, IList<ExternalResourceReference>> GetExternalResourceReferencesExpanded()` | `element.GetExternalResourceReferencesExpanded()` | IDictionary<ExternalResourceType, IList<ExternalResourceReference>> |
| `ICollection<ElementId> GetGeneratingElementIds(GeometryObject)` | `element.GetGeneratingElementIds(geometryObject)` | ICollection<ElementId> |
| `GeometryObject GetGeometryObjectFromReference(Reference)` | `element.GetGeometryObjectFromReference(reference)` | GeometryObject |
| `Double GetMaterialArea(ElementId, Boolean)` | `element.GetMaterialArea(materialId, usePaintMaterial)` | Double |
| `ICollection<ElementId> GetMaterialIds(Boolean)` | `element.GetMaterialIds(returnPaintMaterials)` | ICollection<ElementId> |
| `Double GetMaterialVolume(ElementId)` | `element.GetMaterialVolume(materialId)` | Double |
| `IList<ElementId> GetMonitoredLinkElementIds()` | `element.GetMonitoredLinkElementIds()` | IList<ElementId> |
| `IList<ElementId> GetMonitoredLocalElementIds()` | `element.GetMonitoredLocalElementIds()` | IList<ElementId> |
| `IList<Parameter> GetOrderedParameters()` | `element.GetOrderedParameters()` | IList<Parameter> |
| `Parameter GetParameter(ForgeTypeId)` | `element.GetParameter(parameterTypeId)` | Parameter |
| `FormatOptions GetParameterFormatOptions(ElementId)` | `element.GetParameterFormatOptions(parameterId)` | FormatOptions |
| `IList<Parameter> GetParameters(String)` | `element.GetParameters(name)` | IList<Parameter> |
| `ElementOnPhaseStatus GetPhaseStatus(ElementId)` | `element.GetPhaseStatus(phaseId)` | ElementOnPhaseStatus |
| `IList<Subelement> GetSubelements()` | `element.GetSubelements()` | IList<Subelement> |
| `ElementId GetTypeId()` | `element.GetTypeId()` | ElementId |
| `ICollection<ElementId> GetValidTypes(Document, ICollection<ElementId>)` | `Element.GetValidTypes(document, elementIds)` | ICollection<ElementId> |
| `ICollection<ElementId> GetValidTypes()` | `element.GetValidTypes()` | ICollection<ElementId> |
| `Boolean HasPhases()` | `element.HasPhases()` | Boolean |
| `Boolean IsCreatedPhaseOrderValid(ElementId)` | `element.IsCreatedPhaseOrderValid(createdPhaseId)` | Boolean |
| `Boolean IsDemolishedPhaseOrderValid(ElementId)` | `element.IsDemolishedPhaseOrderValid(demolishedPhaseId)` | Boolean |
| `Boolean IsExternalFileReference()` | `element.IsExternalFileReference()` | Boolean |
| `Boolean IsHidden(View)` | `element.IsHidden(pView)` | Boolean |
| `Boolean IsMonitoringLinkElement()` | `element.IsMonitoringLinkElement()` | Boolean |
| `Boolean IsMonitoringLocalElement()` | `element.IsMonitoringLocalElement()` | Boolean |
| `Boolean IsPhaseCreatedValid(ElementId)` | `element.IsPhaseCreatedValid(createdPhaseId)` | Boolean |
| `Boolean IsPhaseDemolishedValid(ElementId)` | `element.IsPhaseDemolishedValid(demolishedPhaseId)` | Boolean |
| `Boolean IsValidType(Document, ICollection<ElementId>, ElementId)` | `Element.IsValidType(document, elementIds, typeId)` | Boolean |
| `Boolean IsValidType(ElementId)` | `element.IsValidType(typeId)` | Boolean |
| `Parameter LookupParameter(String)` | `element.LookupParameter(name)` | Parameter |
| `Boolean RefersToExternalResourceReference(ExternalResourceType)` | `element.RefersToExternalResourceReference(resourceType)` | Boolean |
| `Boolean RefersToExternalResourceReferences()` | `element.RefersToExternalResourceReferences()` | Boolean |
| `Void SetEntity(Entity)` | `element.SetEntity(entity)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
