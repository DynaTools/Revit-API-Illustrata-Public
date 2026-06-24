---
title: GroupSet
classe: Autodesk.Revit.DB.GroupSet
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# GroupSet

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEmpty { get; }` | `groupSet.IsEmpty` | Boolean |
| `Int32 Size { get; }` | `groupSet.Size` | Int32 |
| `Void Clear()` | `groupSet.Clear()` | Void |
| `Boolean Contains(Group)` | `groupSet.Contains(item)` | Boolean |
| `Int32 Erase(Group)` | `groupSet.Erase(item)` | Int32 |
| `GroupSetIterator ForwardIterator()` | `groupSet.ForwardIterator()` | GroupSetIterator |
| `IEnumerator GetEnumerator()` | `groupSet.GetEnumerator()` | IEnumerator |
| `Boolean Insert(Group)` | `groupSet.Insert(item)` | Boolean |
| `GroupSetIterator ReverseIterator()` | `groupSet.ReverseIterator()` | GroupSetIterator |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
