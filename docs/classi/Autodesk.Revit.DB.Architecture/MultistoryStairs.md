---
title: MultistoryStairs
classe: Autodesk.Revit.DB.Architecture.MultistoryStairs
namespace: Autodesk.Revit.DB.Architecture
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 15
---

# MultistoryStairs

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double ActualTreadDepth { get; set; }` | `multistoryStairs.ActualTreadDepth` | Double |
| `ElementId StandardStairsId { get; }` | `multistoryStairs.StandardStairsId` | ElementId |
| `Boolean CanConnectLevel(ElementId)` | `multistoryStairs.CanConnectLevel(levelId)` | Boolean |
| `Boolean CanDisconnectLevel(ElementId)` | `multistoryStairs.CanDisconnectLevel(levelId)` | Boolean |
| `Void ConnectLevels(ISet<ElementId>)` | `multistoryStairs.ConnectLevels(levelIds)` | Void |
| `MultistoryStairs Create(Stairs)` | `MultistoryStairs.Create(stairs)` | MultistoryStairs |
| `Void DisconnectLevels(ISet<ElementId>)` | `multistoryStairs.DisconnectLevels(levelIds)` | Void |
| `ISet<ElementId> GetAllConnectedLevels()` | `multistoryStairs.GetAllConnectedLevels()` | ISet<ElementId> |
| `ISet<ElementId> GetAllStairsIds()` | `multistoryStairs.GetAllStairsIds()` | ISet<ElementId> |
| `Stairs GetStairsOnLevel(ElementId)` | `multistoryStairs.GetStairsOnLevel(levelId)` | Stairs |
| `ISet<ElementId> GetStairsPlacementLevels(Stairs)` | `multistoryStairs.GetStairsPlacementLevels(stairs)` | ISet<ElementId> |
| `Boolean IsAcceptableForMultistoryStairs(Stairs)` | `MultistoryStairs.IsAcceptableForMultistoryStairs(stairs)` | Boolean |
| `Boolean IsPinned(Stairs)` | `multistoryStairs.IsPinned(stairs)` | Boolean |
| `Stairs Pin(ElementId)` | `multistoryStairs.Pin(levelId)` | Stairs |
| `Stairs Unpin(ElementId)` | `multistoryStairs.Unpin(levelId)` | Stairs |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
