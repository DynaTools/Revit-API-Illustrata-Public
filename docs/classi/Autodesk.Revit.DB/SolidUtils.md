---
title: SolidUtils
classe: Autodesk.Revit.DB.SolidUtils
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 6
---

# SolidUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Solid Clone(Solid)` | `SolidUtils.Clone(solid)` | Solid |
| `Solid CreateTransformed(Solid, Transform)` | `SolidUtils.CreateTransformed(solid, transform)` | Solid |
| `IList<EdgeEndPoint> FindAllEdgeEndPointsAtVertex(EdgeEndPoint)` | `SolidUtils.FindAllEdgeEndPointsAtVertex(edgeEndPoint)` | IList<EdgeEndPoint> |
| `Boolean IsValidForTessellation(Solid)` | `SolidUtils.IsValidForTessellation(solidOrShell)` | Boolean |
| `IList<Solid> SplitVolumes(Solid)` | `SolidUtils.SplitVolumes(solid)` | IList<Solid> |
| `TriangulatedSolidOrShell TessellateSolidOrShell(Solid, SolidOrShellTessellationControls)` | `SolidUtils.TessellateSolidOrShell(solidOrShell, tessellationControls)` | TriangulatedSolidOrShell |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
