---
title: Level
classe: Autodesk.Revit.DB.Level
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.DatumPlane
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# Level

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double Elevation { get; set; }` | `level.Elevation` | Double |
| `Double ProjectElevation { get; }` | `level.ProjectElevation` | Double |
| `Level Create(Document, Double)` | `Level.Create(document, elevation)` | Level |
| `ElementId FindAssociatedPlanViewId()` | `level.FindAssociatedPlanViewId()` | ElementId |
| `ElementId GetNearestLevelId(Document, Double)` | `Level.GetNearestLevelId(document, elevation)` | ElementId |
| `ElementId GetNearestLevelId(Document, Double, Double&)` | `Level.GetNearestLevelId(document, elevation, offset)` | ElementId |
| `Reference GetPlaneReference()` | `level.GetPlaneReference()` | Reference |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
