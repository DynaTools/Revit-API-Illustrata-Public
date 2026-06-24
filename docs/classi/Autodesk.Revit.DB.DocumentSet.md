---
title: DocumentSet
classe: Autodesk.Revit.DB.DocumentSet
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# DocumentSet

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEmpty { get; }` | `documentSet.IsEmpty` | Boolean |
| `Int32 Size { get; }` | `documentSet.Size` | Int32 |
| `Void Clear()` | `documentSet.Clear()` | Void |
| `Boolean Contains(Document)` | `documentSet.Contains(item)` | Boolean |
| `Int32 Erase(Document)` | `documentSet.Erase(item)` | Int32 |
| `DocumentSetIterator ForwardIterator()` | `documentSet.ForwardIterator()` | DocumentSetIterator |
| `IEnumerator GetEnumerator()` | `documentSet.GetEnumerator()` | IEnumerator |
| `Boolean Insert(Document)` | `documentSet.Insert(item)` | Boolean |
| `DocumentSetIterator ReverseIterator()` | `documentSet.ReverseIterator()` | DocumentSetIterator |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
