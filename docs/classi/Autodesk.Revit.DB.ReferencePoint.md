---
title: ReferencePoint
classe: Autodesk.Revit.DB.ReferencePoint
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 16
---

# ReferencePoint

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `CoordinatePlaneVisibility CoordinatePlaneVisibility { get; set; }` | `referencePoint.CoordinatePlaneVisibility` | CoordinatePlaneVisibility |
| `String Name { get; set; }` | `referencePoint.Name` | String |
| `XYZ Position { get; set; }` | `referencePoint.Position` | XYZ |
| `Boolean ShowNormalReferencePlaneOnly { get; set; }` | `referencePoint.ShowNormalReferencePlaneOnly` | Boolean |
| `Boolean Visible { get; set; }` | `referencePoint.Visible` | Boolean |
| `Reference GetCoordinatePlaneReferenceXY()` | `referencePoint.GetCoordinatePlaneReferenceXY()` | Reference |
| `Reference GetCoordinatePlaneReferenceXZ()` | `referencePoint.GetCoordinatePlaneReferenceXZ()` | Reference |
| `Reference GetCoordinatePlaneReferenceYZ()` | `referencePoint.GetCoordinatePlaneReferenceYZ()` | Reference |
| `Transform GetCoordinateSystem()` | `referencePoint.GetCoordinateSystem()` | Transform |
| `ElementId GetHubId()` | `referencePoint.GetHubId()` | ElementId |
| `CurveByPointsArray GetInterpolatingCurves()` | `referencePoint.GetInterpolatingCurves()` | CurveByPointsArray |
| `PointElementReference GetPointElementReference()` | `referencePoint.GetPointElementReference()` | PointElementReference |
| `FamilyElementVisibility GetVisibility()` | `referencePoint.GetVisibility()` | FamilyElementVisibility |
| `Void SetCoordinateSystem(Transform)` | `referencePoint.SetCoordinateSystem(coordinateSystem)` | Void |
| `Void SetPointElementReference(PointElementReference)` | `referencePoint.SetPointElementReference(pointElementReference)` | Void |
| `Void SetVisibility(FamilyElementVisibility)` | `referencePoint.SetVisibility(visibility)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
