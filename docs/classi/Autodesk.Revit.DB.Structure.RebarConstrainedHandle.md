---
title: RebarConstrainedHandle
classe: Autodesk.Revit.DB.Structure.RebarConstrainedHandle
namespace: Autodesk.Revit.DB.Structure
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 15
---

# RebarConstrainedHandle

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `RebarHandleBehavior HandleBehavior { get; set; }` | `rebarConstrainedHandle.HandleBehavior` | RebarHandleBehavior |
| `Boolean IsValidObject { get; }` | `rebarConstrainedHandle.IsValidObject` | Boolean |
| `Boolean CanSetBehavior(RebarHandleBehavior)` | `rebarConstrainedHandle.CanSetBehavior(handleBehavior)` | Boolean |
| `Void Dispose()` | `rebarConstrainedHandle.Dispose()` | Void |
| `Int32 GetCustomHandleTag()` | `rebarConstrainedHandle.GetCustomHandleTag()` | Int32 |
| `Int32 GetEdgeNumber()` | `rebarConstrainedHandle.GetEdgeNumber()` | Int32 |
| `String GetHandleName()` | `rebarConstrainedHandle.GetHandleName()` | String |
| `Surface GetHandleSurface()` | `rebarConstrainedHandle.GetHandleSurface()` | Surface |
| `RebarHandleType GetHandleType()` | `rebarConstrainedHandle.GetHandleType()` | RebarHandleType |
| `IList<RebarHandleBehavior> GetPossibleHandleBehaviors()` | `rebarConstrainedHandle.GetPossibleHandleBehaviors()` | IList<RebarHandleBehavior> |
| `Boolean IsCustomHandle()` | `rebarConstrainedHandle.IsCustomHandle()` | Boolean |
| `Boolean IsEdgeHandle()` | `rebarConstrainedHandle.IsEdgeHandle()` | Boolean |
| `Boolean IsEqual(RebarConstrainedHandle)` | `rebarConstrainedHandle.IsEqual(other)` | Boolean |
| `Boolean IsValid()` | `rebarConstrainedHandle.IsValid()` | Boolean |
| `Void Move(XYZ)` | `rebarConstrainedHandle.Move(translataion)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
