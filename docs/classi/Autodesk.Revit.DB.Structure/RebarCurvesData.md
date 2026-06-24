---
title: RebarCurvesData
classe: Autodesk.Revit.DB.Structure.RebarCurvesData
namespace: Autodesk.Revit.DB.Structure
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# RebarCurvesData

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `rebarCurvesData.IsValidObject` | Boolean |
| `RebarFreeFormValidationResult AddBarGeometry(CurveLoop)` | `rebarCurvesData.AddBarGeometry(curves)` | RebarFreeFormValidationResult |
| `RebarFreeFormValidationResult AddBarGeometry(IList<Curve>)` | `rebarCurvesData.AddBarGeometry(curves)` | RebarFreeFormValidationResult |
| `Boolean CanAddBarGeometry()` | `rebarCurvesData.CanAddBarGeometry()` | Boolean |
| `Void ClearAllAddedBarGeometry()` | `rebarCurvesData.ClearAllAddedBarGeometry()` | Void |
| `Void Dispose()` | `rebarCurvesData.Dispose()` | Void |
| `IList<Curve> GetAddedBarGeometry(Int32)` | `rebarCurvesData.GetAddedBarGeometry(barIndex)` | IList<Curve> |
| `IList<Curve> GetDistributionPath()` | `rebarCurvesData.GetDistributionPath()` | IList<Curve> |
| `Int32 GetNumberOfBarGeometry()` | `rebarCurvesData.GetNumberOfBarGeometry()` | Int32 |
| `RebarUpdateCurvesData GetRebarUpdateCurvesData()` | `rebarCurvesData.GetRebarUpdateCurvesData()` | RebarUpdateCurvesData |
| `Void SetDistributionPath(IList<Curve>)` | `rebarCurvesData.SetDistributionPath(path)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
