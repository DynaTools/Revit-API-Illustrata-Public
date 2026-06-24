---
title: RebarShapeDefinition
classe: Autodesk.Revit.DB.Structure.RebarShapeDefinition
namespace: Autodesk.Revit.DB.Structure
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 14
---

# RebarShapeDefinition

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean Complete { get; }` | `rebarShapeDefinition.Complete` | Boolean |
| `Boolean IsPlanar { get; }` | `rebarShapeDefinition.IsPlanar` | Boolean |
| `Boolean IsValidObject { get; }` | `rebarShapeDefinition.IsValidObject` | Boolean |
| `Void AddFormulaParameter(ElementId, String)` | `rebarShapeDefinition.AddFormulaParameter(paramId, formula)` | Void |
| `Void AddParameter(ElementId, Double)` | `rebarShapeDefinition.AddParameter(paramId, defaultValue)` | Void |
| `Boolean CheckDefaultParameterValues(Double, Double)` | `rebarShapeDefinition.CheckDefaultParameterValues(bendRadius, barDiameter)` | Boolean |
| `Void Dispose()` | `rebarShapeDefinition.Dispose()` | Void |
| `Double GetParameterDefaultValue(ElementId)` | `rebarShapeDefinition.GetParameterDefaultValue(paramId)` | Double |
| `String GetParameterFormula(ElementId)` | `rebarShapeDefinition.GetParameterFormula(paramId)` | String |
| `IList<ElementId> GetParameters()` | `rebarShapeDefinition.GetParameters()` | IList<ElementId> |
| `Boolean HasParameter(ElementId)` | `rebarShapeDefinition.HasParameter(paramId)` | Boolean |
| `Void RemoveParameter(ElementId)` | `rebarShapeDefinition.RemoveParameter(paramId)` | Void |
| `Void SetParameterDefaultValue(ElementId, Double)` | `rebarShapeDefinition.SetParameterDefaultValue(paramId, value)` | Void |
| `Void SetParameterFormula(ElementId, String)` | `rebarShapeDefinition.SetParameterFormula(paramId, formula)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
