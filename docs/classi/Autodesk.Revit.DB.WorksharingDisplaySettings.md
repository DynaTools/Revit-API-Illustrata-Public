---
title: WorksharingDisplaySettings
classe: Autodesk.Revit.DB.WorksharingDisplaySettings
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 15
---

# WorksharingDisplaySettings

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean CanUserHaveOverrides(String)` | `worksharingDisplaySettings.CanUserHaveOverrides(username)` | Boolean |
| `ICollection<String> GetAllUsersWithGraphicOverrides()` | `worksharingDisplaySettings.GetAllUsersWithGraphicOverrides()` | ICollection<String> |
| `WorksharingDisplayGraphicSettings GetGraphicOverrides(WorksetId)` | `worksharingDisplaySettings.GetGraphicOverrides(worksetId)` | WorksharingDisplayGraphicSettings |
| `WorksharingDisplayGraphicSettings GetGraphicOverrides(String)` | `worksharingDisplaySettings.GetGraphicOverrides(username)` | WorksharingDisplayGraphicSettings |
| `WorksharingDisplayGraphicSettings GetGraphicOverrides(ModelUpdatesStatus)` | `worksharingDisplaySettings.GetGraphicOverrides(statusInCentral)` | WorksharingDisplayGraphicSettings |
| `WorksharingDisplayGraphicSettings GetGraphicOverrides(CheckoutStatus)` | `worksharingDisplaySettings.GetGraphicOverrides(ownershipStatus)` | WorksharingDisplayGraphicSettings |
| `WorksharingDisplaySettings GetOrCreateWorksharingDisplaySettings(Document)` | `WorksharingDisplaySettings.GetOrCreateWorksharingDisplaySettings(doc)` | WorksharingDisplaySettings |
| `ICollection<String> GetRemovedUsers()` | `worksharingDisplaySettings.GetRemovedUsers()` | ICollection<String> |
| `Void RemoveUsers(Document, ICollection<String>, ICollection<String>&)` | `worksharingDisplaySettings.RemoveUsers(document, usersToRemove, usersActuallyRemoved)` | Void |
| `Int32 RestoreUsers(ICollection<String>)` | `worksharingDisplaySettings.RestoreUsers(usersToRestore)` | Int32 |
| `Void SetGraphicOverrides(WorksetId, WorksharingDisplayGraphicSettings)` | `worksharingDisplaySettings.SetGraphicOverrides(worksetId, overrides)` | Void |
| `Void SetGraphicOverrides(CheckoutStatus, WorksharingDisplayGraphicSettings)` | `worksharingDisplaySettings.SetGraphicOverrides(status, overrides)` | Void |
| `Void SetGraphicOverrides(ModelUpdatesStatus, WorksharingDisplayGraphicSettings)` | `worksharingDisplaySettings.SetGraphicOverrides(status, overrides)` | Void |
| `Void SetGraphicOverrides(String, WorksharingDisplayGraphicSettings)` | `worksharingDisplaySettings.SetGraphicOverrides(username, overrides)` | Void |
| `Boolean UserHasGraphicOverrides(String)` | `worksharingDisplaySettings.UserHasGraphicOverrides(username)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
