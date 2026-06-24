---
title: FlexPipe
classe: Autodesk.Revit.DB.Plumbing.FlexPipe
namespace: Autodesk.Revit.DB.Plumbing
eredita: Autodesk.Revit.DB.MEPCurve
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# FlexPipe

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ EndTangent { get; set; }` | `flexPipe.EndTangent` | XYZ |
| `FlexPipeType FlexPipeType { get; set; }` | `flexPipe.FlexPipeType` | FlexPipeType |
| `PipeFlowState FlowState { get; }` | `flexPipe.FlowState` | PipeFlowState |
| `IList<XYZ> Points { get; set; }` | `flexPipe.Points` | IList<XYZ> |
| `XYZ StartTangent { get; set; }` | `flexPipe.StartTangent` | XYZ |
| `FlexPipe Create(Document, ElementId, ElementId, ElementId, XYZ, XYZ, IList<XYZ>)` | `FlexPipe.Create(document, systemTypeId, pipeTypeId, levelId, startTangent, endTangent, points)` | FlexPipe |
| `FlexPipe Create(Document, ElementId, ElementId, ElementId, IList<XYZ>)` | `FlexPipe.Create(document, systemTypeId, pipeTypeId, levelId, points)` | FlexPipe |
| `Boolean IsFlexPipeTypeId(Document, ElementId)` | `FlexPipe.IsFlexPipeTypeId(document, pipeTypeId)` | Boolean |
| `Boolean IsPipingSystemTypeId(Document, ElementId)` | `FlexPipe.IsPipingSystemTypeId(document, systemTypeId)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
