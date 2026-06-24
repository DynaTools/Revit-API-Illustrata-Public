---
title: TemperatureRatingType
classe: Autodesk.Revit.DB.Electrical.TemperatureRatingType
namespace: Autodesk.Revit.DB.Electrical
eredita: Autodesk.Revit.DB.ElementType
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 12
---

# TemperatureRatingType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `CorrectionFactorSet CorrectionFactors { get; }` | `temperatureRatingType.CorrectionFactors` | CorrectionFactorSet |
| `InsulationTypeSet InsulationTypes { get; }` | `temperatureRatingType.InsulationTypes` | InsulationTypeSet |
| `Boolean IsInUse { get; }` | `temperatureRatingType.IsInUse` | Boolean |
| `WireMaterialType MaterialType { get; }` | `temperatureRatingType.MaterialType` | WireMaterialType |
| `String Name { get; set; }` | `temperatureRatingType.Name` | String |
| `WireSizeSet WireSizes { get; }` | `temperatureRatingType.WireSizes` | WireSizeSet |
| `CorrectionFactor AddCorrectionFactor(Double, Double)` | `temperatureRatingType.AddCorrectionFactor(temperature, factor)` | CorrectionFactor |
| `InsulationType AddInsulationType(String)` | `temperatureRatingType.AddInsulationType(name)` | InsulationType |
| `WireSize AddWireSize(String, Int64, Double)` | `temperatureRatingType.AddWireSize(size, ampacity, diameter)` | WireSize |
| `Void RemoveCorrectionFactor(CorrectionFactor)` | `temperatureRatingType.RemoveCorrectionFactor(correctionFactor)` | Void |
| `Void RemoveInsulationType(InsulationType)` | `temperatureRatingType.RemoveInsulationType(insulationType)` | Void |
| `Void RemoveWireSize(WireSize)` | `temperatureRatingType.RemoveWireSize(wireSize)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
