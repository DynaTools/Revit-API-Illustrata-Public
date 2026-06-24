---
title: DocumentChangedEventArgs
classe: Autodesk.Revit.DB.Events.DocumentChangedEventArgs
namespace: Autodesk.Revit.DB.Events
eredita: Autodesk.Revit.DB.Events.RevitAPISingleEventArgs
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# DocumentChangedEventArgs

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `UndoOperation Operation { get; }` | `documentChangedEventArgs.Operation` | UndoOperation |
| `ICollection<ElementId> GetAddedElementIds(ElementFilter)` | `documentChangedEventArgs.GetAddedElementIds(filter)` | ICollection<ElementId> |
| `ICollection<ElementId> GetAddedElementIds()` | `documentChangedEventArgs.GetAddedElementIds()` | ICollection<ElementId> |
| `ICollection<ElementId> GetDeletedElementIds()` | `documentChangedEventArgs.GetDeletedElementIds()` | ICollection<ElementId> |
| `Document GetDocument()` | `documentChangedEventArgs.GetDocument()` | Document |
| `ICollection<ElementId> GetModifiedElementIds(ElementFilter)` | `documentChangedEventArgs.GetModifiedElementIds(filter)` | ICollection<ElementId> |
| `ICollection<ElementId> GetModifiedElementIds()` | `documentChangedEventArgs.GetModifiedElementIds()` | ICollection<ElementId> |
| `IList<String> GetTransactionNames()` | `documentChangedEventArgs.GetTransactionNames()` | IList<String> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
