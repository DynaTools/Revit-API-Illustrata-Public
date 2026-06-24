---
title: RebarBarType
classe: Autodesk.Revit.DB.Structure.RebarBarType
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.ElementType
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 29
---

# RebarBarType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double BarModelDiameter { get; set; }` | `rebarBarType.BarModelDiameter` | Double |
| `Double BarNominalDiameter { get; set; }` | `rebarBarType.BarNominalDiameter` | Double |
| `RebarDeformationType DeformationType { get; set; }` | `rebarBarType.DeformationType` | RebarDeformationType |
| `Double MaximumBendRadius { get; set; }` | `rebarBarType.MaximumBendRadius` | Double |
| `Double StandardBendDiameter { get; set; }` | `rebarBarType.StandardBendDiameter` | Double |
| `Double StandardHookBendDiameter { get; set; }` | `rebarBarType.StandardHookBendDiameter` | Double |
| `Double StirrupTieBendDiameter { get; set; }` | `rebarBarType.StirrupTieBendDiameter` | Double |
| `RebarBarType Create(Document)` | `RebarBarType.Create(ADoc)` | RebarBarType |
| `ElementId CreateDefaultRebarBarType(Document)` | `RebarBarType.CreateDefaultRebarBarType(ADoc)` | ElementId |
| `Boolean GetAutoCalcHookLengths(ElementId)` | `rebarBarType.GetAutoCalcHookLengths(hookId)` | Boolean |
| `Boolean GetAutoCalculatedLapLength(ElementId)` | `rebarBarType.GetAutoCalculatedLapLength(rebarSpliceTypeId)` | Boolean |
| `Boolean GetAutoCalculatedStaggerLength(ElementId)` | `rebarBarType.GetAutoCalculatedStaggerLength(rebarSpliceTypeId)` | Boolean |
| `Double GetHookLength(ElementId)` | `rebarBarType.GetHookLength(hookId)` | Double |
| `Double GetHookOffsetLength(ElementId)` | `rebarBarType.GetHookOffsetLength(hookId)` | Double |
| `Boolean GetHookPermission(ElementId)` | `rebarBarType.GetHookPermission(hookId)` | Boolean |
| `Double GetHookTangentLength(ElementId)` | `rebarBarType.GetHookTangentLength(hookId)` | Double |
| `Double GetLapLength(ElementId)` | `rebarBarType.GetLapLength(rebarSpliceTypeId)` | Double |
| `RebarRoundingManager GetReinforcementRoundingManager()` | `rebarBarType.GetReinforcementRoundingManager()` | RebarRoundingManager |
| `Double GetStaggerLength(ElementId)` | `rebarBarType.GetStaggerLength(rebarSpliceTypeId)` | Double |
| `Void SetAutoCalcHookLengths(ElementId, Boolean)` | `rebarBarType.SetAutoCalcHookLengths(hookId, autoCalculated)` | Void |
| `Void SetAutoCalculatedLapLength(ElementId, Boolean)` | `rebarBarType.SetAutoCalculatedLapLength(rebarSpliceTypeId, autoCalculated)` | Void |
| `Void SetAutoCalculatedStaggerLength(ElementId, Boolean)` | `rebarBarType.SetAutoCalculatedStaggerLength(rebarSpliceTypeId, autoCalculated)` | Void |
| `Void SetBarTypeDiameters(BarTypeDiameterOptions)` | `rebarBarType.SetBarTypeDiameters(diametersOptions)` | Void |
| `Void SetHookLength(ElementId, Double)` | `rebarBarType.SetHookLength(hookId, hookLength)` | Void |
| `Void SetHookOffsetLength(ElementId, Double)` | `rebarBarType.SetHookOffsetLength(hookId, newLength)` | Void |
| `Void SetHookPermission(ElementId, Boolean)` | `rebarBarType.SetHookPermission(hookId, permission)` | Void |
| `Void SetHookTangentLength(ElementId, Double)` | `rebarBarType.SetHookTangentLength(hookId, newLength)` | Void |
| `Void SetLapLength(ElementId, Double)` | `rebarBarType.SetLapLength(rebarSpliceTypeId, lapLength)` | Void |
| `Void SetStaggerLength(ElementId, Double)` | `rebarBarType.SetStaggerLength(rebarSpliceTypeId, staggerLength)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
