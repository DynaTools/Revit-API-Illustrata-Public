---
title: FabricationPart
classe: Autodesk.Revit.DB.FabricationPart
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 120
---

# FabricationPart

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String Alias { get; }` | `fabricationPart.Alias` | String |
| `Double BottomOfPartElevation { get; }` | `fabricationPart.BottomOfPartElevation` | Double |
| `Double CenterlineLength { get; }` | `fabricationPart.CenterlineLength` | Double |
| `ConnectorManager ConnectorManager { get; }` | `fabricationPart.ConnectorManager` | ConnectorManager |
| `Int32 CutType { get; }` | `fabricationPart.CutType` | Int32 |
| `ConnectorDomainType DomainType { get; }` | `fabricationPart.DomainType` | ConnectorDomainType |
| `Int32 DoubleWallMaterial { get; }` | `fabricationPart.DoubleWallMaterial` | Int32 |
| `Double DoubleWallMaterialArea { get; }` | `fabricationPart.DoubleWallMaterialArea` | Double |
| `Double DoubleWallMaterialThickness { get; }` | `fabricationPart.DoubleWallMaterialThickness` | Double |
| `String FreeSize { get; }` | `fabricationPart.FreeSize` | String |
| `AssetPropertyUInt64 GeometryChecksum { get; }` | `fabricationPart.GeometryChecksum` | AssetPropertyUInt64 |
| `Int32 HangerRodKit { get; set; }` | `fabricationPart.HangerRodKit` | Int32 |
| `Boolean HasDoubleWall { get; }` | `fabricationPart.HasDoubleWall` | Boolean |
| `Boolean HasInsulation { get; }` | `fabricationPart.HasInsulation` | Boolean |
| `Boolean HasLining { get; }` | `fabricationPart.HasLining` | Boolean |
| `Double InsulationArea { get; }` | `fabricationPart.InsulationArea` | Double |
| `Int32 InsulationSpecification { get; set; }` | `fabricationPart.InsulationSpecification` | Int32 |
| `Double InsulationThickness { get; }` | `fabricationPart.InsulationThickness` | Double |
| `String InsulationType { get; }` | `fabricationPart.InsulationType` | String |
| `Boolean IsBoughtOut { get; }` | `fabricationPart.IsBoughtOut` | Boolean |
| `Int32 ItemCustomId { get; }` | `fabricationPart.ItemCustomId` | Int32 |
| `String ItemNumber { get; set; }` | `fabricationPart.ItemNumber` | String |
| `Double LevelOffset { get; }` | `fabricationPart.LevelOffset` | Double |
| `Double LiningArea { get; }` | `fabricationPart.LiningArea` | Double |
| `Double LiningThickness { get; }` | `fabricationPart.LiningThickness` | Double |
| `String LiningType { get; }` | `fabricationPart.LiningType` | String |
| `Int32 Material { get; set; }` | `fabricationPart.Material` | Int32 |
| `Int32 MaterialGauge { get; }` | `fabricationPart.MaterialGauge` | Int32 |
| `Double MaterialThickness { get; }` | `fabricationPart.MaterialThickness` | Double |
| `String Notes { get; set; }` | `fabricationPart.Notes` | String |
| `XYZ Origin { get; }` | `fabricationPart.Origin` | XYZ |
| `String OverallSize { get; }` | `fabricationPart.OverallSize` | String |
| `Guid PartGuid { get; }` | `fabricationPart.PartGuid` | Guid |
| `Int32 PartStatus { get; set; }` | `fabricationPart.PartStatus` | Int32 |
| `String ProductCode { get; }` | `fabricationPart.ProductCode` | String |
| `String ProductDataRange { get; }` | `fabricationPart.ProductDataRange` | String |
| `String ProductFinishDescription { get; }` | `fabricationPart.ProductFinishDescription` | String |
| `String ProductInstallType { get; }` | `fabricationPart.ProductInstallType` | String |
| `Int32 ProductListEntry { get; set; }` | `fabricationPart.ProductListEntry` | Int32 |
| `String ProductLongDescription { get; }` | `fabricationPart.ProductLongDescription` | String |
| `String ProductMaterialDescription { get; }` | `fabricationPart.ProductMaterialDescription` | String |
| `String ProductName { get; }` | `fabricationPart.ProductName` | String |
| `String ProductOriginalEquipmentManufacture { get; }` | `fabricationPart.ProductOriginalEquipmentManufacture` | String |
| `String ProductShortDescription { get; }` | `fabricationPart.ProductShortDescription` | String |
| `String ProductSizeDescription { get; }` | `fabricationPart.ProductSizeDescription` | String |
| `String ProductSpecificationDescription { get; }` | `fabricationPart.ProductSpecificationDescription` | String |
| `String ServiceAbbreviation { get; }` | `fabricationPart.ServiceAbbreviation` | String |
| `Int32 ServiceId { get; set; }` | `fabricationPart.ServiceId` | Int32 |
| `String ServiceName { get; }` | `fabricationPart.ServiceName` | String |
| `Int32 ServiceType { get; }` | `fabricationPart.ServiceType` | Int32 |
| `Double SheetMetalArea { get; }` | `fabricationPart.SheetMetalArea` | Double |
| `String Size { get; }` | `fabricationPart.Size` | String |
| `Double Slope { get; }` | `fabricationPart.Slope` | Double |
| `Int32 Specification { get; set; }` | `fabricationPart.Specification` | Int32 |
| `String SpoolName { get; set; }` | `fabricationPart.SpoolName` | String |
| `Double TopOfPartElevation { get; }` | `fabricationPart.TopOfPartElevation` | Double |
| `ValidationStatus ValidationStatus { get; }` | `fabricationPart.ValidationStatus` | ValidationStatus |
| `String Vendor { get; }` | `fabricationPart.Vendor` | String |
| `String VendorCode { get; }` | `fabricationPart.VendorCode` | String |
| `Double Weight { get; }` | `fabricationPart.Weight` | Double |
| `Boolean AddPartCustomData(Int32)` | `fabricationPart.AddPartCustomData(customId)` | Boolean |
| `Double AdjustEndLength(Connector, Double, Boolean)` | `fabricationPart.AdjustEndLength(connector, lengthToAdjust, totalLengthOnly)` | Double |
| `Boolean AlignPartByConnector(Document, Connector, XYZ, Double, Double, Double, FabricationPartJustification, Transform)` | `FabricationPart.AlignPartByConnector(document, connector, position, rotation, rotationPerpendicular, slope, justification, trf)` | Boolean |
| `Boolean AlignPartByConnectors(Document, Connector, Connector, Double)` | `FabricationPart.AlignPartByConnectors(document, connector, toConnector, axisRotation)` | Boolean |
| `Boolean AlignPartByConnectorToConnector(Document, Connector, Connector, Double, Double, FabricationPartJustification)` | `FabricationPart.AlignPartByConnectorToConnector(document, connector, fixedConnector, rotation, slope, justification)` | Boolean |
| `Boolean AlignPartByInsertionPoint(Document, ElementId, XYZ, Double, Double, Double, FabricationPartJustification, Transform)` | `FabricationPart.AlignPartByInsertionPoint(document, partId, position, rotation, rotationPerpendicular, slope, justification, trf)` | Boolean |
| `Boolean AlignPartByInsertionPointAndCutInToStraight(Document, ElementId, ElementId, XYZ, Double, Double, Boolean)` | `FabricationPart.AlignPartByInsertionPointAndCutInToStraight(document, straightId, partId, position, rotation, slope, flip)` | Boolean |
| `Boolean CanAdjustEndLength(Connector)` | `fabricationPart.CanAdjustEndLength(connector)` | Boolean |
| `Boolean CanASlopeBeApplied()` | `fabricationPart.CanASlopeBeApplied()` | Boolean |
| `Boolean CanFlipPart()` | `fabricationPart.CanFlipPart()` | Boolean |
| `Boolean CanSplitStraight(XYZ)` | `fabricationPart.CanSplitStraight(position)` | Boolean |
| `Boolean ConnectAndCouple(Document, Connector, Connector)` | `FabricationPart.ConnectAndCouple(document, connector, toConnector)` | Boolean |
| `FabricationPart Create(Document, FabricationItemFile, ElementId)` | `FabricationPart.Create(document, itemFile, levelId)` | FabricationPart |
| `FabricationPart Create(Document, FabricationServiceButton, Int32, ElementId)` | `FabricationPart.Create(document, button, condition, levelId)` | FabricationPart |
| `FabricationPart Create(Document, FabricationServiceButton, Double, Double, ElementId)` | `FabricationPart.Create(document, button, width, depth, levelId)` | FabricationPart |
| `FabricationPart CreateHanger(Document, FabricationServiceButton, Int32, ElementId)` | `FabricationPart.CreateHanger(document, button, condition, levelId)` | FabricationPart |
| `FabricationPart CreateHanger(Document, FabricationServiceButton, Int32, ElementId, Connector, Double, Boolean)` | `FabricationPart.CreateHanger(document, button, condition, hostId, hostConnector, distance, attachToStructure)` | FabricationPart |
| `FabricationPart CreateHanger(Document, FabricationServiceButton, ElementId, Connector, Double, Boolean)` | `FabricationPart.CreateHanger(document, button, hostId, hostConnector, distance, attachToStructure)` | FabricationPart |
| `Boolean Flip()` | `fabricationPart.Flip()` | Boolean |
| `String GetCalculatedDimensionValue(FabricationDimensionDefinition)` | `fabricationPart.GetCalculatedDimensionValue(dim)` | String |
| `IList<String> GetDimensionCalculatedOptions(FabricationDimensionDefinition)` | `fabricationPart.GetDimensionCalculatedOptions(dim)` | IList<String> |
| `IList<FabricationDimensionDefinition> GetDimensions()` | `fabricationPart.GetDimensions()` | IList<FabricationDimensionDefinition> |
| `Double GetDimensionValue(FabricationDimensionDefinition)` | `fabricationPart.GetDimensionValue(dim)` | Double |
| `FabricationHostedInfo GetHostedInfo()` | `fabricationPart.GetHostedInfo()` | FabricationHostedInfo |
| `GeometryElement GetInsulationLiningGeometry()` | `fabricationPart.GetInsulationLiningGeometry()` | GeometryElement |
| `IList<FabricationAncillaryUsage> GetPartAncillaryUsage()` | `fabricationPart.GetPartAncillaryUsage()` | IList<FabricationAncillaryUsage> |
| `Int32 GetPartCustomDataInteger(Int32)` | `fabricationPart.GetPartCustomDataInteger(customId)` | Int32 |
| `Double GetPartCustomDataReal(Int32)` | `fabricationPart.GetPartCustomDataReal(customId)` | Double |
| `String GetPartCustomDataText(Int32)` | `fabricationPart.GetPartCustomDataText(customId)` | String |
| `Int32 GetProductListEntryCount()` | `fabricationPart.GetProductListEntryCount()` | Int32 |
| `String GetProductListEntryName(Int32)` | `fabricationPart.GetProductListEntryName(index)` | String |
| `FabricationRodInfo GetRodInfo()` | `fabricationPart.GetRodInfo()` | FabricationRodInfo |
| `Transform GetTransform()` | `fabricationPart.GetTransform()` | Transform |
| `IList<FabricationVersionInfo> GetVersionHistory()` | `fabricationPart.GetVersionHistory()` | IList<FabricationVersionInfo> |
| `Boolean HasCustomData(Int32)` | `fabricationPart.HasCustomData(customId)` | Boolean |
| `Boolean HasNoConnections()` | `fabricationPart.HasNoConnections()` | Boolean |
| `Boolean IsAHanger()` | `fabricationPart.IsAHanger()` | Boolean |
| `Boolean IsAStraight()` | `fabricationPart.IsAStraight()` | Boolean |
| `Boolean IsATap()` | `fabricationPart.IsATap()` | Boolean |
| `Boolean IsDimensionCalculated(FabricationDimensionDefinition)` | `fabricationPart.IsDimensionCalculated(dim)` | Boolean |
| `Boolean IsProductList()` | `fabricationPart.IsProductList()` | Boolean |
| `Boolean IsProductListEntryCompatibleSize(Int32)` | `fabricationPart.IsProductListEntryCompatibleSize(productEntry)` | Boolean |
| `Boolean IsSameAs(FabricationPart, IList<FabricationPartCompareType>)` | `fabricationPart.IsSameAs(part, ignoreFields)` | Boolean |
| `ISet<ElementId> OptimizeLengths(Document, ISet<ElementId>)` | `FabricationPart.OptimizeLengths(document, partIds)` | ISet<ElementId> |
| `Void PlaceAsTap(Document, Connector, Connector, Double, Double, Double)` | `FabricationPart.PlaceAsTap(document, tapPartConnector, hostPartConnector, distance, axisRotation, secondaryAxisRotation)` | Void |
| `Boolean PlaceFittingAsCutIn(Document, ElementId, ElementId, XYZ, Connector, Double)` | `FabricationPart.PlaceFittingAsCutIn(document, straightId, fittingId, position, fittingConnector, axisRotation)` | Boolean |
| `Boolean RemovePartCustomData(Int32)` | `fabricationPart.RemovePartCustomData(customId)` | Boolean |
| `Void Reposition(Document, ElementId)` | `FabricationPart.Reposition(document, partId)` | Void |
| `Void RotateConnectedPartByConnector(Document, Connector, Double)` | `FabricationPart.RotateConnectedPartByConnector(document, connector, axisRotationBy)` | Void |
| `Void RotateConnectedTap(Document, FabricationPart, Double, Double)` | `FabricationPart.RotateConnectedTap(document, tap, primaryAxisRotateBy, secondaryAxisRotateBy)` | Void |
| `ISet<ElementId> SaveAsFabricationJob(Document, ISet<ElementId>, String, FabricationSaveJobOptions)` | `FabricationPart.SaveAsFabricationJob(document, ids, filename, saveOptions)` | ISet<ElementId> |
| `Void SetCalculatedDimensionValue(FabricationDimensionDefinition, String)` | `fabricationPart.SetCalculatedDimensionValue(dim, value)` | Void |
| `Void SetDimensionValue(FabricationDimensionDefinition, Double)` | `fabricationPart.SetDimensionValue(dim, newValue)` | Void |
| `Void SetPartCustomDataInteger(Int32, Int32)` | `fabricationPart.SetPartCustomDataInteger(customId, value)` | Void |
| `Void SetPartCustomDataReal(Int32, Double)` | `fabricationPart.SetPartCustomDataReal(customId, value)` | Void |
| `Void SetPartCustomDataText(Int32, String)` | `fabricationPart.SetPartCustomDataText(customId, value)` | Void |
| `Void SetPositionByEnd(Connector, XYZ)` | `fabricationPart.SetPositionByEnd(connector, position)` | Void |
| `ElementId SplitStraight(XYZ)` | `fabricationPart.SplitStraight(position)` | ElementId |
| `ElementId SplitStraight(Document, ElementId, XYZ)` | `fabricationPart.SplitStraight(document, partId, position)` | ElementId |
| `FabricationPartFitResult StretchAndFit(Document, Connector, FabricationPartRouteEnd, ISet<ElementId>&)` | `FabricationPart.StretchAndFit(document, stretchConnector, target, newPartIds)` | FabricationPartFitResult |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
