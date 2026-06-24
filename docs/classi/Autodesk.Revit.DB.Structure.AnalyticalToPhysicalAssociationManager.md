---
title: AnalyticalToPhysicalAssociationManager
classe: Autodesk.Revit.DB.Structure.AnalyticalToPhysicalAssociationManager
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# AnalyticalToPhysicalAssociationManager

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean EnableAssistedAssociation { get; set; }` | `AnalyticalToPhysicalAssociationManager.EnableAssistedAssociation` | Boolean |
| `Void AddAssociation(ISet<ElementId>, ISet<ElementId>)` | `analyticalToPhysicalAssociationManager.AddAssociation(analyticalElementIds, physicalElementIds)` | Void |
| `Void AddAssociation(ElementId, ElementId)` | `analyticalToPhysicalAssociationManager.AddAssociation(analyticalElementId, physicalElementId)` | Void |
| `AnalyticalToPhysicalAssociationManager GetAnalyticalToPhysicalAssociationManager(Document)` | `AnalyticalToPhysicalAssociationManager.GetAnalyticalToPhysicalAssociationManager(doc)` | AnalyticalToPhysicalAssociationManager |
| `ElementId GetAssociatedElementId(ElementId)` | `analyticalToPhysicalAssociationManager.GetAssociatedElementId(elementId)` | ElementId |
| `ISet<ElementId> GetAssociatedElementIds(ElementId)` | `analyticalToPhysicalAssociationManager.GetAssociatedElementIds(elementId)` | ISet<ElementId> |
| `Boolean HasAssociation(ElementId)` | `analyticalToPhysicalAssociationManager.HasAssociation(id)` | Boolean |
| `Boolean IsAnalyticalElement(Document, ElementId)` | `AnalyticalToPhysicalAssociationManager.IsAnalyticalElement(doc, id)` | Boolean |
| `Boolean IsPhysicalElement(Document, ElementId)` | `AnalyticalToPhysicalAssociationManager.IsPhysicalElement(doc, id)` | Boolean |
| `Void RemoveAssociation(ElementId)` | `analyticalToPhysicalAssociationManager.RemoveAssociation(id)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
