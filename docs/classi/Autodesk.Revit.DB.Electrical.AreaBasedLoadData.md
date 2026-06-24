---
title: AreaBasedLoadData
classe: Autodesk.Revit.DB.Electrical.AreaBasedLoadData
namespace: Autodesk.Revit.DB.Electrical
eredita: Autodesk.Revit.DB.Mechanical.ZoneElementDomainData
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 21
---

# AreaBasedLoadData

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double ApparentLoad { get; }` | `areaBasedLoadData.ApparentLoad` | Double |
| `Double ApparentPowerDensity { get; }` | `areaBasedLoadData.ApparentPowerDensity` | Double |
| `ElementId AreaBasedLoadType { get; set; }` | `areaBasedLoadData.AreaBasedLoadType` | ElementId |
| `ElectricalConnectedPhases ConnectedPhases { get; }` | `areaBasedLoadData.ConnectedPhases` | ElectricalConnectedPhases |
| `Double Current { get; }` | `areaBasedLoadData.Current` | Double |
| `ElementId LoadClassification { get; }` | `areaBasedLoadData.LoadClassification` | ElementId |
| `Double LoadDensity { get; }` | `areaBasedLoadData.LoadDensity` | Double |
| `ElectricalLoadType LoadType { get; }` | `areaBasedLoadData.LoadType` | ElectricalLoadType |
| `Int32 PhasesNumber { get; set; }` | `areaBasedLoadData.PhasesNumber` | Int32 |
| `Double PowerFactor { get; }` | `areaBasedLoadData.PowerFactor` | Double |
| `PowerFactorStateType PowerFactorState { get; }` | `areaBasedLoadData.PowerFactorState` | PowerFactorStateType |
| `Double TrueLoad { get; }` | `areaBasedLoadData.TrueLoad` | Double |
| `Double Voltage { get; set; }` | `areaBasedLoadData.Voltage` | Double |
| `Void AddElectricalLoadArea(ElementId)` | `areaBasedLoadData.AddElectricalLoadArea(electricalLoadAreaId)` | Void |
| `Boolean CanConnectToUpstreamNode(ElementId)` | `areaBasedLoadData.CanConnectToUpstreamNode(upstreamNodeId)` | Boolean |
| `Boolean CanDisconnectFromUpstreamNode()` | `areaBasedLoadData.CanDisconnectFromUpstreamNode()` | Boolean |
| `Void ConnectToUpstreamNode(ElementId)` | `areaBasedLoadData.ConnectToUpstreamNode(upstreamNodeId)` | Void |
| `Void DisconnectFromUpstreamNode()` | `areaBasedLoadData.DisconnectFromUpstreamNode()` | Void |
| `ISet<ElementId> GetElectricalLoadAreas()` | `areaBasedLoadData.GetElectricalLoadAreas()` | ISet<ElementId> |
| `ElementId GetUpstreamNodeId()` | `areaBasedLoadData.GetUpstreamNodeId()` | ElementId |
| `Void RemoveElectricalLoadArea(ElementId)` | `areaBasedLoadData.RemoveElectricalLoadArea(electricalLoadAreaId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
