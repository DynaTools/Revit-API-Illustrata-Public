---
title: FabricSheetType
classe: Autodesk.Revit.DB.Structure.FabricSheetType
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.ElementType
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 36
---

# FabricSheetType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId MajorDirectionWireType { get; set; }` | `fabricSheetType.MajorDirectionWireType` | ElementId |
| `Double MajorEndOverhang { get; }` | `fabricSheetType.MajorEndOverhang` | Double |
| `Double MajorLapSpliceLength { get; set; }` | `fabricSheetType.MajorLapSpliceLength` | Double |
| `FabricSheetLayoutPattern MajorLayoutPattern { get; }` | `fabricSheetType.MajorLayoutPattern` | FabricSheetLayoutPattern |
| `Int32 MajorNumberOfWires { get; }` | `fabricSheetType.MajorNumberOfWires` | Int32 |
| `Double MajorReinforcementArea { get; }` | `fabricSheetType.MajorReinforcementArea` | Double |
| `Double MajorSpacing { get; }` | `fabricSheetType.MajorSpacing` | Double |
| `Double MajorStartOverhang { get; }` | `fabricSheetType.MajorStartOverhang` | Double |
| `ElementId Material { get; set; }` | `fabricSheetType.Material` | ElementId |
| `ElementId MinorDirectionWireType { get; set; }` | `fabricSheetType.MinorDirectionWireType` | ElementId |
| `Double MinorEndOverhang { get; }` | `fabricSheetType.MinorEndOverhang` | Double |
| `Double MinorLapSpliceLength { get; set; }` | `fabricSheetType.MinorLapSpliceLength` | Double |
| `FabricSheetLayoutPattern MinorLayoutPattern { get; }` | `fabricSheetType.MinorLayoutPattern` | FabricSheetLayoutPattern |
| `Int32 MinorNumberOfWires { get; }` | `fabricSheetType.MinorNumberOfWires` | Int32 |
| `Double MinorReinforcementArea { get; }` | `fabricSheetType.MinorReinforcementArea` | Double |
| `Double MinorSpacing { get; }` | `fabricSheetType.MinorSpacing` | Double |
| `Double MinorStartOverhang { get; }` | `fabricSheetType.MinorStartOverhang` | Double |
| `Double OverallLength { get; }` | `fabricSheetType.OverallLength` | Double |
| `Double OverallWidth { get; }` | `fabricSheetType.OverallWidth` | Double |
| `Double SheetMass { get; set; }` | `fabricSheetType.SheetMass` | Double |
| `Double SheetMassUnit { get; }` | `fabricSheetType.SheetMassUnit` | Double |
| `ElementId CreateDefaultFabricSheetType(Document)` | `FabricSheetType.CreateDefaultFabricSheetType(ADoc)` | ElementId |
| `FabricRoundingManager GetReinforcementRoundingManager()` | `fabricSheetType.GetReinforcementRoundingManager()` | FabricRoundingManager |
| `FabricWireItem GetWireItem(Int32, WireDistributionDirection)` | `fabricSheetType.GetWireItem(wireIndex, direction)` | FabricWireItem |
| `Boolean IsCustom()` | `fabricSheetType.IsCustom()` | Boolean |
| `Boolean IsValidMajorLapSplice(Double)` | `fabricSheetType.IsValidMajorLapSplice(majorLapSplice)` | Boolean |
| `Boolean IsValidMinorLapSplice(Double)` | `fabricSheetType.IsValidMinorLapSplice(minorLapSplice)` | Boolean |
| `Void SetLayoutAsCustomPattern(Double, Double, IList<FabricWireItem>, IList<FabricWireItem>)` | `fabricSheetType.SetLayoutAsCustomPattern(minorStartOverhang, majorStartOverhang, minorFabricWireItems, majorFabricWireItems)` | Void |
| `Void SetMajorLayoutAsActualSpacing(Double, Double, Double)` | `fabricSheetType.SetMajorLayoutAsActualSpacing(overallWidth, minorStartOverhang, spacing)` | Void |
| `Void SetMajorLayoutAsFixedNumber(Double, Double, Double, Int32)` | `fabricSheetType.SetMajorLayoutAsFixedNumber(overallWidth, minorStartOverhang, minorEndOverhang, numberOfWires)` | Void |
| `Void SetMajorLayoutAsMaximumSpacing(Double, Double, Double, Double)` | `fabricSheetType.SetMajorLayoutAsMaximumSpacing(overallWidth, minorStartOverhang, minorEndOverhang, spacing)` | Void |
| `Void SetMajorLayoutAsNumberWithSpacing(Double, Double, Int32, Double)` | `fabricSheetType.SetMajorLayoutAsNumberWithSpacing(overallWidth, minorStartOverhang, numberOfWires, spacing)` | Void |
| `Void SetMinorLayoutAsActualSpacing(Double, Double, Double)` | `fabricSheetType.SetMinorLayoutAsActualSpacing(overallLength, majorStartOverhang, spacing)` | Void |
| `Void SetMinorLayoutAsFixedNumber(Double, Double, Double, Int32)` | `fabricSheetType.SetMinorLayoutAsFixedNumber(overallLength, majorStartOverhang, majorEndOverhang, numberOfWires)` | Void |
| `Void SetMinorLayoutAsMaximumSpacing(Double, Double, Double, Double)` | `fabricSheetType.SetMinorLayoutAsMaximumSpacing(overallLength, majorStartOverhang, majorEndOverhang, spacing)` | Void |
| `Void SetMinorLayoutAsNumberWithSpacing(Double, Double, Int32, Double)` | `fabricSheetType.SetMinorLayoutAsNumberWithSpacing(overallLength, majorStartOverhang, numberOfWires, spacing)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
