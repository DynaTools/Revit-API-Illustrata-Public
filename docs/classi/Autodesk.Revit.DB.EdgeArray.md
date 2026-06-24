---
title: EdgeArray
classe: Autodesk.Revit.DB.EdgeArray
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# EdgeArray

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEmpty { get; }` | `edgeArray.IsEmpty` | Boolean |
| `Edge Item { get; set; }` | `edgeArray.Item` | Edge |
| `Int32 Size { get; }` | `edgeArray.Size` | Int32 |
| `Void Append(Edge)` | `edgeArray.Append(item)` | Void |
| `Void Clear()` | `edgeArray.Clear()` | Void |
| `EdgeArrayIterator ForwardIterator()` | `edgeArray.ForwardIterator()` | EdgeArrayIterator |
| `IEnumerator GetEnumerator()` | `edgeArray.GetEnumerator()` | IEnumerator |
| `Void Insert(Edge, Int32)` | `edgeArray.Insert(item, index)` | Void |
| `EdgeArrayIterator ReverseIterator()` | `edgeArray.ReverseIterator()` | EdgeArrayIterator |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
