---
title: RebarTrimExtendData
classe: Autodesk.Revit.DB.Structure.RebarTrimExtendData
namespace: Autodesk.Revit.DB.Structure
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# RebarTrimExtendData

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `rebarTrimExtendData.IsValidObject` | Boolean |
| `RebarFreeFormValidationResult AddBarGeometry(CurveLoop)` | `rebarTrimExtendData.AddBarGeometry(curves)` | RebarFreeFormValidationResult |
| `RebarFreeFormValidationResult AddBarGeometry(IList<Curve>)` | `rebarTrimExtendData.AddBarGeometry(curves)` | RebarFreeFormValidationResult |
| `Boolean CanAddBarGeometry()` | `rebarTrimExtendData.CanAddBarGeometry()` | Boolean |
| `Void ClearAllAddedBarGeometry()` | `rebarTrimExtendData.ClearAllAddedBarGeometry()` | Void |
| `Boolean CreateEndConstraint(IList<Reference>, Boolean, Double)` | `rebarTrimExtendData.CreateEndConstraint(targetReferences, isConstraintToCover, offsetValue)` | Boolean |
| `Boolean CreateStartConstraint(IList<Reference>, Boolean, Double)` | `rebarTrimExtendData.CreateStartConstraint(targetReferences, isConstraintToCover, offsetValue)` | Boolean |
| `Void Dispose()` | `rebarTrimExtendData.Dispose()` | Void |
| `IList<Curve> GetAddedBarGeometry(Int32)` | `rebarTrimExtendData.GetAddedBarGeometry(barIndex)` | IList<Curve> |
| `Int32 GetNumberOfBarGeometry()` | `rebarTrimExtendData.GetNumberOfBarGeometry()` | Int32 |
| `RebarUpdateCurvesData GetRebarUpdateCurvesData()` | `rebarTrimExtendData.GetRebarUpdateCurvesData()` | RebarUpdateCurvesData |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
