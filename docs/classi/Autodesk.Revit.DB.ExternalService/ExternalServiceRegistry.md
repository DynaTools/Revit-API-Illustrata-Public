---
title: ExternalServiceRegistry
classe: Autodesk.Revit.DB.ExternalService.ExternalServiceRegistry
namespace: Autodesk.Revit.DB.ExternalService
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# ExternalServiceRegistry

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ExternalServiceResult ExecuteService(Guid, Guid, IExternalData)` | `ExternalServiceRegistry.ExecuteService(executionKey, serverId, data)` | ExternalServiceResult |
| `ExternalServiceResult ExecuteService(Guid, Document, IExternalData)` | `ExternalServiceRegistry.ExecuteService(executionKey, document, data)` | ExternalServiceResult |
| `ExternalServiceResult ExecuteService(Guid, IExternalData)` | `ExternalServiceRegistry.ExecuteService(executionKey, data)` | ExternalServiceResult |
| `ExternalService GetService(ExternalServiceId)` | `ExternalServiceRegistry.GetService(serviceId)` | ExternalService |
| `IList<ExternalService> GetServices()` | `ExternalServiceRegistry.GetServices()` | IList<ExternalService> |
| `Guid RegisterService(ISingleServerService, Guid, ExternalServiceOptions)` | `ExternalServiceRegistry.RegisterService(service, defaultServerId, options)` | Guid |
| `Guid RegisterService(IMultiServerService, ExternalServiceOptions, ExecutionPolicy)` | `ExternalServiceRegistry.RegisterService(service, options, policy)` | Guid |
| `Guid RegisterService(ISingleServerService, ExternalServiceOptions)` | `ExternalServiceRegistry.RegisterService(service, options)` | Guid |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
