---
title: ExternalResourceReference
classe: Autodesk.Revit.DB.ExternalResourceReference
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# ExternalResourceReference

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String InSessionPath { get; set; }` | `externalResourceReference.InSessionPath` | String |
| `Boolean IsValidObject { get; }` | `externalResourceReference.IsValidObject` | Boolean |
| `Guid ServerId { get; }` | `externalResourceReference.ServerId` | Guid |
| `String Version { get; set; }` | `externalResourceReference.Version` | String |
| `ExternalResourceReference CreateLocalResource(Document, ExternalResourceType, ModelPath, PathType)` | `ExternalResourceReference.CreateLocalResource(doc, resourceType, path, pathType)` | ExternalResourceReference |
| `Void Dispose()` | `externalResourceReference.Dispose()` | Void |
| `IDictionary<String, String> GetReferenceInformation()` | `externalResourceReference.GetReferenceInformation()` | IDictionary<String, String> |
| `String GetResourceShortDisplayName()` | `externalResourceReference.GetResourceShortDisplayName()` | String |
| `ResourceVersionStatus GetResourceVersionStatus()` | `externalResourceReference.GetResourceVersionStatus()` | ResourceVersionStatus |
| `Boolean HasValidDisplayPath()` | `externalResourceReference.HasValidDisplayPath()` | Boolean |
| `Boolean IsValidReference(ExternalResourceType)` | `externalResourceReference.IsValidReference(resourceType)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
