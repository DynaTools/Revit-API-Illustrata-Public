---
title: CurveByPoints
classe: Autodesk.Revit.DB.CurveByPoints
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.CurveElement
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# CurveByPoints

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsReferenceLine { get; set; }` | `curveByPoints.IsReferenceLine` | Boolean |
| `ReferenceType ReferenceType { get; set; }` | `curveByPoints.ReferenceType` | ReferenceType |
| `SketchPlane SketchPlane { get; set; }` | `curveByPoints.SketchPlane` | SketchPlane |
| `GraphicsStyle Subcategory { get; set; }` | `curveByPoints.Subcategory` | GraphicsStyle |
| `Boolean Visible { get; set; }` | `curveByPoints.Visible` | Boolean |
| `ReferencePointArray GetPoints()` | `curveByPoints.GetPoints()` | ReferencePointArray |
| `FamilyElementVisibility GetVisibility()` | `curveByPoints.GetVisibility()` | FamilyElementVisibility |
| `Void SetPoints(ReferencePointArray)` | `curveByPoints.SetPoints(points)` | Void |
| `Void SetVisibility(FamilyElementVisibility)` | `curveByPoints.SetVisibility(visibility)` | Void |
| `Boolean SortPoints(ReferencePointArray)` | `CurveByPoints.SortPoints(arr)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
