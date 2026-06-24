---
title: ParameterFilterElement
classe: Autodesk.Revit.DB.ParameterFilterElement
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.FilterElement
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# ParameterFilterElement

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean AllRuleParametersApplicable(ElementFilter)` | `parameterFilterElement.AllRuleParametersApplicable(elementFilter)` | Boolean |
| `Boolean AllRuleParametersApplicable(Document, ICollection<ElementId>, ElementFilter)` | `ParameterFilterElement.AllRuleParametersApplicable(aDocument, categories, elementFilter)` | Boolean |
| `Void ClearRules()` | `parameterFilterElement.ClearRules()` | Void |
| `ParameterFilterElement Create(Document, String, ICollection<ElementId>, ElementFilter)` | `ParameterFilterElement.Create(aDocument, name, categories, elementFilter)` | ParameterFilterElement |
| `ParameterFilterElement Create(Document, String, ICollection<ElementId>)` | `ParameterFilterElement.Create(aDocument, name, categories)` | ParameterFilterElement |
| `Boolean ElementFilterIsAcceptableForParameterFilterElement(Document, ISet<ElementId>, ElementFilter)` | `ParameterFilterElement.ElementFilterIsAcceptableForParameterFilterElement(aDocument, categories, elementFilter)` | Boolean |
| `Boolean ElementFilterIsAcceptableForParameterFilterElement(ElementFilter)` | `parameterFilterElement.ElementFilterIsAcceptableForParameterFilterElement(elementFilter)` | Boolean |
| `ICollection<ElementId> GetCategories()` | `parameterFilterElement.GetCategories()` | ICollection<ElementId> |
| `ElementFilter GetElementFilter()` | `parameterFilterElement.GetElementFilter()` | ElementFilter |
| `ISet<ElementId> GetElementFilterParameters()` | `parameterFilterElement.GetElementFilterParameters()` | ISet<ElementId> |
| `ISet<ElementId> GetElementFilterParametersForCategory(ElementId)` | `parameterFilterElement.GetElementFilterParametersForCategory(categoryId)` | ISet<ElementId> |
| `Void SetCategories(ICollection<ElementId>)` | `parameterFilterElement.SetCategories(categories)` | Void |
| `Boolean SetElementFilter(ElementFilter)` | `parameterFilterElement.SetElementFilter(elementFilter)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
