---
title: CircuitNamingScheme
classe: Autodesk.Revit.DB.Electrical.CircuitNamingScheme
namespace: Autodesk.Revit.DB.Electrical
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 5
---

# CircuitNamingScheme

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `CircuitNamingScheme Create(Document, String, IList<TableCellCombinedParameterData>)` | `CircuitNamingScheme.Create(document, name, data)` | CircuitNamingScheme |
| `IList<TableCellCombinedParameterData> GetCombinedParameters()` | `circuitNamingScheme.GetCombinedParameters()` | IList<TableCellCombinedParameterData> |
| `Boolean IsNameUnique(Document, String)` | `CircuitNamingScheme.IsNameUnique(aDocument, name)` | Boolean |
| `Boolean IsValidCombinedParameters(Document, IList<TableCellCombinedParameterData>)` | `CircuitNamingScheme.IsValidCombinedParameters(aDocument, data)` | Boolean |
| `Void SetCombinedParameters(IList<TableCellCombinedParameterData>)` | `circuitNamingScheme.SetCombinedParameters(data)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
