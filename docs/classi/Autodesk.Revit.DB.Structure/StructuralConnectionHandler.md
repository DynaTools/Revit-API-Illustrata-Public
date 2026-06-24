---
title: StructuralConnectionHandler
classe: Autodesk.Revit.DB.Structure.StructuralConnectionHandler
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 20
---

# StructuralConnectionHandler

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId ApprovalTypeId { get; set; }` | `structuralConnectionHandler.ApprovalTypeId` | ElementId |
| `StructuralConnectionCodeCheckingStatus CodeCheckingStatus { get; set; }` | `structuralConnectionHandler.CodeCheckingStatus` | StructuralConnectionCodeCheckingStatus |
| `Boolean OverrideTypeParams { get; set; }` | `structuralConnectionHandler.OverrideTypeParams` | Boolean |
| `Int32 SingleElementEndIndex { get; set; }` | `structuralConnectionHandler.SingleElementEndIndex` | Int32 |
| `Void AddElementIds(IList<ElementId>)` | `structuralConnectionHandler.AddElementIds(elemIds)` | Void |
| `Void AddReferences(Document, IList<Reference>)` | `structuralConnectionHandler.AddReferences(document, picks)` | Void |
| `StructuralConnectionHandler Create(Document, IList<ElementId>, ElementId, IList<ConnectionInputPoint>)` | `StructuralConnectionHandler.Create(document, idsToConnect, typeId, additionalInputPoints)` | StructuralConnectionHandler |
| `StructuralConnectionHandler Create(Document, IList<ElementId>, String)` | `StructuralConnectionHandler.Create(document, elementIds, typeName)` | StructuralConnectionHandler |
| `StructuralConnectionHandler Create(Document, IList<ElementId>, ElementId)` | `StructuralConnectionHandler.Create(document, idsToConnect, typeId)` | StructuralConnectionHandler |
| `StructuralConnectionHandler CreateGenericConnection(Document, IList<ElementId>)` | `StructuralConnectionHandler.CreateGenericConnection(document, idsToConnect)` | StructuralConnectionHandler |
| `IList<ElementId> GetConnectedElementIds()` | `structuralConnectionHandler.GetConnectedElementIds()` | IList<ElementId> |
| `ConnectionInputPoint GetInputPoint(Guid)` | `structuralConnectionHandler.GetInputPoint(id)` | ConnectionInputPoint |
| `IList<ConnectionInputPoint> GetInputPoints()` | `structuralConnectionHandler.GetInputPoints()` | IList<ConnectionInputPoint> |
| `IList<Reference> GetInputReferences()` | `structuralConnectionHandler.GetInputReferences()` | IList<Reference> |
| `XYZ GetOrigin()` | `structuralConnectionHandler.GetOrigin()` | XYZ |
| `Boolean IsCustom()` | `structuralConnectionHandler.IsCustom()` | Boolean |
| `Boolean IsDetailed()` | `structuralConnectionHandler.IsDetailed()` | Boolean |
| `Void RemoveElementIds(IList<ElementId>)` | `structuralConnectionHandler.RemoveElementIds(elemIds)` | Void |
| `Void RemoveReferences(IList<Reference>)` | `structuralConnectionHandler.RemoveReferences(picks)` | Void |
| `Void SetDefaultElementOrder()` | `structuralConnectionHandler.SetDefaultElementOrder()` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
