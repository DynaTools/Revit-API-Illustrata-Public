---
title: ParameterMap
classe: Autodesk.Revit.DB.ParameterMap
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# ParameterMap

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEmpty { get; }` | `parameterMap.IsEmpty` | Boolean |
| `Parameter Item { get; set; }` | `parameterMap.Item` | Parameter |
| `Int32 Size { get; }` | `parameterMap.Size` | Int32 |
| `Void Clear()` | `parameterMap.Clear()` | Void |
| `Boolean Contains(String)` | `parameterMap.Contains(key)` | Boolean |
| `Int32 Erase(String)` | `parameterMap.Erase(key)` | Int32 |
| `ParameterMapIterator ForwardIterator()` | `parameterMap.ForwardIterator()` | ParameterMapIterator |
| `IEnumerator GetEnumerator()` | `parameterMap.GetEnumerator()` | IEnumerator |
| `Boolean Insert(String, Parameter)` | `parameterMap.Insert(key, item)` | Boolean |
| `ParameterMapIterator ReverseIterator()` | `parameterMap.ReverseIterator()` | ParameterMapIterator |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
