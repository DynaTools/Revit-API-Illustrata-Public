---
title: SiteSubRegion
classe: Autodesk.Revit.DB.Architecture.SiteSubRegion
namespace: Autodesk.Revit.DB.Architecture
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# SiteSubRegion

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId HostId { get; }` | `siteSubRegion.HostId` | ElementId |
| `Boolean IsValidObject { get; }` | `siteSubRegion.IsValidObject` | Boolean |
| `TopographySurface TopographySurface { get; }` | `siteSubRegion.TopographySurface` | TopographySurface |
| `SiteSubRegion Create(Document, IList<CurveLoop>, ElementId)` | `SiteSubRegion.Create(document, curveLoops, hostTopoSurfaceId)` | SiteSubRegion |
| `SiteSubRegion Create(Document, IList<CurveLoop>)` | `SiteSubRegion.Create(document, curveLoops)` | SiteSubRegion |
| `Void Dispose()` | `siteSubRegion.Dispose()` | Void |
| `IList<CurveLoop> GetBoundary()` | `siteSubRegion.GetBoundary()` | IList<CurveLoop> |
| `Boolean IsValidBoundary(IList<CurveLoop>)` | `SiteSubRegion.IsValidBoundary(curveLoops)` | Boolean |
| `Void SetBoundary(IList<CurveLoop>)` | `siteSubRegion.SetBoundary(curveLoops)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
