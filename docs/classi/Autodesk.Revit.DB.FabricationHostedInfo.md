---
title: FabricationHostedInfo
classe: Autodesk.Revit.DB.FabricationHostedInfo
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# FabricationHostedInfo

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId HostId { get; }` | `fabricationHostedInfo.HostId` | ElementId |
| `Boolean IsValidObject { get; }` | `fabricationHostedInfo.IsValidObject` | Boolean |
| `Void DisconnectFromHost()` | `fabricationHostedInfo.DisconnectFromHost()` | Void |
| `Void Dispose()` | `fabricationHostedInfo.Dispose()` | Void |
| `Line GetBearerCenterline()` | `fabricationHostedInfo.GetBearerCenterline()` | Line |
| `Void PlaceOnHost(ElementId, Connector, Double, Double)` | `fabricationHostedInfo.PlaceOnHost(hostId, hostConnector, distance, axisRotation)` | Void |
| `Void PlaceOnHost(ElementId, Connector, Double)` | `fabricationHostedInfo.PlaceOnHost(hostId, hostConnector, distance)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
