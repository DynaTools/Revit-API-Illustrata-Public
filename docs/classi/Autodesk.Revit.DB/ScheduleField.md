---
title: ScheduleField
classe: Autodesk.Revit.DB.ScheduleField
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 42
---

# ScheduleField

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String ColumnHeading { get; set; }` | `scheduleField.ColumnHeading` | String |
| `ScheduleDefinition Definition { get; }` | `scheduleField.Definition` | ScheduleDefinition |
| `ScheduleFieldDisplayType DisplayType { get; set; }` | `scheduleField.DisplayType` | ScheduleFieldDisplayType |
| `ScheduleFieldId FieldId { get; }` | `scheduleField.FieldId` | ScheduleFieldId |
| `Int32 FieldIndex { get; }` | `scheduleField.FieldIndex` | Int32 |
| `ScheduleFieldType FieldType { get; }` | `scheduleField.FieldType` | ScheduleFieldType |
| `Double GridColumnWidth { get; set; }` | `scheduleField.GridColumnWidth` | Double |
| `Boolean HasSchedulableField { get; }` | `scheduleField.HasSchedulableField` | Boolean |
| `ScheduleHeadingOrientation HeadingOrientation { get; set; }` | `scheduleField.HeadingOrientation` | ScheduleHeadingOrientation |
| `ScheduleHorizontalAlignment HorizontalAlignment { get; set; }` | `scheduleField.HorizontalAlignment` | ScheduleHorizontalAlignment |
| `Boolean IsCalculatedField { get; }` | `scheduleField.IsCalculatedField` | Boolean |
| `Boolean IsCombinedParameterField { get; }` | `scheduleField.IsCombinedParameterField` | Boolean |
| `Boolean IsHidden { get; set; }` | `scheduleField.IsHidden` | Boolean |
| `Boolean IsOverridden { get; }` | `scheduleField.IsOverridden` | Boolean |
| `Boolean IsValidObject { get; }` | `scheduleField.IsValidObject` | Boolean |
| `String MultipleValuesCustomText { get; set; }` | `scheduleField.MultipleValuesCustomText` | String |
| `ScheduleFieldMultipleValuesDisplayType MultipleValuesDisplayType { get; set; }` | `scheduleField.MultipleValuesDisplayType` | ScheduleFieldMultipleValuesDisplayType |
| `String MultipleValuesText { get; }` | `scheduleField.MultipleValuesText` | String |
| `ElementId ParameterId { get; }` | `scheduleField.ParameterId` | ElementId |
| `ScheduleFieldId PercentageBy { get; set; }` | `scheduleField.PercentageBy` | ScheduleFieldId |
| `ScheduleFieldId PercentageOf { get; set; }` | `scheduleField.PercentageOf` | ScheduleFieldId |
| `ViewSchedule Schedule { get; }` | `scheduleField.Schedule` | ViewSchedule |
| `Double SheetColumnWidth { get; set; }` | `scheduleField.SheetColumnWidth` | Double |
| `Boolean TotalByAssemblyType { get; set; }` | `scheduleField.TotalByAssemblyType` | Boolean |
| `ScheduleVerticalAlignment VerticalAlignment { get; set; }` | `scheduleField.VerticalAlignment` | ScheduleVerticalAlignment |
| `Boolean CanDisplayMinMax()` | `scheduleField.CanDisplayMinMax()` | Boolean |
| `Boolean CanTotal()` | `scheduleField.CanTotal()` | Boolean |
| `Boolean CanTotalByAssemblyType()` | `scheduleField.CanTotalByAssemblyType()` | Boolean |
| `Boolean CreatesCircularReferences(ScheduleFieldId)` | `scheduleField.CreatesCircularReferences(fieldId)` | Boolean |
| `Void Dispose()` | `scheduleField.Dispose()` | Void |
| `IList<TableCellCombinedParameterData> GetCombinedParameters()` | `scheduleField.GetCombinedParameters()` | IList<TableCellCombinedParameterData> |
| `CustomFieldData GetCustomFieldData()` | `scheduleField.GetCustomFieldData()` | CustomFieldData |
| `FormatOptions GetFormatOptions()` | `scheduleField.GetFormatOptions()` | FormatOptions |
| `String GetName()` | `scheduleField.GetName()` | String |
| `SchedulableField GetSchedulableField()` | `scheduleField.GetSchedulableField()` | SchedulableField |
| `ForgeTypeId GetSpecTypeId()` | `scheduleField.GetSpecTypeId()` | ForgeTypeId |
| `TableCellStyle GetStyle()` | `scheduleField.GetStyle()` | TableCellStyle |
| `Boolean IsValidCombinedParameters(IList<TableCellCombinedParameterData>)` | `scheduleField.IsValidCombinedParameters(data)` | Boolean |
| `Void ResetOverride()` | `scheduleField.ResetOverride()` | Void |
| `Void SetCombinedParameters(IList<TableCellCombinedParameterData>)` | `scheduleField.SetCombinedParameters(data)` | Void |
| `Void SetFormatOptions(FormatOptions)` | `scheduleField.SetFormatOptions(formatOptions)` | Void |
| `Void SetStyle(TableCellStyle)` | `scheduleField.SetStyle(style)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
