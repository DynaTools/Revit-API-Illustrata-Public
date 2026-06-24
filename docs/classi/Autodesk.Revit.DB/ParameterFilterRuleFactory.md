---
title: ParameterFilterRuleFactory
classe: Autodesk.Revit.DB.ParameterFilterRuleFactory
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 49
---

# ParameterFilterRuleFactory

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `parameterFilterRuleFactory.IsValidObject` | Boolean |
| `FilterRule CreateBeginsWithRule(ElementId, String)` | `ParameterFilterRuleFactory.CreateBeginsWithRule(parameter, value)` | FilterRule |
| `FilterRule CreateBeginsWithRule(ElementId, String, Boolean)` | `ParameterFilterRuleFactory.CreateBeginsWithRule(parameter, value, caseSensitive)` | FilterRule |
| `FilterRule CreateContainsRule(ElementId, String)` | `ParameterFilterRuleFactory.CreateContainsRule(parameter, value)` | FilterRule |
| `FilterRule CreateContainsRule(ElementId, String, Boolean)` | `ParameterFilterRuleFactory.CreateContainsRule(parameter, value, caseSensitive)` | FilterRule |
| `FilterRule CreateEndsWithRule(ElementId, String)` | `ParameterFilterRuleFactory.CreateEndsWithRule(parameter, value)` | FilterRule |
| `FilterRule CreateEndsWithRule(ElementId, String, Boolean)` | `ParameterFilterRuleFactory.CreateEndsWithRule(parameter, value, caseSensitive)` | FilterRule |
| `FilterRule CreateEqualsRule(ElementId, ElementId)` | `ParameterFilterRuleFactory.CreateEqualsRule(parameter, value)` | FilterRule |
| `FilterRule CreateEqualsRule(ElementId, Int32)` | `ParameterFilterRuleFactory.CreateEqualsRule(parameter, value)` | FilterRule |
| `FilterRule CreateEqualsRule(ElementId, Double, Double)` | `ParameterFilterRuleFactory.CreateEqualsRule(parameter, value, epsilon)` | FilterRule |
| `FilterRule CreateEqualsRule(ElementId, String)` | `ParameterFilterRuleFactory.CreateEqualsRule(parameter, value)` | FilterRule |
| `FilterRule CreateEqualsRule(ElementId, String, Boolean)` | `ParameterFilterRuleFactory.CreateEqualsRule(parameter, value, caseSensitive)` | FilterRule |
| `FilterRule CreateGreaterOrEqualRule(ElementId, ElementId)` | `ParameterFilterRuleFactory.CreateGreaterOrEqualRule(parameter, value)` | FilterRule |
| `FilterRule CreateGreaterOrEqualRule(ElementId, Int32)` | `ParameterFilterRuleFactory.CreateGreaterOrEqualRule(parameter, value)` | FilterRule |
| `FilterRule CreateGreaterOrEqualRule(ElementId, Double, Double)` | `ParameterFilterRuleFactory.CreateGreaterOrEqualRule(parameter, value, epsilon)` | FilterRule |
| `FilterRule CreateGreaterOrEqualRule(ElementId, String)` | `ParameterFilterRuleFactory.CreateGreaterOrEqualRule(parameter, value)` | FilterRule |
| `FilterRule CreateGreaterOrEqualRule(ElementId, String, Boolean)` | `ParameterFilterRuleFactory.CreateGreaterOrEqualRule(parameter, value, caseSensitive)` | FilterRule |
| `FilterRule CreateGreaterRule(ElementId, ElementId)` | `ParameterFilterRuleFactory.CreateGreaterRule(parameter, value)` | FilterRule |
| `FilterRule CreateGreaterRule(ElementId, Int32)` | `ParameterFilterRuleFactory.CreateGreaterRule(parameter, value)` | FilterRule |
| `FilterRule CreateGreaterRule(ElementId, Double, Double)` | `ParameterFilterRuleFactory.CreateGreaterRule(parameter, value, epsilon)` | FilterRule |
| `FilterRule CreateGreaterRule(ElementId, String)` | `ParameterFilterRuleFactory.CreateGreaterRule(parameter, value)` | FilterRule |
| `FilterRule CreateGreaterRule(ElementId, String, Boolean)` | `ParameterFilterRuleFactory.CreateGreaterRule(parameter, value, caseSensitive)` | FilterRule |
| `FilterRule CreateHasNoValueParameterRule(ElementId)` | `ParameterFilterRuleFactory.CreateHasNoValueParameterRule(parameter)` | FilterRule |
| `FilterRule CreateHasValueParameterRule(ElementId)` | `ParameterFilterRuleFactory.CreateHasValueParameterRule(parameter)` | FilterRule |
| `FilterRule CreateIsAssociatedWithGlobalParameterRule(ElementId, ElementId)` | `ParameterFilterRuleFactory.CreateIsAssociatedWithGlobalParameterRule(parameter, value)` | FilterRule |
| `FilterRule CreateIsNotAssociatedWithGlobalParameterRule(ElementId, ElementId)` | `ParameterFilterRuleFactory.CreateIsNotAssociatedWithGlobalParameterRule(parameter, value)` | FilterRule |
| `FilterRule CreateLessOrEqualRule(ElementId, ElementId)` | `ParameterFilterRuleFactory.CreateLessOrEqualRule(parameter, value)` | FilterRule |
| `FilterRule CreateLessOrEqualRule(ElementId, Int32)` | `ParameterFilterRuleFactory.CreateLessOrEqualRule(parameter, value)` | FilterRule |
| `FilterRule CreateLessOrEqualRule(ElementId, Double, Double)` | `ParameterFilterRuleFactory.CreateLessOrEqualRule(parameter, value, epsilon)` | FilterRule |
| `FilterRule CreateLessOrEqualRule(ElementId, String)` | `ParameterFilterRuleFactory.CreateLessOrEqualRule(parameter, value)` | FilterRule |
| `FilterRule CreateLessOrEqualRule(ElementId, String, Boolean)` | `ParameterFilterRuleFactory.CreateLessOrEqualRule(parameter, value, caseSensitive)` | FilterRule |
| `FilterRule CreateLessRule(ElementId, ElementId)` | `ParameterFilterRuleFactory.CreateLessRule(parameter, value)` | FilterRule |
| `FilterRule CreateLessRule(ElementId, Int32)` | `ParameterFilterRuleFactory.CreateLessRule(parameter, value)` | FilterRule |
| `FilterRule CreateLessRule(ElementId, Double, Double)` | `ParameterFilterRuleFactory.CreateLessRule(parameter, value, epsilon)` | FilterRule |
| `FilterRule CreateLessRule(ElementId, String)` | `ParameterFilterRuleFactory.CreateLessRule(parameter, value)` | FilterRule |
| `FilterRule CreateLessRule(ElementId, String, Boolean)` | `ParameterFilterRuleFactory.CreateLessRule(parameter, value, caseSensitive)` | FilterRule |
| `FilterRule CreateNotBeginsWithRule(ElementId, String)` | `ParameterFilterRuleFactory.CreateNotBeginsWithRule(parameter, value)` | FilterRule |
| `FilterRule CreateNotBeginsWithRule(ElementId, String, Boolean)` | `ParameterFilterRuleFactory.CreateNotBeginsWithRule(parameter, value, caseSensitive)` | FilterRule |
| `FilterRule CreateNotContainsRule(ElementId, String)` | `ParameterFilterRuleFactory.CreateNotContainsRule(parameter, value)` | FilterRule |
| `FilterRule CreateNotContainsRule(ElementId, String, Boolean)` | `ParameterFilterRuleFactory.CreateNotContainsRule(parameter, value, caseSensitive)` | FilterRule |
| `FilterRule CreateNotEndsWithRule(ElementId, String)` | `ParameterFilterRuleFactory.CreateNotEndsWithRule(parameter, value)` | FilterRule |
| `FilterRule CreateNotEndsWithRule(ElementId, String, Boolean)` | `ParameterFilterRuleFactory.CreateNotEndsWithRule(parameter, value, caseSensitive)` | FilterRule |
| `FilterRule CreateNotEqualsRule(ElementId, ElementId)` | `ParameterFilterRuleFactory.CreateNotEqualsRule(parameter, value)` | FilterRule |
| `FilterRule CreateNotEqualsRule(ElementId, Int32)` | `ParameterFilterRuleFactory.CreateNotEqualsRule(parameter, value)` | FilterRule |
| `FilterRule CreateNotEqualsRule(ElementId, Double, Double)` | `ParameterFilterRuleFactory.CreateNotEqualsRule(parameter, value, epsilon)` | FilterRule |
| `FilterRule CreateNotEqualsRule(ElementId, String)` | `ParameterFilterRuleFactory.CreateNotEqualsRule(parameter, value)` | FilterRule |
| `FilterRule CreateNotEqualsRule(ElementId, String, Boolean)` | `ParameterFilterRuleFactory.CreateNotEqualsRule(parameter, value, caseSensitive)` | FilterRule |
| `FilterRule CreateSharedParameterApplicableRule(String)` | `ParameterFilterRuleFactory.CreateSharedParameterApplicableRule(parameterName)` | FilterRule |
| `Void Dispose()` | `parameterFilterRuleFactory.Dispose()` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
