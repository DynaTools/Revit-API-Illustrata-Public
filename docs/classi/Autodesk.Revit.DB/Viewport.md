---
title: Viewport
classe: Autodesk.Revit.DB.Viewport
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 15
---

# Viewport

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double LabelLineLength { get; set; }` | `viewport.LabelLineLength` | Double |
| `XYZ LabelOffset { get; set; }` | `viewport.LabelOffset` | XYZ |
| `ViewportRotation Rotation { get; set; }` | `viewport.Rotation` | ViewportRotation |
| `ElementId SheetId { get; }` | `viewport.SheetId` | ElementId |
| `ElementId ViewId { get; set; }` | `viewport.ViewId` | ElementId |
| `ViewportPositioning ViewportPositioning { get; set; }` | `viewport.ViewportPositioning` | ViewportPositioning |
| `Boolean CanAddViewToSheet(Document, ElementId, ElementId)` | `Viewport.CanAddViewToSheet(document, viewSheetId, viewId)` | Boolean |
| `Viewport Create(Document, ElementId, ElementId, XYZ)` | `Viewport.Create(document, viewSheetId, viewId, point)` | Viewport |
| `XYZ GetBoxCenter()` | `viewport.GetBoxCenter()` | XYZ |
| `Outline GetBoxOutline()` | `viewport.GetBoxOutline()` | Outline |
| `Outline GetLabelOutline()` | `viewport.GetLabelOutline()` | Outline |
| `Transform GetProjectionToSheetTransform()` | `viewport.GetProjectionToSheetTransform()` | Transform |
| `Boolean HasViewportTransforms()` | `viewport.HasViewportTransforms()` | Boolean |
| `Boolean IsViewIdValidForViewport(ElementId)` | `viewport.IsViewIdValidForViewport(viewId)` | Boolean |
| `Void SetBoxCenter(XYZ)` | `viewport.SetBoxCenter(newCenterPoint)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
