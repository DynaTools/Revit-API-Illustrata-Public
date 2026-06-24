---
title: LineLoad
classe: Autodesk.Revit.DB.Structure.LineLoad
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Structure.LoadBase
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 16
---

# LineLoad

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ EndPoint { get; }` | `lineLoad.EndPoint` | XYZ |
| `XYZ ForceVector1 { get; set; }` | `lineLoad.ForceVector1` | XYZ |
| `XYZ ForceVector2 { get; set; }` | `lineLoad.ForceVector2` | XYZ |
| `Boolean IsProjected { get; set; }` | `lineLoad.IsProjected` | Boolean |
| `Boolean IsUniform { get; }` | `lineLoad.IsUniform` | Boolean |
| `XYZ MomentVector1 { get; set; }` | `lineLoad.MomentVector1` | XYZ |
| `XYZ MomentVector2 { get; set; }` | `lineLoad.MomentVector2` | XYZ |
| `XYZ StartPoint { get; }` | `lineLoad.StartPoint` | XYZ |
| `LineLoad Create(Document, ElementId, Curve, XYZ, XYZ, LineLoadType)` | `LineLoad.Create(document, hostElemId, curve, forceVector1, momentVector1, symbol)` | LineLoad |
| `LineLoad Create(Document, ElementId, Int32, XYZ, XYZ, LineLoadType)` | `LineLoad.Create(document, hostElemId, curveIndex, forceVector1, momentVector1, symbol)` | LineLoad |
| `LineLoad Create(Document, ElementId, XYZ, XYZ, LineLoadType)` | `LineLoad.Create(document, hostElemId, forceVector1, momentVector1, symbol)` | LineLoad |
| `Curve GetCurve()` | `lineLoad.GetCurve()` | Curve |
| `Boolean IsCurveInsideHostBoundaries(Document, ElementId, Curve)` | `LineLoad.IsCurveInsideHostBoundaries(doc, hostId, curve)` | Boolean |
| `Boolean IsValidHostId(Document, ElementId)` | `LineLoad.IsValidHostId(pDoc, hostId)` | Boolean |
| `Void SetCurve(Curve)` | `lineLoad.SetCurve(curve)` | Void |
| `Boolean SetPoints(XYZ, XYZ)` | `lineLoad.SetPoints(startPoint, endPoint)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
