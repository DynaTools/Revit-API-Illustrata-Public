---
title: ParameterUtils
classe: Autodesk.Revit.DB.ParameterUtils
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# ParameterUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String DownloadCompanyName(Document, ForgeTypeId)` | `ParameterUtils.DownloadCompanyName(document, parameterTypeId)` | String |
| `SharedParameterElement DownloadParameter(Document, ParameterDownloadOptions, ForgeTypeId)` | `ParameterUtils.DownloadParameter(document, options, parameterTypeId)` | SharedParameterElement |
| `ParameterDownloadOptions DownloadParameterOptions(ForgeTypeId)` | `ParameterUtils.DownloadParameterOptions(parameterTypeId)` | ParameterDownloadOptions |
| `IList<ForgeTypeId> GetAllBuiltInGroups()` | `ParameterUtils.GetAllBuiltInGroups()` | IList<ForgeTypeId> |
| `IList<ForgeTypeId> GetAllBuiltInParameters()` | `ParameterUtils.GetAllBuiltInParameters()` | IList<ForgeTypeId> |
| `BuiltInParameter GetBuiltInParameter(ForgeTypeId)` | `ParameterUtils.GetBuiltInParameter(parameterTypeId)` | BuiltInParameter |
| `ForgeTypeId GetParameterTypeId(BuiltInParameter)` | `ParameterUtils.GetParameterTypeId(builtInParam)` | ForgeTypeId |
| `Boolean IsBuiltInGroup(ForgeTypeId)` | `ParameterUtils.IsBuiltInGroup(groupTypeId)` | Boolean |
| `Boolean IsBuiltInParameter(ElementId)` | `ParameterUtils.IsBuiltInParameter(parameterId)` | Boolean |
| `Boolean IsBuiltInParameter(ForgeTypeId)` | `ParameterUtils.IsBuiltInParameter(parameterTypeId)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
