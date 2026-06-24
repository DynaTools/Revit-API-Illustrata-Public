---
title: View3D
classe: Autodesk.Revit.DB.View3D
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.View
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 30
---

# View3D

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsLocked { get; }` | `view3D.IsLocked` | Boolean |
| `Boolean IsPerspective { get; }` | `view3D.IsPerspective` | Boolean |
| `Boolean IsSectionBoxActive { get; set; }` | `view3D.IsSectionBoxActive` | Boolean |
| `Boolean ProjectGridsOnSectionBox { get; set; }` | `view3D.ProjectGridsOnSectionBox` | Boolean |
| `Boolean CanResetCameraTarget()` | `view3D.CanResetCameraTarget()` | Boolean |
| `Boolean CanSaveOrientation()` | `view3D.CanSaveOrientation()` | Boolean |
| `Boolean CanToggleBetweenPerspectiveAndIsometric()` | `view3D.CanToggleBetweenPerspectiveAndIsometric()` | Boolean |
| `View3D CreateIsometric(Document, ElementId)` | `View3D.CreateIsometric(document, viewFamilyTypeId)` | View3D |
| `View3D CreatePerspective(Document, ElementId)` | `View3D.CreatePerspective(document, viewFamilyTypeId)` | View3D |
| `ISet<ElementId> GetLevelsThatShowGrids()` | `view3D.GetLevelsThatShowGrids()` | ISet<ElementId> |
| `ViewOrientation3D GetOrientation()` | `view3D.GetOrientation()` | ViewOrientation3D |
| `RenderingSettings GetRenderingSettings()` | `view3D.GetRenderingSettings()` | RenderingSettings |
| `ViewOrientation3D GetSavedOrientation()` | `view3D.GetSavedOrientation()` | ViewOrientation3D |
| `BoundingBoxXYZ GetSectionBox()` | `view3D.GetSectionBox()` | BoundingBoxXYZ |
| `Boolean HasBeenLocked()` | `view3D.HasBeenLocked()` | Boolean |
| `Void HideGridsOnLevel(ElementId)` | `view3D.HideGridsOnLevel(levelId)` | Void |
| `Void OrientTo(XYZ)` | `view3D.OrientTo(forwardDirection)` | Void |
| `Void ResetCameraTarget()` | `view3D.ResetCameraTarget()` | Void |
| `Void RestoreOrientationAndLock()` | `view3D.RestoreOrientationAndLock()` | Void |
| `Void SaveOrientation()` | `view3D.SaveOrientation()` | Void |
| `Void SaveOrientationAndLock()` | `view3D.SaveOrientationAndLock()` | Void |
| `Void ScalePerspectiveCropBox(Double)` | `view3D.ScalePerspectiveCropBox(multiplier)` | Void |
| `Void SetOrientation(ViewOrientation3D)` | `view3D.SetOrientation(newViewOrientation3D)` | Void |
| `Void SetRenderingSettings(RenderingSettings)` | `view3D.SetRenderingSettings(settings)` | Void |
| `Void SetSectionBox(BoundingBoxXYZ)` | `view3D.SetSectionBox(boundingBoxXYZ)` | Void |
| `Void ShowGridsOnLevel(ElementId)` | `view3D.ShowGridsOnLevel(levelId)` | Void |
| `Void ShowGridsOnLevels(ISet<ElementId>)` | `view3D.ShowGridsOnLevels(levelsIds)` | Void |
| `Void ToggleToIsometric()` | `view3D.ToggleToIsometric()` | Void |
| `Void ToggleToPerspective()` | `view3D.ToggleToPerspective()` | Void |
| `Void Unlock()` | `view3D.Unlock()` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
