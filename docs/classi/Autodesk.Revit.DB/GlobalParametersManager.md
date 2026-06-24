---
title: GlobalParametersManager
classe: Autodesk.Revit.DB.GlobalParametersManager
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# GlobalParametersManager

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `globalParametersManager.IsValidObject` | Boolean |
| `Boolean AreGlobalParametersAllowed(Document)` | `GlobalParametersManager.AreGlobalParametersAllowed(document)` | Boolean |
| `Void Dispose()` | `globalParametersManager.Dispose()` | Void |
| `ElementId FindByName(Document, String)` | `GlobalParametersManager.FindByName(document, name)` | ElementId |
| `ISet<ElementId> GetAllGlobalParameters(Document)` | `GlobalParametersManager.GetAllGlobalParameters(document)` | ISet<ElementId> |
| `IList<ElementId> GetGlobalParametersOrdered(Document)` | `GlobalParametersManager.GetGlobalParametersOrdered(document)` | IList<ElementId> |
| `Boolean IsUniqueName(Document, String)` | `GlobalParametersManager.IsUniqueName(document, name)` | Boolean |
| `Boolean IsValidGlobalParameter(Document, ElementId)` | `GlobalParametersManager.IsValidGlobalParameter(document, parameterId)` | Boolean |
| `Boolean MoveParameterDownOrder(Document, ElementId)` | `GlobalParametersManager.MoveParameterDownOrder(document, parameterId)` | Boolean |
| `Boolean MoveParameterUpOrder(Document, ElementId)` | `GlobalParametersManager.MoveParameterUpOrder(document, parameterId)` | Boolean |
| `Void SortParameters(Document, ParametersOrder)` | `GlobalParametersManager.SortParameters(document, order)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
