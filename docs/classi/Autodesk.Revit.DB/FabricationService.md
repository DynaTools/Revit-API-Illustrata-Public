---
title: FabricationService
classe: Autodesk.Revit.DB.FabricationService
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 17
---

# FabricationService

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String Abbreviation { get; }` | `fabricationService.Abbreviation` | String |
| `String FabricationSystemName { get; }` | `fabricationService.FabricationSystemName` | String |
| `Boolean IsValidObject { get; }` | `fabricationService.IsValidObject` | Boolean |
| `String Name { get; }` | `fabricationService.Name` | String |
| `Int32 PaletteCount { get; }` | `fabricationService.PaletteCount` | Int32 |
| `Int32 ServiceId { get; }` | `fabricationService.ServiceId` | Int32 |
| `Void Dispose()` | `fabricationService.Dispose()` | Void |
| `FabricationServiceButton GetButton(Int32, Int32)` | `fabricationService.GetButton(paletteIndex, buttonIndex)` | FabricationServiceButton |
| `Int32 GetButtonCount(Int32)` | `fabricationService.GetButtonCount(palette)` | Int32 |
| `String GetPaletteName(Int32)` | `fabricationService.GetPaletteName(palette)` | String |
| `Boolean IsCompatibleWith(FabricationService)` | `fabricationService.IsCompatibleWith(otherService)` | Boolean |
| `Boolean IsPaletteExcluded(Int32)` | `fabricationService.IsPaletteExcluded(paletteIndex)` | Boolean |
| `Boolean IsValidButtonIndex(Int32, Int32)` | `fabricationService.IsValidButtonIndex(paletteIndex, buttonIndex)` | Boolean |
| `Boolean IsValidPaletteIndex(Int32)` | `fabricationService.IsValidPaletteIndex(paletteIndex)` | Boolean |
| `Void OverrideServiceButtonExclusion(Int32, Int32, Boolean)` | `fabricationService.OverrideServiceButtonExclusion(paletteIndex, buttonIndex, exclude)` | Void |
| `Void ResetServiceExclusionOverrides()` | `fabricationService.ResetServiceExclusionOverrides()` | Void |
| `Boolean SetServicePaletteExclusions(IList<Int32>)` | `fabricationService.SetServicePaletteExclusions(excludedPalettes)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
