---
title: PipingSystem
classe: Autodesk.Revit.DB.Plumbing.PipingSystem
namespace: Autodesk.Revit.DB.Plumbing
eredita: Autodesk.Revit.DB.MEPSystem
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 17
---

# PipingSystem

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Connector BaseEquipmentConnector { get; set; }` | `pipingSystem.BaseEquipmentConnector` | Connector |
| `Boolean IsWellConnected { get; }` | `pipingSystem.IsWellConnected` | Boolean |
| `ElementSet PipingNetwork { get; }` | `pipingSystem.PipingNetwork` | ElementSet |
| `PipeSystemType SystemType { get; }` | `pipingSystem.SystemType` | PipeSystemType |
| `Boolean CanBeHydraulicLoopBoundary(Element)` | `PipingSystem.CanBeHydraulicLoopBoundary(element)` | Boolean |
| `PipingSystem Create(Document, ElementId, String)` | `PipingSystem.Create(ADocument, typeId, name)` | PipingSystem |
| `PipingSystem Create(Document, ElementId)` | `PipingSystem.Create(ADocument, typeId)` | PipingSystem |
| `ISet<ElementId> CreateHydraulicSeparation(Document, ISet<ElementId>)` | `PipingSystem.CreateHydraulicSeparation(document, pipeElementIds)` | ISet<ElementId> |
| `Void DeleteHydraulicSeparation(Document, ISet<ElementId>)` | `PipingSystem.DeleteHydraulicSeparation(document, pipeElementIds)` | Void |
| `Double GetFixtureUnits()` | `pipingSystem.GetFixtureUnits()` | Double |
| `Double GetFlow()` | `pipingSystem.GetFlow()` | Double |
| `ISet<ElementId> GetPumpSets()` | `pipingSystem.GetPumpSets()` | ISet<ElementId> |
| `Double GetStaticPressure()` | `pipingSystem.GetStaticPressure()` | Double |
| `Double GetVolume()` | `pipingSystem.GetVolume()` | Double |
| `Boolean IsFlowServerMissing()` | `pipingSystem.IsFlowServerMissing()` | Boolean |
| `Boolean IsHydraulicLoopBoundary(Element)` | `PipingSystem.IsHydraulicLoopBoundary(element)` | Boolean |
| `Boolean IsPressureDropServerMissing()` | `pipingSystem.IsPressureDropServerMissing()` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
