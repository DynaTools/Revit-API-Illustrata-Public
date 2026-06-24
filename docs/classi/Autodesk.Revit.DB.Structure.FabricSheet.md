---
title: FabricSheet
classe: Autodesk.Revit.DB.Structure.FabricSheet
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 33
---

# FabricSheet

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ BendFinalLoopOrientationVector { get; }` | `fabricSheet.BendFinalLoopOrientationVector` | XYZ |
| `BentFabricBendDirection BentFabricBendDirection { get; set; }` | `fabricSheet.BentFabricBendDirection` | BentFabricBendDirection |
| `Double BentFabricLongitudinalCutLength { get; set; }` | `fabricSheet.BentFabricLongitudinalCutLength` | Double |
| `BentFabricStraightWiresLocation BentFabricStraightWiresLocation { get; set; }` | `fabricSheet.BentFabricStraightWiresLocation` | BentFabricStraightWiresLocation |
| `Double CoverOffset { get; set; }` | `fabricSheet.CoverOffset` | Double |
| `Double CutOverallLength { get; }` | `fabricSheet.CutOverallLength` | Double |
| `Double CutOverallWidth { get; }` | `fabricSheet.CutOverallWidth` | Double |
| `Double CutSheetMass { get; }` | `fabricSheet.CutSheetMass` | Double |
| `ElementId FabricAreaOwnerId { get; }` | `fabricSheet.FabricAreaOwnerId` | ElementId |
| `FabricHostReference FabricHostReference { get; set; }` | `fabricSheet.FabricHostReference` | FabricHostReference |
| `FabricLocation FabricLocation { get; set; }` | `fabricSheet.FabricLocation` | FabricLocation |
| `String FabricNumber { get; }` | `fabricSheet.FabricNumber` | String |
| `ElementId HostId { get; }` | `fabricSheet.HostId` | ElementId |
| `Boolean IsBent { get; }` | `fabricSheet.IsBent` | Boolean |
| `ElementId SketchId { get; }` | `fabricSheet.SketchId` | ElementId |
| `FabricSheet Create(Document, ElementId, ElementId, CurveLoop)` | `FabricSheet.Create(document, concreteHostElementId, fabricSheetTypeId, bendProfile)` | FabricSheet |
| `FabricSheet Create(Document, Element, ElementId)` | `FabricSheet.Create(document, hostElement, fabricSheetTypeId)` | FabricSheet |
| `CurveLoop GetBendProfile()` | `fabricSheet.GetBendProfile()` | CurveLoop |
| `CurveLoop GetBendProfileWithFillets()` | `fabricSheet.GetBendProfileWithFillets()` | CurveLoop |
| `FabricRoundingManager GetReinforcementRoundingManager()` | `fabricSheet.GetReinforcementRoundingManager()` | FabricRoundingManager |
| `IDictionary<ElementId, Double> GetSegmentParameterIdsAndLengths(Boolean)` | `fabricSheet.GetSegmentParameterIdsAndLengths(rounded)` | IDictionary<ElementId, Double> |
| `Transform GetSheetLocation()` | `fabricSheet.GetSheetLocation()` | Transform |
| `IList<Curve> GetWireCenterlines()` | `fabricSheet.GetWireCenterlines()` | IList<Curve> |
| `IList<Curve> GetWireCenterlines(WireDistributionDirection)` | `fabricSheet.GetWireCenterlines(wireDirection)` | IList<Curve> |
| `Boolean IsCoverOffsetValid(Double)` | `fabricSheet.IsCoverOffsetValid(coverOffset)` | Boolean |
| `Boolean IsSingleFabricSheetWithinHost(Element, Transform)` | `fabricSheet.IsSingleFabricSheetWithinHost(hostElement, transform)` | Boolean |
| `Boolean IsUnobscuredInView(View)` | `fabricSheet.IsUnobscuredInView(view)` | Boolean |
| `Boolean IsValidHost(Element)` | `FabricSheet.IsValidHost(host)` | Boolean |
| `Boolean IsValidHost(Document, ElementId)` | `FabricSheet.IsValidHost(document, concreteHostElementId)` | Boolean |
| `Void PlaceInHost(Element, Transform)` | `fabricSheet.PlaceInHost(hostElement, transform)` | Void |
| `Void SetBendProfile(CurveLoop)` | `fabricSheet.SetBendProfile(bendProfile)` | Void |
| `Void SetSegmentLength(ElementId, Double)` | `fabricSheet.SetSegmentLength(segmentParameterId, value)` | Void |
| `Void SetUnobscuredInView(View, Boolean)` | `fabricSheet.SetUnobscuredInView(view, unobscured)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
