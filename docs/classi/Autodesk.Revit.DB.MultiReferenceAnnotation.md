---
title: MultiReferenceAnnotation
classe: Autodesk.Revit.DB.MultiReferenceAnnotation
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# MultiReferenceAnnotation

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId DimensionId { get; }` | `multiReferenceAnnotation.DimensionId` | ElementId |
| `ElementId TagId { get; }` | `multiReferenceAnnotation.TagId` | ElementId |
| `Boolean AreElementsValidForMultiReferenceAnnotation(Document, MultiReferenceAnnotationOptions)` | `MultiReferenceAnnotation.AreElementsValidForMultiReferenceAnnotation(document, options)` | Boolean |
| `Boolean AreReferencesValidForLinearDimension(Document, ElementId, MultiReferenceAnnotationOptions)` | `MultiReferenceAnnotation.AreReferencesValidForLinearDimension(document, ownerViewId, options)` | Boolean |
| `Boolean AreReferencesValidForLinearFixedDimension(Document, ElementId, MultiReferenceAnnotationOptions)` | `MultiReferenceAnnotation.AreReferencesValidForLinearFixedDimension(document, ownerViewId, options)` | Boolean |
| `MultiReferenceAnnotation Create(Document, ElementId, MultiReferenceAnnotationOptions)` | `MultiReferenceAnnotation.Create(document, ownerViewId, options)` | MultiReferenceAnnotation |
| `Boolean Is3DViewValidForDimension(Document, ElementId, MultiReferenceAnnotationOptions)` | `MultiReferenceAnnotation.Is3DViewValidForDimension(document, ownerViewId, options)` | Boolean |
| `Boolean IsLinearFixedDimensionDirectionValid(Document, ElementId, MultiReferenceAnnotationOptions)` | `MultiReferenceAnnotation.IsLinearFixedDimensionDirectionValid(document, viewId, options)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
