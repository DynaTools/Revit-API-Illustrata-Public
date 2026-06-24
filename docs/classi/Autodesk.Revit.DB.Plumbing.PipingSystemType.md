---
title: PipingSystemType
classe: Autodesk.Revit.DB.Plumbing.PipingSystemType
namespace: Autodesk.Revit.DB.Plumbing
eredita: Autodesk.Revit.DB.MEPSystemType
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# PipingSystemType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `FlowConversionMode FlowConversionMethod { get; set; }` | `pipingSystemType.FlowConversionMethod` | FlowConversionMode |
| `Double FluidTemperature { get; set; }` | `pipingSystemType.FluidTemperature` | Double |
| `ElementId FluidType { get; set; }` | `pipingSystemType.FluidType` | ElementId |
| `RiseDropSymbol SingleLineBendDropType { get; set; }` | `pipingSystemType.SingleLineBendDropType` | RiseDropSymbol |
| `RiseDropSymbol SingleLineBendRiseType { get; set; }` | `pipingSystemType.SingleLineBendRiseType` | RiseDropSymbol |
| `RiseDropSymbol SingleLineJunctionDropType { get; set; }` | `pipingSystemType.SingleLineJunctionDropType` | RiseDropSymbol |
| `RiseDropSymbol SingleLineJunctionRiseType { get; set; }` | `pipingSystemType.SingleLineJunctionRiseType` | RiseDropSymbol |
| `RiseDropSymbol TwoLineDropType { get; set; }` | `pipingSystemType.TwoLineDropType` | RiseDropSymbol |
| `RiseDropSymbol TwoLineRiseType { get; set; }` | `pipingSystemType.TwoLineRiseType` | RiseDropSymbol |
| `PipingSystemType Create(Document, MEPSystemClassification, String)` | `PipingSystemType.Create(ADoc, systemClassification, name)` | PipingSystemType |
| `Boolean ValidateRiseDropSymbolType(RiseDropSymbol)` | `pipingSystemType.ValidateRiseDropSymbolType(risedropType)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
