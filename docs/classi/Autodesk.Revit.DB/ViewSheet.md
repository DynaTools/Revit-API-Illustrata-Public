---
title: ViewSheet
classe: Autodesk.Revit.DB.ViewSheet
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.View
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 18
---

# ViewSheet

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsPlaceholder { get; }` | `viewSheet.IsPlaceholder` | Boolean |
| `ElementId SheetCollectionId { get; set; }` | `viewSheet.SheetCollectionId` | ElementId |
| `String SheetNumber { get; set; }` | `viewSheet.SheetNumber` | String |
| `Boolean CanBeDuplicated(SheetDuplicateOption)` | `viewSheet.CanBeDuplicated(duplicateOption)` | Boolean |
| `Void ConvertToRealSheet(ElementId)` | `viewSheet.ConvertToRealSheet(titleBlockTypeId)` | Void |
| `ViewSheet Create(Document, ElementId)` | `ViewSheet.Create(document, titleBlockTypeId)` | ViewSheet |
| `ViewSheet CreatePlaceholder(Document)` | `ViewSheet.CreatePlaceholder(aDoc)` | ViewSheet |
| `Void DeleteViewport(Viewport)` | `viewSheet.DeleteViewport(viewport)` | Void |
| `ElementId Duplicate(SheetDuplicateOption)` | `viewSheet.Duplicate(duplicateOption)` | ElementId |
| `ICollection<ElementId> GetAdditionalRevisionIds()` | `viewSheet.GetAdditionalRevisionIds()` | ICollection<ElementId> |
| `ISet<ElementId> GetAllPlacedViews()` | `viewSheet.GetAllPlacedViews()` | ISet<ElementId> |
| `ISet<ElementId> GetAllRevisionCloudIds()` | `viewSheet.GetAllRevisionCloudIds()` | ISet<ElementId> |
| `IList<ElementId> GetAllRevisionIds()` | `viewSheet.GetAllRevisionIds()` | IList<ElementId> |
| `ICollection<ElementId> GetAllViewports()` | `viewSheet.GetAllViewports()` | ICollection<ElementId> |
| `ElementId GetCurrentRevision()` | `viewSheet.GetCurrentRevision()` | ElementId |
| `String GetRevisionCloudNumberOnSheet(ElementId)` | `viewSheet.GetRevisionCloudNumberOnSheet(revisionCloudId)` | String |
| `String GetRevisionNumberOnSheet(ElementId)` | `viewSheet.GetRevisionNumberOnSheet(revisionId)` | String |
| `Void SetAdditionalRevisionIds(ICollection<ElementId>)` | `viewSheet.SetAdditionalRevisionIds(projectRevisionIds)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
