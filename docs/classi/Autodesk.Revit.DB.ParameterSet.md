---
title: ParameterSet
classe: Autodesk.Revit.DB.ParameterSet
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# ParameterSet

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEmpty { get; }` | `parameterSet.IsEmpty` | Boolean |
| `Int32 Size { get; }` | `parameterSet.Size` | Int32 |
| `Void Clear()` | `parameterSet.Clear()` | Void |
| `Boolean Contains(Parameter)` | `parameterSet.Contains(item)` | Boolean |
| `Int32 Erase(Parameter)` | `parameterSet.Erase(item)` | Int32 |
| `ParameterSetIterator ForwardIterator()` | `parameterSet.ForwardIterator()` | ParameterSetIterator |
| `IEnumerator GetEnumerator()` | `parameterSet.GetEnumerator()` | IEnumerator |
| `Boolean Insert(Parameter)` | `parameterSet.Insert(item)` | Boolean |
| `ParameterSetIterator ReverseIterator()` | `parameterSet.ReverseIterator()` | ParameterSetIterator |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
