---
title: RebarCoupler
classe: Autodesk.Revit.DB.Structure.RebarCoupler
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# RebarCoupler

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String CouplerMark { get; set; }` | `rebarCoupler.CouplerMark` | String |
| `Double RotationAngle { get; set; }` | `rebarCoupler.RotationAngle` | Double |
| `Boolean CouplerLinkTwoBars()` | `rebarCoupler.CouplerLinkTwoBars()` | Boolean |
| `RebarCoupler Create(Document, ElementId, ReinforcementData, ReinforcementData, RebarCouplerError&)` | `RebarCoupler.Create(doc, typeId, pFirstData, pSecondData, error)` | RebarCoupler |
| `IList<ReinforcementData> GetCoupledReinforcementData()` | `rebarCoupler.GetCoupledReinforcementData()` | IList<ReinforcementData> |
| `Transform GetCouplerPositionTransform(Int32)` | `rebarCoupler.GetCouplerPositionTransform(couplerPositionIndex)` | Transform |
| `Int32 GetCouplerQuantity()` | `rebarCoupler.GetCouplerQuantity()` | Int32 |
| `IList<XYZ> GetPointsForPlacement()` | `rebarCoupler.GetPointsForPlacement()` | IList<XYZ> |
| `Boolean IsUnobscuredInView(View)` | `rebarCoupler.IsUnobscuredInView(view)` | Boolean |
| `Void SetUnobscuredInView(View, Boolean)` | `rebarCoupler.SetUnobscuredInView(view, unobscured)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
