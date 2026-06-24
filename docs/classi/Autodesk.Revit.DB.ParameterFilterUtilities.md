---
title: ParameterFilterUtilities
classe: Autodesk.Revit.DB.ParameterFilterUtilities
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 5
---

# ParameterFilterUtilities

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ICollection<ElementId> GetAllFilterableCategories()` | `ParameterFilterUtilities.GetAllFilterableCategories()` | ICollection<ElementId> |
| `ICollection<ElementId> GetFilterableParametersInCommon(Document, ICollection<ElementId>)` | `ParameterFilterUtilities.GetFilterableParametersInCommon(aDoc, categories)` | ICollection<ElementId> |
| `IList<ElementId> GetInapplicableParameters(Document, ICollection<ElementId>, IList<ElementId>)` | `ParameterFilterUtilities.GetInapplicableParameters(aDoc, categories, parameters)` | IList<ElementId> |
| `Boolean IsParameterApplicable(Element, ElementId)` | `ParameterFilterUtilities.IsParameterApplicable(element, parameter)` | Boolean |
| `ICollection<ElementId> RemoveUnfilterableCategories(ICollection<ElementId>)` | `ParameterFilterUtilities.RemoveUnfilterableCategories(categories)` | ICollection<ElementId> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
