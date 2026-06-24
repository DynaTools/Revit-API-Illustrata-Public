---
title: ElementArray
classe: Autodesk.Revit.DB.ElementArray
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# ElementArray

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEmpty { get; }` | `elementArray.IsEmpty` | Boolean |
| `Element Item { get; set; }` | `elementArray.Item` | Element |
| `Int32 Size { get; }` | `elementArray.Size` | Int32 |
| `Void Append(Element)` | `elementArray.Append(item)` | Void |
| `Void Clear()` | `elementArray.Clear()` | Void |
| `ElementArrayIterator ForwardIterator()` | `elementArray.ForwardIterator()` | ElementArrayIterator |
| `IEnumerator GetEnumerator()` | `elementArray.GetEnumerator()` | IEnumerator |
| `Void Insert(Element, Int32)` | `elementArray.Insert(item, index)` | Void |
| `ElementArrayIterator ReverseIterator()` | `elementArray.ReverseIterator()` | ElementArrayIterator |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
