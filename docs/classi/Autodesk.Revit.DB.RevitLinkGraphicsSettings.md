---
title: RevitLinkGraphicsSettings
classe: Autodesk.Revit.DB.RevitLinkGraphicsSettings
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 22
---

# RevitLinkGraphicsSettings

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `LinkVisibility ColorFill { get; set; }` | `revitLinkGraphicsSettings.ColorFill` | LinkVisibility |
| `Boolean IsValidObject { get; }` | `revitLinkGraphicsSettings.IsValidObject` | Boolean |
| `ElementId LinkedViewId { get; set; }` | `revitLinkGraphicsSettings.LinkedViewId` | ElementId |
| `LinkVisibility LinkVisibilityType { get; set; }` | `revitLinkGraphicsSettings.LinkVisibilityType` | LinkVisibility |
| `LinkVisibility NestedLinks { get; set; }` | `revitLinkGraphicsSettings.NestedLinks` | LinkVisibility |
| `LinkVisibility ObjectStyles { get; set; }` | `revitLinkGraphicsSettings.ObjectStyles` | LinkVisibility |
| `LinkVisibility ViewFilterType { get; set; }` | `revitLinkGraphicsSettings.ViewFilterType` | LinkVisibility |
| `LinkVisibility ViewRange { get; set; }` | `revitLinkGraphicsSettings.ViewRange` | LinkVisibility |
| `Void Dispose()` | `revitLinkGraphicsSettings.Dispose()` | Void |
| `ViewDiscipline GetDiscipline()` | `revitLinkGraphicsSettings.GetDiscipline()` | ViewDiscipline |
| `LinkVisibility GetDisciplineType()` | `revitLinkGraphicsSettings.GetDisciplineType()` | LinkVisibility |
| `ElementId GetPhaseFilterId()` | `revitLinkGraphicsSettings.GetPhaseFilterId()` | ElementId |
| `LinkVisibility GetPhaseFilterType()` | `revitLinkGraphicsSettings.GetPhaseFilterType()` | LinkVisibility |
| `ElementId GetPhaseId()` | `revitLinkGraphicsSettings.GetPhaseId()` | ElementId |
| `LinkVisibility GetPhaseType()` | `revitLinkGraphicsSettings.GetPhaseType()` | LinkVisibility |
| `ViewDetailLevel GetViewDetailLevel()` | `revitLinkGraphicsSettings.GetViewDetailLevel()` | ViewDetailLevel |
| `LinkVisibility GetViewDetailLevelType()` | `revitLinkGraphicsSettings.GetViewDetailLevelType()` | LinkVisibility |
| `Boolean IsViewRangeSupported(View)` | `RevitLinkGraphicsSettings.IsViewRangeSupported(view)` | Boolean |
| `Void SetDiscipline(LinkVisibility, ViewDiscipline)` | `revitLinkGraphicsSettings.SetDiscipline(disciplineType, discipline)` | Void |
| `Void SetPhase(LinkVisibility, ElementId)` | `revitLinkGraphicsSettings.SetPhase(phaseType, phaseId)` | Void |
| `Void SetPhaseFilter(LinkVisibility, ElementId)` | `revitLinkGraphicsSettings.SetPhaseFilter(phaseFilterType, phaseFilterId)` | Void |
| `Void SetViewDetailLevel(LinkVisibility, ViewDetailLevel)` | `revitLinkGraphicsSettings.SetViewDetailLevel(viewDetailLevelType, viewDetailLevel)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
