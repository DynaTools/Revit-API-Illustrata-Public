---
title: DimensionType
classe: Autodesk.Revit.DB.DimensionType
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.ElementType
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 17
---

# DimensionType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `AlternateUnits AlternateUnits { get; set; }` | `dimensionType.AlternateUnits` | AlternateUnits |
| `String AlternateUnitsPrefix { get; set; }` | `dimensionType.AlternateUnitsPrefix` | String |
| `String AlternateUnitsSuffix { get; set; }` | `dimensionType.AlternateUnitsSuffix` | String |
| `String Prefix { get; set; }` | `dimensionType.Prefix` | String |
| `DimensionStyleType StyleType { get; }` | `dimensionType.StyleType` | DimensionStyleType |
| `String Suffix { get; set; }` | `dimensionType.Suffix` | String |
| `Boolean CanHaveEqualityFormula()` | `dimensionType.CanHaveEqualityFormula()` | Boolean |
| `Boolean CanHaveOrdinateDimensionSetting()` | `dimensionType.CanHaveOrdinateDimensionSetting()` | Boolean |
| `FormatOptions GetAlternateUnitsFormatOptions()` | `dimensionType.GetAlternateUnitsFormatOptions()` | FormatOptions |
| `IList<DimensionEqualityLabelFormatting> GetEqualityFormula()` | `dimensionType.GetEqualityFormula()` | IList<DimensionEqualityLabelFormatting> |
| `OrdinateDimensionSetting GetOrdinateDimensionSetting()` | `dimensionType.GetOrdinateDimensionSetting()` | OrdinateDimensionSetting |
| `ForgeTypeId GetSpecTypeId()` | `dimensionType.GetSpecTypeId()` | ForgeTypeId |
| `FormatOptions GetUnitsFormatOptions()` | `dimensionType.GetUnitsFormatOptions()` | FormatOptions |
| `Void SetAlternateUnitsFormatOptions(FormatOptions)` | `dimensionType.SetAlternateUnitsFormatOptions(formatOptions)` | Void |
| `Void SetEqualityFormula(IList<DimensionEqualityLabelFormatting>)` | `dimensionType.SetEqualityFormula(formattingArr)` | Void |
| `Void SetOrdinateDimensionSetting(OrdinateDimensionSetting)` | `dimensionType.SetOrdinateDimensionSetting(ordinateDimSetting)` | Void |
| `Void SetUnitsFormatOptions(FormatOptions)` | `dimensionType.SetUnitsFormatOptions(formatOptions)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
