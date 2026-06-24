---
title: ElectricalAnalyticalNode
classe: Autodesk.Revit.DB.Electrical.ElectricalAnalyticalNode
namespace: Autodesk.Revit.DB.Electrical
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# ElectricalAnalyticalNode

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElectricalAnalyticalNodeType NodeType { get; }` | `electricalAnalyticalNode.NodeType` | ElectricalAnalyticalNodeType |
| `Double TotalLoad { get; }` | `electricalAnalyticalNode.TotalLoad` | Double |
| `Boolean CanConnectToUpstreamNode(ElementId)` | `electricalAnalyticalNode.CanConnectToUpstreamNode(upstreamNodeId)` | Boolean |
| `Boolean CanDisconnectFromUpstreamNode(ElementId)` | `electricalAnalyticalNode.CanDisconnectFromUpstreamNode(upstreamNodeId)` | Boolean |
| `Void ConnectToUpstreamNode(ElementId)` | `electricalAnalyticalNode.ConnectToUpstreamNode(upstreamNodeId)` | Void |
| `ElectricalAnalyticalNode Create(Document, ElectricalAnalyticalNodeType, String)` | `ElectricalAnalyticalNode.Create(document, type, name)` | ElectricalAnalyticalNode |
| `Void DisconnectFromUpstreamNode(ElementId)` | `electricalAnalyticalNode.DisconnectFromUpstreamNode(upstreamNodeId)` | Void |
| `ISet<ElementId> GetAllDownstreamLoadIds()` | `electricalAnalyticalNode.GetAllDownstreamLoadIds()` | ISet<ElementId> |
| `AnalyticalDistributionNodePropertyData GetAnalyticalPropertyData()` | `electricalAnalyticalNode.GetAnalyticalPropertyData()` | AnalyticalDistributionNodePropertyData |
| `IList<ElementId> GetDownstreamNodeIds()` | `electricalAnalyticalNode.GetDownstreamNodeIds()` | IList<ElementId> |
| `IList<ElementId> GetUpstreamNodeIds()` | `electricalAnalyticalNode.GetUpstreamNodeIds()` | IList<ElementId> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
