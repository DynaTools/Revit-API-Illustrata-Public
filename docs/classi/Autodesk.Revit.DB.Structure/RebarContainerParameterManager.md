---
title: RebarContainerParameterManager
classe: Autodesk.Revit.DB.Structure.RebarContainerParameterManager
namespace: Autodesk.Revit.DB.Structure
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 18
---

# RebarContainerParameterManager

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `rebarContainerParameterManager.IsValidObject` | Boolean |
| `Void AddOverride(ElementId, ElementId)` | `rebarContainerParameterManager.AddOverride(paramId, value)` | Void |
| `Void AddOverride(ElementId, String)` | `rebarContainerParameterManager.AddOverride(paramId, value)` | Void |
| `Void AddOverride(ElementId, Int32)` | `rebarContainerParameterManager.AddOverride(paramId, value)` | Void |
| `Void AddOverride(ElementId, Double)` | `rebarContainerParameterManager.AddOverride(paramId, value)` | Void |
| `Void AddSharedParameterAsOverride(ElementId)` | `rebarContainerParameterManager.AddSharedParameterAsOverride(paramId)` | Void |
| `Void ClearOverrides()` | `rebarContainerParameterManager.ClearOverrides()` | Void |
| `Void Dispose()` | `rebarContainerParameterManager.Dispose()` | Void |
| `Double GetDoubleOverrideValue(ElementId)` | `rebarContainerParameterManager.GetDoubleOverrideValue(paramId)` | Double |
| `ElementId GetElementIdOverrideValue(ElementId)` | `rebarContainerParameterManager.GetElementIdOverrideValue(paramId)` | ElementId |
| `Int32 GetIntOverrideValue(ElementId)` | `rebarContainerParameterManager.GetIntOverrideValue(paramId)` | Int32 |
| `String GetStringOverrideValue(ElementId)` | `rebarContainerParameterManager.GetStringOverrideValue(paramId)` | String |
| `Boolean IsOverriddenParameterModifiable(ElementId)` | `rebarContainerParameterManager.IsOverriddenParameterModifiable(paramId)` | Boolean |
| `Boolean IsParameterOverridden(ElementId)` | `rebarContainerParameterManager.IsParameterOverridden(paramId)` | Boolean |
| `Boolean IsRebarContainerParameter(ElementId)` | `rebarContainerParameterManager.IsRebarContainerParameter(paramId)` | Boolean |
| `Void RemoveOverride(ElementId)` | `rebarContainerParameterManager.RemoveOverride(paramId)` | Void |
| `Void SetOverriddenParameterModifiable(ElementId)` | `rebarContainerParameterManager.SetOverriddenParameterModifiable(paramId)` | Void |
| `Void SetOverriddenParameterReadonly(ElementId)` | `rebarContainerParameterManager.SetOverriddenParameterReadonly(paramId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
