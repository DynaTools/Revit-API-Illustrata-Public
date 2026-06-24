---
title: MEPAnalyticalConnection
classe: Autodesk.Revit.DB.MEPAnalyticalConnection
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.MEPCurve
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 4
---

# MEPAnalyticalConnection

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean CanSupportAnalyticalConnection(Connector)` | `MEPAnalyticalConnection.CanSupportAnalyticalConnection(connector)` | Boolean |
| `MEPAnalyticalConnection Create(Document, ElementId, Connector, Connector)` | `MEPAnalyticalConnection.Create(doc, typeId, startConnector, endConnector)` | MEPAnalyticalConnection |
| `ISet<ElementId> CreateMultipleConnections(Document, ElementId, IList<Connector>, IList<ElementId>)` | `MEPAnalyticalConnection.CreateMultipleConnections(doc, typeId, equipmentOpenConnectors, curveIdsToConnect)` | ISet<ElementId> |
| `Double GetFlow()` | `mEPAnalyticalConnection.GetFlow()` | Double |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
