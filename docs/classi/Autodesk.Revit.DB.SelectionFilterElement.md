---
title: SelectionFilterElement
classe: Autodesk.Revit.DB.SelectionFilterElement
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.FilterElement
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# SelectionFilterElement

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Void AddSet(ICollection<ElementId>)` | `selectionFilterElement.AddSet(ids)` | Void |
| `Void AddSingle(ElementId)` | `selectionFilterElement.AddSingle(id)` | Void |
| `Void Clear()` | `selectionFilterElement.Clear()` | Void |
| `Boolean Contains(ElementId)` | `selectionFilterElement.Contains(id)` | Boolean |
| `SelectionFilterElement Create(Document, String)` | `SelectionFilterElement.Create(document, name)` | SelectionFilterElement |
| `ICollection<ElementId> GetElementIds()` | `selectionFilterElement.GetElementIds()` | ICollection<ElementId> |
| `Boolean IsEmpty()` | `selectionFilterElement.IsEmpty()` | Boolean |
| `Int32 RemoveSet(ICollection<ElementId>)` | `selectionFilterElement.RemoveSet(ids)` | Int32 |
| `Void RemoveSingle(ElementId)` | `selectionFilterElement.RemoveSingle(id)` | Void |
| `Void SetElementIds(ICollection<ElementId>)` | `selectionFilterElement.SetElementIds(ids)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
