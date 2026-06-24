---
title: AnalyticalPowerDistributableNodeData
classe: Autodesk.Revit.DB.Electrical.AnalyticalPowerDistributableNodeData
namespace: Autodesk.Revit.DB.Electrical
eredita: Autodesk.Revit.DB.Electrical.AnalyticalDistributionNodePropertyData
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# AnalyticalPowerDistributableNodeData

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 AssignedPhasesNumber { get; }` | `analyticalPowerDistributableNodeData.AssignedPhasesNumber` | Int32 |
| `Double AssignedVoltage { get; }` | `analyticalPowerDistributableNodeData.AssignedVoltage` | Double |
| `ElementId DistributionSystem { get; set; }` | `analyticalPowerDistributableNodeData.DistributionSystem` | ElementId |
| `IList<ElectricalConnectedPhases> GetAllAvailableConnectedPhasesOnDownstream(ElementId)` | `analyticalPowerDistributableNodeData.GetAllAvailableConnectedPhasesOnDownstream(id)` | IList<ElectricalConnectedPhases> |
| `ElectricalPerPhaseData GetApparentPerPhaseResults()` | `analyticalPowerDistributableNodeData.GetApparentPerPhaseResults()` | ElectricalPerPhaseData |
| `ElectricalConnectedPhases GetConnectedPhasesOnDownstream(ElementId)` | `analyticalPowerDistributableNodeData.GetConnectedPhasesOnDownstream(id)` | ElectricalConnectedPhases |
| `ElectricalPerPhaseData GetDemandPerPhaseResults()` | `analyticalPowerDistributableNodeData.GetDemandPerPhaseResults()` | ElectricalPerPhaseData |
| `Void SetConnectedPhasesOnDownstream(ElementId, ElectricalConnectedPhases)` | `analyticalPowerDistributableNodeData.SetConnectedPhasesOnDownstream(id, connectedPhases)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
