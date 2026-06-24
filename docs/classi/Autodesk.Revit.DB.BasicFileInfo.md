---
title: BasicFileInfo
classe: Autodesk.Revit.DB.BasicFileInfo
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 18
---

# BasicFileInfo

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean AllLocalChangesSavedToCentral { get; }` | `basicFileInfo.AllLocalChangesSavedToCentral` | Boolean |
| `String CentralPath { get; }` | `basicFileInfo.CentralPath` | String |
| `String Format { get; }` | `basicFileInfo.Format` | String |
| `Boolean IsCentral { get; }` | `basicFileInfo.IsCentral` | Boolean |
| `Boolean IsCreatedLocal { get; }` | `basicFileInfo.IsCreatedLocal` | Boolean |
| `Boolean IsInProgress { get; }` | `basicFileInfo.IsInProgress` | Boolean |
| `Boolean IsLocal { get; }` | `basicFileInfo.IsLocal` | Boolean |
| `Boolean IsSavedInCurrentVersion { get; }` | `basicFileInfo.IsSavedInCurrentVersion` | Boolean |
| `Boolean IsSavedInLaterVersion { get; }` | `basicFileInfo.IsSavedInLaterVersion` | Boolean |
| `Boolean IsValidObject { get; }` | `basicFileInfo.IsValidObject` | Boolean |
| `Boolean IsWorkshared { get; }` | `basicFileInfo.IsWorkshared` | Boolean |
| `LanguageType LanguageWhenSaved { get; }` | `basicFileInfo.LanguageWhenSaved` | LanguageType |
| `Guid LatestCentralEpisodeGUID { get; }` | `basicFileInfo.LatestCentralEpisodeGUID` | Guid |
| `Int32 LatestCentralVersion { get; }` | `basicFileInfo.LatestCentralVersion` | Int32 |
| `String Username { get; }` | `basicFileInfo.Username` | String |
| `Void Dispose()` | `basicFileInfo.Dispose()` | Void |
| `BasicFileInfo Extract(String)` | `BasicFileInfo.Extract(file)` | BasicFileInfo |
| `DocumentVersion GetDocumentVersion()` | `basicFileInfo.GetDocumentVersion()` | DocumentVersion |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
