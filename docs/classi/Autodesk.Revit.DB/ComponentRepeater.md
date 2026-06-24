---
title: ComponentRepeater
classe: Autodesk.Revit.DB.ComponentRepeater
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# ComponentRepeater

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId DefaultFamilyType { get; set; }` | `componentRepeater.DefaultFamilyType` | ElementId |
| `Int32 DimensionCount { get; }` | `componentRepeater.DimensionCount` | Int32 |
| `Boolean CanElementBeRepeated(Document, ElementId)` | `ComponentRepeater.CanElementBeRepeated(ADoc, elementId)` | Boolean |
| `IEnumerator<ComponentRepeaterSlot> GetEnumerator()` | `componentRepeater.GetEnumerator()` | IEnumerator<ComponentRepeaterSlot> |
| `Boolean IsTypeValidForRepeater(ElementId)` | `componentRepeater.IsTypeValidForRepeater(typeId)` | Boolean |
| `ISet<ElementId> RemoveRepeaters(Document, ISet<ElementId>)` | `ComponentRepeater.RemoveRepeaters(document, elementIds)` | ISet<ElementId> |
| `IList<ComponentRepeater> RepeatElements(Document, ICollection<ElementId>)` | `ComponentRepeater.RepeatElements(document, elementIds)` | IList<ComponentRepeater> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
