---
title: CitySet
classe: Autodesk.Revit.DB.CitySet
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# CitySet

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEmpty { get; }` | `citySet.IsEmpty` | Boolean |
| `Int32 Size { get; }` | `citySet.Size` | Int32 |
| `Void Clear()` | `citySet.Clear()` | Void |
| `Boolean Contains(City)` | `citySet.Contains(item)` | Boolean |
| `Int32 Erase(City)` | `citySet.Erase(item)` | Int32 |
| `CitySetIterator ForwardIterator()` | `citySet.ForwardIterator()` | CitySetIterator |
| `IEnumerator GetEnumerator()` | `citySet.GetEnumerator()` | IEnumerator |
| `Boolean Insert(City)` | `citySet.Insert(item)` | Boolean |
| `CitySetIterator ReverseIterator()` | `citySet.ReverseIterator()` | CitySetIterator |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
