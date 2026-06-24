---
title: TableData
classe: Autodesk.Revit.DB.TableData
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# TableData

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean FreezeColumnsAndRows { get; set; }` | `tableData.FreezeColumnsAndRows` | Boolean |
| `Boolean IsValidObject { get; }` | `tableData.IsValidObject` | Boolean |
| `Int32 NumberOfSections { get; }` | `tableData.NumberOfSections` | Int32 |
| `Double Width { get; set; }` | `tableData.Width` | Double |
| `Int32 WidthInPixels { get; }` | `tableData.WidthInPixels` | Int32 |
| `Int32 ZoomLevel { get; set; }` | `tableData.ZoomLevel` | Int32 |
| `Void Dispose()` | `tableData.Dispose()` | Void |
| `TableSectionData GetSectionData(Int32)` | `tableData.GetSectionData(nIndex)` | TableSectionData |
| `TableSectionData GetSectionData(SectionType)` | `tableData.GetSectionData(sectionType)` | TableSectionData |
| `Boolean IsEqual(TableData)` | `tableData.IsEqual(OtherElem)` | Boolean |
| `Boolean IsValidZoomLevel(Int32)` | `tableData.IsValidZoomLevel(zoomLevel)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
