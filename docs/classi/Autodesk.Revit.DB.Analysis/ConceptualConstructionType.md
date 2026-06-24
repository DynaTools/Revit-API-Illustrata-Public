---
title: ConceptualConstructionType
classe: Autodesk.Revit.DB.Analysis.ConceptualConstructionType
namespace: Autodesk.Revit.DB.Analysis
eredita: Autodesk.Revit.DB.ElementType
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 14
---

# ConceptualConstructionType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId MassSurfaceSubCategoryId { get; }` | `conceptualConstructionType.MassSurfaceSubCategoryId` | ElementId |
| `ElementId MaterialId { get; set; }` | `conceptualConstructionType.MaterialId` | ElementId |
| `ICollection<ElementId> GetAllConceptualConstructionsForCategory(Document, ElementId)` | `ConceptualConstructionType.GetAllConceptualConstructionsForCategory(ccda, massSubCategoryId)` | ICollection<ElementId> |
| `ElementId GetFloorOrSlabConstructionType(Document, ConceptualConstructionFloorSlabType)` | `ConceptualConstructionType.GetFloorOrSlabConstructionType(ccda, typeEnum)` | ElementId |
| `Int32 GetGBSId(ElementId)` | `conceptualConstructionType.GetGBSId(massSurfaceSubCategoryId)` | Int32 |
| `ElementId GetOpeningConstructionType(Document, ConceptualConstructionOpeningType)` | `ConceptualConstructionType.GetOpeningConstructionType(ccda, typeEnum)` | ElementId |
| `ElementId GetRoofConstructionType(Document, ConceptualConstructionRoofType)` | `ConceptualConstructionType.GetRoofConstructionType(ccda, typeEnum)` | ElementId |
| `ElementId GetShadeConstructionType(Document, ConceptualConstructionShadeType)` | `ConceptualConstructionType.GetShadeConstructionType(ccda, typeEnum)` | ElementId |
| `ElementId GetWallConstructionType(Document, ConceptualConstructionWallType)` | `ConceptualConstructionType.GetWallConstructionType(ccda, typeEnum)` | ElementId |
| `ElementId GetWindowOrSkylightConstructionType(Document, ConceptualConstructionWindowSkylightType)` | `ConceptualConstructionType.GetWindowOrSkylightConstructionType(ccda, typeEnum)` | ElementId |
| `Boolean IsValidConceptualConstructionId(Document, ElementId)` | `ConceptualConstructionType.IsValidConceptualConstructionId(ccda, constructionTypeId)` | Boolean |
| `Boolean IsValidConceptualConstructionIdForCategory(Document, ElementId, ElementId)` | `ConceptualConstructionType.IsValidConceptualConstructionIdForCategory(ccda, constructionTypeId, massSubcategoryId)` | Boolean |
| `Boolean IsValidSubcategoryForMassSurfaceDatas(ElementId)` | `ConceptualConstructionType.IsValidSubcategoryForMassSurfaceDatas(massSubCategoryId)` | Boolean |
| `Boolean IsValidSurfaceSubcategoryForConstruction(ElementId)` | `conceptualConstructionType.IsValidSurfaceSubcategoryForConstruction(massSurfaceSubcategoryId)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
