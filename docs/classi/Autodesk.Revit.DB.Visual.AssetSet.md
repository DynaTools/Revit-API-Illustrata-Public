---
title: AssetSet
classe: Autodesk.Revit.DB.Visual.AssetSet
namespace: Autodesk.Revit.DB.Visual
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# AssetSet

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEmpty { get; }` | `assetSet.IsEmpty` | Boolean |
| `Int32 Size { get; }` | `assetSet.Size` | Int32 |
| `Void Clear()` | `assetSet.Clear()` | Void |
| `Boolean Contains(Asset)` | `assetSet.Contains(item)` | Boolean |
| `Int32 Erase(Asset)` | `assetSet.Erase(item)` | Int32 |
| `AssetSetIterator ForwardIterator()` | `assetSet.ForwardIterator()` | AssetSetIterator |
| `IEnumerator GetEnumerator()` | `assetSet.GetEnumerator()` | IEnumerator |
| `Boolean Insert(Asset)` | `assetSet.Insert(item)` | Boolean |
| `AssetSetIterator ReverseIterator()` | `assetSet.ReverseIterator()` | AssetSetIterator |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
