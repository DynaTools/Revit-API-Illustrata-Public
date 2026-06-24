---
title: ViewSet
classe: Autodesk.Revit.DB.ViewSet
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# ViewSet

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEmpty { get; }` | `viewSet.IsEmpty` | Boolean |
| `Int32 Size { get; }` | `viewSet.Size` | Int32 |
| `Void Clear()` | `viewSet.Clear()` | Void |
| `Boolean Contains(View)` | `viewSet.Contains(item)` | Boolean |
| `Int32 Erase(View)` | `viewSet.Erase(item)` | Int32 |
| `ViewSetIterator ForwardIterator()` | `viewSet.ForwardIterator()` | ViewSetIterator |
| `IEnumerator GetEnumerator()` | `viewSet.GetEnumerator()` | IEnumerator |
| `Boolean Insert(View)` | `viewSet.Insert(item)` | Boolean |
| `ViewSetIterator ReverseIterator()` | `viewSet.ReverseIterator()` | ViewSetIterator |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
