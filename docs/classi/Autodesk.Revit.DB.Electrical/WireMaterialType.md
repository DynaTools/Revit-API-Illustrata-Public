---
title: WireMaterialType
classe: Autodesk.Revit.DB.Electrical.WireMaterialType
namespace: Autodesk.Revit.DB.Electrical
eredita: Autodesk.Revit.DB.ElementType
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# WireMaterialType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `GroundConductorSizeSet GroundConductorSizes { get; }` | `wireMaterialType.GroundConductorSizes` | GroundConductorSizeSet |
| `Boolean IsInUse { get; }` | `wireMaterialType.IsInUse` | Boolean |
| `String Name { get; set; }` | `wireMaterialType.Name` | String |
| `TemperatureRatingTypeSet TemperatureRatings { get; }` | `wireMaterialType.TemperatureRatings` | TemperatureRatingTypeSet |
| `GroundConductorSize AddGroundConductorSize(Int64, String)` | `wireMaterialType.AddGroundConductorSize(ampacity, size)` | GroundConductorSize |
| `TemperatureRatingType AddTemperatureRatingType(String, TemperatureRatingType)` | `wireMaterialType.AddTemperatureRatingType(name, baseOn)` | TemperatureRatingType |
| `Void RemoveGroundConductorSize(GroundConductorSize)` | `wireMaterialType.RemoveGroundConductorSize(grdConductorSize)` | Void |
| `Void RemoveTemperatureRatingType(TemperatureRatingType)` | `wireMaterialType.RemoveTemperatureRatingType(temperatureRating)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
