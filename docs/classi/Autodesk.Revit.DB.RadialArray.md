---
title: RadialArray
classe: Autodesk.Revit.DB.RadialArray
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.BaseArray
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 12
---

# RadialArray

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 NumMembers { get; set; }` | `radialArray.NumMembers` | Int32 |
| `ICollection<ElementId> ArrayElementsWithoutAssociation(Document, View, ICollection<ElementId>, Int32, Line, Double, ArrayAnchorMember)` | `RadialArray.ArrayElementsWithoutAssociation(aDoc, dBView, ids, count, axis, angle, anchorMember)` | ICollection<ElementId> |
| `ICollection<ElementId> ArrayElementWithoutAssociation(Document, View, ElementId, Int32, Line, Double, ArrayAnchorMember)` | `RadialArray.ArrayElementWithoutAssociation(aDoc, dBView, id, count, axis, angle, anchorMember)` | ICollection<ElementId> |
| `RadialArray Create(Document, View, ElementId, Int32, Line, Double, ArrayAnchorMember)` | `RadialArray.Create(aDoc, dBView, id, count, axis, angle, anchorMember)` | RadialArray |
| `RadialArray Create(Document, View, ICollection<ElementId>, Int32, Line, Double, ArrayAnchorMember)` | `RadialArray.Create(aDoc, dBView, ids, count, axis, angle, anchorMember)` | RadialArray |
| `ICollection<ElementId> GetCopiedMemberIds()` | `radialArray.GetCopiedMemberIds()` | ICollection<ElementId> |
| `Int32 GetMinimumSize(Document)` | `RadialArray.GetMinimumSize(document)` | Int32 |
| `Int32 GetNumberOfMembersIncludingPlaceholders()` | `radialArray.GetNumberOfMembersIncludingPlaceholders()` | Int32 |
| `ICollection<ElementId> GetOriginalMemberIds()` | `radialArray.GetOriginalMemberIds()` | ICollection<ElementId> |
| `Boolean IsRotationAngleValid(Double)` | `RadialArray.IsRotationAngleValid(angle)` | Boolean |
| `Boolean IsValidArraySize(Int32)` | `RadialArray.IsValidArraySize(count)` | Boolean |
| `Boolean IsValidNumberOfMembers(Int32, Document)` | `RadialArray.IsValidNumberOfMembers(count, pADoc)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
