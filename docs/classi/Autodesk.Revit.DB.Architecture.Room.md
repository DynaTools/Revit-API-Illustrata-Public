---
title: Room
classe: Autodesk.Revit.DB.Architecture.Room
namespace: Autodesk.Revit.DB.Architecture
eredita: Autodesk.Revit.DB.SpatialElement
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# Room

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double BaseOffset { get; set; }` | `room.BaseOffset` | Double |
| `GeometryElement ClosedShell { get; }` | `room.ClosedShell` | GeometryElement |
| `Double LimitOffset { get; set; }` | `room.LimitOffset` | Double |
| `Double UnboundedHeight { get; }` | `room.UnboundedHeight` | Double |
| `Level UpperLimit { get; set; }` | `room.UpperLimit` | Level |
| `Double Volume { get; }` | `room.Volume` | Double |
| `Boolean IsPointInRoom(XYZ)` | `room.IsPointInRoom(point)` | Boolean |
| `Void Unplace()` | `room.Unplace()` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
