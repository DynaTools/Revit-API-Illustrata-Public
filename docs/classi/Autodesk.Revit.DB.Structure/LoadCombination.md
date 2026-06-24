---
title: LoadCombination
classe: Autodesk.Revit.DB.Structure.LoadCombination
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# LoadCombination

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsThirdPartyGenerated { get; }` | `loadCombination.IsThirdPartyGenerated` | Boolean |
| `LoadCombinationState State { get; set; }` | `loadCombination.State` | LoadCombinationState |
| `LoadCombinationType Type { get; set; }` | `loadCombination.Type` | LoadCombinationType |
| `LoadCombination Create(Document, String, LoadCombinationType, LoadCombinationState)` | `LoadCombination.Create(document, name, type, state)` | LoadCombination |
| `LoadCombination Create(Document, String)` | `LoadCombination.Create(document, name)` | LoadCombination |
| `IList<ElementId> GetCaseAndCombinationIds()` | `loadCombination.GetCaseAndCombinationIds()` | IList<ElementId> |
| `IList<LoadComponent> GetComponents()` | `loadCombination.GetComponents()` | IList<LoadComponent> |
| `IList<ElementId> GetUsageIds()` | `loadCombination.GetUsageIds()` | IList<ElementId> |
| `Void SetComponents(IList<LoadComponent>)` | `loadCombination.SetComponents(components)` | Void |
| `Void SetUsageIds(IList<ElementId>)` | `loadCombination.SetUsageIds(usageIds)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
