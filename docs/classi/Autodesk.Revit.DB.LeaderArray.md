---
title: LeaderArray
classe: Autodesk.Revit.DB.LeaderArray
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# LeaderArray

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEmpty { get; }` | `leaderArray.IsEmpty` | Boolean |
| `Leader Item { get; set; }` | `leaderArray.Item` | Leader |
| `Int32 Size { get; }` | `leaderArray.Size` | Int32 |
| `Void Append(Leader)` | `leaderArray.Append(item)` | Void |
| `Void Clear()` | `leaderArray.Clear()` | Void |
| `LeaderArrayIterator ForwardIterator()` | `leaderArray.ForwardIterator()` | LeaderArrayIterator |
| `IEnumerator GetEnumerator()` | `leaderArray.GetEnumerator()` | IEnumerator |
| `Void Insert(Leader, Int32)` | `leaderArray.Insert(item, index)` | Void |
| `LeaderArrayIterator ReverseIterator()` | `leaderArray.ReverseIterator()` | LeaderArrayIterator |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
