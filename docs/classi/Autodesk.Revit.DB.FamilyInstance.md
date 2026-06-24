---
title: FamilyInstance
classe: Autodesk.Revit.DB.FamilyInstance
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Instance
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 56
---

# FamilyInstance

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean CanFlipFacing { get; }` | `familyInstance.CanFlipFacing` | Boolean |
| `Boolean CanFlipHand { get; }` | `familyInstance.CanFlipHand` | Boolean |
| `Boolean CanFlipWorkPlane { get; }` | `familyInstance.CanFlipWorkPlane` | Boolean |
| `Boolean CanRotate { get; }` | `familyInstance.CanRotate` | Boolean |
| `Boolean CanSplit { get; }` | `familyInstance.CanSplit` | Boolean |
| `IExtension ExtensionUtility { get; }` | `familyInstance.ExtensionUtility` | IExtension |
| `Boolean FacingFlipped { get; }` | `familyInstance.FacingFlipped` | Boolean |
| `XYZ FacingOrientation { get; }` | `familyInstance.FacingOrientation` | XYZ |
| `Room FromRoom { get; }` | `familyInstance.FromRoom` | Room |
| `Room FromRoom { get; }` | `familyInstance.FromRoom` | Room |
| `Boolean HandFlipped { get; }` | `familyInstance.HandFlipped` | Boolean |
| `XYZ HandOrientation { get; }` | `familyInstance.HandOrientation` | XYZ |
| `Boolean HasSpatialElementCalculationPoint { get; }` | `familyInstance.HasSpatialElementCalculationPoint` | Boolean |
| `Boolean HasSpatialElementFromToCalculationPoints { get; }` | `familyInstance.HasSpatialElementFromToCalculationPoints` | Boolean |
| `Element Host { get; }` | `familyInstance.Host` | Element |
| `Reference HostFace { get; }` | `familyInstance.HostFace` | Reference |
| `Double HostParameter { get; }` | `familyInstance.HostParameter` | Double |
| `Boolean Invisible { get; }` | `familyInstance.Invisible` | Boolean |
| `Boolean IsSlantedColumn { get; }` | `familyInstance.IsSlantedColumn` | Boolean |
| `Boolean IsWorkPlaneFlipped { get; set; }` | `familyInstance.IsWorkPlaneFlipped` | Boolean |
| `Location Location { get; }` | `familyInstance.Location` | Location |
| `MEPModel MEPModel { get; }` | `familyInstance.MEPModel` | MEPModel |
| `Boolean Mirrored { get; }` | `familyInstance.Mirrored` | Boolean |
| `Room Room { get; }` | `familyInstance.Room` | Room |
| `Room Room { get; }` | `familyInstance.Room` | Room |
| `Space Space { get; }` | `familyInstance.Space` | Space |
| `Space Space { get; }` | `familyInstance.Space` | Space |
| `ElementId StructuralMaterialId { get; set; }` | `familyInstance.StructuralMaterialId` | ElementId |
| `StructuralMaterialType StructuralMaterialType { get; }` | `familyInstance.StructuralMaterialType` | StructuralMaterialType |
| `StructuralType StructuralType { get; }` | `familyInstance.StructuralType` | StructuralType |
| `StructuralInstanceUsage StructuralUsage { get; set; }` | `familyInstance.StructuralUsage` | StructuralInstanceUsage |
| `Element SuperComponent { get; }` | `familyInstance.SuperComponent` | Element |
| `FamilySymbol Symbol { get; set; }` | `familyInstance.Symbol` | FamilySymbol |
| `Room ToRoom { get; }` | `familyInstance.ToRoom` | Room |
| `Room ToRoom { get; }` | `familyInstance.ToRoom` | Room |
| `Boolean AddCoping(FamilyInstance)` | `familyInstance.AddCoping(cutter)` | Boolean |
| `Boolean flipFacing()` | `familyInstance.flipFacing()` | Boolean |
| `Void FlipFromToRoom()` | `familyInstance.FlipFromToRoom()` | Void |
| `Boolean flipHand()` | `familyInstance.flipHand()` | Boolean |
| `ICollection<ElementId> GetCopingIds()` | `familyInstance.GetCopingIds()` | ICollection<ElementId> |
| `IList<FamilyPointPlacementReference> GetFamilyPointPlacementReferences()` | `familyInstance.GetFamilyPointPlacementReferences()` | IList<FamilyPointPlacementReference> |
| `GeometryElement GetOriginalGeometry(Options)` | `familyInstance.GetOriginalGeometry(options)` | GeometryElement |
| `Reference GetReferenceByName(String)` | `familyInstance.GetReferenceByName(name)` | Reference |
| `String GetReferenceName(Reference)` | `familyInstance.GetReferenceName(reference)` | String |
| `IList<Reference> GetReferences(FamilyInstanceReferenceType)` | `familyInstance.GetReferences(referenceType)` | IList<Reference> |
| `FamilyInstanceReferenceType GetReferenceType(Reference)` | `familyInstance.GetReferenceType(reference)` | FamilyInstanceReferenceType |
| `XYZ GetSpatialElementCalculationPoint()` | `familyInstance.GetSpatialElementCalculationPoint()` | XYZ |
| `IList<XYZ> GetSpatialElementFromToCalculationPoints()` | `familyInstance.GetSpatialElementFromToCalculationPoints()` | IList<XYZ> |
| `ICollection<ElementId> GetSubComponentIds()` | `familyInstance.GetSubComponentIds()` | ICollection<ElementId> |
| `SweptProfile GetSweptProfile()` | `familyInstance.GetSweptProfile()` | SweptProfile |
| `Boolean HasModifiedGeometry()` | `familyInstance.HasModifiedGeometry()` | Boolean |
| `Boolean HasSweptProfile()` | `familyInstance.HasSweptProfile()` | Boolean |
| `Boolean RemoveCoping(FamilyInstance)` | `familyInstance.RemoveCoping(cutter)` | Boolean |
| `Boolean rotate()` | `familyInstance.rotate()` | Boolean |
| `Boolean SetCopingIds(ICollection<ElementId>)` | `familyInstance.SetCopingIds(cutters)` | Boolean |
| `ElementId Split(Double)` | `familyInstance.Split(param)` | ElementId |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
