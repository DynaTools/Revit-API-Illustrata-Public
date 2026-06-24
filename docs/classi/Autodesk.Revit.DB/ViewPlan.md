---
title: ViewPlan
classe: Autodesk.Revit.DB.ViewPlan
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.View
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 12
---

# ViewPlan

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `AreaScheme AreaScheme { get; }` | `viewPlan.AreaScheme` | AreaScheme |
| `IList<PlanViewRangeError> CheckPlanViewRangeValidity(PlanViewRange)` | `viewPlan.CheckPlanViewRangeValidity(planViewRange)` | IList<PlanViewRangeError> |
| `ViewPlan Create(Document, ElementId, ElementId)` | `ViewPlan.Create(document, viewFamilyTypeId, levelId)` | ViewPlan |
| `ViewPlan CreateAreaPlan(Document, ElementId, ElementId)` | `ViewPlan.CreateAreaPlan(document, areaSchemeId, levelId)` | ViewPlan |
| `ElementId GetUnderlayBaseLevel()` | `viewPlan.GetUnderlayBaseLevel()` | ElementId |
| `UnderlayOrientation GetUnderlayOrientation()` | `viewPlan.GetUnderlayOrientation()` | UnderlayOrientation |
| `ElementId GetUnderlayTopLevel()` | `viewPlan.GetUnderlayTopLevel()` | ElementId |
| `PlanViewRange GetViewRange()` | `viewPlan.GetViewRange()` | PlanViewRange |
| `Void SetUnderlayBaseLevel(ElementId)` | `viewPlan.SetUnderlayBaseLevel(levelId)` | Void |
| `Void SetUnderlayOrientation(UnderlayOrientation)` | `viewPlan.SetUnderlayOrientation(uo)` | Void |
| `Void SetUnderlayRange(ElementId, ElementId)` | `viewPlan.SetUnderlayRange(baseLevelId, topLevelId)` | Void |
| `Void SetViewRange(PlanViewRange)` | `viewPlan.SetViewRange(planViewRange)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
