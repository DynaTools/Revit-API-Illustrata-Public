---
title: WallSweep
classe: Autodesk.Revit.DB.WallSweep
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.HostObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 4
---

# WallSweep

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `WallSweep Create(Wall, ElementId, WallSweepInfo)` | `WallSweep.Create(wall, wallSweepType, wallSweepInfo)` | WallSweep |
| `IList<ElementId> GetHostIds()` | `wallSweep.GetHostIds()` | IList<ElementId> |
| `WallSweepInfo GetWallSweepInfo()` | `wallSweep.GetWallSweepInfo()` | WallSweepInfo |
| `Boolean WallAllowsWallSweep(Wall)` | `WallSweep.WallAllowsWallSweep(wall)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
