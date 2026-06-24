---
title: FluidType
classe: Autodesk.Revit.DB.Plumbing.FluidType
namespace: Autodesk.Revit.DB.Plumbing
eredita: Autodesk.Revit.DB.ElementType
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# FluidType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Void AddTemperature(FluidTemperature)` | `fluidType.AddTemperature(fluidTemperature)` | Void |
| `Void ClearAllTemperatures()` | `fluidType.ClearAllTemperatures()` | Void |
| `FluidType Create(Document, String, FluidType)` | `FluidType.Create(document, fluidTypeName, basedOnFluidType)` | FluidType |
| `FluidType Create(Document, String)` | `FluidType.Create(document, fluidTypeName)` | FluidType |
| `IEnumerator<FluidTemperature> GetEnumerator()` | `fluidType.GetEnumerator()` | IEnumerator<FluidTemperature> |
| `FluidTemperatureSetIterator GetFluidTemperatureSetIterator()` | `fluidType.GetFluidTemperatureSetIterator()` | FluidTemperatureSetIterator |
| `FluidType GetFluidType(Document, String)` | `FluidType.GetFluidType(document, fluidTypeName)` | FluidType |
| `FluidTemperature GetTemperature(Double)` | `fluidType.GetTemperature(temperature)` | FluidTemperature |
| `Boolean IsFluidInUse(Document, ElementId)` | `FluidType.IsFluidInUse(document, fluidId)` | Boolean |
| `Void RemoveTemperature(Double)` | `fluidType.RemoveTemperature(temperature)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
