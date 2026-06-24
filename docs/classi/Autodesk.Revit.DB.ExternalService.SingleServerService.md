---
title: SingleServerService
classe: Autodesk.Revit.DB.ExternalService.SingleServerService
namespace: Autodesk.Revit.DB.ExternalService
eredita: Autodesk.Revit.DB.ExternalService.ExternalService
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 5
---

# SingleServerService

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Guid GetActiveServerId(Document)` | `singleServerService.GetActiveServerId(document)` | Guid |
| `Guid GetActiveServerId()` | `singleServerService.GetActiveServerId()` | Guid |
| `Void SetActiveServer(Guid, Document)` | `singleServerService.SetActiveServer(serverId, document)` | Void |
| `Void SetActiveServer(Guid)` | `singleServerService.SetActiveServer(serverId)` | Void |
| `Void UnsetActiveServer(Document)` | `singleServerService.UnsetActiveServer(document)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
