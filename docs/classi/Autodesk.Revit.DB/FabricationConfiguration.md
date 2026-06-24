---
title: FabricationConfiguration
classe: Autodesk.Revit.DB.FabricationConfiguration
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 71
---

# FabricationConfiguration

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean AncillaryExists(Int32)` | `fabricationConfiguration.AncillaryExists(ancillaryId)` | Boolean |
| `Boolean AreItemFilesLoaded(IList<FabricationItemFile>)` | `fabricationConfiguration.AreItemFilesLoaded(itemFiles)` | Boolean |
| `Boolean CanBeSwapped()` | `fabricationConfiguration.CanBeSwapped()` | Boolean |
| `Boolean CanUnloadItemFiles(IList<FabricationItemFile>)` | `fabricationConfiguration.CanUnloadItemFiles(itemFiles)` | Boolean |
| `Int32 CheckConnectionsForAllFabricationParts()` | `fabricationConfiguration.CheckConnectionsForAllFabricationParts()` | Int32 |
| `Boolean CustomDataExists(Int32)` | `fabricationConfiguration.CustomDataExists(customDataId)` | Boolean |
| `Boolean DamperExists(Int32)` | `fabricationConfiguration.DamperExists(damperId)` | Boolean |
| `IList<Int32> GetAllDampers()` | `fabricationConfiguration.GetAllDampers()` | IList<Int32> |
| `IList<Int32> GetAllFabricationConnectorDefinitions(ConnectorDomainType, ConnectorProfileType)` | `fabricationConfiguration.GetAllFabricationConnectorDefinitions(domain, shape)` | IList<Int32> |
| `IList<Int32> GetAllInsulationSpecifications(FabricationPart)` | `fabricationConfiguration.GetAllInsulationSpecifications(pFabPart)` | IList<Int32> |
| `IList<FabricationItemFile> GetAllLoadedItemFiles()` | `fabricationConfiguration.GetAllLoadedItemFiles()` | IList<FabricationItemFile> |
| `IList<FabricationService> GetAllLoadedServices()` | `fabricationConfiguration.GetAllLoadedServices()` | IList<FabricationService> |
| `IList<Int32> GetAllMaterials(FabricationPart)` | `fabricationConfiguration.GetAllMaterials(part)` | IList<Int32> |
| `IList<Int32> GetAllPartCustomData()` | `fabricationConfiguration.GetAllPartCustomData()` | IList<Int32> |
| `IList<Int32> GetAllPartStatuses()` | `fabricationConfiguration.GetAllPartStatuses()` | IList<Int32> |
| `IList<FabricationService> GetAllServices()` | `fabricationConfiguration.GetAllServices()` | IList<FabricationService> |
| `IList<Int32> GetAllSpecifications(FabricationPart)` | `fabricationConfiguration.GetAllSpecifications(part)` | IList<Int32> |
| `IList<FabricationItemFile> GetAllUsedItemFiles()` | `fabricationConfiguration.GetAllUsedItemFiles()` | IList<FabricationItemFile> |
| `IList<FabricationService> GetAllUsedServices()` | `fabricationConfiguration.GetAllUsedServices()` | IList<FabricationService> |
| `IList<Int32> GetAncillaries(FabricationAncillaryType, Boolean, Boolean)` | `fabricationConfiguration.GetAncillaries(type, includeKits, filterKits)` | IList<Int32> |
| `String GetAncillaryGroup(Int32)` | `fabricationConfiguration.GetAncillaryGroup(ancillaryId)` | String |
| `String GetAncillaryGroupName(Int32)` | `fabricationConfiguration.GetAncillaryGroupName(ancillaryId)` | String |
| `String GetAncillaryName(Int32)` | `fabricationConfiguration.GetAncillaryName(ancillaryId)` | String |
| `String GetDamperName(Int32)` | `fabricationConfiguration.GetDamperName(damperId)` | String |
| `FabricationConfiguration GetFabricationConfiguration(Document)` | `FabricationConfiguration.GetFabricationConfiguration(document)` | FabricationConfiguration |
| `FabricationConfigurationInfo GetFabricationConfigurationInfo()` | `fabricationConfiguration.GetFabricationConfigurationInfo()` | FabricationConfigurationInfo |
| `ConnectorDomainType GetFabricationConnectorDomain(Int32)` | `fabricationConfiguration.GetFabricationConnectorDomain(fabricationConnectorId)` | ConnectorDomainType |
| `String GetFabricationConnectorGroup(Int32)` | `fabricationConfiguration.GetFabricationConnectorGroup(fabricationConnectorId)` | String |
| `String GetFabricationConnectorName(Int32)` | `fabricationConfiguration.GetFabricationConnectorName(fabricationConnectorId)` | String |
| `ConnectorProfileType GetFabricationConnectorShape(Int32)` | `fabricationConfiguration.GetFabricationConnectorShape(fabricationConnectorId)` | ConnectorProfileType |
| `String GetInsulationSpecificationAbbreviation(Int32)` | `fabricationConfiguration.GetInsulationSpecificationAbbreviation(insulationSpecificationId)` | String |
| `String GetInsulationSpecificationGroup(Int32)` | `fabricationConfiguration.GetInsulationSpecificationGroup(specId)` | String |
| `String GetInsulationSpecificationName(Int32)` | `fabricationConfiguration.GetInsulationSpecificationName(specId)` | String |
| `IList<FabricationItemFolder> GetItemFolders()` | `fabricationConfiguration.GetItemFolders()` | IList<FabricationItemFolder> |
| `String GetMaterialAbbreviation(Int32)` | `fabricationConfiguration.GetMaterialAbbreviation(materialId)` | String |
| `Int32 GetMaterialByGUID(Guid)` | `fabricationConfiguration.GetMaterialByGUID(materialGUID)` | Int32 |
| `Int32 GetMaterialGaugeByGUID(Guid, Int32)` | `fabricationConfiguration.GetMaterialGaugeByGUID(gaugeGUID, materialId)` | Int32 |
| `Guid GetMaterialGaugeGUID(Int32, Int32)` | `fabricationConfiguration.GetMaterialGaugeGUID(materialId, gaugeId)` | Guid |
| `String GetMaterialGroup(Int32)` | `fabricationConfiguration.GetMaterialGroup(materialId)` | String |
| `Guid GetMaterialGUID(Int32)` | `fabricationConfiguration.GetMaterialGUID(materialId)` | Guid |
| `String GetMaterialName(Int32)` | `fabricationConfiguration.GetMaterialName(materialId)` | String |
| `String GetPartCustomDataName(Int32)` | `fabricationConfiguration.GetPartCustomDataName(customDataId)` | String |
| `FabricationCustomDataType GetPartCustomDataType(Int32)` | `fabricationConfiguration.GetPartCustomDataType(customDataId)` | FabricationCustomDataType |
| `String GetPartStatusDescription(Int32)` | `fabricationConfiguration.GetPartStatusDescription(statusId)` | String |
| `String GetProfile()` | `fabricationConfiguration.GetProfile()` | String |
| `FabricationService GetService(Int32)` | `fabricationConfiguration.GetService(serviceId)` | FabricationService |
| `Int32 GetServiceByGUID(Guid)` | `fabricationConfiguration.GetServiceByGUID(serviceGUID)` | Int32 |
| `Guid GetServiceGUID(Int32)` | `fabricationConfiguration.GetServiceGUID(serviceId)` | Guid |
| `String GetServiceTypeName(Int32)` | `fabricationConfiguration.GetServiceTypeName(serviceTypeId)` | String |
| `String GetSpecificationAbbreviation(Int32)` | `fabricationConfiguration.GetSpecificationAbbreviation(specificationId)` | String |
| `Int32 GetSpecificationByGUID(Guid)` | `fabricationConfiguration.GetSpecificationByGUID(specificationGUID)` | Int32 |
| `String GetSpecificationGroup(Int32)` | `fabricationConfiguration.GetSpecificationGroup(specId)` | String |
| `Guid GetSpecificationGUID(Int32)` | `fabricationConfiguration.GetSpecificationGUID(specificationId)` | Guid |
| `String GetSpecificationName(Int32)` | `fabricationConfiguration.GetSpecificationName(specId)` | String |
| `ISet<ElementId> GetUpdatedStraightsFromValidateConnections()` | `fabricationConfiguration.GetUpdatedStraightsFromValidateConnections()` | ISet<ElementId> |
| `Boolean HasValidConfiguration()` | `fabricationConfiguration.HasValidConfiguration()` | Boolean |
| `Boolean IsAncillaryKit(Int32)` | `fabricationConfiguration.IsAncillaryKit(ancillaryId)` | Boolean |
| `IList<FabricationItemFile> LoadItemFiles(IList<FabricationItemFile>)` | `fabricationConfiguration.LoadItemFiles(itemFiles)` | IList<FabricationItemFile> |
| `IList<Int32> LoadServices(IList<Int32>)` | `fabricationConfiguration.LoadServices(serviceIds)` | IList<Int32> |
| `Int32 LocateFabricationConnector(String, String, ConnectorDomainType, ConnectorProfileType)` | `fabricationConfiguration.LocateFabricationConnector(group, name, domain, shape)` | Int32 |
| `Int32 LocateInsulationSpecification(String, String)` | `fabricationConfiguration.LocateInsulationSpecification(group, name)` | Int32 |
| `Int32 LocateMaterial(String, String)` | `fabricationConfiguration.LocateMaterial(group, name)` | Int32 |
| `Int32 LocateSpecification(String, String)` | `fabricationConfiguration.LocateSpecification(group, name)` | Int32 |
| `Void PostReviewableWarningsForBadConnections(ConnectionValidationInfo)` | `fabricationConfiguration.PostReviewableWarningsForBadConnections(info)` | Void |
| `ConfigurationReloadInfo ReloadConfiguration()` | `fabricationConfiguration.ReloadConfiguration()` | ConfigurationReloadInfo |
| `Void SetConfiguration(FabricationConfigurationInfo, String)` | `fabricationConfiguration.SetConfiguration(fabricationConfigurationInfo, profile)` | Void |
| `Void SetConfiguration(FabricationConfigurationInfo)` | `fabricationConfiguration.SetConfiguration(fabricationConfigurationInfo)` | Void |
| `Boolean SetServicesToLoad(IList<Int32>)` | `fabricationConfiguration.SetServicesToLoad(serviceIds)` | Boolean |
| `Void UnloadItemFiles(IList<FabricationItemFile>)` | `fabricationConfiguration.UnloadItemFiles(itemFiles)` | Void |
| `Void UnloadServices(IList<Int32>)` | `fabricationConfiguration.UnloadServices(serviceIds)` | Void |
| `ConnectionValidationInfo ValidateConnectionsForAllFabricationParts(Boolean)` | `fabricationConfiguration.ValidateConnectionsForAllFabricationParts(updateGapForStraights)` | ConnectionValidationInfo |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
