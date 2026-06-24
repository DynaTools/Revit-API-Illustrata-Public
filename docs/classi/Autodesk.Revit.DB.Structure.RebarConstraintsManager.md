---
title: RebarConstraintsManager
classe: Autodesk.Revit.DB.Structure.RebarConstraintsManager
namespace: Autodesk.Revit.DB.Structure
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 19
---

# RebarConstraintsManager

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsRebarConstrainedPlacementEnabled { get; set; }` | `RebarConstraintsManager.IsRebarConstrainedPlacementEnabled` | Boolean |
| `Boolean IsValidObject { get; }` | `rebarConstraintsManager.IsValidObject` | Boolean |
| `Boolean AllowConstraintTargets(RebarConstrainedHandle, IList<Reference>)` | `rebarConstraintsManager.AllowConstraintTargets(handle, targetsToConstrain)` | Boolean |
| `Boolean ApplyRebarConstraints(IList<RebarConstraint>, IList<Reference>, IList<Reference>)` | `rebarConstraintsManager.ApplyRebarConstraints(constraintsToApply, oldTargets, newTargets)` | Boolean |
| `Void ClearHandleConstraintPairHighlighting(Document)` | `rebarConstraintsManager.ClearHandleConstraintPairHighlighting(aDoc)` | Void |
| `Void Dispose()` | `rebarConstraintsManager.Dispose()` | Void |
| `IList<RebarConstrainedHandle> GetAllConstrainedHandles()` | `rebarConstraintsManager.GetAllConstrainedHandles()` | IList<RebarConstrainedHandle> |
| `IList<RebarConstrainedHandle> GetAllHandles()` | `rebarConstraintsManager.GetAllHandles()` | IList<RebarConstrainedHandle> |
| `IList<RebarConstraint> GetConstraintCandidatesForHandle(RebarConstrainedHandle, Reference)` | `rebarConstraintsManager.GetConstraintCandidatesForHandle(handle, reference)` | IList<RebarConstraint> |
| `IList<RebarConstraint> GetConstraintCandidatesForHandle(RebarConstrainedHandle, ElementId)` | `rebarConstraintsManager.GetConstraintCandidatesForHandle(handle, elementId)` | IList<RebarConstraint> |
| `IList<RebarConstraint> GetConstraintCandidatesForHandle(RebarConstrainedHandle)` | `rebarConstraintsManager.GetConstraintCandidatesForHandle(handle)` | IList<RebarConstraint> |
| `RebarConstraint GetCurrentConstraintOnHandle(RebarConstrainedHandle)` | `rebarConstraintsManager.GetCurrentConstraintOnHandle(handle)` | RebarConstraint |
| `RebarConstraint GetPreferredConstraintOnHandle(RebarConstrainedHandle)` | `rebarConstraintsManager.GetPreferredConstraintOnHandle(handle)` | RebarConstraint |
| `Boolean HasValidRebar()` | `rebarConstraintsManager.HasValidRebar()` | Boolean |
| `Void HighlightHandleConstraintPairInAllViews(Document, RebarConstrainedHandle, RebarConstraint)` | `rebarConstraintsManager.HighlightHandleConstraintPairInAllViews(aDoc, handle, constraint)` | Void |
| `Void RemovePreferredConstraintFromHandle(RebarConstrainedHandle)` | `rebarConstraintsManager.RemovePreferredConstraintFromHandle(handle)` | Void |
| `Void SetPreferredConstraint(RebarConstraint)` | `rebarConstraintsManager.SetPreferredConstraint(constraint)` | Void |
| `Void SetPreferredConstraintForHandle(RebarConstrainedHandle, RebarConstraint)` | `rebarConstraintsManager.SetPreferredConstraintForHandle(handle, constraint)` | Void |
| `Void SetPreferredConstraintsToSurfaceForHandles(IList<RebarConstrainedHandle>)` | `rebarConstraintsManager.SetPreferredConstraintsToSurfaceForHandles(handles)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
