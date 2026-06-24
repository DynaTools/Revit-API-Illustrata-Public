---
title: FailureDefinition
classe: Autodesk.Revit.DB.FailureDefinition
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 12
---

# FailureDefinition

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `failureDefinition.IsValidObject` | Boolean |
| `FailureSeverity Severity { get; }` | `failureDefinition.Severity` | FailureSeverity |
| `FailureDefinition AddResolutionType(FailureResolutionType, String, Type)` | `failureDefinition.AddResolutionType(type, caption, classOfResolution)` | FailureDefinition |
| `FailureDefinition CreateFailureDefinition(FailureDefinitionId, FailureSeverity, String)` | `FailureDefinition.CreateFailureDefinition(id, severity, messageString)` | FailureDefinition |
| `Void Dispose()` | `failureDefinition.Dispose()` | Void |
| `IList<FailureResolutionType> GetApplicableResolutionTypes()` | `failureDefinition.GetApplicableResolutionTypes()` | IList<FailureResolutionType> |
| `FailureResolutionType GetDefaultResolutionType()` | `failureDefinition.GetDefaultResolutionType()` | FailureResolutionType |
| `String GetDescriptionText()` | `failureDefinition.GetDescriptionText()` | String |
| `String GetResolutionCaption(FailureResolutionType)` | `failureDefinition.GetResolutionCaption(type)` | String |
| `Boolean HasResolutions()` | `failureDefinition.HasResolutions()` | Boolean |
| `Boolean IsResolutionApplicable(FailureResolutionType)` | `failureDefinition.IsResolutionApplicable(type)` | Boolean |
| `FailureDefinition SetDefaultResolutionType(FailureResolutionType)` | `failureDefinition.SetDefaultResolutionType(type)` | FailureDefinition |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
