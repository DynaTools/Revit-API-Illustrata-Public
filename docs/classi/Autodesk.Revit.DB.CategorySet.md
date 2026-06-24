---
title: CategorySet
classe: Autodesk.Revit.DB.CategorySet
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# CategorySet

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEmpty { get; }` | `categorySet.IsEmpty` | Boolean |
| `Int32 Size { get; }` | `categorySet.Size` | Int32 |
| `Void Clear()` | `categorySet.Clear()` | Void |
| `Boolean Contains(Category)` | `categorySet.Contains(item)` | Boolean |
| `Int32 Erase(Category)` | `categorySet.Erase(item)` | Int32 |
| `CategorySetIterator ForwardIterator()` | `categorySet.ForwardIterator()` | CategorySetIterator |
| `IEnumerator GetEnumerator()` | `categorySet.GetEnumerator()` | IEnumerator |
| `Boolean Insert(Category)` | `categorySet.Insert(item)` | Boolean |
| `CategorySetIterator ReverseIterator()` | `categorySet.ReverseIterator()` | CategorySetIterator |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
