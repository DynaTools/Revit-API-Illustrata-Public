---
title: ElectricalDemandFactorDefinition
classe: Autodesk.Revit.DB.Electrical.ElectricalDemandFactorDefinition
namespace: Autodesk.Revit.DB.Electrical
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# ElectricalDemandFactorDefinition

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double AdditionalLoad { get; set; }` | `electricalDemandFactorDefinition.AdditionalLoad` | Double |
| `Boolean IncludeAdditionalLoad { get; set; }` | `electricalDemandFactorDefinition.IncludeAdditionalLoad` | Boolean |
| `ElectricalDemandFactorRule RuleType { get; set; }` | `electricalDemandFactorDefinition.RuleType` | ElectricalDemandFactorRule |
| `Void AddValue(ElectricalDemandFactorValue)` | `electricalDemandFactorDefinition.AddValue(dfValue)` | Void |
| `Void ClearValues()` | `electricalDemandFactorDefinition.ClearValues()` | Void |
| `ElectricalDemandFactorDefinition Create(Document, String)` | `ElectricalDemandFactorDefinition.Create(ADoc, strName)` | ElectricalDemandFactorDefinition |
| `Double GetApplicableDemandFactor(Double)` | `electricalDemandFactorDefinition.GetApplicableDemandFactor(numberOrLoad)` | Double |
| `ICollection<ElectricalDemandFactorValue> GetValues()` | `electricalDemandFactorDefinition.GetValues()` | ICollection<ElectricalDemandFactorValue> |
| `Int32 GetValuesCount()` | `electricalDemandFactorDefinition.GetValuesCount()` | Int32 |
| `Void RemoveValue(ElectricalDemandFactorValue)` | `electricalDemandFactorDefinition.RemoveValue(dfValue)` | Void |
| `Void SetValues(ICollection<ElectricalDemandFactorValue>)` | `electricalDemandFactorDefinition.SetValues(values)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
