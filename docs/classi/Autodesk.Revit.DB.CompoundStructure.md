---
title: CompoundStructure
classe: Autodesk.Revit.DB.CompoundStructure
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 80
---

# CompoundStructure

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double CutoffHeight { get; set; }` | `compoundStructure.CutoffHeight` | Double |
| `EndCapCondition EndCap { get; set; }` | `compoundStructure.EndCap` | EndCapCondition |
| `Boolean HasStructuralDeck { get; }` | `compoundStructure.HasStructuralDeck` | Boolean |
| `Boolean IsEmpty { get; }` | `compoundStructure.IsEmpty` | Boolean |
| `Boolean IsValidObject { get; }` | `compoundStructure.IsValidObject` | Boolean |
| `Boolean IsVerticallyCompound { get; }` | `compoundStructure.IsVerticallyCompound` | Boolean |
| `Int32 LayerCount { get; }` | `compoundStructure.LayerCount` | Int32 |
| `Double MinimumSampleHeight { get; }` | `compoundStructure.MinimumSampleHeight` | Double |
| `OpeningWrappingCondition OpeningWrapping { get; set; }` | `compoundStructure.OpeningWrapping` | OpeningWrappingCondition |
| `Double SampleHeight { get; set; }` | `compoundStructure.SampleHeight` | Double |
| `Int32 StructuralMaterialIndex { get; set; }` | `compoundStructure.StructuralMaterialIndex` | Int32 |
| `Int32 VariableLayerIndex { get; set; }` | `compoundStructure.VariableLayerIndex` | Int32 |
| `Void AddWallSweep(WallSweepInfo)` | `compoundStructure.AddWallSweep(wallSweepInfo)` | Void |
| `Void AssociateRegionWithLayer(Int32, Int32)` | `compoundStructure.AssociateRegionWithLayer(regionId, layerIdx)` | Void |
| `Boolean CanLayerBeStructuralMaterial(Int32)` | `compoundStructure.CanLayerBeStructuralMaterial(layerIndex)` | Boolean |
| `Boolean CanLayerBeVariable(Int32)` | `compoundStructure.CanLayerBeVariable(variableLayerIndex)` | Boolean |
| `Boolean CanLayerWidthBeNonZero(Int32)` | `compoundStructure.CanLayerWidthBeNonZero(layerIdx)` | Boolean |
| `Boolean CanSplitAndMergeRegionsBeUsed()` | `compoundStructure.CanSplitAndMergeRegionsBeUsed()` | Boolean |
| `Boolean ChangeRegionWidth(Int32, Double)` | `compoundStructure.ChangeRegionWidth(regionId, newWidth)` | Boolean |
| `Void ClearWallSweeps(WallSweepType)` | `compoundStructure.ClearWallSweeps(wallSweepType)` | Void |
| `CompoundStructure CreateSimpleCompoundStructure(IList<CompoundStructureLayer>)` | `CompoundStructure.CreateSimpleCompoundStructure(layers)` | CompoundStructure |
| `CompoundStructure CreateSingleLayerCompoundStructure(Double, MaterialFunctionAssignment, Double, ElementId)` | `CompoundStructure.CreateSingleLayerCompoundStructure(sampleHeight, layerFunction, width, materialId)` | CompoundStructure |
| `CompoundStructure CreateSingleLayerCompoundStructure(MaterialFunctionAssignment, Double, ElementId)` | `CompoundStructure.CreateSingleLayerCompoundStructure(layerFunction, width, materialId)` | CompoundStructure |
| `Boolean DeleteLayer(Int32)` | `compoundStructure.DeleteLayer(layerIdx)` | Boolean |
| `Void Dispose()` | `compoundStructure.Dispose()` | Void |
| `Int32 FindEnclosingRegionAndSegments(UV, RectangularGridSegmentOrientation, Int32&, Int32&)` | `compoundStructure.FindEnclosingRegionAndSegments(gridUV, splitDirection, segmentId1, segmentId2)` | Int32 |
| `IList<Int32> GetAdjacentRegions(Int32)` | `compoundStructure.GetAdjacentRegions(segmentId)` | IList<Int32> |
| `Int32 GetCoreBoundaryLayerIndex(ShellLayerType)` | `compoundStructure.GetCoreBoundaryLayerIndex(shellLayerType)` | Int32 |
| `StructDeckEmbeddingType GetDeckEmbeddingType(Int32)` | `compoundStructure.GetDeckEmbeddingType(layerIdx)` | StructDeckEmbeddingType |
| `ElementId GetDeckProfileId(Int32)` | `compoundStructure.GetDeckProfileId(layerIdx)` | ElementId |
| `IList<Int32> GetExtendableRegionIds(Boolean)` | `compoundStructure.GetExtendableRegionIds(top)` | IList<Int32> |
| `Int32 GetFirstCoreLayerIndex()` | `compoundStructure.GetFirstCoreLayerIndex()` | Int32 |
| `Int32 GetLastCoreLayerIndex()` | `compoundStructure.GetLastCoreLayerIndex()` | Int32 |
| `Int32 GetLayerAssociatedToRegion(Int32)` | `compoundStructure.GetLayerAssociatedToRegion(regionId)` | Int32 |
| `MaterialFunctionAssignment GetLayerFunction(Int32)` | `compoundStructure.GetLayerFunction(layerIdx)` | MaterialFunctionAssignment |
| `IList<CompoundStructureLayer> GetLayers()` | `compoundStructure.GetLayers()` | IList<CompoundStructureLayer> |
| `Double GetLayerWidth(Int32)` | `compoundStructure.GetLayerWidth(layerIdx)` | Double |
| `ElementId GetMaterialId(Int32)` | `compoundStructure.GetMaterialId(layerIdx)` | ElementId |
| `Double GetMinimumLayerThickness()` | `CompoundStructure.GetMinimumLayerThickness()` | Double |
| `Int32 GetNumberOfShellLayers(ShellLayerType)` | `compoundStructure.GetNumberOfShellLayers(shellLayerType)` | Int32 |
| `Double GetOffsetForLocationLine(WallLocationLine)` | `compoundStructure.GetOffsetForLocationLine(wallLocationLine)` | Double |
| `Int32 GetPreviousNonZeroLayerIndex(Int32)` | `compoundStructure.GetPreviousNonZeroLayerIndex(thisIdx)` | Int32 |
| `BoundingBoxUV GetRegionEnvelope(Int32)` | `compoundStructure.GetRegionEnvelope(regionId)` | BoundingBoxUV |
| `IList<Int32> GetRegionIds()` | `compoundStructure.GetRegionIds()` | IList<Int32> |
| `IList<Int32> GetRegionsAlongLevel(Double)` | `compoundStructure.GetRegionsAlongLevel(height)` | IList<Int32> |
| `IList<Int32> GetRegionsAssociatedToLayer(Int32)` | `compoundStructure.GetRegionsAssociatedToLayer(layerIdx)` | IList<Int32> |
| `Double GetSegmentCoordinate(Int32)` | `compoundStructure.GetSegmentCoordinate(segmentId)` | Double |
| `Void GetSegmentEndPoints(Int32, Int32, UV&, UV&)` | `compoundStructure.GetSegmentEndPoints(segmentId, regionId, end1, end2)` | Void |
| `IList<Int32> GetSegmentIds()` | `compoundStructure.GetSegmentIds()` | IList<Int32> |
| `RectangularGridSegmentOrientation GetSegmentOrientation(Int32)` | `compoundStructure.GetSegmentOrientation(segmentId)` | RectangularGridSegmentOrientation |
| `CompoundStructure GetSimpleCompoundStructure(Double, Double)` | `compoundStructure.GetSimpleCompoundStructure(wallHeight, distAboveBase)` | CompoundStructure |
| `IList<WallSweepInfo> GetWallSweepsInfo(WallSweepType)` | `compoundStructure.GetWallSweepsInfo(wallSweepType)` | IList<WallSweepInfo> |
| `Double GetWidth()` | `compoundStructure.GetWidth()` | Double |
| `Double GetWidth(Int32)` | `compoundStructure.GetWidth(regionId)` | Double |
| `Boolean IsCoreLayer(Int32)` | `compoundStructure.IsCoreLayer(layerIdx)` | Boolean |
| `Boolean IsEqual(CompoundStructure)` | `compoundStructure.IsEqual(otherStructure)` | Boolean |
| `Boolean IsLayerValid(Int32, CompoundStructureLayer)` | `compoundStructure.IsLayerValid(layerIdx, layer)` | Boolean |
| `Boolean IsRectangularRegion(Int32)` | `compoundStructure.IsRectangularRegion(regionId)` | Boolean |
| `Boolean IsSimpleRegion(Int32)` | `compoundStructure.IsSimpleRegion(regionId)` | Boolean |
| `Boolean IsStructuralDeck(Int32)` | `compoundStructure.IsStructuralDeck(layerIdx)` | Boolean |
| `Boolean IsValid(Document, IDictionary<Int32, CompoundStructureError>&, IDictionary<Int32, Int32>&)` | `compoundStructure.IsValid(doc, errMap, twoLayerErrorsMap)` | Boolean |
| `Boolean IsValidRegionId(Int32)` | `compoundStructure.IsValidRegionId(regionId)` | Boolean |
| `Boolean IsValidSampleHeight(Double)` | `compoundStructure.IsValidSampleHeight(height)` | Boolean |
| `Boolean IsValidSegmentId(Int32)` | `compoundStructure.IsValidSegmentId(segmentId)` | Boolean |
| `Boolean IsVerticallyHomogeneous()` | `compoundStructure.IsVerticallyHomogeneous()` | Boolean |
| `Int32 MergeRegionsAdjacentToSegment(Int32, Int32)` | `compoundStructure.MergeRegionsAdjacentToSegment(segmentId, layerIdxForMergedRegion)` | Int32 |
| `Boolean ParticipatesInWrapping(Int32)` | `compoundStructure.ParticipatesInWrapping(layerIdx)` | Boolean |
| `Void RemoveWallSweep(WallSweepType, Int32)` | `compoundStructure.RemoveWallSweep(wallSweepType, id)` | Void |
| `Void SetDeckEmbeddingType(Int32, StructDeckEmbeddingType)` | `compoundStructure.SetDeckEmbeddingType(layerIdx, embedType)` | Void |
| `Void SetDeckProfileId(Int32, ElementId)` | `compoundStructure.SetDeckProfileId(layerIdx, profileId)` | Void |
| `Void SetExtendableRegionIds(Boolean, IList<Int32>)` | `compoundStructure.SetExtendableRegionIds(top, regionIds)` | Void |
| `Void SetLayer(Int32, CompoundStructureLayer)` | `compoundStructure.SetLayer(layerIdx, layer)` | Void |
| `Void SetLayerFunction(Int32, MaterialFunctionAssignment)` | `compoundStructure.SetLayerFunction(layerIdx, function)` | Void |
| `Void SetLayers(IList<CompoundStructureLayer>)` | `compoundStructure.SetLayers(layers)` | Void |
| `Void SetLayerWidth(Int32, Double)` | `compoundStructure.SetLayerWidth(layerIdx, width)` | Void |
| `Void SetMaterialId(Int32, ElementId)` | `compoundStructure.SetMaterialId(layerIdx, materialId)` | Void |
| `Void SetNumberOfShellLayers(ShellLayerType, Int32)` | `compoundStructure.SetNumberOfShellLayers(shellLayerType, numLayers)` | Void |
| `Void SetParticipatesInWrapping(Int32, Boolean)` | `compoundStructure.SetParticipatesInWrapping(layerIdx, participatesInWrapping)` | Void |
| `Int32 SplitRegion(UV, RectangularGridSegmentOrientation)` | `compoundStructure.SplitRegion(gridUV, splitDirection)` | Int32 |
| `Int32 SplitRegion(UV, RectangularGridSegmentOrientation, Int32&)` | `compoundStructure.SplitRegion(gridUV, splitDirection, newSegmentId)` | Int32 |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
