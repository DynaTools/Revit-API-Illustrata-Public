---
title: ViewShapeBuilder
classe: Autodesk.Revit.DB.ViewShapeBuilder
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.ShapeBuilder
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# ViewShapeBuilder

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ ViewNormal { get; set; }` | `viewShapeBuilder.ViewNormal` | XYZ |
| `DirectShapeTargetViewType ViewType { get; set; }` | `viewShapeBuilder.ViewType` | DirectShapeTargetViewType |
| `Void AddCurve(Curve)` | `viewShapeBuilder.AddCurve(GCurve)` | Void |
| `Void Reset()` | `viewShapeBuilder.Reset()` | Void |
| `Boolean ValidateCurve(Curve, DirectShapeTargetViewType)` | `ViewShapeBuilder.ValidateCurve(GCurve, targetViewType)` | Boolean |
| `Boolean ValidateCurve(Curve)` | `viewShapeBuilder.ValidateCurve(GCurve)` | Boolean |
| `Boolean ValidateShape(IList<GeometryObject>, DirectShapeTargetViewType)` | `ViewShapeBuilder.ValidateShape(shape, targetViewType)` | Boolean |
| `Boolean ValidateViewType(DirectShapeTargetViewType)` | `ViewShapeBuilder.ValidateViewType(targetViewType)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
