---
title: UpdaterRegistry
classe: Autodesk.Revit.DB.UpdaterRegistry
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 23
---

# UpdaterRegistry

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `updaterRegistry.IsValidObject` | Boolean |
| `Void AddTrigger(UpdaterId, ElementFilter, ChangeType)` | `UpdaterRegistry.AddTrigger(id, filter, change)` | Void |
| `Void AddTrigger(UpdaterId, Document, ElementFilter, ChangeType)` | `UpdaterRegistry.AddTrigger(id, document, filter, change)` | Void |
| `Void AddTrigger(UpdaterId, Document, ICollection<ElementId>, ChangeType)` | `UpdaterRegistry.AddTrigger(id, document, elements, change)` | Void |
| `Void DisableUpdater(UpdaterId)` | `UpdaterRegistry.DisableUpdater(id)` | Void |
| `Void Dispose()` | `updaterRegistry.Dispose()` | Void |
| `Void EnableUpdater(UpdaterId)` | `UpdaterRegistry.EnableUpdater(id)` | Void |
| `Boolean GetIsUpdaterOptional(UpdaterId)` | `UpdaterRegistry.GetIsUpdaterOptional(id)` | Boolean |
| `IList<UpdaterInfo> GetRegisteredUpdaterInfos()` | `UpdaterRegistry.GetRegisteredUpdaterInfos()` | IList<UpdaterInfo> |
| `IList<UpdaterInfo> GetRegisteredUpdaterInfos(Document)` | `UpdaterRegistry.GetRegisteredUpdaterInfos(document)` | IList<UpdaterInfo> |
| `Boolean IsUpdaterEnabled(UpdaterId)` | `UpdaterRegistry.IsUpdaterEnabled(id)` | Boolean |
| `Boolean IsUpdaterRegistered(UpdaterId, Document)` | `UpdaterRegistry.IsUpdaterRegistered(id, document)` | Boolean |
| `Boolean IsUpdaterRegistered(UpdaterId)` | `UpdaterRegistry.IsUpdaterRegistered(id)` | Boolean |
| `Void RegisterUpdater(IUpdater, Document, Boolean)` | `UpdaterRegistry.RegisterUpdater(updater, document, isOptional)` | Void |
| `Void RegisterUpdater(IUpdater, Boolean)` | `UpdaterRegistry.RegisterUpdater(updater, isOptional)` | Void |
| `Void RegisterUpdater(IUpdater, Document)` | `UpdaterRegistry.RegisterUpdater(updater, document)` | Void |
| `Void RegisterUpdater(IUpdater)` | `UpdaterRegistry.RegisterUpdater(updater)` | Void |
| `Void RemoveAllTriggers(UpdaterId)` | `UpdaterRegistry.RemoveAllTriggers(id)` | Void |
| `Void RemoveDocumentTriggers(UpdaterId, Document)` | `UpdaterRegistry.RemoveDocumentTriggers(id, document)` | Void |
| `Void SetExecutionOrder(UpdaterId, UpdaterId)` | `UpdaterRegistry.SetExecutionOrder(first, second)` | Void |
| `Void SetIsUpdaterOptional(UpdaterId, Boolean)` | `UpdaterRegistry.SetIsUpdaterOptional(id, isOptional)` | Void |
| `Void UnregisterUpdater(UpdaterId, Document)` | `UpdaterRegistry.UnregisterUpdater(id, document)` | Void |
| `Void UnregisterUpdater(UpdaterId)` | `UpdaterRegistry.UnregisterUpdater(id)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
