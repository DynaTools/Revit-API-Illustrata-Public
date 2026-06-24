---
title: CurveByPointsUtils
classe: Autodesk.Revit.DB.CurveByPointsUtils
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 12
---

# CurveByPointsUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `curveByPointsUtils.IsValidObject` | Boolean |
| `Void AddCurvesToFaceRegion(Document, IList<ElementId>)` | `CurveByPointsUtils.AddCurvesToFaceRegion(document, curveElemIds)` | Void |
| `CurveElement CreateArcThroughPoints(Document, ReferencePoint, ReferencePoint, ReferencePoint)` | `CurveByPointsUtils.CreateArcThroughPoints(document, startPoint, endPoint, interiorPoint)` | CurveElement |
| `Void CreateRectangle(Document, ReferencePoint, ReferencePoint, CurveProjectionType, Boolean, Boolean, IList<ElementId>&, IList<ElementId>&)` | `CurveByPointsUtils.CreateRectangle(document, startPoint, endPoint, projectionType, boundaryReferenceLines, boundaryCurvesFollowSurface, createdCurvesIds, createdCornersIds)` | Void |
| `Void Dispose()` | `curveByPointsUtils.Dispose()` | Void |
| `IList<Reference> GetFaceRegions(Document, Reference)` | `CurveByPointsUtils.GetFaceRegions(cda, referenceOfFace)` | IList<Reference> |
| `Reference GetHostFace(CurveElement)` | `CurveByPointsUtils.GetHostFace(curveElem)` | Reference |
| `CurveProjectionType GetProjectionType(CurveElement)` | `CurveByPointsUtils.GetProjectionType(curveElem)` | CurveProjectionType |
| `Boolean GetSketchOnSurface(CurveElement)` | `CurveByPointsUtils.GetSketchOnSurface(curveElem)` | Boolean |
| `Void SetProjectionType(CurveElement, CurveProjectionType)` | `CurveByPointsUtils.SetProjectionType(curveElem, value)` | Void |
| `Void SetSketchOnSurface(CurveElement, Boolean)` | `CurveByPointsUtils.SetSketchOnSurface(curveElem, sketchOnSurface)` | Void |
| `Boolean ValidateCurveElementIdArrayForFaceRegions(Document, IList<ElementId>)` | `CurveByPointsUtils.ValidateCurveElementIdArrayForFaceRegions(document, curveElemIds)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
