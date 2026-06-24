---
title: MultiServerService
classe: Autodesk.Revit.DB.ExternalService.MultiServerService
namespace: Autodesk.Revit.DB.ExternalService
eredita: Autodesk.Revit.DB.ExternalService.ExternalService
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 6
---

# MultiServerService

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ExecutionPolicy ExecutionPolicy { get; }` | `multiServerService.ExecutionPolicy` | ExecutionPolicy |
| `IList<Guid> GetActiveServerIds(Document)` | `multiServerService.GetActiveServerIds(document)` | IList<Guid> |
| `IList<Guid> GetActiveServerIds()` | `multiServerService.GetActiveServerIds()` | IList<Guid> |
| `Void SetActiveServers(IList<Guid>, Document)` | `multiServerService.SetActiveServers(serverIds, document)` | Void |
| `Void SetActiveServers(IList<Guid>)` | `multiServerService.SetActiveServers(serverIds)` | Void |
| `Boolean SetServerState(Guid, Document, Boolean)` | `multiServerService.SetServerState(serverId, document, bActive)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
