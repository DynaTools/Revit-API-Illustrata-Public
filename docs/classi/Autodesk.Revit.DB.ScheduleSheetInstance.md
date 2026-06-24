---
title: ScheduleSheetInstance
classe: Autodesk.Revit.DB.ScheduleSheetInstance
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# ScheduleSheetInstance

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsTitleblockRevisionSchedule { get; }` | `scheduleSheetInstance.IsTitleblockRevisionSchedule` | Boolean |
| `XYZ Point { get; set; }` | `scheduleSheetInstance.Point` | XYZ |
| `ViewportRotation Rotation { get; set; }` | `scheduleSheetInstance.Rotation` | ViewportRotation |
| `ElementId ScheduleId { get; }` | `scheduleSheetInstance.ScheduleId` | ElementId |
| `Int32 SegmentIndex { get; set; }` | `scheduleSheetInstance.SegmentIndex` | Int32 |
| `ScheduleSheetInstance Create(Document, ElementId, ElementId, XYZ, Int32)` | `ScheduleSheetInstance.Create(document, viewSheetId, scheduleId, origin, segmentIndex)` | ScheduleSheetInstance |
| `ScheduleSheetInstance Create(Document, ElementId, ElementId, XYZ)` | `ScheduleSheetInstance.Create(document, viewSheetId, scheduleId, origin)` | ScheduleSheetInstance |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
