---
title: UnitUtils
classe: Autodesk.Revit.DB.UnitUtils
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 14
---

# UnitUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double Convert(Double, ForgeTypeId, ForgeTypeId)` | `UnitUtils.Convert(value, currentUnitTypeId, desiredUnitTypeId)` | Double |
| `Double ConvertFromInternalUnits(Double, ForgeTypeId)` | `UnitUtils.ConvertFromInternalUnits(value, unitTypeId)` | Double |
| `Double ConvertToInternalUnits(Double, ForgeTypeId)` | `UnitUtils.ConvertToInternalUnits(value, unitTypeId)` | Double |
| `IList<ForgeTypeId> GetAllDisciplines()` | `UnitUtils.GetAllDisciplines()` | IList<ForgeTypeId> |
| `IList<ForgeTypeId> GetAllMeasurableSpecs()` | `UnitUtils.GetAllMeasurableSpecs()` | IList<ForgeTypeId> |
| `IList<ForgeTypeId> GetAllUnits()` | `UnitUtils.GetAllUnits()` | IList<ForgeTypeId> |
| `ForgeTypeId GetDiscipline(ForgeTypeId)` | `UnitUtils.GetDiscipline(specTypeId)` | ForgeTypeId |
| `String GetTypeCatalogStringForSpec(ForgeTypeId)` | `UnitUtils.GetTypeCatalogStringForSpec(specTypeId)` | String |
| `String GetTypeCatalogStringForUnit(ForgeTypeId)` | `UnitUtils.GetTypeCatalogStringForUnit(unitTypeId)` | String |
| `IList<ForgeTypeId> GetValidUnits(ForgeTypeId)` | `UnitUtils.GetValidUnits(specTypeId)` | IList<ForgeTypeId> |
| `Boolean IsMeasurableSpec(ForgeTypeId)` | `UnitUtils.IsMeasurableSpec(specTypeId)` | Boolean |
| `Boolean IsSymbol(ForgeTypeId)` | `UnitUtils.IsSymbol(symbolTypeId)` | Boolean |
| `Boolean IsUnit(ForgeTypeId)` | `UnitUtils.IsUnit(unitTypeId)` | Boolean |
| `Boolean IsValidUnit(ForgeTypeId, ForgeTypeId)` | `UnitUtils.IsValidUnit(specTypeId, unitTypeId)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
