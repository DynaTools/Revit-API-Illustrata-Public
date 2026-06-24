---
title: LoadBase
classe: Autodesk.Revit.DB.Structure.LoadBase
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# LoadBase

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId HostElementId { get; }` | `loadBase.HostElementId` | ElementId |
| `Boolean IsConstrainedOnHost { get; }` | `loadBase.IsConstrainedOnHost` | Boolean |
| `Boolean IsHosted { get; }` | `loadBase.IsHosted` | Boolean |
| `Boolean IsReaction { get; set; }` | `loadBase.IsReaction` | Boolean |
| `LoadCase LoadCase { get; }` | `loadBase.LoadCase` | LoadCase |
| `ElementId LoadCaseId { get; set; }` | `loadBase.LoadCaseId` | ElementId |
| `String LoadCaseName { get; }` | `loadBase.LoadCaseName` | String |
| `String LoadCategoryName { get; }` | `loadBase.LoadCategoryName` | String |
| `String LoadNatureName { get; }` | `loadBase.LoadNatureName` | String |
| `LoadOrientTo OrientTo { get; set; }` | `loadBase.OrientTo` | LoadOrientTo |
| `ElementId WorkPlaneId { get; }` | `loadBase.WorkPlaneId` | ElementId |
| `Boolean IsOrientToPermitted(LoadOrientTo)` | `loadBase.IsOrientToPermitted(orientTo)` | Boolean |
| `Void RemoveHostConstraint()` | `loadBase.RemoveHostConstraint()` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
