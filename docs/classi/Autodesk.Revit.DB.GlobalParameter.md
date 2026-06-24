---
title: GlobalParameter
classe: Autodesk.Revit.DB.GlobalParameter
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.ParameterElement
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 19
---

# GlobalParameter

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsDrivenByDimension { get; }` | `globalParameter.IsDrivenByDimension` | Boolean |
| `Boolean IsDrivenByFormula { get; }` | `globalParameter.IsDrivenByFormula` | Boolean |
| `Boolean IsReporting { get; set; }` | `globalParameter.IsReporting` | Boolean |
| `Boolean CanChangeReporting()` | `globalParameter.CanChangeReporting()` | Boolean |
| `Boolean CanLabelDimension(ElementId)` | `globalParameter.CanLabelDimension(dimensionId)` | Boolean |
| `GlobalParameter Create(Document, String, ForgeTypeId)` | `GlobalParameter.Create(document, name, specTypeId)` | GlobalParameter |
| `ISet<ElementId> GetAffectedElements()` | `globalParameter.GetAffectedElements()` | ISet<ElementId> |
| `ISet<ElementId> GetAffectedGlobalParameters()` | `globalParameter.GetAffectedGlobalParameters()` | ISet<ElementId> |
| `String GetFormula()` | `globalParameter.GetFormula()` | String |
| `ISet<ElementId> GetLabeledDimensions()` | `globalParameter.GetLabeledDimensions()` | ISet<ElementId> |
| `String GetLabelName()` | `globalParameter.GetLabelName()` | String |
| `ParameterValue GetValue()` | `globalParameter.GetValue()` | ParameterValue |
| `Boolean HasValidTypeForReporting()` | `globalParameter.HasValidTypeForReporting()` | Boolean |
| `Boolean IsValidFormula(String)` | `globalParameter.IsValidFormula(expression)` | Boolean |
| `Void LabelDimension(ElementId)` | `globalParameter.LabelDimension(dimensionId)` | Void |
| `Void SetDrivingDimension(ElementId)` | `globalParameter.SetDrivingDimension(dimensionId)` | Void |
| `Void SetFormula(String)` | `globalParameter.SetFormula(expression)` | Void |
| `Void SetValue(ParameterValue)` | `globalParameter.SetValue(value)` | Void |
| `Void UnlabelDimension(ElementId)` | `globalParameter.UnlabelDimension(dimensionId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
