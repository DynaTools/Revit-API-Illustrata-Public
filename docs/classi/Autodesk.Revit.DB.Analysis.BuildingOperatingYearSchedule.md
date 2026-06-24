---
title: BuildingOperatingYearSchedule
classe: Autodesk.Revit.DB.Analysis.BuildingOperatingYearSchedule
namespace: Autodesk.Revit.DB.Analysis
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 4
---

# BuildingOperatingYearSchedule

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String ScheduleName { get; set; }` | `buildingOperatingYearSchedule.ScheduleName` | String |
| `BuildingOperatingYearSchedule Create(Document, BuildingOperatingDaySchedule, String)` | `BuildingOperatingYearSchedule.Create(document, daySchedule, name)` | BuildingOperatingYearSchedule |
| `BuildingOperatingDaySchedule GetScheduleForDay(DateTime)` | `buildingOperatingYearSchedule.GetScheduleForDay(day)` | BuildingOperatingDaySchedule |
| `Void SetScheduleForDay(DateTime, BuildingOperatingDaySchedule)` | `buildingOperatingYearSchedule.SetScheduleForDay(day, daySchedule)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
