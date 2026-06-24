---
title: ExternalResourceBrowserData
classe: Autodesk.Revit.DB.ExternalResourceBrowserData
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 17
---

# ExternalResourceBrowserData

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String FolderPath { get; }` | `externalResourceBrowserData.FolderPath` | String |
| `Boolean IsValidObject { get; }` | `externalResourceBrowserData.IsValidObject` | Boolean |
| `Guid ServerId { get; }` | `externalResourceBrowserData.ServerId` | Guid |
| `Void AddResource(String, String, IDictionary<String, String>)` | `externalResourceBrowserData.AddResource(resourceName, version, referenceInformation)` | Void |
| `Void AddResource(String, String)` | `externalResourceBrowserData.AddResource(resourceName, version)` | Void |
| `Void AddResource(String, IDictionary<String, String>)` | `externalResourceBrowserData.AddResource(resourceName, referenceInformation)` | Void |
| `Void AddResource(String)` | `externalResourceBrowserData.AddResource(resourceName)` | Void |
| `Void AddSubFolder(String, String)` | `externalResourceBrowserData.AddSubFolder(folderName, iconPath)` | Void |
| `Void AddSubFolder(String)` | `externalResourceBrowserData.AddSubFolder(folderName)` | Void |
| `Boolean CallingDocumentHasModelPath()` | `externalResourceBrowserData.CallingDocumentHasModelPath()` | Boolean |
| `Void Dispose()` | `externalResourceBrowserData.Dispose()` | Void |
| `ModelPath GetCallingDocumentModelPath()` | `externalResourceBrowserData.GetCallingDocumentModelPath()` | ModelPath |
| `ExternalResourceMatchOptions GetMatchOptions()` | `externalResourceBrowserData.GetMatchOptions()` | ExternalResourceMatchOptions |
| `IList<ExternalResourceReference> GetResources()` | `externalResourceBrowserData.GetResources()` | IList<ExternalResourceReference> |
| `IList<ExternalResourceSubFolder> GetSubFoldersData()` | `externalResourceBrowserData.GetSubFoldersData()` | IList<ExternalResourceSubFolder> |
| `Boolean IsValidFolderName(String)` | `externalResourceBrowserData.IsValidFolderName(folderName)` | Boolean |
| `Boolean IsValidResourceName(String)` | `externalResourceBrowserData.IsValidResourceName(resourceName)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
