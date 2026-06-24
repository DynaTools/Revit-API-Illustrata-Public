---
title: EvaluatedParameter
classe: Autodesk.Revit.DB.EvaluatedParameter
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# EvaluatedParameter

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `InternalDefinition Definition { get; }` | `evaluatedParameter.Definition` | InternalDefinition |
| `Boolean HasValue { get; }` | `evaluatedParameter.HasValue` | Boolean |
| `Boolean IsValidObject { get; }` | `evaluatedParameter.IsValidObject` | Boolean |
| `StorageType StorageType { get; }` | `evaluatedParameter.StorageType` | StorageType |
| `ParameterValue Value { get; }` | `evaluatedParameter.Value` | ParameterValue |
| `String AsValueString(Document, FormatOptions)` | `evaluatedParameter.AsValueString(doc, options)` | String |
| `String AsValueString(Document)` | `evaluatedParameter.AsValueString(doc)` | String |
| `Void Dispose()` | `evaluatedParameter.Dispose()` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
