---
title: ViewSchedule
classe: Autodesk.Revit.DB.ViewSchedule
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.TableView
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 64
---

# ViewSchedule

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId BodyTextTypeId { get; set; }` | `viewSchedule.BodyTextTypeId` | ElementId |
| `ScheduleDefinition Definition { get; }` | `viewSchedule.Definition` | ScheduleDefinition |
| `ScheduleDefinition EmbeddedDefinition { get; }` | `viewSchedule.EmbeddedDefinition` | ScheduleDefinition |
| `Boolean HasStripedRows { get; set; }` | `viewSchedule.HasStripedRows` | Boolean |
| `ElementId HeaderTextTypeId { get; set; }` | `viewSchedule.HeaderTextTypeId` | ElementId |
| `Boolean IsHeaderFrozen { get; set; }` | `ViewSchedule.IsHeaderFrozen` | Boolean |
| `Boolean IsInternalKeynoteSchedule { get; }` | `viewSchedule.IsInternalKeynoteSchedule` | Boolean |
| `Boolean IsTitleblockRevisionSchedule { get; }` | `viewSchedule.IsTitleblockRevisionSchedule` | Boolean |
| `String KeyScheduleParameterName { get; set; }` | `viewSchedule.KeyScheduleParameterName` | String |
| `Double RowHeight { get; set; }` | `viewSchedule.RowHeight` | Double |
| `RowHeightOverrideOptions RowHeightOverride { get; set; }` | `viewSchedule.RowHeightOverride` | RowHeightOverrideOptions |
| `ElementId TitleTextTypeId { get; set; }` | `viewSchedule.TitleTextTypeId` | ElementId |
| `Boolean UseStripedRowsOnSheets { get; set; }` | `viewSchedule.UseStripedRowsOnSheets` | Boolean |
| `Boolean CanGroupHeaders(Int32, Int32, Int32, Int32)` | `viewSchedule.CanGroupHeaders(top, left, bottom, right)` | Boolean |
| `Boolean CanUngroupHeaders(Int32, Int32, Int32, Int32)` | `viewSchedule.CanUngroupHeaders(top, left, bottom, right)` | Boolean |
| `ViewSchedule CreateKeynoteLegend(Document)` | `ViewSchedule.CreateKeynoteLegend(document)` | ViewSchedule |
| `ViewSchedule CreateKeySchedule(Document, ElementId)` | `ViewSchedule.CreateKeySchedule(document, categoryId)` | ViewSchedule |
| `ViewSchedule CreateMaterialTakeoff(Document, ElementId)` | `ViewSchedule.CreateMaterialTakeoff(document, categoryId)` | ViewSchedule |
| `ViewSchedule CreateNoteBlock(Document, ElementId)` | `ViewSchedule.CreateNoteBlock(document, familyId)` | ViewSchedule |
| `ViewSchedule CreateRevisionSchedule(Document)` | `ViewSchedule.CreateRevisionSchedule(document)` | ViewSchedule |
| `ViewSchedule CreateSchedule(Document, ElementId, ElementId)` | `ViewSchedule.CreateSchedule(document, categoryId, areaSchemeId)` | ViewSchedule |
| `ViewSchedule CreateSchedule(Document, ElementId)` | `ViewSchedule.CreateSchedule(document, categoryId)` | ViewSchedule |
| `ViewSchedule CreateSheetList(Document)` | `ViewSchedule.CreateSheetList(document)` | ViewSchedule |
| `ViewSchedule CreateViewList(Document)` | `ViewSchedule.CreateViewList(document)` | ViewSchedule |
| `Void DeleteSegment(Int32)` | `viewSchedule.DeleteSegment(segmentIndex)` | Void |
| `Void Export(String, String, ViewScheduleExportOptions)` | `viewSchedule.Export(folder, name, options)` | Void |
| `String GetDefaultNameForKeynoteLegend(Document)` | `ViewSchedule.GetDefaultNameForKeynoteLegend(document)` | String |
| `String GetDefaultNameForKeySchedule(Document, ElementId)` | `ViewSchedule.GetDefaultNameForKeySchedule(document, categoryId)` | String |
| `String GetDefaultNameForMaterialTakeoff(Document, ElementId)` | `ViewSchedule.GetDefaultNameForMaterialTakeoff(document, categoryId)` | String |
| `String GetDefaultNameForNoteBlock(Document)` | `ViewSchedule.GetDefaultNameForNoteBlock(document)` | String |
| `String GetDefaultNameForRevisionSchedule(Document)` | `ViewSchedule.GetDefaultNameForRevisionSchedule(document)` | String |
| `String GetDefaultNameForSchedule(Document, ElementId, ElementId)` | `ViewSchedule.GetDefaultNameForSchedule(document, categoryId, areaSchemeId)` | String |
| `String GetDefaultNameForSchedule(Document, ElementId)` | `ViewSchedule.GetDefaultNameForSchedule(document, categoryId)` | String |
| `String GetDefaultNameForSheetList(Document)` | `ViewSchedule.GetDefaultNameForSheetList(document)` | String |
| `String GetDefaultNameForViewList(Document)` | `ViewSchedule.GetDefaultNameForViewList(document)` | String |
| `String GetDefaultParameterNameForKeySchedule(Document, ElementId)` | `ViewSchedule.GetDefaultParameterNameForKeySchedule(document, categoryId)` | String |
| `ScheduleHeightsOnSheet GetScheduleHeightsOnSheet()` | `viewSchedule.GetScheduleHeightsOnSheet()` | ScheduleHeightsOnSheet |
| `IList<ElementId> GetScheduleInstances(Int32)` | `viewSchedule.GetScheduleInstances(segmentIndex)` | IList<ElementId> |
| `Int32 GetSegmentCount()` | `viewSchedule.GetSegmentCount()` | Int32 |
| `Double GetSegmentHeight(Int32)` | `viewSchedule.GetSegmentHeight(segmentIndex)` | Double |
| `Color GetStripedRowsColor(StripedRowPattern)` | `viewSchedule.GetStripedRowsColor(index)` | Color |
| `TableData GetTableData()` | `viewSchedule.GetTableData()` | TableData |
| `ICollection<ElementId> GetValidCategoriesForKeySchedule()` | `ViewSchedule.GetValidCategoriesForKeySchedule()` | ICollection<ElementId> |
| `ICollection<ElementId> GetValidCategoriesForMaterialTakeoff()` | `ViewSchedule.GetValidCategoriesForMaterialTakeoff()` | ICollection<ElementId> |
| `ICollection<ElementId> GetValidCategoriesForSchedule()` | `ViewSchedule.GetValidCategoriesForSchedule()` | ICollection<ElementId> |
| `ICollection<ElementId> GetValidFamiliesForNoteBlock(Document)` | `ViewSchedule.GetValidFamiliesForNoteBlock(document)` | ICollection<ElementId> |
| `Void GroupHeaders(Int32, Int32, Int32, Int32, String)` | `viewSchedule.GroupHeaders(top, left, bottom, right, caption)` | Void |
| `Boolean HasImageField()` | `viewSchedule.HasImageField()` | Boolean |
| `Boolean IsDataOutOfDate()` | `viewSchedule.IsDataOutOfDate()` | Boolean |
| `Boolean IsSplit()` | `viewSchedule.IsSplit()` | Boolean |
| `Boolean IsValidCategoryForKeySchedule(ElementId)` | `ViewSchedule.IsValidCategoryForKeySchedule(categoryId)` | Boolean |
| `Boolean IsValidCategoryForMaterialTakeoff(ElementId)` | `ViewSchedule.IsValidCategoryForMaterialTakeoff(categoryId)` | Boolean |
| `Boolean IsValidCategoryForSchedule(ElementId)` | `ViewSchedule.IsValidCategoryForSchedule(categoryId)` | Boolean |
| `Boolean IsValidFamilyForNoteBlock(Document, ElementId)` | `ViewSchedule.IsValidFamilyForNoteBlock(document, familyId)` | Boolean |
| `Boolean IsValidTextTypeId(ElementId)` | `viewSchedule.IsValidTextTypeId(textTypeId)` | Boolean |
| `Void MergeSegments(Int32, Int32)` | `viewSchedule.MergeSegments(movedSegmentIndex, targetSegmentIndex)` | Void |
| `Boolean RefreshData()` | `viewSchedule.RefreshData()` | Boolean |
| `Void RestoreImageSize()` | `viewSchedule.RestoreImageSize()` | Void |
| `Void SetSegmentHeight(Int32, Double)` | `viewSchedule.SetSegmentHeight(segmentIndex, height)` | Void |
| `Void SetStripedRowsColor(StripedRowPattern, Color)` | `viewSchedule.SetStripedRowsColor(index, color)` | Void |
| `Void Split(IList<Double>)` | `viewSchedule.Split(segmentHeights)` | Void |
| `Void Split(Int32)` | `viewSchedule.Split(segmentNumber)` | Void |
| `Void SplitSegment(Int32, IList<Double>)` | `viewSchedule.SplitSegment(segmentIndex, segmentHeights)` | Void |
| `Void UngroupHeaders(Int32, Int32, Int32, Int32)` | `viewSchedule.UngroupHeaders(top, left, bottom, right)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
