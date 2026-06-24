---
title: BindingMap
classe: Autodesk.Revit.DB.BindingMap
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.DefinitionBindingMap
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# BindingMap

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Binding Item { get; set; }` | `bindingMap.Item` | Binding |
| `Void Clear()` | `bindingMap.Clear()` | Void |
| `Boolean Contains(Definition)` | `bindingMap.Contains(key)` | Boolean |
| `Int32 Erase(Definition)` | `bindingMap.Erase(key)` | Int32 |
| `Boolean Insert(Definition, Binding, ForgeTypeId)` | `bindingMap.Insert(key, item, groupTypeId)` | Boolean |
| `Boolean Insert(Definition, Binding)` | `bindingMap.Insert(key, item)` | Boolean |
| `Boolean ReInsert(Definition, Binding, ForgeTypeId)` | `bindingMap.ReInsert(key, item, groupTypeId)` | Boolean |
| `Boolean ReInsert(Definition, Binding)` | `bindingMap.ReInsert(key, item)` | Boolean |
| `Boolean Remove(Definition)` | `bindingMap.Remove(key)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
