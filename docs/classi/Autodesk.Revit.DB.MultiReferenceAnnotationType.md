---
title: MultiReferenceAnnotationType
classe: Autodesk.Revit.DB.MultiReferenceAnnotationType
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.ElementType
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# MultiReferenceAnnotationType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId DimensionStyleId { get; set; }` | `multiReferenceAnnotationType.DimensionStyleId` | ElementId |
| `Boolean GroupTagHeads { get; set; }` | `multiReferenceAnnotationType.GroupTagHeads` | Boolean |
| `ElementId ReferenceCategoryId { get; }` | `multiReferenceAnnotationType.ReferenceCategoryId` | ElementId |
| `Boolean ShowDimensionText { get; set; }` | `multiReferenceAnnotationType.ShowDimensionText` | Boolean |
| `ElementId TagTypeId { get; set; }` | `multiReferenceAnnotationType.TagTypeId` | ElementId |
| `MultiReferenceAnnotationType CreateDefault(Document)` | `MultiReferenceAnnotationType.CreateDefault(document)` | MultiReferenceAnnotationType |
| `ElementId GetAllowedTagCategory()` | `multiReferenceAnnotationType.GetAllowedTagCategory()` | ElementId |
| `Boolean IsAllowedDimensionStyle(ElementId)` | `multiReferenceAnnotationType.IsAllowedDimensionStyle(dimensionStyleId)` | Boolean |
| `Boolean IsAllowedReferenceCategory(ElementId)` | `multiReferenceAnnotationType.IsAllowedReferenceCategory(referenceCategoryId)` | Boolean |
| `Boolean IsAllowedTagCategory(ElementId)` | `MultiReferenceAnnotationType.IsAllowedTagCategory(tagCategoryId)` | Boolean |
| `Boolean IsAllowedTagType(ElementId)` | `multiReferenceAnnotationType.IsAllowedTagType(tagTypeId)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
