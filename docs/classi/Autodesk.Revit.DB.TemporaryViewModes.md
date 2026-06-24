---
title: TemporaryViewModes
classe: Autodesk.Revit.DB.TemporaryViewModes
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 18
---

# TemporaryViewModes

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Color CustomColor { get; set; }` | `temporaryViewModes.CustomColor` | Color |
| `String CustomTitle { get; set; }` | `temporaryViewModes.CustomTitle` | String |
| `Boolean IsValidObject { get; }` | `temporaryViewModes.IsValidObject` | Boolean |
| `PreviewFamilyVisibilityMode PreviewFamilyVisibility { get; set; }` | `temporaryViewModes.PreviewFamilyVisibility` | PreviewFamilyVisibilityMode |
| `Boolean PreviewFamilyVisibilityDefaultOnState { get; set; }` | `TemporaryViewModes.PreviewFamilyVisibilityDefaultOnState` | Boolean |
| `Boolean PreviewFamilyVisibilityDefaultUncutState { get; set; }` | `TemporaryViewModes.PreviewFamilyVisibilityDefaultUncutState` | Boolean |
| `Boolean RevealConstraints { get; set; }` | `temporaryViewModes.RevealConstraints` | Boolean |
| `Boolean RevealHiddenElements { get; set; }` | `temporaryViewModes.RevealHiddenElements` | Boolean |
| `WorksharingDisplayMode WorksharingDisplay { get; set; }` | `temporaryViewModes.WorksharingDisplay` | WorksharingDisplayMode |
| `Void DeactivateAllModes()` | `temporaryViewModes.DeactivateAllModes()` | Void |
| `Void DeactivateMode(TemporaryViewMode)` | `temporaryViewModes.DeactivateMode(mode)` | Void |
| `String GetCaption(TemporaryViewMode)` | `temporaryViewModes.GetCaption(mode)` | String |
| `Boolean IsCustomized()` | `temporaryViewModes.IsCustomized()` | Boolean |
| `Boolean IsModeActive(TemporaryViewMode)` | `temporaryViewModes.IsModeActive(mode)` | Boolean |
| `Boolean IsModeAvailable(TemporaryViewMode)` | `temporaryViewModes.IsModeAvailable(mode)` | Boolean |
| `Boolean IsModeEnabled(TemporaryViewMode)` | `temporaryViewModes.IsModeEnabled(mode)` | Boolean |
| `Boolean IsValidState(PreviewFamilyVisibilityMode)` | `temporaryViewModes.IsValidState(state)` | Boolean |
| `Void RemoveCustomization()` | `temporaryViewModes.RemoveCustomization()` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
