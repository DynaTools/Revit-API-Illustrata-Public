---
title: TableSectionData
classe: Autodesk.Revit.DB.TableSectionData
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 73
---

# TableSectionData

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 FirstColumnNumber { get; }` | `tableSectionData.FirstColumnNumber` | Int32 |
| `Int32 FirstRowNumber { get; }` | `tableSectionData.FirstRowNumber` | Int32 |
| `Boolean HideSection { get; set; }` | `tableSectionData.HideSection` | Boolean |
| `Boolean IsValidObject { get; }` | `tableSectionData.IsValidObject` | Boolean |
| `Int32 LastColumnNumber { get; }` | `tableSectionData.LastColumnNumber` | Int32 |
| `Int32 LastRowNumber { get; }` | `tableSectionData.LastRowNumber` | Int32 |
| `Boolean NeedsRefresh { get; set; }` | `tableSectionData.NeedsRefresh` | Boolean |
| `Int32 NumberOfColumns { get; set; }` | `tableSectionData.NumberOfColumns` | Int32 |
| `Int32 NumberOfRows { get; set; }` | `tableSectionData.NumberOfRows` | Int32 |
| `Boolean AllowOverrideCellStyle(Int32, Int32)` | `tableSectionData.AllowOverrideCellStyle(nRow, nCol)` | Boolean |
| `Boolean CanInsertColumn(Int32)` | `tableSectionData.CanInsertColumn(nIndex)` | Boolean |
| `Boolean CanInsertRow(Int32)` | `tableSectionData.CanInsertRow(nIndex)` | Boolean |
| `Boolean CanRemoveColumn(Int32)` | `tableSectionData.CanRemoveColumn(nIndex)` | Boolean |
| `Boolean CanRemoveRow(Int32)` | `tableSectionData.CanRemoveRow(nIndex)` | Boolean |
| `Void ClearCell(Int32, Int32)` | `tableSectionData.ClearCell(nRow, nCol)` | Void |
| `Void Dispose()` | `tableSectionData.Dispose()` | Void |
| `TableCellCalculatedValueData GetCellCalculatedValue(Int32)` | `tableSectionData.GetCellCalculatedValue(nCol)` | TableCellCalculatedValueData |
| `TableCellCalculatedValueData GetCellCalculatedValue(Int32, Int32)` | `tableSectionData.GetCellCalculatedValue(nRow, nCol)` | TableCellCalculatedValueData |
| `ElementId GetCellCategoryId(Int32)` | `tableSectionData.GetCellCategoryId(nCol)` | ElementId |
| `ElementId GetCellCategoryId(Int32, Int32)` | `tableSectionData.GetCellCategoryId(nRow, nCol)` | ElementId |
| `IList<TableCellCombinedParameterData> GetCellCombinedParameters(Int32)` | `tableSectionData.GetCellCombinedParameters(nCol)` | IList<TableCellCombinedParameterData> |
| `IList<TableCellCombinedParameterData> GetCellCombinedParameters(Int32, Int32)` | `tableSectionData.GetCellCombinedParameters(nRow, nCol)` | IList<TableCellCombinedParameterData> |
| `FormatOptions GetCellFormatOptions(Int32, Document)` | `tableSectionData.GetCellFormatOptions(nCol, dcument)` | FormatOptions |
| `FormatOptions GetCellFormatOptions(Int32, Int32, Document)` | `tableSectionData.GetCellFormatOptions(nRow, nCol, document)` | FormatOptions |
| `ElementId GetCellParamId(Int32)` | `tableSectionData.GetCellParamId(nCol)` | ElementId |
| `ElementId GetCellParamId(Int32, Int32)` | `tableSectionData.GetCellParamId(nRow, nCol)` | ElementId |
| `ForgeTypeId GetCellSpec(Int32, Int32)` | `tableSectionData.GetCellSpec(nRow, nCol)` | ForgeTypeId |
| `String GetCellText(Int32, Int32)` | `tableSectionData.GetCellText(nRow, nCol)` | String |
| `CellType GetCellType(Int32)` | `tableSectionData.GetCellType(nCol)` | CellType |
| `CellType GetCellType(Int32, Int32)` | `tableSectionData.GetCellType(nRow, nCol)` | CellType |
| `Double GetColumnWidth(Int32)` | `tableSectionData.GetColumnWidth(nCol)` | Double |
| `Int32 GetColumnWidthInPixels(Int32)` | `tableSectionData.GetColumnWidthInPixels(nCol)` | Int32 |
| `Guid GetCustomFieldId(Int32, Int32)` | `tableSectionData.GetCustomFieldId(row, col)` | Guid |
| `TableMergedCell GetMergedCell(Int32, Int32)` | `tableSectionData.GetMergedCell(nRow, nCol)` | TableMergedCell |
| `Double GetRowHeight(Int32)` | `tableSectionData.GetRowHeight(nRow)` | Double |
| `Int32 GetRowHeightInPixels(Int32)` | `tableSectionData.GetRowHeightInPixels(nRow)` | Int32 |
| `TableCellStyle GetTableCellStyle(Int32, Int32)` | `tableSectionData.GetTableCellStyle(nRow, nCol)` | TableCellStyle |
| `Void InsertColumn(Int32)` | `tableSectionData.InsertColumn(index)` | Void |
| `Void InsertImage(Int32, Int32, ElementId)` | `tableSectionData.InsertImage(nRow, nColumn, imageSymbolId)` | Void |
| `Void InsertRow(Int32)` | `tableSectionData.InsertRow(nIndex)` | Void |
| `Boolean IsAcceptableParamIdAndCategoryId(Int32, ElementId, ElementId)` | `tableSectionData.IsAcceptableParamIdAndCategoryId(nRow, paramId, categoryId)` | Boolean |
| `Boolean IsAcceptableParamIdAndCategoryId(ElementId, ElementId)` | `tableSectionData.IsAcceptableParamIdAndCategoryId(paramId, categoryId)` | Boolean |
| `Boolean IsCellFormattable(Int32, Int32)` | `tableSectionData.IsCellFormattable(nRow, nCol)` | Boolean |
| `Boolean IsCellOverridden(Int32)` | `tableSectionData.IsCellOverridden(nCol)` | Boolean |
| `Boolean IsCellOverridden(Int32, Int32)` | `tableSectionData.IsCellOverridden(nRow, nCol)` | Boolean |
| `Boolean IsDataOutOfDate()` | `tableSectionData.IsDataOutOfDate()` | Boolean |
| `Boolean IsValidColumnNumber(Int32)` | `tableSectionData.IsValidColumnNumber(nCol)` | Boolean |
| `Boolean IsValidImageSymbolId(ElementId)` | `tableSectionData.IsValidImageSymbolId(imageSymbolId)` | Boolean |
| `Boolean IsValidRowNumber(Int32)` | `tableSectionData.IsValidRowNumber(nRow)` | Boolean |
| `Void MergeCells(TableMergedCell)` | `tableSectionData.MergeCells(mergedCell)` | Void |
| `Boolean RefreshData()` | `tableSectionData.RefreshData()` | Boolean |
| `Void RemoveColumn(Int32)` | `tableSectionData.RemoveColumn(nIndex)` | Void |
| `Void RemoveRow(Int32)` | `tableSectionData.RemoveRow(nIndex)` | Void |
| `Void ResetCellOverride(Int32)` | `tableSectionData.ResetCellOverride(nCol)` | Void |
| `Void ResetCellOverride(Int32, Int32)` | `tableSectionData.ResetCellOverride(nRow, nCol)` | Void |
| `Void SetCellCalculatedValue(Int32, TableCellCalculatedValueData)` | `tableSectionData.SetCellCalculatedValue(nCol, pCalcValue)` | Void |
| `Void SetCellCalculatedValue(Int32, Int32, TableCellCalculatedValueData)` | `tableSectionData.SetCellCalculatedValue(nRow, nCol, pCalcValue)` | Void |
| `Void SetCellCombinedParameters(Int32, IList<TableCellCombinedParameterData>)` | `tableSectionData.SetCellCombinedParameters(nCol, paramData)` | Void |
| `Void SetCellCombinedParameters(Int32, Int32, IList<TableCellCombinedParameterData>)` | `tableSectionData.SetCellCombinedParameters(nRow, nCol, paramData)` | Void |
| `Void SetCellFormatOptions(Int32, Int32, FormatOptions)` | `tableSectionData.SetCellFormatOptions(nRow, nCol, options)` | Void |
| `Void SetCellParamIdAndCategoryId(Int32, ElementId, ElementId)` | `tableSectionData.SetCellParamIdAndCategoryId(nCol, paramId, categoryId)` | Void |
| `Void SetCellParamIdAndCategoryId(Int32, Int32, ElementId, ElementId)` | `tableSectionData.SetCellParamIdAndCategoryId(nRow, nCol, paramId, categoryId)` | Void |
| `Void SetCellStyle(TableCellStyle)` | `tableSectionData.SetCellStyle(Style)` | Void |
| `Void SetCellStyle(Int32, TableCellStyle)` | `tableSectionData.SetCellStyle(nCol, Style)` | Void |
| `Void SetCellStyle(Int32, Int32, TableCellStyle)` | `tableSectionData.SetCellStyle(nRow, nCol, Style)` | Void |
| `Void SetCellText(Int32, Int32, String)` | `tableSectionData.SetCellText(nRow, nCol, text)` | Void |
| `Void SetCellType(Int32, CellType)` | `tableSectionData.SetCellType(nCol, type)` | Void |
| `Void SetCellType(Int32, Int32, CellType)` | `tableSectionData.SetCellType(nRow, nCol, type)` | Void |
| `Void SetColumnWidth(Int32, Double)` | `tableSectionData.SetColumnWidth(nCol, width)` | Void |
| `Void SetColumnWidthInPixels(Int32, Int32)` | `tableSectionData.SetColumnWidthInPixels(nCol, width)` | Void |
| `Void SetMergedCell(Int32, Int32, TableMergedCell)` | `tableSectionData.SetMergedCell(nRow, nCol, mergedCell)` | Void |
| `Void SetRowHeight(Int32, Double)` | `tableSectionData.SetRowHeight(nRow, height)` | Void |
| `Void SetRowHeightInPixels(Int32, Int32)` | `tableSectionData.SetRowHeightInPixels(nRow, height)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
