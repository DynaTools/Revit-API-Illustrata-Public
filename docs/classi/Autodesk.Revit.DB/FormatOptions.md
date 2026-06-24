---
title: FormatOptions
classe: Autodesk.Revit.DB.FormatOptions
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 31
---

# FormatOptions

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double Accuracy { get; set; }` | `formatOptions.Accuracy` | Double |
| `Boolean IsValidObject { get; }` | `formatOptions.IsValidObject` | Boolean |
| `RoundingMethod RoundingMethod { get; set; }` | `formatOptions.RoundingMethod` | RoundingMethod |
| `Boolean SuppressLeadingZeros { get; set; }` | `formatOptions.SuppressLeadingZeros` | Boolean |
| `Boolean SuppressSpaces { get; set; }` | `formatOptions.SuppressSpaces` | Boolean |
| `Boolean SuppressTrailingZeros { get; set; }` | `formatOptions.SuppressTrailingZeros` | Boolean |
| `Boolean UseDefault { get; set; }` | `formatOptions.UseDefault` | Boolean |
| `Boolean UseDigitGrouping { get; set; }` | `formatOptions.UseDigitGrouping` | Boolean |
| `Boolean UsePlusPrefix { get; set; }` | `formatOptions.UsePlusPrefix` | Boolean |
| `Boolean CanHaveSymbol()` | `formatOptions.CanHaveSymbol()` | Boolean |
| `Boolean CanHaveSymbol(ForgeTypeId)` | `FormatOptions.CanHaveSymbol(unitTypeId)` | Boolean |
| `Boolean CanSuppressLeadingZeros()` | `formatOptions.CanSuppressLeadingZeros()` | Boolean |
| `Boolean CanSuppressLeadingZeros(ForgeTypeId)` | `FormatOptions.CanSuppressLeadingZeros(unitTypeId)` | Boolean |
| `Boolean CanSuppressSpaces()` | `formatOptions.CanSuppressSpaces()` | Boolean |
| `Boolean CanSuppressSpaces(ForgeTypeId)` | `FormatOptions.CanSuppressSpaces(unitTypeId)` | Boolean |
| `Boolean CanSuppressTrailingZeros()` | `formatOptions.CanSuppressTrailingZeros()` | Boolean |
| `Boolean CanSuppressTrailingZeros(ForgeTypeId)` | `FormatOptions.CanSuppressTrailingZeros(unitTypeId)` | Boolean |
| `Boolean CanUsePlusPrefix()` | `formatOptions.CanUsePlusPrefix()` | Boolean |
| `Boolean CanUsePlusPrefix(ForgeTypeId)` | `FormatOptions.CanUsePlusPrefix(unitTypeId)` | Boolean |
| `Void Dispose()` | `formatOptions.Dispose()` | Void |
| `ForgeTypeId GetSymbolTypeId()` | `formatOptions.GetSymbolTypeId()` | ForgeTypeId |
| `ForgeTypeId GetUnitTypeId()` | `formatOptions.GetUnitTypeId()` | ForgeTypeId |
| `IList<ForgeTypeId> GetValidSymbols()` | `formatOptions.GetValidSymbols()` | IList<ForgeTypeId> |
| `IList<ForgeTypeId> GetValidSymbols(ForgeTypeId)` | `FormatOptions.GetValidSymbols(unitTypeId)` | IList<ForgeTypeId> |
| `Boolean IsValidAccuracy(Double)` | `formatOptions.IsValidAccuracy(accuracy)` | Boolean |
| `Boolean IsValidAccuracy(ForgeTypeId, Double)` | `FormatOptions.IsValidAccuracy(unitTypeId, accuracy)` | Boolean |
| `Boolean IsValidForSpec(ForgeTypeId)` | `formatOptions.IsValidForSpec(specTypeId)` | Boolean |
| `Boolean IsValidSymbol(ForgeTypeId)` | `formatOptions.IsValidSymbol(symbolTypeId)` | Boolean |
| `Boolean IsValidSymbol(ForgeTypeId, ForgeTypeId)` | `FormatOptions.IsValidSymbol(unitTypeId, symbolTypeId)` | Boolean |
| `Void SetSymbolTypeId(ForgeTypeId)` | `formatOptions.SetSymbolTypeId(symbolTypeId)` | Void |
| `FormatOptions SetUnitTypeId(ForgeTypeId)` | `formatOptions.SetUnitTypeId(unitTypeId)` | FormatOptions |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
