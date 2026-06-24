---
title: ElectricalSetting
classe: Autodesk.Revit.DB.Electrical.ElectricalSetting
namespace: Autodesk.Revit.DB.Electrical
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 26
---

# ElectricalSetting

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `CircuitLoadCalculationMethod CircuitLoadCalculationMethod { get; set; }` | `electricalSetting.CircuitLoadCalculationMethod` | CircuitLoadCalculationMethod |
| `String CircuitNamePhaseA { get; set; }` | `electricalSetting.CircuitNamePhaseA` | String |
| `String CircuitNamePhaseB { get; set; }` | `electricalSetting.CircuitNamePhaseB` | String |
| `String CircuitNamePhaseC { get; set; }` | `electricalSetting.CircuitNamePhaseC` | String |
| `Double CircuitPathOffset { get; set; }` | `electricalSetting.CircuitPathOffset` | Double |
| `Double CircuitRating { get; set; }` | `electricalSetting.CircuitRating` | Double |
| `CircuitSequence CircuitSequence { get; set; }` | `electricalSetting.CircuitSequence` | CircuitSequence |
| `DistributionSysTypeSet DistributionSysTypes { get; }` | `electricalSetting.DistributionSysTypes` | DistributionSysTypeSet |
| `VoltageTypeSet VoltageTypes { get; }` | `electricalSetting.VoltageTypes` | VoltageTypeSet |
| `WireConduitTypeSet WireConduitTypes { get; }` | `electricalSetting.WireConduitTypes` | WireConduitTypeSet |
| `WireMaterialTypeSet WireMaterialTypes { get; }` | `electricalSetting.WireMaterialTypes` | WireMaterialTypeSet |
| `WireTypeSet WireTypes { get; }` | `electricalSetting.WireTypes` | WireTypeSet |
| `DistributionSysType AddDistributionSysType(String, ElectricalPhase, ElectricalPhaseConfiguration, Int32, VoltageType, VoltageType)` | `electricalSetting.AddDistributionSysType(name, phase, phaseConfig, numWire, volLineToLine, volLineToGround)` | DistributionSysType |
| `VoltageType AddVoltageType(String, Double, Double, Double)` | `electricalSetting.AddVoltageType(name, actualValue, minValue, maxValue)` | VoltageType |
| `WireMaterialType AddWireMaterialType(String, WireMaterialType)` | `electricalSetting.AddWireMaterialType(name, baseMaterial)` | WireMaterialType |
| `WireType AddWireType(String, WireMaterialType, TemperatureRatingType, InsulationType, WireSize, Double, Boolean, NeutralMode, WireConduitType)` | `electricalSetting.AddWireType(name, materialType, temperatureRating, insulation, maxSize, neutralMultiplier, neutralRequired, neutralMode, conduit)` | WireType |
| `CircuitNamingSchemeSettings GetCircuitNamingSchemeSettings(Document)` | `ElectricalSetting.GetCircuitNamingSchemeSettings(cda)` | CircuitNamingSchemeSettings |
| `ElectricalSetting GetElectricalSettings(Document)` | `ElectricalSetting.GetElectricalSettings(document)` | ElectricalSetting |
| `IList<Double> GetSpecificFittingAngles()` | `electricalSetting.GetSpecificFittingAngles()` | IList<Double> |
| `Boolean GetSpecificFittingAngleStatus(Double)` | `electricalSetting.GetSpecificFittingAngleStatus(angle)` | Boolean |
| `Boolean IsValidSpecificFittingAngle(Double)` | `electricalSetting.IsValidSpecificFittingAngle(angle)` | Boolean |
| `Void RemoveDistributionSysType(DistributionSysType)` | `electricalSetting.RemoveDistributionSysType(distributionSysType)` | Void |
| `Void RemoveVoltageType(VoltageType)` | `electricalSetting.RemoveVoltageType(voltageType)` | Void |
| `Void RemoveWireMaterialType(WireMaterialType)` | `electricalSetting.RemoveWireMaterialType(materialType)` | Void |
| `Void RemoveWireType(WireType)` | `electricalSetting.RemoveWireType(wireType)` | Void |
| `Void SetSpecificFittingAngleStatus(Double, Boolean)` | `electricalSetting.SetSpecificFittingAngleStatus(angle, bStatus)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
