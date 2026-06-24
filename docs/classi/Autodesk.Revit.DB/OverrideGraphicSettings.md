---
title: OverrideGraphicSettings
classe: Autodesk.Revit.DB.OverrideGraphicSettings
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 45
---

# OverrideGraphicSettings

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Color CutBackgroundPatternColor { get; }` | `overrideGraphicSettings.CutBackgroundPatternColor` | Color |
| `ElementId CutBackgroundPatternId { get; }` | `overrideGraphicSettings.CutBackgroundPatternId` | ElementId |
| `Color CutForegroundPatternColor { get; }` | `overrideGraphicSettings.CutForegroundPatternColor` | Color |
| `ElementId CutForegroundPatternId { get; }` | `overrideGraphicSettings.CutForegroundPatternId` | ElementId |
| `Color CutLineColor { get; }` | `overrideGraphicSettings.CutLineColor` | Color |
| `ElementId CutLinePatternId { get; }` | `overrideGraphicSettings.CutLinePatternId` | ElementId |
| `Int32 CutLineWeight { get; }` | `overrideGraphicSettings.CutLineWeight` | Int32 |
| `ViewDetailLevel DetailLevel { get; }` | `overrideGraphicSettings.DetailLevel` | ViewDetailLevel |
| `Boolean Halftone { get; }` | `overrideGraphicSettings.Halftone` | Boolean |
| `Int32 InvalidPenNumber { get; }` | `OverrideGraphicSettings.InvalidPenNumber` | Int32 |
| `Boolean IsCutBackgroundPatternVisible { get; }` | `overrideGraphicSettings.IsCutBackgroundPatternVisible` | Boolean |
| `Boolean IsCutForegroundPatternVisible { get; }` | `overrideGraphicSettings.IsCutForegroundPatternVisible` | Boolean |
| `Boolean IsSurfaceBackgroundPatternVisible { get; }` | `overrideGraphicSettings.IsSurfaceBackgroundPatternVisible` | Boolean |
| `Boolean IsSurfaceForegroundPatternVisible { get; }` | `overrideGraphicSettings.IsSurfaceForegroundPatternVisible` | Boolean |
| `Boolean IsValidObject { get; }` | `overrideGraphicSettings.IsValidObject` | Boolean |
| `Color ProjectionLineColor { get; }` | `overrideGraphicSettings.ProjectionLineColor` | Color |
| `ElementId ProjectionLinePatternId { get; }` | `overrideGraphicSettings.ProjectionLinePatternId` | ElementId |
| `Int32 ProjectionLineWeight { get; }` | `overrideGraphicSettings.ProjectionLineWeight` | Int32 |
| `Color SurfaceBackgroundPatternColor { get; }` | `overrideGraphicSettings.SurfaceBackgroundPatternColor` | Color |
| `ElementId SurfaceBackgroundPatternId { get; }` | `overrideGraphicSettings.SurfaceBackgroundPatternId` | ElementId |
| `Color SurfaceForegroundPatternColor { get; }` | `overrideGraphicSettings.SurfaceForegroundPatternColor` | Color |
| `ElementId SurfaceForegroundPatternId { get; }` | `overrideGraphicSettings.SurfaceForegroundPatternId` | ElementId |
| `Int32 Transparency { get; }` | `overrideGraphicSettings.Transparency` | Int32 |
| `Void Dispose()` | `overrideGraphicSettings.Dispose()` | Void |
| `OverrideGraphicSettings SetCutBackgroundPatternColor(Color)` | `overrideGraphicSettings.SetCutBackgroundPatternColor(color)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetCutBackgroundPatternId(ElementId)` | `overrideGraphicSettings.SetCutBackgroundPatternId(fillPatternId)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetCutBackgroundPatternVisible(Boolean)` | `overrideGraphicSettings.SetCutBackgroundPatternVisible(fillPatternVisible)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetCutForegroundPatternColor(Color)` | `overrideGraphicSettings.SetCutForegroundPatternColor(color)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetCutForegroundPatternId(ElementId)` | `overrideGraphicSettings.SetCutForegroundPatternId(fillPatternId)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetCutForegroundPatternVisible(Boolean)` | `overrideGraphicSettings.SetCutForegroundPatternVisible(fillPatternVisible)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetCutLineColor(Color)` | `overrideGraphicSettings.SetCutLineColor(color)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetCutLinePatternId(ElementId)` | `overrideGraphicSettings.SetCutLinePatternId(linePatternId)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetCutLineWeight(Int32)` | `overrideGraphicSettings.SetCutLineWeight(lineWeight)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetDetailLevel(ViewDetailLevel)` | `overrideGraphicSettings.SetDetailLevel(detailLevel)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetHalftone(Boolean)` | `overrideGraphicSettings.SetHalftone(halftone)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetProjectionLineColor(Color)` | `overrideGraphicSettings.SetProjectionLineColor(color)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetProjectionLinePatternId(ElementId)` | `overrideGraphicSettings.SetProjectionLinePatternId(linePatternId)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetProjectionLineWeight(Int32)` | `overrideGraphicSettings.SetProjectionLineWeight(lineWeight)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetSurfaceBackgroundPatternColor(Color)` | `overrideGraphicSettings.SetSurfaceBackgroundPatternColor(color)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetSurfaceBackgroundPatternId(ElementId)` | `overrideGraphicSettings.SetSurfaceBackgroundPatternId(fillPatternId)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetSurfaceBackgroundPatternVisible(Boolean)` | `overrideGraphicSettings.SetSurfaceBackgroundPatternVisible(fillPatternVisible)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetSurfaceForegroundPatternColor(Color)` | `overrideGraphicSettings.SetSurfaceForegroundPatternColor(color)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetSurfaceForegroundPatternId(ElementId)` | `overrideGraphicSettings.SetSurfaceForegroundPatternId(fillPatternId)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetSurfaceForegroundPatternVisible(Boolean)` | `overrideGraphicSettings.SetSurfaceForegroundPatternVisible(fillPatternVisible)` | OverrideGraphicSettings |
| `OverrideGraphicSettings SetSurfaceTransparency(Int32)` | `overrideGraphicSettings.SetSurfaceTransparency(transparency)` | OverrideGraphicSettings |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
