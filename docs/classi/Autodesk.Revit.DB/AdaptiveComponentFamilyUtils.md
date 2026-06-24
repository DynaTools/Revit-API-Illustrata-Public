---
title: AdaptiveComponentFamilyUtils
classe: Autodesk.Revit.DB.AdaptiveComponentFamilyUtils
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 14
---

# AdaptiveComponentFamilyUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 GetNumberOfAdaptivePoints(Family)` | `AdaptiveComponentFamilyUtils.GetNumberOfAdaptivePoints(family)` | Int32 |
| `Int32 GetNumberOfPlacementPoints(Family)` | `AdaptiveComponentFamilyUtils.GetNumberOfPlacementPoints(family)` | Int32 |
| `Int32 GetNumberOfShapeHandlePoints(Family)` | `AdaptiveComponentFamilyUtils.GetNumberOfShapeHandlePoints(family)` | Int32 |
| `Int32 GetPlacementNumber(Document, ElementId)` | `AdaptiveComponentFamilyUtils.GetPlacementNumber(doc, refPointId)` | Int32 |
| `AdaptivePointConstraintType GetPointConstraintType(Document, ElementId)` | `AdaptiveComponentFamilyUtils.GetPointConstraintType(doc, refPointId)` | AdaptivePointConstraintType |
| `AdaptivePointOrientationType GetPointOrientationType(Document, ElementId)` | `AdaptiveComponentFamilyUtils.GetPointOrientationType(doc, refPointId)` | AdaptivePointOrientationType |
| `Boolean IsAdaptiveComponentFamily(Family)` | `AdaptiveComponentFamilyUtils.IsAdaptiveComponentFamily(family)` | Boolean |
| `Boolean IsAdaptivePlacementPoint(Document, ElementId)` | `AdaptiveComponentFamilyUtils.IsAdaptivePlacementPoint(doc, refPointId)` | Boolean |
| `Boolean IsAdaptivePoint(Document, ElementId)` | `AdaptiveComponentFamilyUtils.IsAdaptivePoint(doc, refPointId)` | Boolean |
| `Boolean IsAdaptiveShapeHandlePoint(Document, ElementId)` | `AdaptiveComponentFamilyUtils.IsAdaptiveShapeHandlePoint(doc, refPointId)` | Boolean |
| `Void MakeAdaptivePoint(Document, ElementId, AdaptivePointType)` | `AdaptiveComponentFamilyUtils.MakeAdaptivePoint(doc, refPointId, type)` | Void |
| `Void SetPlacementNumber(Document, ElementId, Int32)` | `AdaptiveComponentFamilyUtils.SetPlacementNumber(doc, refPointId, placementNumber)` | Void |
| `Void SetPointConstraintType(Document, ElementId, AdaptivePointConstraintType)` | `AdaptiveComponentFamilyUtils.SetPointConstraintType(doc, refPointId, constraintType)` | Void |
| `Void SetPointOrientationType(Document, ElementId, AdaptivePointOrientationType)` | `AdaptiveComponentFamilyUtils.SetPointOrientationType(doc, refPointId, orientationType)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
