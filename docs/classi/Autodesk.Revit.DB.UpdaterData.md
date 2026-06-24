---
title: UpdaterData
classe: Autodesk.Revit.DB.UpdaterData
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# UpdaterData

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `updaterData.IsValidObject` | Boolean |
| `Void Dispose()` | `updaterData.Dispose()` | Void |
| `ICollection<ElementId> GetAddedElementIds()` | `updaterData.GetAddedElementIds()` | ICollection<ElementId> |
| `ICollection<ElementId> GetDeletedElementIds()` | `updaterData.GetDeletedElementIds()` | ICollection<ElementId> |
| `Document GetDocument()` | `updaterData.GetDocument()` | Document |
| `ICollection<ElementId> GetModifiedElementIds()` | `updaterData.GetModifiedElementIds()` | ICollection<ElementId> |
| `Boolean IsChangeTriggered(ElementId, ChangeType)` | `updaterData.IsChangeTriggered(id, type)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
