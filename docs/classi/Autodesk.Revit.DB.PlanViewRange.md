---
title: PlanViewRange
classe: Autodesk.Revit.DB.PlanViewRange
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# PlanViewRange

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId Current { get; }` | `PlanViewRange.Current` | ElementId |
| `Boolean IsValidObject { get; }` | `planViewRange.IsValidObject` | Boolean |
| `ElementId LevelAbove { get; }` | `PlanViewRange.LevelAbove` | ElementId |
| `ElementId LevelBelow { get; }` | `PlanViewRange.LevelBelow` | ElementId |
| `ElementId Unlimited { get; }` | `PlanViewRange.Unlimited` | ElementId |
| `Void Dispose()` | `planViewRange.Dispose()` | Void |
| `ElementId GetLevelId(PlanViewPlane)` | `planViewRange.GetLevelId(planViewPlane)` | ElementId |
| `Double GetOffset(PlanViewPlane)` | `planViewRange.GetOffset(planViewPlane)` | Double |
| `Void SetLevelId(PlanViewPlane, ElementId)` | `planViewRange.SetLevelId(planViewPlane, id)` | Void |
| `Void SetOffset(PlanViewPlane, Double)` | `planViewRange.SetOffset(planViewPlane, offset)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
