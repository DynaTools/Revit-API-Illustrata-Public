---
title: WorksharingUtils
classe: Autodesk.Revit.DB.WorksharingUtils
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# WorksharingUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `worksharingUtils.IsValidObject` | Boolean |
| `ISet<ElementId> CheckoutElements(Document, ISet<ElementId>, TransactWithCentralOptions)` | `WorksharingUtils.CheckoutElements(document, elementsToCheckout, options)` | ISet<ElementId> |
| `ICollection<ElementId> CheckoutElements(Document, ICollection<ElementId>)` | `WorksharingUtils.CheckoutElements(document, elementsToCheckout)` | ICollection<ElementId> |
| `ISet<WorksetId> CheckoutWorksets(Document, ISet<WorksetId>, TransactWithCentralOptions)` | `WorksharingUtils.CheckoutWorksets(document, worksetsToCheckout, options)` | ISet<WorksetId> |
| `ICollection<WorksetId> CheckoutWorksets(Document, ICollection<WorksetId>)` | `WorksharingUtils.CheckoutWorksets(document, worksetsToCheckout)` | ICollection<WorksetId> |
| `Void CreateNewLocal(ModelPath, ModelPath)` | `WorksharingUtils.CreateNewLocal(sourcePath, targetPath)` | Void |
| `Void Dispose()` | `worksharingUtils.Dispose()` | Void |
| `CheckoutStatus GetCheckoutStatus(Document, ElementId)` | `WorksharingUtils.GetCheckoutStatus(document, elementId)` | CheckoutStatus |
| `CheckoutStatus GetCheckoutStatus(Document, ElementId, String&)` | `WorksharingUtils.GetCheckoutStatus(document, elementId, owner)` | CheckoutStatus |
| `ModelUpdatesStatus GetModelUpdatesStatus(Document, ElementId)` | `WorksharingUtils.GetModelUpdatesStatus(document, elementId)` | ModelUpdatesStatus |
| `IList<WorksetPreview> GetUserWorksetInfo(ModelPath)` | `WorksharingUtils.GetUserWorksetInfo(path)` | IList<WorksetPreview> |
| `WorksharingTooltipInfo GetWorksharingTooltipInfo(Document, ElementId)` | `WorksharingUtils.GetWorksharingTooltipInfo(document, elementId)` | WorksharingTooltipInfo |
| `RelinquishedItems RelinquishOwnership(Document, RelinquishOptions, TransactWithCentralOptions)` | `WorksharingUtils.RelinquishOwnership(document, generalCategories, options)` | RelinquishedItems |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
