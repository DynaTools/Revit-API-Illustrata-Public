---
title: FailureMessageAccessor
classe: Autodesk.Revit.DB.FailureMessageAccessor
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 15
---

# FailureMessageAccessor

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `failureMessageAccessor.IsValidObject` | Boolean |
| `FailureMessage CloneFailureMessage()` | `failureMessageAccessor.CloneFailureMessage()` | FailureMessage |
| `Void Dispose()` | `failureMessageAccessor.Dispose()` | Void |
| `ICollection<ElementId> GetAdditionalElementIds()` | `failureMessageAccessor.GetAdditionalElementIds()` | ICollection<ElementId> |
| `FailureResolutionType GetCurrentResolutionType()` | `failureMessageAccessor.GetCurrentResolutionType()` | FailureResolutionType |
| `String GetDefaultResolutionCaption()` | `failureMessageAccessor.GetDefaultResolutionCaption()` | String |
| `String GetDescriptionText()` | `failureMessageAccessor.GetDescriptionText()` | String |
| `ICollection<ElementId> GetFailingElementIds()` | `failureMessageAccessor.GetFailingElementIds()` | ICollection<ElementId> |
| `FailureDefinitionId GetFailureDefinitionId()` | `failureMessageAccessor.GetFailureDefinitionId()` | FailureDefinitionId |
| `Int32 GetNumberOfResolutions()` | `failureMessageAccessor.GetNumberOfResolutions()` | Int32 |
| `FailureSeverity GetSeverity()` | `failureMessageAccessor.GetSeverity()` | FailureSeverity |
| `Boolean HasResolutionOfType(FailureResolutionType)` | `failureMessageAccessor.HasResolutionOfType(type)` | Boolean |
| `Boolean HasResolutions()` | `failureMessageAccessor.HasResolutions()` | Boolean |
| `Void SetCurrentResolutionType(FailureResolutionType)` | `failureMessageAccessor.SetCurrentResolutionType(resolutionType)` | Void |
| `Boolean ShouldMergeWithMessage(FailureMessageAccessor)` | `failureMessageAccessor.ShouldMergeWithMessage(messageToMergeWith)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
