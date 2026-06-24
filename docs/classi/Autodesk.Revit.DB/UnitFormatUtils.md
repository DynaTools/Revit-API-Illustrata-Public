---
title: UnitFormatUtils
classe: Autodesk.Revit.DB.UnitFormatUtils
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 6
---

# UnitFormatUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String Format(Units, ForgeTypeId, Double, Boolean)` | `UnitFormatUtils.Format(units, specTypeId, value, forEditing)` | String |
| `String Format(Units, ForgeTypeId, Double, Boolean, FormatValueOptions)` | `UnitFormatUtils.Format(units, specTypeId, value, forEditing, formatValueOptions)` | String |
| `Boolean TryParse(Units, ForgeTypeId, String, Double&, String&)` | `UnitFormatUtils.TryParse(units, specTypeId, stringToParse, value, message)` | Boolean |
| `Boolean TryParse(Units, ForgeTypeId, String, Double&)` | `UnitFormatUtils.TryParse(units, specTypeId, stringToParse, value)` | Boolean |
| `Boolean TryParse(Units, ForgeTypeId, String, ValueParsingOptions, Double&, String&)` | `UnitFormatUtils.TryParse(units, specTypeId, stringToParse, valueParsingOptions, value, message)` | Boolean |
| `Boolean TryParse(Units, ForgeTypeId, String, ValueParsingOptions, Double&)` | `UnitFormatUtils.TryParse(units, specTypeId, stringToParse, valueParsingOptions, value)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
