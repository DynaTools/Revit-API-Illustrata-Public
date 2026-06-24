---
title: WorksetTable
classe: Autodesk.Revit.DB.WorksetTable
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# WorksetTable

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `worksetTable.IsValidObject` | Boolean |
| `Boolean CanDeleteWorkset(Document, WorksetId, DeleteWorksetSettings)` | `WorksetTable.CanDeleteWorkset(document, worksetId, deleteWorksetSettings)` | Boolean |
| `Void DeleteWorkset(Document, WorksetId, DeleteWorksetSettings)` | `WorksetTable.DeleteWorkset(document, worksetId, deleteWorksetSettings)` | Void |
| `Void Dispose()` | `worksetTable.Dispose()` | Void |
| `WorksetId GetActiveWorksetId()` | `worksetTable.GetActiveWorksetId()` | WorksetId |
| `Workset GetWorkset(Guid)` | `worksetTable.GetWorkset(guid)` | Workset |
| `Workset GetWorkset(WorksetId)` | `worksetTable.GetWorkset(id)` | Workset |
| `Boolean IsWorksetNameUnique(Document, String)` | `WorksetTable.IsWorksetNameUnique(aDoc, name)` | Boolean |
| `Void RenameWorkset(Document, WorksetId, String)` | `WorksetTable.RenameWorkset(aDoc, worksetId, name)` | Void |
| `Void SetActiveWorksetId(WorksetId)` | `worksetTable.SetActiveWorksetId(worksetId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
