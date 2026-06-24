---
title: AreaReinforcement
classe: Autodesk.Revit.DB.Structure.AreaReinforcement
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 23
---

# AreaReinforcement

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double AdditionalBottomCoverOffset { get; set; }` | `areaReinforcement.AdditionalBottomCoverOffset` | Double |
| `Double AdditionalTopCoverOffset { get; set; }` | `areaReinforcement.AdditionalTopCoverOffset` | Double |
| `AreaReinforcementType AreaReinforcementType { get; }` | `areaReinforcement.AreaReinforcementType` | AreaReinforcementType |
| `XYZ Direction { get; }` | `areaReinforcement.Direction` | XYZ |
| `IList<ElementId> ConvertRebarInSystemToRebars(Document, AreaReinforcement)` | `AreaReinforcement.ConvertRebarInSystemToRebars(doc, system)` | IList<ElementId> |
| `AreaReinforcement Create(Document, Element, XYZ, ElementId, ElementId, ElementId)` | `AreaReinforcement.Create(document, hostElement, majorDirection, areaReinforcementTypeId, rebarBarTypeId, rebarHookTypeId)` | AreaReinforcement |
| `AreaReinforcement Create(Document, Element, IList<Curve>, XYZ, ElementId, ElementId, ElementId)` | `AreaReinforcement.Create(document, hostElement, curveArray, majorDirection, areaReinforcementTypeId, rebarBarTypeId, rebarHookTypeId)` | AreaReinforcement |
| `IList<ElementId> GetBoundaryCurveIds()` | `areaReinforcement.GetBoundaryCurveIds()` | IList<ElementId> |
| `ElementId GetHostId()` | `areaReinforcement.GetHostId()` | ElementId |
| `XYZ GetLayerDirection(AreaReinforcementLayerType)` | `areaReinforcement.GetLayerDirection(layer)` | XYZ |
| `Line GetLineFromLayerAtIndex(AreaReinforcementLayerType, Int32)` | `areaReinforcement.GetLineFromLayerAtIndex(layer, linePositionIndex)` | Line |
| `Transform GetMovedLineTransform(AreaReinforcementLayerType, Int32)` | `areaReinforcement.GetMovedLineTransform(layer, linePositionIndex)` | Transform |
| `Int32 GetNumberOfLines(AreaReinforcementLayerType)` | `areaReinforcement.GetNumberOfLines(layer)` | Int32 |
| `IList<ElementId> GetRebarInSystemIds()` | `areaReinforcement.GetRebarInSystemIds()` | IList<ElementId> |
| `Boolean IsLayerActive(AreaReinforcementLayerType)` | `areaReinforcement.IsLayerActive(layer)` | Boolean |
| `Boolean IsLineIncluded(AreaReinforcementLayerType, Int32)` | `areaReinforcement.IsLineIncluded(layer, linePositionIndex)` | Boolean |
| `Boolean IsUnobscuredInView(View)` | `areaReinforcement.IsUnobscuredInView(view)` | Boolean |
| `Void MoveLine(XYZ, AreaReinforcementLayerType, Int32)` | `areaReinforcement.MoveLine(translation, layer, linePositionIndex)` | Void |
| `IList<ElementId> RemoveAreaReinforcementSystem(Document, AreaReinforcement)` | `AreaReinforcement.RemoveAreaReinforcementSystem(doc, system)` | IList<ElementId> |
| `Void ResetMovedLineTransform(AreaReinforcementLayerType, Int32)` | `areaReinforcement.ResetMovedLineTransform(layer, linePositionIndex)` | Void |
| `Void SetLayerActive(Boolean, AreaReinforcementLayerType)` | `areaReinforcement.SetLayerActive(active, layer)` | Void |
| `Void SetLineIncluded(Boolean, AreaReinforcementLayerType, Int32)` | `areaReinforcement.SetLineIncluded(include, layer, linePositionIndex)` | Void |
| `Void SetUnobscuredInView(View, Boolean)` | `areaReinforcement.SetUnobscuredInView(view, unobscured)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
