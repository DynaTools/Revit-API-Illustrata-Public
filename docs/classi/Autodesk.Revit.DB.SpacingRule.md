---
title: SpacingRule
classe: Autodesk.Revit.DB.SpacingRule
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# SpacingRule

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double BeltMeasurement { get; set; }` | `spacingRule.BeltMeasurement` | Double |
| `Double Distance { get; set; }` | `spacingRule.Distance` | Double |
| `Double GridlinesRotation { get; set; }` | `spacingRule.GridlinesRotation` | Double |
| `Boolean HasBeltMeasurement { get; }` | `spacingRule.HasBeltMeasurement` | Boolean |
| `SpacingRuleJustification Justification { get; set; }` | `spacingRule.Justification` | SpacingRuleJustification |
| `SpacingRuleLayout Layout { get; }` | `spacingRule.Layout` | SpacingRuleLayout |
| `Int32 Number { get; set; }` | `spacingRule.Number` | Int32 |
| `Double Offset { get; set; }` | `spacingRule.Offset` | Double |
| `Void SetLayoutFixedDistance(Double, SpacingRuleJustification, Double, Double)` | `spacingRule.SetLayoutFixedDistance(distance, just, gridlinesRotation, offset)` | Void |
| `Void SetLayoutFixedNumber(Int32, SpacingRuleJustification, Double, Double)` | `spacingRule.SetLayoutFixedNumber(number, just, gridlinesRotation, offset)` | Void |
| `Void SetLayoutMaximumSpacing(Double, SpacingRuleJustification, Double, Double)` | `spacingRule.SetLayoutMaximumSpacing(distance, just, gridlinesRotation, offset)` | Void |
| `Void SetLayoutMinimumSpacing(Double, SpacingRuleJustification, Double, Double)` | `spacingRule.SetLayoutMinimumSpacing(distance, just, gridlinesRotation, offset)` | Void |
| `Void SetLayoutNone()` | `spacingRule.SetLayoutNone()` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
