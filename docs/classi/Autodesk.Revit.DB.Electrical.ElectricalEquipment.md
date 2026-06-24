---
title: ElectricalEquipment
classe: Autodesk.Revit.DB.Electrical.ElectricalEquipment
namespace: Autodesk.Revit.DB.Electrical
eredita: Autodesk.Revit.DB.MEPModel
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# ElectricalEquipment

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId CircuitNamingSchemeId { get; set; }` | `electricalEquipment.CircuitNamingSchemeId` | ElementId |
| `DistributionSysType DistributionSystem { get; set; }` | `electricalEquipment.DistributionSystem` | DistributionSysType |
| `Boolean IsSwitchboard { get; }` | `electricalEquipment.IsSwitchboard` | Boolean |
| `Int32 MaxNumberOfCircuits { get; set; }` | `electricalEquipment.MaxNumberOfCircuits` | Int32 |
| `CircuitNaming GetCircuitNamingSchemeType()` | `electricalEquipment.GetCircuitNamingSchemeType()` | CircuitNaming |
| `Boolean IsValidCircuitNamingSchemeId(Document, ElementId)` | `ElectricalEquipment.IsValidCircuitNamingSchemeId(aDocument, circuitNamingSchemeId)` | Boolean |
| `Boolean IsValidDistributionSystem(DistributionSysType)` | `electricalEquipment.IsValidDistributionSystem(distributionSystem)` | Boolean |
| `Void SetCircuitNamingSchemeType(CircuitNaming)` | `electricalEquipment.SetCircuitNamingSchemeType(circuitNamingType)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
