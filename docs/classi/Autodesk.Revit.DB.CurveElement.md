---
title: CurveElement
classe: Autodesk.Revit.DB.CurveElement
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 18
---

# CurveElement

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Reference CenterPointReference { get; }` | `curveElement.CenterPointReference` | Reference |
| `CurveElementType CurveElementType { get; }` | `curveElement.CurveElementType` | CurveElementType |
| `Curve GeometryCurve { get; set; }` | `curveElement.GeometryCurve` | Curve |
| `Element LineStyle { get; set; }` | `curveElement.LineStyle` | Element |
| `SketchPlane SketchPlane { get; set; }` | `curveElement.SketchPlane` | SketchPlane |
| `Boolean SupportsTangentLocks { get; }` | `curveElement.SupportsTangentLocks` | Boolean |
| `CurveElement CreateAreaBasedLoadBoundaryLine(Document, Curve, ElementId)` | `CurveElement.CreateAreaBasedLoadBoundaryLine(document, curve, levelId)` | CurveElement |
| `IList<CurveElement> CreateAreaBasedLoadBoundaryLines(Document, IList<Curve>, ElementId)` | `CurveElement.CreateAreaBasedLoadBoundaryLines(document, curves, levelId)` | IList<CurveElement> |
| `ISet<ElementId> GetAdjoinedCurveElements(Int32)` | `curveElement.GetAdjoinedCurveElements(end)` | ISet<ElementId> |
| `AreaBasedLoadBoundaryLineData GetAreaBasedLoadBoundaryLineData()` | `curveElement.GetAreaBasedLoadBoundaryLineData()` | AreaBasedLoadBoundaryLineData |
| `ICollection<ElementId> GetLineStyleIds()` | `curveElement.GetLineStyleIds()` | ICollection<ElementId> |
| `Boolean GetTangentLock(Int32, ElementId)` | `curveElement.GetTangentLock(end, other)` | Boolean |
| `Boolean HasTangentJoin(Int32, ElementId)` | `curveElement.HasTangentJoin(end, other)` | Boolean |
| `Boolean HasTangentLocks(Int32)` | `curveElement.HasTangentLocks(end)` | Boolean |
| `Boolean IsAdjoinedCurveElement(Int32, ElementId)` | `curveElement.IsAdjoinedCurveElement(end, other)` | Boolean |
| `Void SetGeometryCurve(Curve, Boolean)` | `curveElement.SetGeometryCurve(curve, overrideJoins)` | Void |
| `Void SetSketchPlaneAndCurve(SketchPlane, Curve)` | `curveElement.SetSketchPlaneAndCurve(sketchPlane, curve)` | Void |
| `Void SetTangentLock(Int32, ElementId, Boolean)` | `curveElement.SetTangentLock(end, other, state)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
