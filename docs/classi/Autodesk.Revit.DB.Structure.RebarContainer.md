---
title: RebarContainer
classe: Autodesk.Revit.DB.Structure.RebarContainer
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 24
---

# RebarContainer

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 ItemsCount { get; }` | `rebarContainer.ItemsCount` | Int32 |
| `Boolean PresentItemsAsSubelements { get; set; }` | `rebarContainer.PresentItemsAsSubelements` | Boolean |
| `String ScheduleMark { get; set; }` | `rebarContainer.ScheduleMark` | String |
| `RebarContainerItem AppendItemFromCurves(RebarStyle, RebarBarType, RebarHookType, RebarHookType, XYZ, IList<Curve>, RebarHookOrientation, RebarHookOrientation, Boolean, Boolean)` | `rebarContainer.AppendItemFromCurves(style, barType, startHook, endHook, normal, curves, startHookOrient, endHookOrient, useExistingShapeIfPossible, createNewShape)` | RebarContainerItem |
| `RebarContainerItem AppendItemFromCurvesAndShape(RebarShape, RebarBarType, RebarHookType, RebarHookType, XYZ, IList<Curve>, RebarHookOrientation, RebarHookOrientation)` | `rebarContainer.AppendItemFromCurvesAndShape(rebarShape, barType, startHook, endHook, normal, curves, startHookOrient, endHookOrient)` | RebarContainerItem |
| `RebarContainerItem AppendItemFromRebar(Rebar)` | `rebarContainer.AppendItemFromRebar(rebar)` | RebarContainerItem |
| `RebarContainerItem AppendItemFromRebarShape(RebarShape, RebarBarType, XYZ, XYZ, XYZ)` | `rebarContainer.AppendItemFromRebarShape(rebarShape, barType, origin, xVector, yVector)` | RebarContainerItem |
| `Boolean CanApplyPresentationMode(View)` | `rebarContainer.CanApplyPresentationMode(dBView)` | Boolean |
| `Void ClearItems()` | `rebarContainer.ClearItems()` | Void |
| `Boolean Contains(RebarContainerItem)` | `rebarContainer.Contains(pItem)` | Boolean |
| `RebarContainer Create(Document, Element, ElementId)` | `RebarContainer.Create(aDoc, hostElement, rebarContainerTypeId)` | RebarContainer |
| `IEnumerator<RebarContainerItem> GetEnumerator()` | `rebarContainer.GetEnumerator()` | IEnumerator<RebarContainerItem> |
| `ElementId GetHostId()` | `rebarContainer.GetHostId()` | ElementId |
| `RebarContainerItem GetItem(Int32)` | `rebarContainer.GetItem(itemIndex)` | RebarContainerItem |
| `RebarContainerParameterManager GetParametersManager()` | `rebarContainer.GetParametersManager()` | RebarContainerParameterManager |
| `RebarContainerIterator GetRebarContainerIterator()` | `rebarContainer.GetRebarContainerIterator()` | RebarContainerIterator |
| `RebarRoundingManager GetReinforcementRoundingManager()` | `rebarContainer.GetReinforcementRoundingManager()` | RebarRoundingManager |
| `Boolean HasPresentationOverrides(View)` | `rebarContainer.HasPresentationOverrides(dBView)` | Boolean |
| `Boolean IsItemHidden(View, Int32)` | `rebarContainer.IsItemHidden(view, itemIndex)` | Boolean |
| `Boolean IsUnobscuredInView(View)` | `rebarContainer.IsUnobscuredInView(view)` | Boolean |
| `Void RemoveItem(RebarContainerItem)` | `rebarContainer.RemoveItem(pItem)` | Void |
| `Void SetHostId(Document, ElementId)` | `rebarContainer.SetHostId(doc, hostId)` | Void |
| `Void SetItemHiddenStatus(View, Int32, Boolean)` | `rebarContainer.SetItemHiddenStatus(view, itemIndex, hide)` | Void |
| `Void SetUnobscuredInView(View, Boolean)` | `rebarContainer.SetUnobscuredInView(view, unobscured)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
