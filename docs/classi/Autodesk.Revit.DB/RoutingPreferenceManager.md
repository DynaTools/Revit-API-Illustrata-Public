---
title: RoutingPreferenceManager
classe: Autodesk.Revit.DB.RoutingPreferenceManager
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# RoutingPreferenceManager

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `routingPreferenceManager.IsValidObject` | Boolean |
| `ElementId OwnerId { get; }` | `routingPreferenceManager.OwnerId` | ElementId |
| `PreferredJunctionType PreferredJunctionType { get; set; }` | `routingPreferenceManager.PreferredJunctionType` | PreferredJunctionType |
| `Void AddRule(RoutingPreferenceRuleGroupType, RoutingPreferenceRule, Int32)` | `routingPreferenceManager.AddRule(groupType, rule, index)` | Void |
| `Void AddRule(RoutingPreferenceRuleGroupType, RoutingPreferenceRule)` | `routingPreferenceManager.AddRule(groupType, rule)` | Void |
| `Void Dispose()` | `routingPreferenceManager.Dispose()` | Void |
| `ElementId GetMEPPartId(RoutingPreferenceRuleGroupType, RoutingConditions)` | `routingPreferenceManager.GetMEPPartId(groupType, conditions)` | ElementId |
| `Int32 GetNumberOfRules(RoutingPreferenceRuleGroupType)` | `routingPreferenceManager.GetNumberOfRules(eGroupType)` | Int32 |
| `RoutingPreferenceRule GetRule(RoutingPreferenceRuleGroupType, Int32)` | `routingPreferenceManager.GetRule(groupType, index)` | RoutingPreferenceRule |
| `IList<ElementId> GetSharedSizes(Double, ConnectorProfileType)` | `routingPreferenceManager.GetSharedSizes(size, shape)` | IList<ElementId> |
| `Void RemoveRule(RoutingPreferenceRuleGroupType, Int32)` | `routingPreferenceManager.RemoveRule(groupType, index)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
