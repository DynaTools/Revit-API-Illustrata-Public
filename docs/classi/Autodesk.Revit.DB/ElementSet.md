---
title: ElementSet
classe: Autodesk.Revit.DB.ElementSet
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# ElementSet

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEmpty { get; }` | `elementSet.IsEmpty` | Boolean |
| `Int32 Size { get; }` | `elementSet.Size` | Int32 |
| `Void Clear()` | `elementSet.Clear()` | Void |
| `Boolean Contains(Element)` | `elementSet.Contains(item)` | Boolean |
| `Int32 Erase(Element)` | `elementSet.Erase(item)` | Int32 |
| `ElementSetIterator ForwardIterator()` | `elementSet.ForwardIterator()` | ElementSetIterator |
| `IEnumerator GetEnumerator()` | `elementSet.GetEnumerator()` | IEnumerator |
| `Boolean Insert(Element)` | `elementSet.Insert(item)` | Boolean |
| `ElementSetIterator ReverseIterator()` | `elementSet.ReverseIterator()` | ElementSetIterator |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
