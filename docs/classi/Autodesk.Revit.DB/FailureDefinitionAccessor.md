---
title: FailureDefinitionAccessor
classe: Autodesk.Revit.DB.FailureDefinitionAccessor
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# FailureDefinitionAccessor

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `failureDefinitionAccessor.IsValidObject` | Boolean |
| `Void Dispose()` | `failureDefinitionAccessor.Dispose()` | Void |
| `IList<FailureResolutionType> GetApplicableResolutionTypes()` | `failureDefinitionAccessor.GetApplicableResolutionTypes()` | IList<FailureResolutionType> |
| `FailureResolutionType GetDefaultResolutionType()` | `failureDefinitionAccessor.GetDefaultResolutionType()` | FailureResolutionType |
| `String GetDescriptionText()` | `failureDefinitionAccessor.GetDescriptionText()` | String |
| `FailureDefinitionId GetId()` | `failureDefinitionAccessor.GetId()` | FailureDefinitionId |
| `String GetResolutionCaption(FailureResolutionType)` | `failureDefinitionAccessor.GetResolutionCaption(type)` | String |
| `FailureSeverity GetSeverity()` | `failureDefinitionAccessor.GetSeverity()` | FailureSeverity |
| `Boolean HasResolutions()` | `failureDefinitionAccessor.HasResolutions()` | Boolean |
| `Boolean IsResolutionApplicable(FailureResolutionType)` | `failureDefinitionAccessor.IsResolutionApplicable(type)` | Boolean |
| `Void SetDefaultResolutionType(FailureResolutionType)` | `failureDefinitionAccessor.SetDefaultResolutionType(type)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
