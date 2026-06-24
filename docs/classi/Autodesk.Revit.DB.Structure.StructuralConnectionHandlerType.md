---
title: StructuralConnectionHandlerType
classe: Autodesk.Revit.DB.Structure.StructuralConnectionHandlerType
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.ElementType
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# StructuralConnectionHandlerType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Guid ConnectionGuid { get; }` | `structuralConnectionHandlerType.ConnectionGuid` | Guid |
| `Void AddElementsToCustomConnection(StructuralConnectionHandler, IList<Reference>)` | `StructuralConnectionHandlerType.AddElementsToCustomConnection(structuralConnectionHandler, references)` | Void |
| `StructuralConnectionHandlerType Create(Document, String, Guid, String, ElementId, IList<ConnectionInputPointInfo>)` | `StructuralConnectionHandlerType.Create(pADoc, name, guid, familyName, categoryId, inputPointsInfo)` | StructuralConnectionHandlerType |
| `StructuralConnectionHandlerType Create(Document, String, Guid, String, ElementId)` | `StructuralConnectionHandlerType.Create(pADoc, name, guid, familyName, categoryId)` | StructuralConnectionHandlerType |
| `StructuralConnectionHandlerType Create(Document, String, Guid, String)` | `StructuralConnectionHandlerType.Create(pADoc, name, guid, familyName)` | StructuralConnectionHandlerType |
| `ElementId CreateDefaultStructuralConnectionHandlerType(Document)` | `StructuralConnectionHandlerType.CreateDefaultStructuralConnectionHandlerType(pADoc)` | ElementId |
| `ElementId FindGenericConnectionType(Document)` | `StructuralConnectionHandlerType.FindGenericConnectionType(doc)` | ElementId |
| `ElementId GetDefaultConnectionHandlerType(Document)` | `StructuralConnectionHandlerType.GetDefaultConnectionHandlerType(pADoc)` | ElementId |
| `Boolean IsCustom()` | `structuralConnectionHandlerType.IsCustom()` | Boolean |
| `Boolean IsDetailed()` | `structuralConnectionHandlerType.IsDetailed()` | Boolean |
| `Boolean IsGeneric()` | `structuralConnectionHandlerType.IsGeneric()` | Boolean |
| `Boolean IsTypeNameValidForCustomConnection(Document, String)` | `StructuralConnectionHandlerType.IsTypeNameValidForCustomConnection(document, typeName)` | Boolean |
| `Void RemoveMainSubelementsFromCustomConnection(StructuralConnectionHandler, IList<Subelement>)` | `StructuralConnectionHandlerType.RemoveMainSubelementsFromCustomConnection(structuralConnectionHandler, subelements)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
