---
title: RoutingPreferenceRule
classe: Autodesk.Revit.DB.RoutingPreferenceRule
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# RoutingPreferenceRule

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String Description { get; }` | `routingPreferenceRule.Description` | String |
| `Boolean IsValidObject { get; }` | `routingPreferenceRule.IsValidObject` | Boolean |
| `ElementId MEPPartId { get; }` | `routingPreferenceRule.MEPPartId` | ElementId |
| `Int32 NumberOfCriteria { get; }` | `routingPreferenceRule.NumberOfCriteria` | Int32 |
| `RoutingPreferenceManager RoutingPreferenceManager { get; }` | `routingPreferenceRule.RoutingPreferenceManager` | RoutingPreferenceManager |
| `Void AddCriterion(RoutingCriterionBase)` | `routingPreferenceRule.AddCriterion(myCriterion)` | Void |
| `Void Dispose()` | `routingPreferenceRule.Dispose()` | Void |
| `RoutingCriterionBase GetCriterion(Int32)` | `routingPreferenceRule.GetCriterion(index)` | RoutingCriterionBase |
| `Void RemoveCriteron(Int32)` | `routingPreferenceRule.RemoveCriteron(index)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
