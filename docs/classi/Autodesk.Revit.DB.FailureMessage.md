---
title: FailureMessage
classe: Autodesk.Revit.DB.FailureMessage
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 15
---

# FailureMessage

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `failureMessage.IsValidObject` | Boolean |
| `FailureMessage AddResolution(FailureResolutionType, FailureResolution)` | `failureMessage.AddResolution(type, resolution)` | FailureMessage |
| `Void Dispose()` | `failureMessage.Dispose()` | Void |
| `ICollection<ElementId> GetAdditionalElements()` | `failureMessage.GetAdditionalElements()` | ICollection<ElementId> |
| `String GetDefaultResolutionCaption()` | `failureMessage.GetDefaultResolutionCaption()` | String |
| `String GetDescriptionText()` | `failureMessage.GetDescriptionText()` | String |
| `ICollection<ElementId> GetFailingElements()` | `failureMessage.GetFailingElements()` | ICollection<ElementId> |
| `FailureDefinitionId GetFailureDefinitionId()` | `failureMessage.GetFailureDefinitionId()` | FailureDefinitionId |
| `FailureSeverity GetSeverity()` | `failureMessage.GetSeverity()` | FailureSeverity |
| `Boolean HasResolutionOfType(FailureResolutionType)` | `failureMessage.HasResolutionOfType(type)` | Boolean |
| `Boolean HasResolutions()` | `failureMessage.HasResolutions()` | Boolean |
| `FailureMessage SetAdditionalElement(ElementId)` | `failureMessage.SetAdditionalElement(additionalElement)` | FailureMessage |
| `FailureMessage SetAdditionalElements(ICollection<ElementId>)` | `failureMessage.SetAdditionalElements(additionalElements)` | FailureMessage |
| `FailureMessage SetFailingElement(ElementId)` | `failureMessage.SetFailingElement(id)` | FailureMessage |
| `FailureMessage SetFailingElements(ICollection<ElementId>)` | `failureMessage.SetFailingElements(idsToShow)` | FailureMessage |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
