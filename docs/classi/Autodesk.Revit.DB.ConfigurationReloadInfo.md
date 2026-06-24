---
title: ConfigurationReloadInfo
classe: Autodesk.Revit.DB.ConfigurationReloadInfo
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# ConfigurationReloadInfo

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 Disconnects { get; }` | `configurationReloadInfo.Disconnects` | Int32 |
| `Boolean IsValidObject { get; }` | `configurationReloadInfo.IsValidObject` | Boolean |
| `Int32 OutOfDatePartCount { get; }` | `configurationReloadInfo.OutOfDatePartCount` | Int32 |
| `Boolean ProfileNotAvailable { get; }` | `configurationReloadInfo.ProfileNotAvailable` | Boolean |
| `Void Dispose()` | `configurationReloadInfo.Dispose()` | Void |
| `ConnectionValidationInfo GetConnectivityValidation()` | `configurationReloadInfo.GetConnectivityValidation()` | ConnectionValidationInfo |
| `ISet<ElementId> GetCustomDataChangedElements()` | `configurationReloadInfo.GetCustomDataChangedElements()` | ISet<ElementId> |
| `ReloadSwapOutInfo GetOutOfDatePartStatus(Int32)` | `configurationReloadInfo.GetOutOfDatePartStatus(index)` | ReloadSwapOutInfo |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
