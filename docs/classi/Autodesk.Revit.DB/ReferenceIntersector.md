---
title: ReferenceIntersector
classe: Autodesk.Revit.DB.ReferenceIntersector
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# ReferenceIntersector

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean FindReferencesInRevitLinks { get; set; }` | `referenceIntersector.FindReferencesInRevitLinks` | Boolean |
| `Boolean IsValidObject { get; }` | `referenceIntersector.IsValidObject` | Boolean |
| `FindReferenceTarget TargetType { get; set; }` | `referenceIntersector.TargetType` | FindReferenceTarget |
| `ElementId ViewId { get; set; }` | `referenceIntersector.ViewId` | ElementId |
| `Void Dispose()` | `referenceIntersector.Dispose()` | Void |
| `IList<ReferenceWithContext> Find(XYZ, XYZ)` | `referenceIntersector.Find(origin, direction)` | IList<ReferenceWithContext> |
| `ReferenceWithContext FindNearest(XYZ, XYZ)` | `referenceIntersector.FindNearest(origin, direction)` | ReferenceWithContext |
| `ElementFilter GetFilter()` | `referenceIntersector.GetFilter()` | ElementFilter |
| `ICollection<ElementId> GetTargetElementIds()` | `referenceIntersector.GetTargetElementIds()` | ICollection<ElementId> |
| `Void SetFilter(ElementFilter)` | `referenceIntersector.SetFilter(filter)` | Void |
| `Void SetTargetElementIds(ICollection<ElementId>)` | `referenceIntersector.SetTargetElementIds(elementIds)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
