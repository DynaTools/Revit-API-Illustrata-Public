---
title: ExternalService
classe: Autodesk.Revit.DB.ExternalService.ExternalService
namespace: Autodesk.Revit.DB.ExternalService
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 17
---

# ExternalService

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String Description { get; }` | `externalService.Description` | String |
| `Boolean IsSerializable { get; }` | `externalService.IsSerializable` | Boolean |
| `Boolean IsValidObject { get; }` | `externalService.IsValidObject` | Boolean |
| `String Name { get; }` | `externalService.Name` | String |
| `Int32 NumberOfServers { get; }` | `externalService.NumberOfServers` | Int32 |
| `ExternalServiceId ServiceId { get; }` | `externalService.ServiceId` | ExternalServiceId |
| `Boolean SupportActivation { get; }` | `externalService.SupportActivation` | Boolean |
| `String VendorId { get; }` | `externalService.VendorId` | String |
| `Void AddServer(IExternalServer)` | `externalService.AddServer(server)` | Void |
| `Void Dispose()` | `externalService.Dispose()` | Void |
| `Guid GetDefaultServerId()` | `externalService.GetDefaultServerId()` | Guid |
| `ExternalServiceOptions GetOptions()` | `externalService.GetOptions()` | ExternalServiceOptions |
| `Guid GetPublicAccessKey()` | `externalService.GetPublicAccessKey()` | Guid |
| `IList<Guid> GetRegisteredServerIds()` | `externalService.GetRegisteredServerIds()` | IList<Guid> |
| `IExternalServer GetServer(Guid)` | `externalService.GetServer(serverId)` | IExternalServer |
| `Boolean IsRegisteredServerId(Guid)` | `externalService.IsRegisteredServerId(serverId)` | Boolean |
| `Void RemoveServer(Guid)` | `externalService.RemoveServer(serverId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
