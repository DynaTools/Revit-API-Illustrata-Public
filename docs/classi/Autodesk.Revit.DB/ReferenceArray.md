---
title: ReferenceArray
classe: Autodesk.Revit.DB.ReferenceArray
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# ReferenceArray

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEmpty { get; }` | `referenceArray.IsEmpty` | Boolean |
| `Reference Item { get; set; }` | `referenceArray.Item` | Reference |
| `Int32 Size { get; }` | `referenceArray.Size` | Int32 |
| `Void Append(Reference)` | `referenceArray.Append(item)` | Void |
| `Void Clear()` | `referenceArray.Clear()` | Void |
| `ReferenceArrayIterator ForwardIterator()` | `referenceArray.ForwardIterator()` | ReferenceArrayIterator |
| `IEnumerator GetEnumerator()` | `referenceArray.GetEnumerator()` | IEnumerator |
| `Void Insert(Reference, Int32)` | `referenceArray.Insert(item, index)` | Void |
| `ReferenceArrayIterator ReverseIterator()` | `referenceArray.ReverseIterator()` | ReferenceArrayIterator |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
