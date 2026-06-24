---
title: HVACLoadBuildingType
classe: Autodesk.Revit.DB.Analysis.HVACLoadBuildingType
namespace: Autodesk.Revit.DB.Analysis
eredita: Autodesk.Revit.DB.Analysis.HVACLoadType
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# HVACLoadBuildingType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String BuildingTypeName { get; set; }` | `hVACLoadBuildingType.BuildingTypeName` | String |
| `String ClosingTime { get; set; }` | `hVACLoadBuildingType.ClosingTime` | String |
| `String OpeningTime { get; set; }` | `hVACLoadBuildingType.OpeningTime` | String |
| `Double UnoccupiedCoolingSetPoint { get; set; }` | `hVACLoadBuildingType.UnoccupiedCoolingSetPoint` | Double |
| `HVACLoadBuildingType Create(Document, String)` | `HVACLoadBuildingType.Create(document, name)` | HVACLoadBuildingType |
| `Boolean IsNameUnique(String)` | `hVACLoadBuildingType.IsNameUnique(name)` | Boolean |
| `Boolean IsNameUnique(Document, String)` | `HVACLoadBuildingType.IsNameUnique(document, name)` | Boolean |
| `Boolean IsValidTime(String)` | `HVACLoadBuildingType.IsValidTime(hourMinute)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
