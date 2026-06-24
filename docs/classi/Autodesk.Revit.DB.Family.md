---
title: Family
classe: Autodesk.Revit.DB.Family
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 25
---

# Family

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double CurtainPanelHorizontalSpacing { get; set; }` | `family.CurtainPanelHorizontalSpacing` | Double |
| `TilePatternsBuiltIn CurtainPanelTilePattern { get; }` | `family.CurtainPanelTilePattern` | TilePatternsBuiltIn |
| `Double CurtainPanelVerticalSpacing { get; set; }` | `family.CurtainPanelVerticalSpacing` | Double |
| `Category FamilyCategory { get; set; }` | `family.FamilyCategory` | Category |
| `ElementId FamilyCategoryId { get; set; }` | `family.FamilyCategoryId` | ElementId |
| `FamilyPlacementType FamilyPlacementType { get; }` | `family.FamilyPlacementType` | FamilyPlacementType |
| `Boolean IsConceptualMassFamily { get; }` | `family.IsConceptualMassFamily` | Boolean |
| `Boolean IsCurtainPanelFamily { get; }` | `family.IsCurtainPanelFamily` | Boolean |
| `Boolean IsEditable { get; }` | `family.IsEditable` | Boolean |
| `Boolean IsInPlace { get; }` | `family.IsInPlace` | Boolean |
| `Boolean IsOwnerFamily { get; }` | `family.IsOwnerFamily` | Boolean |
| `Boolean IsParametric { get; }` | `family.IsParametric` | Boolean |
| `Boolean IsUserCreated { get; }` | `family.IsUserCreated` | Boolean |
| `Boolean ShowSpatialElementCalculationPoint { get; set; }` | `family.ShowSpatialElementCalculationPoint` | Boolean |
| `String StructuralCodeName { get; set; }` | `family.StructuralCodeName` | String |
| `String StructuralFamilyNameKey { get; set; }` | `family.StructuralFamilyNameKey` | String |
| `StructuralMaterialType StructuralMaterialType { get; }` | `family.StructuralMaterialType` | StructuralMaterialType |
| `StructuralSectionShape StructuralSectionShape { get; set; }` | `family.StructuralSectionShape` | StructuralSectionShape |
| `Boolean CanHaveStructuralSection()` | `family.CanHaveStructuralSection()` | Boolean |
| `Boolean CanLoadFamilies(Document)` | `Family.CanLoadFamilies(document)` | Boolean |
| `Void ExtractPartAtom(String)` | `family.ExtractPartAtom(xmlFilePath)` | Void |
| `ISet<ElementId> GetFamilySymbolIds()` | `family.GetFamilySymbolIds()` | ISet<ElementId> |
| `ISet<ElementId> GetFamilyTypeParameterValues(ElementId)` | `family.GetFamilyTypeParameterValues(parameterId)` | ISet<ElementId> |
| `Boolean HasLargeSketches()` | `family.HasLargeSketches()` | Boolean |
| `Boolean IsAppropriateCategoryId(ElementId)` | `family.IsAppropriateCategoryId(categoryId)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
