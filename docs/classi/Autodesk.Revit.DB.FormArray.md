---
title: FormArray
classe: Autodesk.Revit.DB.FormArray
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# FormArray

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEmpty { get; }` | `formArray.IsEmpty` | Boolean |
| `Form Item { get; set; }` | `formArray.Item` | Form |
| `Int32 Size { get; }` | `formArray.Size` | Int32 |
| `Void Append(Form)` | `formArray.Append(item)` | Void |
| `Void Clear()` | `formArray.Clear()` | Void |
| `FormArrayIterator ForwardIterator()` | `formArray.ForwardIterator()` | FormArrayIterator |
| `IEnumerator GetEnumerator()` | `formArray.GetEnumerator()` | IEnumerator |
| `Void Insert(Form, Int32)` | `formArray.Insert(item, index)` | Void |
| `FormArrayIterator ReverseIterator()` | `formArray.ReverseIterator()` | FormArrayIterator |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
