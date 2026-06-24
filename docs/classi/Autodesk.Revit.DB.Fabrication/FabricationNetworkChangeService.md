---
title: FabricationNetworkChangeService
classe: Autodesk.Revit.DB.Fabrication.FabricationNetworkChangeService
namespace: Autodesk.Revit.DB.Fabrication
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 16
---

# FabricationNetworkChangeService

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `fabricationNetworkChangeService.IsValidObject` | Boolean |
| `FabricationNetworkChangeServiceResult ApplyChange()` | `fabricationNetworkChangeService.ApplyChange()` | FabricationNetworkChangeServiceResult |
| `FabricationNetworkChangeServiceResult ChangeService(ISet<ElementId>, Int32, Int32, Boolean)` | `fabricationNetworkChangeService.ChangeService(selection, serviceId, paletteId, restrictPalette)` | FabricationNetworkChangeServiceResult |
| `FabricationNetworkChangeServiceResult ChangeService(ISet<ElementId>, Int32, Int32)` | `fabricationNetworkChangeService.ChangeService(selection, serviceId, paletteId)` | FabricationNetworkChangeServiceResult |
| `FabricationNetworkChangeServiceResult ChangeSize(ISet<ElementId>, ISet<FabricationPartSizeMap>)` | `fabricationNetworkChangeService.ChangeSize(selection, fabricationPartSizeMaps)` | FabricationNetworkChangeServiceResult |
| `Void Dispose()` | `fabricationNetworkChangeService.Dispose()` | Void |
| `ISet<ElementId> GetElementsThatFailed()` | `fabricationNetworkChangeService.GetElementsThatFailed()` | ISet<ElementId> |
| `ISet<ElementId> GetInLinePartTypes()` | `fabricationNetworkChangeService.GetInLinePartTypes()` | ISet<ElementId> |
| `ISet<FabricationPartSizeMap> GetMapOfAllSizesForStraights()` | `fabricationNetworkChangeService.GetMapOfAllSizesForStraights()` | ISet<FabricationPartSizeMap> |
| `ISet<ElementId> GetStraightsThatWereNotChanged()` | `fabricationNetworkChangeService.GetStraightsThatWereNotChanged()` | ISet<ElementId> |
| `Void SetMapOfInLinePartTypes(IDictionary<ElementId, ElementId>)` | `fabricationNetworkChangeService.SetMapOfInLinePartTypes(fabricationPartTypes)` | Void |
| `Void SetMapOfSizesForStraights(ISet<FabricationPartSizeMap>)` | `fabricationNetworkChangeService.SetMapOfSizesForStraights(fabricationPartSizeMaps)` | Void |
| `Void SetPaletteId(Int32)` | `fabricationNetworkChangeService.SetPaletteId(paletteId)` | Void |
| `Void SetRestrictPalette(Boolean)` | `fabricationNetworkChangeService.SetRestrictPalette(restrictPalette)` | Void |
| `FabricationNetworkChangeServiceResult SetSelection(ISet<ElementId>)` | `fabricationNetworkChangeService.SetSelection(selection)` | FabricationNetworkChangeServiceResult |
| `Void SetServiceId(Int32)` | `fabricationNetworkChangeService.SetServiceId(serviceId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
