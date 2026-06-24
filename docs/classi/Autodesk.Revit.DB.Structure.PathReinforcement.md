---
title: PathReinforcement
classe: Autodesk.Revit.DB.Structure.PathReinforcement
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 20
---

# PathReinforcement

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double AdditionalOffset { get; set; }` | `pathReinforcement.AdditionalOffset` | Double |
| `ReinforcementBarOrientation AlternatingBarOrientation { get; set; }` | `pathReinforcement.AlternatingBarOrientation` | ReinforcementBarOrientation |
| `ElementId AlternatingBarShapeId { get; set; }` | `pathReinforcement.AlternatingBarShapeId` | ElementId |
| `PathReinforcementType PathReinforcementType { get; }` | `pathReinforcement.PathReinforcementType` | PathReinforcementType |
| `ReinforcementBarOrientation PrimaryBarOrientation { get; set; }` | `pathReinforcement.PrimaryBarOrientation` | ReinforcementBarOrientation |
| `ElementId PrimaryBarShapeId { get; set; }` | `pathReinforcement.PrimaryBarShapeId` | ElementId |
| `IList<ElementId> ConvertRebarInSystemToRebars(Document, PathReinforcement)` | `PathReinforcement.ConvertRebarInSystemToRebars(doc, system)` | IList<ElementId> |
| `PathReinforcement Create(Document, Element, IList<Curve>, Boolean, ElementId, ElementId, ElementId, ElementId, ElementId)` | `PathReinforcement.Create(document, hostElement, curveArray, flip, pathReinforcementTypeId, rebarBarTypeId, startRebarHookTypeId, endRebarHookTypeId, rebarShapeId)` | PathReinforcement |
| `PathReinforcement Create(Document, Element, IList<Curve>, Boolean, ElementId, ElementId, ElementId, ElementId)` | `PathReinforcement.Create(document, hostElement, curveArray, flip, pathReinforcementTypeId, rebarBarTypeId, startRebarHookTypeId, endRebarHookTypeId)` | PathReinforcement |
| `IList<ElementId> GetCurveElementIds()` | `pathReinforcement.GetCurveElementIds()` | IList<ElementId> |
| `ElementId GetHostId()` | `pathReinforcement.GetHostId()` | ElementId |
| `ElementId GetOrCreateDefaultRebarShape(Document, ElementId, ElementId, ElementId)` | `PathReinforcement.GetOrCreateDefaultRebarShape(document, rebarBarTypeId, startRebarHookTypeId, endRebarHookTypeId)` | ElementId |
| `IList<ElementId> GetRebarInSystemIds()` | `pathReinforcement.GetRebarInSystemIds()` | IList<ElementId> |
| `Boolean IsAlternatingLayerEnabled()` | `pathReinforcement.IsAlternatingLayerEnabled()` | Boolean |
| `Boolean IsUnobscuredInView(View)` | `pathReinforcement.IsUnobscuredInView(view)` | Boolean |
| `Boolean IsValidAlternatingBarOrientation(ReinforcementBarOrientation)` | `pathReinforcement.IsValidAlternatingBarOrientation(orientation)` | Boolean |
| `Boolean IsValidPrimaryBarOrientation(ReinforcementBarOrientation)` | `pathReinforcement.IsValidPrimaryBarOrientation(orientation)` | Boolean |
| `Boolean IsValidRebarShapeId(Document, ElementId)` | `PathReinforcement.IsValidRebarShapeId(aDoc, elementId)` | Boolean |
| `IList<ElementId> RemovePathReinforcementSystem(Document, PathReinforcement)` | `PathReinforcement.RemovePathReinforcementSystem(doc, system)` | IList<ElementId> |
| `Void SetUnobscuredInView(View, Boolean)` | `pathReinforcement.SetUnobscuredInView(view, unobscured)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
