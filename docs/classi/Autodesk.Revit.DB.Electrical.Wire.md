---
title: Wire
classe: Autodesk.Revit.DB.Electrical.Wire
namespace: Autodesk.Revit.DB.Electrical
eredita: Autodesk.Revit.DB.MEPCurve
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 15
---

# Wire

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 GroundConductorNum { get; set; }` | `wire.GroundConductorNum` | Int32 |
| `Int32 HotConductorNum { get; set; }` | `wire.HotConductorNum` | Int32 |
| `Int32 NeutralConductorNum { get; set; }` | `wire.NeutralConductorNum` | Int32 |
| `Int32 NumberOfVertices { get; }` | `wire.NumberOfVertices` | Int32 |
| `WiringType WiringType { get; set; }` | `wire.WiringType` | WiringType |
| `Void AppendVertex(XYZ)` | `wire.AppendVertex(vertexPoint)` | Void |
| `Boolean AreVertexPointsValid(IList<XYZ>, Connector, Connector)` | `Wire.AreVertexPointsValid(vertexPoints, startConnector, endConnector)` | Boolean |
| `Void ConnectTo(Connector, Connector)` | `wire.ConnectTo(startConnectorTo, endConnectorTo)` | Void |
| `Wire Create(Document, ElementId, ElementId, WiringType, IList<XYZ>, Connector, Connector)` | `Wire.Create(document, wireTypeId, viewId, wiringType, vertexPoints, startConnectorTo, endConnectorTo)` | Wire |
| `IList<ElementId> GetMEPSystems()` | `wire.GetMEPSystems()` | IList<ElementId> |
| `XYZ GetVertex(Int32)` | `wire.GetVertex(index)` | XYZ |
| `Void InsertVertex(Int32, XYZ)` | `wire.InsertVertex(index, vertexPoint)` | Void |
| `Boolean IsVertexPointValid(XYZ)` | `wire.IsVertexPointValid(vertexPoint)` | Boolean |
| `Void RemoveVertex(Int32)` | `wire.RemoveVertex(index)` | Void |
| `Void SetVertex(Int32, XYZ)` | `wire.SetVertex(index, vertexPoint)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
