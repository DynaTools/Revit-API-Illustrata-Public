---
title: WireSet
classe: Autodesk.Revit.DB.Electrical.WireSet
namespace: Autodesk.Revit.DB.Electrical
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# WireSet

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEmpty { get; }` | `wireSet.IsEmpty` | Boolean |
| `Int32 Size { get; }` | `wireSet.Size` | Int32 |
| `Void Clear()` | `wireSet.Clear()` | Void |
| `Boolean Contains(Wire)` | `wireSet.Contains(item)` | Boolean |
| `Int32 Erase(Wire)` | `wireSet.Erase(item)` | Int32 |
| `WireSetIterator ForwardIterator()` | `wireSet.ForwardIterator()` | WireSetIterator |
| `IEnumerator GetEnumerator()` | `wireSet.GetEnumerator()` | IEnumerator |
| `Boolean Insert(Wire)` | `wireSet.Insert(item)` | Boolean |
| `WireSetIterator ReverseIterator()` | `wireSet.ReverseIterator()` | WireSetIterator |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
