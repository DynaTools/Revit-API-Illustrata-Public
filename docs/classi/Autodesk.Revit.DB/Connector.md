---
title: Connector
classe: Autodesk.Revit.DB.Connector
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 48
---

# Connector

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean AllowsSlopeAdjustments { get; }` | `connector.AllowsSlopeAdjustments` | Boolean |
| `ConnectorSet AllRefs { get; }` | `connector.AllRefs` | ConnectorSet |
| `Double Angle { get; set; }` | `connector.Angle` | Double |
| `DuctFlowConfigurationType AssignedDuctFlowConfiguration { get; }` | `connector.AssignedDuctFlowConfiguration` | DuctFlowConfigurationType |
| `DuctLossMethodType AssignedDuctLossMethod { get; }` | `connector.AssignedDuctLossMethod` | DuctLossMethodType |
| `Double AssignedFixtureUnits { get; set; }` | `connector.AssignedFixtureUnits` | Double |
| `Double AssignedFlow { get; set; }` | `connector.AssignedFlow` | Double |
| `FlowDirectionType AssignedFlowDirection { get; }` | `connector.AssignedFlowDirection` | FlowDirectionType |
| `Double AssignedFlowFactor { get; set; }` | `connector.AssignedFlowFactor` | Double |
| `Double AssignedKCoefficient { get; set; }` | `connector.AssignedKCoefficient` | Double |
| `Double AssignedLossCoefficient { get; set; }` | `connector.AssignedLossCoefficient` | Double |
| `PipeFlowConfigurationType AssignedPipeFlowConfiguration { get; }` | `connector.AssignedPipeFlowConfiguration` | PipeFlowConfigurationType |
| `PipeLossMethodType AssignedPipeLossMethod { get; }` | `connector.AssignedPipeLossMethod` | PipeLossMethodType |
| `Double AssignedPressureDrop { get; set; }` | `connector.AssignedPressureDrop` | Double |
| `Double Coefficient { get; }` | `connector.Coefficient` | Double |
| `ConnectorManager ConnectorManager { get; }` | `connector.ConnectorManager` | ConnectorManager |
| `ConnectorType ConnectorType { get; }` | `connector.ConnectorType` | ConnectorType |
| `Transform CoordinateSystem { get; }` | `connector.CoordinateSystem` | Transform |
| `Double Demand { get; }` | `connector.Demand` | Double |
| `String Description { get; }` | `connector.Description` | String |
| `FlowDirectionType Direction { get; }` | `connector.Direction` | FlowDirectionType |
| `Domain Domain { get; }` | `connector.Domain` | Domain |
| `DuctSystemType DuctSystemType { get; }` | `connector.DuctSystemType` | DuctSystemType |
| `ElectricalSystemType ElectricalSystemType { get; }` | `connector.ElectricalSystemType` | ElectricalSystemType |
| `Double EngagementLength { get; }` | `connector.EngagementLength` | Double |
| `Double Flow { get; }` | `connector.Flow` | Double |
| `Double GasketLength { get; }` | `connector.GasketLength` | Double |
| `Double Height { get; set; }` | `connector.Height` | Double |
| `Int32 Id { get; }` | `connector.Id` | Int32 |
| `Boolean IsConnected { get; }` | `connector.IsConnected` | Boolean |
| `Boolean IsMovable { get; }` | `connector.IsMovable` | Boolean |
| `Boolean IsValidObject { get; }` | `connector.IsValidObject` | Boolean |
| `MEPSystem MEPSystem { get; }` | `connector.MEPSystem` | MEPSystem |
| `XYZ Origin { get; set; }` | `connector.Origin` | XYZ |
| `Element Owner { get; }` | `connector.Owner` | Element |
| `PipeSystemType PipeSystemType { get; }` | `connector.PipeSystemType` | PipeSystemType |
| `Double PressureDrop { get; }` | `connector.PressureDrop` | Double |
| `Double Radius { get; set; }` | `connector.Radius` | Double |
| `ConnectorProfileType Shape { get; }` | `connector.Shape` | ConnectorProfileType |
| `Boolean Utility { get; }` | `connector.Utility` | Boolean |
| `Double VelocityPressure { get; }` | `connector.VelocityPressure` | Double |
| `Double Width { get; set; }` | `connector.Width` | Double |
| `Void ConnectTo(Connector)` | `connector.ConnectTo(connector)` | Void |
| `Void DisconnectFrom(Connector)` | `connector.DisconnectFrom(connector)` | Void |
| `Void Dispose()` | `connector.Dispose()` | Void |
| `FabricationConnectorInfo GetFabricationConnectorInfo()` | `connector.GetFabricationConnectorInfo()` | FabricationConnectorInfo |
| `MEPConnectorInfo GetMEPConnectorInfo()` | `connector.GetMEPConnectorInfo()` | MEPConnectorInfo |
| `Boolean IsConnectedTo(Connector)` | `connector.IsConnectedTo(connector)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
