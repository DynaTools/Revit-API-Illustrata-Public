---
title: FamilySizeTable
classe: Autodesk.Revit.DB.FamilySizeTable
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# FamilySizeTable

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `familySizeTable.IsValidObject` | Boolean |
| `Int32 NumberOfColumns { get; }` | `familySizeTable.NumberOfColumns` | Int32 |
| `Int32 NumberOfRows { get; }` | `familySizeTable.NumberOfRows` | Int32 |
| `String AsValueString(Int32, Int32)` | `familySizeTable.AsValueString(row, column)` | String |
| `Void Dispose()` | `familySizeTable.Dispose()` | Void |
| `FamilySizeTableColumn GetColumnHeader(Int32)` | `familySizeTable.GetColumnHeader(index)` | FamilySizeTableColumn |
| `Boolean IsValidColumnIndex(Int32)` | `familySizeTable.IsValidColumnIndex(index)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
