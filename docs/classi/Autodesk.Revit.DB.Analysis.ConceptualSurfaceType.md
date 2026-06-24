---
title: ConceptualSurfaceType
classe: Autodesk.Revit.DB.Analysis.ConceptualSurfaceType
namespace: Autodesk.Revit.DB.Analysis
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 5
---

# ConceptualSurfaceType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId DefaultConstructionTypeId { get; set; }` | `conceptualSurfaceType.DefaultConstructionTypeId` | ElementId |
| `ElementId MassSubCategoryId { get; }` | `conceptualSurfaceType.MassSubCategoryId` | ElementId |
| `IList<ElementId> GetAllMassSubCategoryIds()` | `ConceptualSurfaceType.GetAllMassSubCategoryIds()` | IList<ElementId> |
| `ConceptualSurfaceType GetByMassSubCategoryId(Document, ElementId)` | `ConceptualSurfaceType.GetByMassSubCategoryId(cda, massSubCategoryId)` | ConceptualSurfaceType |
| `ICollection<ElementId> GetConstructionTypeIds()` | `conceptualSurfaceType.GetConstructionTypeIds()` | ICollection<ElementId> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
