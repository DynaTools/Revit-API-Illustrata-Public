---
title: MassInstanceUtils
classe: Autodesk.Revit.DB.MassInstanceUtils
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# MassInstanceUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `massInstanceUtils.IsValidObject` | Boolean |
| `ElementId AddMassLevelDataToMassInstance(Document, ElementId, ElementId)` | `MassInstanceUtils.AddMassLevelDataToMassInstance(document, massInstanceId, levelId)` | ElementId |
| `Void Dispose()` | `massInstanceUtils.Dispose()` | Void |
| `Double GetGrossFloorArea(Document, ElementId)` | `MassInstanceUtils.GetGrossFloorArea(document, massInstanceId)` | Double |
| `Double GetGrossSurfaceArea(Document, ElementId)` | `MassInstanceUtils.GetGrossSurfaceArea(document, massInstanceId)` | Double |
| `Double GetGrossVolume(Document, ElementId)` | `MassInstanceUtils.GetGrossVolume(document, massInstanceId)` | Double |
| `IList<ElementId> GetJoinedElementIds(Document, ElementId)` | `MassInstanceUtils.GetJoinedElementIds(document, massInstanceId)` | IList<ElementId> |
| `IList<ElementId> GetMassLevelDataIds(Document, ElementId)` | `MassInstanceUtils.GetMassLevelDataIds(document, massInstanceId)` | IList<ElementId> |
| `IList<ElementId> GetMassLevelIds(Document, ElementId)` | `MassInstanceUtils.GetMassLevelIds(document, massInstanceId)` | IList<ElementId> |
| `Void RemoveMassLevelDataFromMassInstance(Document, ElementId, ElementId)` | `MassInstanceUtils.RemoveMassLevelDataFromMassInstance(document, massInstanceId, levelId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
