---
title: LinearArray
classe: Autodesk.Revit.DB.LinearArray
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.BaseArray
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 12
---

# LinearArray

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 NumMembers { get; set; }` | `linearArray.NumMembers` | Int32 |
| `ICollection<ElementId> ArrayElementsWithoutAssociation(Document, View, ICollection<ElementId>, Int32, XYZ, ArrayAnchorMember)` | `LinearArray.ArrayElementsWithoutAssociation(aDoc, dBView, ids, count, translationToAnchorMember, anchorMember)` | ICollection<ElementId> |
| `ICollection<ElementId> ArrayElementWithoutAssociation(Document, View, ElementId, Int32, XYZ, ArrayAnchorMember)` | `LinearArray.ArrayElementWithoutAssociation(aDoc, dBView, id, count, translationToAnchorMember, anchorMember)` | ICollection<ElementId> |
| `LinearArray Create(Document, View, ElementId, Int32, XYZ, ArrayAnchorMember)` | `LinearArray.Create(aDoc, dBView, id, count, translationToAnchorMember, anchorMember)` | LinearArray |
| `LinearArray Create(Document, View, ICollection<ElementId>, Int32, XYZ, ArrayAnchorMember)` | `LinearArray.Create(aDoc, dBView, ids, count, translationToAnchorMember, anchorMember)` | LinearArray |
| `ICollection<ElementId> GetCopiedMemberIds()` | `linearArray.GetCopiedMemberIds()` | ICollection<ElementId> |
| `Int32 GetMinimumSize(Document)` | `LinearArray.GetMinimumSize(document)` | Int32 |
| `Int32 GetNumberOfMembersIncludingPlaceholders()` | `linearArray.GetNumberOfMembersIncludingPlaceholders()` | Int32 |
| `ICollection<ElementId> GetOriginalMemberIds()` | `linearArray.GetOriginalMemberIds()` | ICollection<ElementId> |
| `Boolean IsElementArrayable(Document, ElementId)` | `LinearArray.IsElementArrayable(aDoc, id)` | Boolean |
| `Boolean IsValidArraySize(Int32)` | `LinearArray.IsValidArraySize(count)` | Boolean |
| `Boolean IsValidNumberOfMembers(Int32, Document)` | `LinearArray.IsValidNumberOfMembers(count, pADoc)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
