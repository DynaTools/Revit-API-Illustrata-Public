---
title: Pipe
classe: Autodesk.Revit.DB.Plumbing.Pipe
namespace: Autodesk.Revit.DB.Plumbing
eredita: Autodesk.Revit.DB.MEPCurve
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 12
---

# Pipe

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `PipeFlowState FlowState { get; }` | `pipe.FlowState` | PipeFlowState |
| `Boolean IsPlaceholder { get; }` | `pipe.IsPlaceholder` | Boolean |
| `PipeSegment PipeSegment { get; }` | `pipe.PipeSegment` | PipeSegment |
| `PipeType PipeType { get; set; }` | `pipe.PipeType` | PipeType |
| `Pipe Create(Document, ElementId, ElementId, Connector, Connector)` | `Pipe.Create(document, pipeTypeId, levelId, startConnector, endConnector)` | Pipe |
| `Pipe Create(Document, ElementId, ElementId, Connector, XYZ)` | `Pipe.Create(document, pipeTypeId, levelId, startConnector, endPoint)` | Pipe |
| `Pipe Create(Document, ElementId, ElementId, ElementId, XYZ, XYZ)` | `Pipe.Create(document, systemTypeId, pipeTypeId, levelId, startPoint, endPoint)` | Pipe |
| `Pipe CreatePlaceholder(Document, ElementId, ElementId, ElementId, XYZ, XYZ)` | `Pipe.CreatePlaceholder(document, systemTypeId, pipeTypeId, levelId, startPoint, endPoint)` | Pipe |
| `Boolean IsPipeTypeId(Document, ElementId)` | `Pipe.IsPipeTypeId(document, pipeTypeId)` | Boolean |
| `Boolean IsPipingConnector(Connector)` | `Pipe.IsPipingConnector(connector)` | Boolean |
| `Boolean IsPipingSystemTypeId(Document, ElementId)` | `Pipe.IsPipingSystemTypeId(document, systemTypeId)` | Boolean |
| `Void SetSystemType(ElementId)` | `pipe.SetSystemType(systemTypeId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
