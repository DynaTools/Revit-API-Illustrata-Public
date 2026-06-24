---
title: Units
classe: Autodesk.Revit.DB.Units
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# Units

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `DecimalSymbol DecimalSymbol { get; set; }` | `units.DecimalSymbol` | DecimalSymbol |
| `DigitGroupingAmount DigitGroupingAmount { get; set; }` | `units.DigitGroupingAmount` | DigitGroupingAmount |
| `DigitGroupingSymbol DigitGroupingSymbol { get; set; }` | `units.DigitGroupingSymbol` | DigitGroupingSymbol |
| `Boolean IsValidObject { get; }` | `units.IsValidObject` | Boolean |
| `Void Dispose()` | `units.Dispose()` | Void |
| `FormatOptions GetFormatOptions(ForgeTypeId)` | `units.GetFormatOptions(specTypeId)` | FormatOptions |
| `IList<ForgeTypeId> GetModifiableSpecs()` | `Units.GetModifiableSpecs()` | IList<ForgeTypeId> |
| `Boolean IsModifiableSpec(ForgeTypeId)` | `Units.IsModifiableSpec(specTypeId)` | Boolean |
| `Void SetFormatOptions(ForgeTypeId, FormatOptions)` | `units.SetFormatOptions(specTypeId, options)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
