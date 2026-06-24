---
title: FamilySizeTableManager
classe: Autodesk.Revit.DB.FamilySizeTableManager
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# FamilySizeTableManager

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `familySizeTableManager.IsValidObject` | Boolean |
| `Int32 NumberOfSizeTables { get; }` | `familySizeTableManager.NumberOfSizeTables` | Int32 |
| `Boolean CreateFamilySizeTableManager(Document, ElementId)` | `FamilySizeTableManager.CreateFamilySizeTableManager(document, familyId)` | Boolean |
| `Void Dispose()` | `familySizeTableManager.Dispose()` | Void |
| `Boolean ExportSizeTable(String, String)` | `familySizeTableManager.ExportSizeTable(tableName, filePath)` | Boolean |
| `IList<String> GetAllSizeTableNames()` | `familySizeTableManager.GetAllSizeTableNames()` | IList<String> |
| `FamilySizeTableManager GetFamilySizeTableManager(Document, ElementId)` | `FamilySizeTableManager.GetFamilySizeTableManager(document, familyId)` | FamilySizeTableManager |
| `FamilySizeTable GetSizeTable(String)` | `familySizeTableManager.GetSizeTable(tableName)` | FamilySizeTable |
| `Boolean HasSizeTable(String)` | `familySizeTableManager.HasSizeTable(tableName)` | Boolean |
| `Boolean ImportSizeTable(Document, String, FamilySizeTableErrorInfo)` | `familySizeTableManager.ImportSizeTable(document, filePath, errorInfo)` | Boolean |
| `Boolean RemoveSizeTable(String)` | `familySizeTableManager.RemoveSizeTable(tableName)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
