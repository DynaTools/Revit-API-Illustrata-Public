---
title: ConnectorElement
classe: Autodesk.Revit.DB.ConnectorElement
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 27
---

# ConnectorElement

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Transform CoordinateSystem { get; }` | `connectorElement.CoordinateSystem` | Transform |
| `XYZ Direction { get; }` | `connectorElement.Direction` | XYZ |
| `Domain Domain { get; }` | `connectorElement.Domain` | Domain |
| `Double Height { get; }` | `connectorElement.Height` | Double |
| `Boolean IsPrimary { get; }` | `connectorElement.IsPrimary` | Boolean |
| `XYZ Origin { get; }` | `connectorElement.Origin` | XYZ |
| `Double Radius { get; }` | `connectorElement.Radius` | Double |
| `ConnectorProfileType Shape { get; }` | `connectorElement.Shape` | ConnectorProfileType |
| `MEPSystemClassification SystemClassification { get; set; }` | `connectorElement.SystemClassification` | MEPSystemClassification |
| `Double Width { get; }` | `connectorElement.Width` | Double |
| `Void AssignAsPrimary()` | `connectorElement.AssignAsPrimary()` | Void |
| `Void ChangeHostReference(Reference, Edge)` | `connectorElement.ChangeHostReference(planarFace, edge)` | Void |
| `Void ChangeHostReference(Reference)` | `connectorElement.ChangeHostReference(planarFace)` | Void |
| `ConnectorElement CreateCableTrayConnector(Document, Reference, Edge)` | `ConnectorElement.CreateCableTrayConnector(document, planarFace, edge)` | ConnectorElement |
| `ConnectorElement CreateCableTrayConnector(Document, Reference)` | `ConnectorElement.CreateCableTrayConnector(document, planarFace)` | ConnectorElement |
| `ConnectorElement CreateConduitConnector(Document, Reference, Edge)` | `ConnectorElement.CreateConduitConnector(document, planarFace, edge)` | ConnectorElement |
| `ConnectorElement CreateConduitConnector(Document, Reference)` | `ConnectorElement.CreateConduitConnector(document, planarFace)` | ConnectorElement |
| `ConnectorElement CreateDuctConnector(Document, DuctSystemType, ConnectorProfileType, Reference, Edge)` | `ConnectorElement.CreateDuctConnector(document, ductSystemType, profileShape, planarFace, edge)` | ConnectorElement |
| `ConnectorElement CreateDuctConnector(Document, DuctSystemType, ConnectorProfileType, Reference)` | `ConnectorElement.CreateDuctConnector(document, ductSystemType, profileShape, planarFace)` | ConnectorElement |
| `ConnectorElement CreateElectricalConnector(Document, ElectricalSystemType, Reference, Edge)` | `ConnectorElement.CreateElectricalConnector(document, electricalSystemType, planarFace, edge)` | ConnectorElement |
| `ConnectorElement CreateElectricalConnector(Document, ElectricalSystemType, Reference)` | `ConnectorElement.CreateElectricalConnector(document, electricalSystemType, planarFace)` | ConnectorElement |
| `ConnectorElement CreatePipeConnector(Document, PipeSystemType, Reference, Edge)` | `ConnectorElement.CreatePipeConnector(document, pipeSystemType, planarFace, edge)` | ConnectorElement |
| `ConnectorElement CreatePipeConnector(Document, PipeSystemType, Reference)` | `ConnectorElement.CreatePipeConnector(document, pipeSystemType, planarFace)` | ConnectorElement |
| `Void FlipDirection()` | `connectorElement.FlipDirection()` | Void |
| `ConnectorElement GetLinkedConnectorElement()` | `connectorElement.GetLinkedConnectorElement()` | ConnectorElement |
| `Boolean IsSystemClassificationValid(MEPSystemClassification)` | `connectorElement.IsSystemClassificationValid(systemClassification)` | Boolean |
| `Void SetLinkedConnectorElement(ConnectorElement)` | `connectorElement.SetLinkedConnectorElement(otherConnector)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
