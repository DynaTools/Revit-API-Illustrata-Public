---
title: CurveArray
classe: Autodesk.Revit.DB.CurveArray
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# CurveArray

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEmpty { get; }` | `curveArray.IsEmpty` | Boolean |
| `Curve Item { get; set; }` | `curveArray.Item` | Curve |
| `Int32 Size { get; }` | `curveArray.Size` | Int32 |
| `Void Append(Curve)` | `curveArray.Append(item)` | Void |
| `Void Clear()` | `curveArray.Clear()` | Void |
| `CurveArrayIterator ForwardIterator()` | `curveArray.ForwardIterator()` | CurveArrayIterator |
| `IEnumerator GetEnumerator()` | `curveArray.GetEnumerator()` | IEnumerator |
| `Void Insert(Curve, Int32)` | `curveArray.Insert(item, index)` | Void |
| `CurveArrayIterator ReverseIterator()` | `curveArray.ReverseIterator()` | CurveArrayIterator |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
