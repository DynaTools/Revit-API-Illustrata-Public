---
title: ScheduleDefinition
classe: Autodesk.Revit.DB.ScheduleDefinition
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 74
---

# ScheduleDefinition

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId AreaSchemeId { get; }` | `scheduleDefinition.AreaSchemeId` | ElementId |
| `ElementId CategoryId { get; }` | `scheduleDefinition.CategoryId` | ElementId |
| `ScheduleDefinition EmbeddedDefinition { get; }` | `scheduleDefinition.EmbeddedDefinition` | ScheduleDefinition |
| `ElementId FamilyId { get; }` | `scheduleDefinition.FamilyId` | ElementId |
| `String GrandTotalTitle { get; set; }` | `scheduleDefinition.GrandTotalTitle` | String |
| `Boolean HasEmbeddedSchedule { get; }` | `scheduleDefinition.HasEmbeddedSchedule` | Boolean |
| `Boolean IncludeLinkedFiles { get; set; }` | `scheduleDefinition.IncludeLinkedFiles` | Boolean |
| `Boolean IsEmbedded { get; }` | `scheduleDefinition.IsEmbedded` | Boolean |
| `Boolean IsFilteredBySheet { get; set; }` | `scheduleDefinition.IsFilteredBySheet` | Boolean |
| `Boolean IsItemized { get; set; }` | `scheduleDefinition.IsItemized` | Boolean |
| `Boolean IsKeySchedule { get; }` | `scheduleDefinition.IsKeySchedule` | Boolean |
| `Boolean IsMaterialTakeoff { get; }` | `scheduleDefinition.IsMaterialTakeoff` | Boolean |
| `Boolean IsValidObject { get; }` | `scheduleDefinition.IsValidObject` | Boolean |
| `Boolean ShowGrandTotal { get; set; }` | `scheduleDefinition.ShowGrandTotal` | Boolean |
| `Boolean ShowGrandTotalCount { get; set; }` | `scheduleDefinition.ShowGrandTotalCount` | Boolean |
| `Boolean ShowGrandTotalTitle { get; set; }` | `scheduleDefinition.ShowGrandTotalTitle` | Boolean |
| `Boolean ShowGridLines { get; set; }` | `scheduleDefinition.ShowGridLines` | Boolean |
| `Boolean ShowHeaders { get; set; }` | `scheduleDefinition.ShowHeaders` | Boolean |
| `Boolean ShowTitle { get; set; }` | `scheduleDefinition.ShowTitle` | Boolean |
| `Void AddEmbeddedSchedule(ElementId)` | `scheduleDefinition.AddEmbeddedSchedule(categoryId)` | Void |
| `ScheduleField AddField(ScheduleFieldType, ElementId)` | `scheduleDefinition.AddField(fieldType, parameterId)` | ScheduleField |
| `ScheduleField AddField(ScheduleFieldType)` | `scheduleDefinition.AddField(fieldType)` | ScheduleField |
| `ScheduleField AddField(SchedulableField)` | `scheduleDefinition.AddField(schedulableField)` | ScheduleField |
| `Void AddFilter(ScheduleFilter)` | `scheduleDefinition.AddFilter(filter)` | Void |
| `Void AddSortGroupField(ScheduleSortGroupField)` | `scheduleDefinition.AddSortGroupField(sortGroupField)` | Void |
| `Boolean CanFilter()` | `scheduleDefinition.CanFilter()` | Boolean |
| `Boolean CanFilterByGlobalParameters(ScheduleFieldId)` | `scheduleDefinition.CanFilterByGlobalParameters(fieldId)` | Boolean |
| `Boolean CanFilterByParameterExistence(ScheduleFieldId)` | `scheduleDefinition.CanFilterByParameterExistence(fieldId)` | Boolean |
| `Boolean CanFilterBySubstring(ScheduleFieldId)` | `scheduleDefinition.CanFilterBySubstring(fieldId)` | Boolean |
| `Boolean CanFilterByValue(ScheduleFieldId)` | `scheduleDefinition.CanFilterByValue(fieldId)` | Boolean |
| `Boolean CanFilterByValuePresence(ScheduleFieldId)` | `scheduleDefinition.CanFilterByValuePresence(fieldId)` | Boolean |
| `Boolean CanHaveEmbeddedSchedule()` | `scheduleDefinition.CanHaveEmbeddedSchedule()` | Boolean |
| `Boolean CanIncludeLinkedFiles()` | `scheduleDefinition.CanIncludeLinkedFiles()` | Boolean |
| `Boolean CanSortByField(ScheduleFieldId)` | `scheduleDefinition.CanSortByField(fieldId)` | Boolean |
| `Void ClearFields()` | `scheduleDefinition.ClearFields()` | Void |
| `Void ClearFilters()` | `scheduleDefinition.ClearFilters()` | Void |
| `Void ClearSortGroupFields()` | `scheduleDefinition.ClearSortGroupFields()` | Void |
| `Void Dispose()` | `scheduleDefinition.Dispose()` | Void |
| `ScheduleField GetField(ScheduleFieldId)` | `scheduleDefinition.GetField(fieldId)` | ScheduleField |
| `ScheduleField GetField(Int32)` | `scheduleDefinition.GetField(index)` | ScheduleField |
| `Int32 GetFieldCount()` | `scheduleDefinition.GetFieldCount()` | Int32 |
| `ScheduleFieldId GetFieldId(Int32)` | `scheduleDefinition.GetFieldId(index)` | ScheduleFieldId |
| `Int32 GetFieldIndex(ScheduleFieldId)` | `scheduleDefinition.GetFieldIndex(fieldId)` | Int32 |
| `IList<ScheduleFieldId> GetFieldOrder()` | `scheduleDefinition.GetFieldOrder()` | IList<ScheduleFieldId> |
| `ScheduleFilter GetFilter(Int32)` | `scheduleDefinition.GetFilter(index)` | ScheduleFilter |
| `Int32 GetFilterCount()` | `scheduleDefinition.GetFilterCount()` | Int32 |
| `IList<ScheduleFilter> GetFilters()` | `scheduleDefinition.GetFilters()` | IList<ScheduleFilter> |
| `IList<SchedulableField> GetSchedulableFields()` | `scheduleDefinition.GetSchedulableFields()` | IList<SchedulableField> |
| `ScheduleSortGroupField GetSortGroupField(Int32)` | `scheduleDefinition.GetSortGroupField(index)` | ScheduleSortGroupField |
| `Int32 GetSortGroupFieldCount()` | `scheduleDefinition.GetSortGroupFieldCount()` | Int32 |
| `IList<ScheduleSortGroupField> GetSortGroupFields()` | `scheduleDefinition.GetSortGroupFields()` | IList<ScheduleSortGroupField> |
| `ICollection<ElementId> GetValidCategoriesForEmbeddedSchedule()` | `scheduleDefinition.GetValidCategoriesForEmbeddedSchedule()` | ICollection<ElementId> |
| `ScheduleField InsertCombinedParameterField(IList<TableCellCombinedParameterData>, String, Int32)` | `scheduleDefinition.InsertCombinedParameterField(data, fieldName, index)` | ScheduleField |
| `ScheduleField InsertField(ScheduleFieldType, ElementId, Int32)` | `scheduleDefinition.InsertField(fieldType, parameterId, index)` | ScheduleField |
| `ScheduleField InsertField(ScheduleFieldType, Int32)` | `scheduleDefinition.InsertField(fieldType, index)` | ScheduleField |
| `ScheduleField InsertField(SchedulableField, Int32)` | `scheduleDefinition.InsertField(schedulableField, index)` | ScheduleField |
| `Void InsertFilter(ScheduleFilter, Int32)` | `scheduleDefinition.InsertFilter(filter, index)` | Void |
| `Void InsertSortGroupField(ScheduleSortGroupField, Int32)` | `scheduleDefinition.InsertSortGroupField(sortGroupField, index)` | Void |
| `Boolean IsSchedulableField(SchedulableField)` | `scheduleDefinition.IsSchedulableField(schedulableField)` | Boolean |
| `Boolean IsValidCategoryForEmbeddedSchedule(ElementId)` | `scheduleDefinition.IsValidCategoryForEmbeddedSchedule(categoryId)` | Boolean |
| `Boolean IsValidCategoryForFilterBySheet()` | `scheduleDefinition.IsValidCategoryForFilterBySheet()` | Boolean |
| `Boolean IsValidCombinedParameters(IList<TableCellCombinedParameterData>)` | `scheduleDefinition.IsValidCombinedParameters(data)` | Boolean |
| `Boolean IsValidFieldId(ScheduleFieldId)` | `scheduleDefinition.IsValidFieldId(fieldId)` | Boolean |
| `Boolean IsValidFieldIndex(Int32)` | `scheduleDefinition.IsValidFieldIndex(index)` | Boolean |
| `Void RemoveEmbeddedSchedule()` | `scheduleDefinition.RemoveEmbeddedSchedule()` | Void |
| `Void RemoveField(ScheduleFieldId)` | `scheduleDefinition.RemoveField(fieldId)` | Void |
| `Void RemoveField(Int32)` | `scheduleDefinition.RemoveField(index)` | Void |
| `Void RemoveFilter(Int32)` | `scheduleDefinition.RemoveFilter(index)` | Void |
| `Void RemoveSortGroupField(Int32)` | `scheduleDefinition.RemoveSortGroupField(index)` | Void |
| `Void SetFieldOrder(IList<ScheduleFieldId>)` | `scheduleDefinition.SetFieldOrder(fieldIds)` | Void |
| `Void SetFilter(Int32, ScheduleFilter)` | `scheduleDefinition.SetFilter(index, filter)` | Void |
| `Void SetFilters(IList<ScheduleFilter>)` | `scheduleDefinition.SetFilters(filters)` | Void |
| `Void SetSortGroupField(Int32, ScheduleSortGroupField)` | `scheduleDefinition.SetSortGroupField(index, sortGroupField)` | Void |
| `Void SetSortGroupFields(IList<ScheduleSortGroupField>)` | `scheduleDefinition.SetSortGroupFields(sortGroupFields)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
