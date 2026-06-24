---
title: FormulaManager
classe: Autodesk.Revit.DB.FormulaManager
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 6
---

# FormulaManager

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `formulaManager.IsValidObject` | Boolean |
| `Void Dispose()` | `formulaManager.Dispose()` | Void |
| `String Evaluate(ElementId, Document, String)` | `FormulaManager.Evaluate(parameterId, document, formula)` | String |
| `IList<String> GetFunctions()` | `FormulaManager.GetFunctions()` | IList<String> |
| `IList<String> GetOperators()` | `FormulaManager.GetOperators()` | IList<String> |
| `String Validate(ElementId, Document, String)` | `FormulaManager.Validate(parameterId, document, formula)` | String |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
