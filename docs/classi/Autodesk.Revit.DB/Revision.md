---
title: Revision
classe: Autodesk.Revit.DB.Revision
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 14
---

# Revision

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String Description { get; set; }` | `revision.Description` | String |
| `Boolean Issued { get; set; }` | `revision.Issued` | Boolean |
| `String IssuedBy { get; set; }` | `revision.IssuedBy` | String |
| `String IssuedTo { get; set; }` | `revision.IssuedTo` | String |
| `String RevisionDate { get; set; }` | `revision.RevisionDate` | String |
| `String RevisionNumber { get; }` | `revision.RevisionNumber` | String |
| `ElementId RevisionNumberingSequenceId { get; set; }` | `revision.RevisionNumberingSequenceId` | ElementId |
| `Int32 SequenceNumber { get; }` | `revision.SequenceNumber` | Int32 |
| `RevisionVisibility Visibility { get; set; }` | `revision.Visibility` | RevisionVisibility |
| `ISet<ElementId> CombineWithNext(Document, ElementId)` | `Revision.CombineWithNext(document, revisionId)` | ISet<ElementId> |
| `ISet<ElementId> CombineWithPrevious(Document, ElementId)` | `Revision.CombineWithPrevious(document, revisionId)` | ISet<ElementId> |
| `Revision Create(Document)` | `Revision.Create(document)` | Revision |
| `IList<ElementId> GetAllRevisionIds(Document)` | `Revision.GetAllRevisionIds(document)` | IList<ElementId> |
| `Void ReorderRevisionSequence(Document, IList<ElementId>)` | `Revision.ReorderRevisionSequence(document, newSequence)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
