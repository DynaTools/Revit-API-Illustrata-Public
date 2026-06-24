---
title: ControlledApplication
classe: Autodesk.Revit.ApplicationServices.ControlledApplication
namespace: Autodesk.Revit.ApplicationServices
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 23
---

# ControlledApplication

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `AddInId ActiveAddInId { get; }` | `controlledApplication.ActiveAddInId` | AddInId |
| `String AllUsersAddinsLocation { get; }` | `controlledApplication.AllUsersAddinsLocation` | String |
| `CitySet Cities { get; }` | `controlledApplication.Cities` | CitySet |
| `Application Create { get; }` | `controlledApplication.Create` | Application |
| `String CurrentUserAddinsLocation { get; }` | `controlledApplication.CurrentUserAddinsLocation` | String |
| `String CurrentUsersAddinsDataFolderPath { get; }` | `controlledApplication.CurrentUsersAddinsDataFolderPath` | String |
| `String CurrentUsersDataFolderPath { get; }` | `controlledApplication.CurrentUsersDataFolderPath` | String |
| `Boolean IsLateAddinLoading { get; }` | `controlledApplication.IsLateAddinLoading` | Boolean |
| `LanguageType Language { get; }` | `controlledApplication.Language` | LanguageType |
| `ProductType Product { get; }` | `controlledApplication.Product` | ProductType |
| `String RecordingJournalFilename { get; }` | `controlledApplication.RecordingJournalFilename` | String |
| `String SharedParametersFilename { get; set; }` | `controlledApplication.SharedParametersFilename` | String |
| `String SubVersionNumber { get; }` | `controlledApplication.SubVersionNumber` | String |
| `String VersionBuild { get; }` | `controlledApplication.VersionBuild` | String |
| `String VersionName { get; }` | `controlledApplication.VersionName` | String |
| `String VersionNumber { get; }` | `controlledApplication.VersionNumber` | String |
| `FailureDefinitionRegistry GetFailureDefinitionRegistry()` | `ControlledApplication.GetFailureDefinitionRegistry()` | FailureDefinitionRegistry |
| `IDictionary<String, String> GetLibraryPaths()` | `controlledApplication.GetLibraryPaths()` | IDictionary<String, String> |
| `Boolean IsJournalPlaying()` | `controlledApplication.IsJournalPlaying()` | Boolean |
| `DefinitionFile OpenSharedParameterFile()` | `controlledApplication.OpenSharedParameterFile()` | DefinitionFile |
| `Void RegisterFailuresProcessor(IFailuresProcessor)` | `ControlledApplication.RegisterFailuresProcessor(processor)` | Void |
| `Void SetLibraryPaths(IDictionary<String, String>)` | `controlledApplication.SetLibraryPaths(paths)` | Void |
| `Void WriteJournalComment(String, Boolean)` | `controlledApplication.WriteJournalComment(comment, timeStamp)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
