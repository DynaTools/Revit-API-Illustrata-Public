---
title: FabricArea
classe: Autodesk.Revit.DB.Structure.FabricArea
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 26
---

# FabricArea

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double CoverOffset { get; set; }` | `fabricArea.CoverOffset` | Double |
| `XYZ Direction { get; }` | `fabricArea.Direction` | XYZ |
| `XYZ DirectionOrigin { get; }` | `fabricArea.DirectionOrigin` | XYZ |
| `FabricAreaType FabricAreaType { get; }` | `fabricArea.FabricAreaType` | FabricAreaType |
| `FabricLocation FabricLocation { get; set; }` | `fabricArea.FabricLocation` | FabricLocation |
| `ElementId FabricSheetTypeId { get; set; }` | `fabricArea.FabricSheetTypeId` | ElementId |
| `ElementId HostId { get; }` | `fabricArea.HostId` | ElementId |
| `FabricLapSplicePosition LapSplicePosition { get; set; }` | `fabricArea.LapSplicePosition` | FabricLapSplicePosition |
| `Double MajorLapSpliceLength { get; set; }` | `fabricArea.MajorLapSpliceLength` | Double |
| `FabricSheetAlignment MajorSheetAlignment { get; set; }` | `fabricArea.MajorSheetAlignment` | FabricSheetAlignment |
| `Double MinorLapSpliceLength { get; set; }` | `fabricArea.MinorLapSpliceLength` | Double |
| `FabricSheetAlignment MinorSheetAlignment { get; set; }` | `fabricArea.MinorSheetAlignment` | FabricSheetAlignment |
| `ElementId SketchId { get; }` | `fabricArea.SketchId` | ElementId |
| `ElementId TagViewId { get; set; }` | `fabricArea.TagViewId` | ElementId |
| `IList<CurveLoop> CopyCurveLoopsInSketch()` | `fabricArea.CopyCurveLoopsInSketch()` | IList<CurveLoop> |
| `FabricArea Create(Document, Element, XYZ, ElementId, ElementId)` | `FabricArea.Create(aDoc, hostElement, majorDirection, fabricAreaTypeId, fabricSheetTypeId)` | FabricArea |
| `FabricArea Create(Document, Element, IList<CurveLoop>, XYZ, XYZ, ElementId, ElementId)` | `FabricArea.Create(aDoc, hostElement, curveLoops, majorDirection, majorDirectionOrigin, fabricAreaTypeId, fabricSheetTypeId)` | FabricArea |
| `IList<ElementId> GetBoundaryCurveIds()` | `fabricArea.GetBoundaryCurveIds()` | IList<ElementId> |
| `IList<ElementId> GetFabricSheetElementIds()` | `fabricArea.GetFabricSheetElementIds()` | IList<ElementId> |
| `FabricRoundingManager GetReinforcementRoundingManager()` | `fabricArea.GetReinforcementRoundingManager()` | FabricRoundingManager |
| `Double GetTotalSheetMass()` | `fabricArea.GetTotalSheetMass()` | Double |
| `IList<ElementId> GetValidViewsForTags()` | `fabricArea.GetValidViewsForTags()` | IList<ElementId> |
| `Boolean IsCoverOffsetValid(Double)` | `fabricArea.IsCoverOffsetValid(coverOffset)` | Boolean |
| `Boolean IsValidMajorLapSplice(Double)` | `fabricArea.IsValidMajorLapSplice(majorLapSplice)` | Boolean |
| `Boolean IsValidMinorLapSplice(Double)` | `fabricArea.IsValidMinorLapSplice(minorLapSplice)` | Boolean |
| `IList<ElementId> RemoveFabricReinforcementSystem(Document, FabricArea)` | `FabricArea.RemoveFabricReinforcementSystem(doc, system)` | IList<ElementId> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
