---
title: DatumPlane
classe: Autodesk.Revit.DB.DatumPlane
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 17
---

# DatumPlane

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Leader AddLeader(DatumEnds, View)` | `datumPlane.AddLeader(datumEnd, view)` | Leader |
| `Boolean CanBeVisibleInView(View)` | `datumPlane.CanBeVisibleInView(view)` | Boolean |
| `IList<Curve> GetCurvesInView(DatumExtentType, View)` | `datumPlane.GetCurvesInView(extentMode, view)` | IList<Curve> |
| `DatumExtentType GetDatumExtentTypeInView(DatumEnds, View)` | `datumPlane.GetDatumExtentTypeInView(datumEnd, view)` | DatumExtentType |
| `Leader GetLeader(DatumEnds, View)` | `datumPlane.GetLeader(datumEnd, view)` | Leader |
| `ISet<ElementId> GetPropagationViews(View)` | `datumPlane.GetPropagationViews(view)` | ISet<ElementId> |
| `Boolean HasBubbleInView(DatumEnds, View)` | `datumPlane.HasBubbleInView(datumEnd, view)` | Boolean |
| `Void HideBubbleInView(DatumEnds, View)` | `datumPlane.HideBubbleInView(datumEnd, view)` | Void |
| `Boolean IsBubbleVisibleInView(DatumEnds, View)` | `datumPlane.IsBubbleVisibleInView(datumEnd, view)` | Boolean |
| `Boolean IsCurveValidInView(DatumExtentType, View, Curve)` | `datumPlane.IsCurveValidInView(extentMode, view, curve)` | Boolean |
| `Boolean IsLeaderValid(DatumEnds, View, Leader)` | `datumPlane.IsLeaderValid(datumEnd, view, leader)` | Boolean |
| `Void Maximize3DExtents()` | `datumPlane.Maximize3DExtents()` | Void |
| `Void PropagateToViews(View, ISet<ElementId>)` | `datumPlane.PropagateToViews(view, parallelViews)` | Void |
| `Void SetCurveInView(DatumExtentType, View, Curve)` | `datumPlane.SetCurveInView(extentMode, view, curve)` | Void |
| `Void SetDatumExtentType(DatumEnds, View, DatumExtentType)` | `datumPlane.SetDatumExtentType(datumEnd, view, extentMode)` | Void |
| `Void SetLeader(DatumEnds, View, Leader)` | `datumPlane.SetLeader(datumEnd, view, pLeader)` | Void |
| `Void ShowBubbleInView(DatumEnds, View)` | `datumPlane.ShowBubbleInView(datumEnd, view)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
