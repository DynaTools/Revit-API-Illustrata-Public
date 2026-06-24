---
title: MultiReferenceAnnotationOptions
classe: Autodesk.Revit.DB.MultiReferenceAnnotationOptions
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 16
---

# MultiReferenceAnnotationOptions

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ DimensionLineDirection { get; set; }` | `multiReferenceAnnotationOptions.DimensionLineDirection` | XYZ |
| `XYZ DimensionLineOrigin { get; set; }` | `multiReferenceAnnotationOptions.DimensionLineOrigin` | XYZ |
| `XYZ DimensionPlaneNormal { get; set; }` | `multiReferenceAnnotationOptions.DimensionPlaneNormal` | XYZ |
| `DimensionStyleType DimensionStyleType { get; set; }` | `multiReferenceAnnotationOptions.DimensionStyleType` | DimensionStyleType |
| `Boolean IsValidObject { get; }` | `multiReferenceAnnotationOptions.IsValidObject` | Boolean |
| `MultiReferenceAnnotationType MultiReferenceAnnotationType { get; }` | `multiReferenceAnnotationOptions.MultiReferenceAnnotationType` | MultiReferenceAnnotationType |
| `Boolean TagHasLeader { get; set; }` | `multiReferenceAnnotationOptions.TagHasLeader` | Boolean |
| `XYZ TagHeadPosition { get; set; }` | `multiReferenceAnnotationOptions.TagHeadPosition` | XYZ |
| `Void Dispose()` | `multiReferenceAnnotationOptions.Dispose()` | Void |
| `Boolean ElementsMatchReferenceCategory(ICollection<ElementId>)` | `multiReferenceAnnotationOptions.ElementsMatchReferenceCategory(elements)` | Boolean |
| `IList<Reference> GetAdditionalReferencesToDimension()` | `multiReferenceAnnotationOptions.GetAdditionalReferencesToDimension()` | IList<Reference> |
| `ICollection<ElementId> GetElementsToDimension()` | `multiReferenceAnnotationOptions.GetElementsToDimension()` | ICollection<ElementId> |
| `Boolean IsAllowedDimensionStyleType(DimensionStyleType)` | `multiReferenceAnnotationOptions.IsAllowedDimensionStyleType(dimensionStyleType)` | Boolean |
| `Boolean ReferencesDontMatchReferenceCategory(IList<Reference>)` | `multiReferenceAnnotationOptions.ReferencesDontMatchReferenceCategory(references)` | Boolean |
| `Void SetAdditionalReferencesToDimension(IList<Reference>)` | `multiReferenceAnnotationOptions.SetAdditionalReferencesToDimension(referencesToDimension)` | Void |
| `Void SetElementsToDimension(ICollection<ElementId>)` | `multiReferenceAnnotationOptions.SetElementsToDimension(elementsToDimension)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
