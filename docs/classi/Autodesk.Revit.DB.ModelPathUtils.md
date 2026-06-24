---
title: ModelPathUtils
classe: Autodesk.Revit.DB.ModelPathUtils
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 6
---

# ModelPathUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String CloudRegionEMEA { get; }` | `ModelPathUtils.CloudRegionEMEA` | String |
| `String CloudRegionUS { get; }` | `ModelPathUtils.CloudRegionUS` | String |
| `ModelPath ConvertCloudGUIDsToCloudPath(String, Guid, Guid)` | `ModelPathUtils.ConvertCloudGUIDsToCloudPath(region, projectGuid, modelGuid)` | ModelPath |
| `String ConvertModelPathToUserVisiblePath(ModelPath)` | `ModelPathUtils.ConvertModelPathToUserVisiblePath(path)` | String |
| `ModelPath ConvertUserVisiblePathToModelPath(String)` | `ModelPathUtils.ConvertUserVisiblePathToModelPath(strPath)` | ModelPath |
| `Boolean IsValidUserVisibleFullServerPath(String)` | `ModelPathUtils.IsValidUserVisibleFullServerPath(strPath)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
