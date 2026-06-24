---
title: DefinitionBindingMap
classe: Autodesk.Revit.DB.DefinitionBindingMap
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# DefinitionBindingMap

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEmpty { get; }` | `definitionBindingMap.IsEmpty` | Boolean |
| `Binding Item { get; set; }` | `definitionBindingMap.Item` | Binding |
| `Int32 Size { get; }` | `definitionBindingMap.Size` | Int32 |
| `Void Clear()` | `definitionBindingMap.Clear()` | Void |
| `Boolean Contains(Definition)` | `definitionBindingMap.Contains(key)` | Boolean |
| `Int32 Erase(Definition)` | `definitionBindingMap.Erase(key)` | Int32 |
| `DefinitionBindingMapIterator ForwardIterator()` | `definitionBindingMap.ForwardIterator()` | DefinitionBindingMapIterator |
| `IEnumerator GetEnumerator()` | `definitionBindingMap.GetEnumerator()` | IEnumerator |
| `Boolean Insert(Definition, Binding)` | `definitionBindingMap.Insert(key, item)` | Boolean |
| `DefinitionBindingMapIterator ReverseIterator()` | `definitionBindingMap.ReverseIterator()` | DefinitionBindingMapIterator |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
