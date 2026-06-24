---
title: AssemblyViewUtils
classe: Autodesk.Revit.DB.AssemblyViewUtils
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 12
---

# AssemblyViewUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Void AcquireAssemblyViews(Document, ElementId, ElementId)` | `AssemblyViewUtils.AcquireAssemblyViews(document, sourceAssemblyInstanceId, targetAssemblyInstanceId)` | Void |
| `View3D Create3DOrthographic(Document, ElementId, ElementId, Boolean)` | `AssemblyViewUtils.Create3DOrthographic(document, assemblyInstanceId, viewTemplateId, isAssigned)` | View3D |
| `View3D Create3DOrthographic(Document, ElementId)` | `AssemblyViewUtils.Create3DOrthographic(document, assemblyInstanceId)` | View3D |
| `ViewSection CreateDetailSection(Document, ElementId, AssemblyDetailViewOrientation, ElementId, Boolean)` | `AssemblyViewUtils.CreateDetailSection(document, assemblyInstanceId, direction, viewTemplateId, isAssigned)` | ViewSection |
| `ViewSection CreateDetailSection(Document, ElementId, AssemblyDetailViewOrientation)` | `AssemblyViewUtils.CreateDetailSection(document, assemblyInstanceId, direction)` | ViewSection |
| `ViewSchedule CreateMaterialTakeoff(Document, ElementId, ElementId, Boolean)` | `AssemblyViewUtils.CreateMaterialTakeoff(document, assemblyInstanceId, viewTemplateId, isAssigned)` | ViewSchedule |
| `ViewSchedule CreateMaterialTakeoff(Document, ElementId)` | `AssemblyViewUtils.CreateMaterialTakeoff(document, assemblyInstanceId)` | ViewSchedule |
| `ViewSchedule CreatePartList(Document, ElementId, ElementId, Boolean)` | `AssemblyViewUtils.CreatePartList(document, assemblyInstanceId, viewTemplateId, isAssigned)` | ViewSchedule |
| `ViewSchedule CreatePartList(Document, ElementId)` | `AssemblyViewUtils.CreatePartList(document, assemblyInstanceId)` | ViewSchedule |
| `ViewSheet CreateSheet(Document, ElementId, ElementId)` | `AssemblyViewUtils.CreateSheet(document, assemblyInstanceId, titleBlockId)` | ViewSheet |
| `ViewSchedule CreateSingleCategorySchedule(Document, ElementId, ElementId, ElementId, Boolean)` | `AssemblyViewUtils.CreateSingleCategorySchedule(document, assemblyInstanceId, scheduleCategoryId, viewTemplateId, isAssigned)` | ViewSchedule |
| `ViewSchedule CreateSingleCategorySchedule(Document, ElementId, ElementId)` | `AssemblyViewUtils.CreateSingleCategorySchedule(document, assemblyInstanceId, scheduleCategoryId)` | ViewSchedule |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
