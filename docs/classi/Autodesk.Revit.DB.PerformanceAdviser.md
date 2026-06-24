---
title: PerformanceAdviser
classe: Autodesk.Revit.DB.PerformanceAdviser
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 24
---

# PerformanceAdviser

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `performanceAdviser.IsValidObject` | Boolean |
| `Void AddRule(PerformanceAdviserRuleId, IPerformanceAdviserRule)` | `performanceAdviser.AddRule(id, rule)` | Void |
| `Void DeleteRule(PerformanceAdviserRuleId)` | `performanceAdviser.DeleteRule(id)` | Void |
| `Void Dispose()` | `performanceAdviser.Dispose()` | Void |
| `IList<FailureMessage> ExecuteAllRules(Document)` | `performanceAdviser.ExecuteAllRules(document)` | IList<FailureMessage> |
| `IList<FailureMessage> ExecuteRules(Document, IList<Int32>)` | `performanceAdviser.ExecuteRules(document, rules)` | IList<FailureMessage> |
| `IList<FailureMessage> ExecuteRules(Document, IList<PerformanceAdviserRuleId>)` | `performanceAdviser.ExecuteRules(document, rules)` | IList<FailureMessage> |
| `IList<PerformanceAdviserRuleId> GetAllRuleIds()` | `performanceAdviser.GetAllRuleIds()` | IList<PerformanceAdviserRuleId> |
| `ElementFilter GetElementFilterFromRule(Int32, Document)` | `performanceAdviser.GetElementFilterFromRule(index, document)` | ElementFilter |
| `ElementFilter GetElementFilterFromRule(PerformanceAdviserRuleId, Document)` | `performanceAdviser.GetElementFilterFromRule(id, document)` | ElementFilter |
| `Int32 GetNumberOfRules()` | `performanceAdviser.GetNumberOfRules()` | Int32 |
| `PerformanceAdviser GetPerformanceAdviser()` | `PerformanceAdviser.GetPerformanceAdviser()` | PerformanceAdviser |
| `String GetRuleDescription(Int32)` | `performanceAdviser.GetRuleDescription(index)` | String |
| `String GetRuleDescription(PerformanceAdviserRuleId)` | `performanceAdviser.GetRuleDescription(id)` | String |
| `PerformanceAdviserRuleId GetRuleId(Int32)` | `performanceAdviser.GetRuleId(index)` | PerformanceAdviserRuleId |
| `String GetRuleName(Int32)` | `performanceAdviser.GetRuleName(index)` | String |
| `String GetRuleName(PerformanceAdviserRuleId)` | `performanceAdviser.GetRuleName(id)` | String |
| `Boolean IsRuleEnabled(PerformanceAdviserRuleId)` | `performanceAdviser.IsRuleEnabled(id)` | Boolean |
| `Boolean IsRuleEnabled(Int32)` | `performanceAdviser.IsRuleEnabled(index)` | Boolean |
| `Void PostWarning(FailureMessage)` | `performanceAdviser.PostWarning(message)` | Void |
| `Void SetRuleEnabled(PerformanceAdviserRuleId, Boolean)` | `performanceAdviser.SetRuleEnabled(id, enabled)` | Void |
| `Void SetRuleEnabled(Int32, Boolean)` | `performanceAdviser.SetRuleEnabled(index, enabled)` | Void |
| `Boolean WillRuleCheckElements(Int32)` | `performanceAdviser.WillRuleCheckElements(index)` | Boolean |
| `Boolean WillRuleCheckElements(PerformanceAdviserRuleId)` | `performanceAdviser.WillRuleCheckElements(id)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
