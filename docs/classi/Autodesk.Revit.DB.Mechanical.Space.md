---
title: Space
classe: Autodesk.Revit.DB.Mechanical.Space
namespace: Autodesk.Revit.DB.Mechanical
eredita: Autodesk.Revit.DB.SpatialElement
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 54
---

# Space

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double ActualExhaustAirflow { get; }` | `space.ActualExhaustAirflow` | Double |
| `Double ActualHVACLoad { get; }` | `space.ActualHVACLoad` | Double |
| `Double ActualLightingLoad { get; }` | `space.ActualLightingLoad` | Double |
| `Double ActualOtherLoad { get; }` | `space.ActualOtherLoad` | Double |
| `Double ActualPowerLoad { get; }` | `space.ActualPowerLoad` | Double |
| `Double ActualReturnAirflow { get; }` | `space.ActualReturnAirflow` | Double |
| `Double ActualSupplyAirflow { get; }` | `space.ActualSupplyAirflow` | Double |
| `Double AirChangesPerHour { get; }` | `space.AirChangesPerHour` | Double |
| `Double AreaperPerson { get; set; }` | `space.AreaperPerson` | Double |
| `Double AverageEstimatedIllumination { get; }` | `space.AverageEstimatedIllumination` | Double |
| `BaseLoadOn BaseHeatLoadOn { get; set; }` | `space.BaseHeatLoadOn` | BaseLoadOn |
| `Double BaseOffset { get; set; }` | `space.BaseOffset` | Double |
| `Double CalculatedCoolingLoad { get; }` | `space.CalculatedCoolingLoad` | Double |
| `Double CalculatedHeatingLoad { get; }` | `space.CalculatedHeatingLoad` | Double |
| `Double CalculatedSupplyAirflow { get; }` | `space.CalculatedSupplyAirflow` | Double |
| `Double CeilingReflectance { get; set; }` | `space.CeilingReflectance` | Double |
| `GeometryElement ClosedShell { get; }` | `space.ClosedShell` | GeometryElement |
| `ConditionType ConditionType { get; set; }` | `space.ConditionType` | ConditionType |
| `Double DesignCoolingLoad { get; set; }` | `space.DesignCoolingLoad` | Double |
| `Double DesignExhaustAirflow { get; set; }` | `space.DesignExhaustAirflow` | Double |
| `Double DesignHeatingLoad { get; set; }` | `space.DesignHeatingLoad` | Double |
| `Double DesignHVACLoadperArea { get; set; }` | `space.DesignHVACLoadperArea` | Double |
| `Double DesignLightingLoad { get; set; }` | `space.DesignLightingLoad` | Double |
| `Double DesignOtherLoadperArea { get; set; }` | `space.DesignOtherLoadperArea` | Double |
| `Double DesignPowerLoad { get; set; }` | `space.DesignPowerLoad` | Double |
| `Double DesignReturnAirflow { get; set; }` | `space.DesignReturnAirflow` | Double |
| `Double DesignSupplyAirflow { get; set; }` | `space.DesignSupplyAirflow` | Double |
| `Double FloorReflectance { get; set; }` | `space.FloorReflectance` | Double |
| `Double LatentHeatGainperPerson { get; set; }` | `space.LatentHeatGainperPerson` | Double |
| `Double LightingCalculationWorkplane { get; set; }` | `space.LightingCalculationWorkplane` | Double |
| `BaseLoadOn LightingLoadUnit { get; set; }` | `space.LightingLoadUnit` | BaseLoadOn |
| `Double LimitOffset { get; set; }` | `space.LimitOffset` | Double |
| `Double NumberofPeople { get; set; }` | `space.NumberofPeople` | Double |
| `OccupancyUnit OccupancyUnit { get; set; }` | `space.OccupancyUnit` | OccupancyUnit |
| `Boolean Occupiable { get; }` | `space.Occupiable` | Boolean |
| `Double OutdoorAirflow { get; }` | `space.OutdoorAirflow` | Double |
| `OutdoorAirFlowStandard OutdoorAirFlowStandard { get; }` | `space.OutdoorAirFlowStandard` | OutdoorAirFlowStandard |
| `Double OutdoorAirPerArea { get; }` | `space.OutdoorAirPerArea` | Double |
| `Double OutdoorAirPerPerson { get; }` | `space.OutdoorAirPerPerson` | Double |
| `Boolean Plenum { get; }` | `space.Plenum` | Boolean |
| `BaseLoadOn PowerLoadUnit { get; set; }` | `space.PowerLoadUnit` | BaseLoadOn |
| `ReturnAirflowType ReturnAirflow { get; set; }` | `space.ReturnAirflow` | ReturnAirflowType |
| `Room Room { get; }` | `space.Room` | Room |
| `Double SensibleHeatGainperPerson { get; set; }` | `space.SensibleHeatGainperPerson` | Double |
| `Double SpaceCavityRatio { get; }` | `space.SpaceCavityRatio` | Double |
| `MEPSpaceConstruction SpaceConstruction { get; }` | `space.SpaceConstruction` | MEPSpaceConstruction |
| `SpaceType SpaceType { get; set; }` | `space.SpaceType` | SpaceType |
| `ElementId SpaceTypeId { get; set; }` | `space.SpaceTypeId` | ElementId |
| `Double UnboundedHeight { get; }` | `space.UnboundedHeight` | Double |
| `Level UpperLimit { get; set; }` | `space.UpperLimit` | Level |
| `Double Volume { get; }` | `space.Volume` | Double |
| `Double WallReflectance { get; set; }` | `space.WallReflectance` | Double |
| `Zone Zone { get; }` | `space.Zone` | Zone |
| `Boolean IsPointInSpace(XYZ)` | `space.IsPointInSpace(point)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
