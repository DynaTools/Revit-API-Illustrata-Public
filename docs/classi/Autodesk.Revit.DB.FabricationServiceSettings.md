---
title: FabricationServiceSettings
classe: Autodesk.Revit.DB.FabricationServiceSettings
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# FabricationServiceSettings

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId AirFluidType { get; }` | `FabricationServiceSettings.AirFluidType` | ElementId |
| `FabricationServiceSettings GetFabricationServiceSettings(Document)` | `FabricationServiceSettings.GetFabricationServiceSettings(doc)` | FabricationServiceSettings |
| `Double GetFluidTemperature(FabricationService)` | `fabricationServiceSettings.GetFluidTemperature(service)` | Double |
| `ElementId GetFluidType(FabricationService)` | `fabricationServiceSettings.GetFluidType(service)` | ElementId |
| `Boolean HasValidFluidSetting(FabricationService)` | `fabricationServiceSettings.HasValidFluidSetting(service)` | Boolean |
| `Void RemoveFluidSetting(FabricationService)` | `fabricationServiceSettings.RemoveFluidSetting(service)` | Void |
| `Void SetFluidTypeAndTemperature(FabricationService, ElementId, Double)` | `fabricationServiceSettings.SetFluidTypeAndTemperature(service, fluidId, temperature)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
