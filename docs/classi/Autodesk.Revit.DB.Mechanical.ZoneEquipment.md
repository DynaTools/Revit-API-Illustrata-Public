---
title: ZoneEquipment
classe: Autodesk.Revit.DB.Mechanical.ZoneEquipment
namespace: Autodesk.Revit.DB.Mechanical
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 5
---

# ZoneEquipment

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ZoneEquipment Create(Document, String)` | `ZoneEquipment.Create(document, name)` | ZoneEquipment |
| `ISet<ElementId> GetAssociatedZoneEquipment(Document, ISet<ElementId>)` | `ZoneEquipment.GetAssociatedZoneEquipment(document, spaces)` | ISet<ElementId> |
| `ISet<ElementId> GetAssociatedZoneEquipment(Document, ElementId)` | `ZoneEquipment.GetAssociatedZoneEquipment(document, spaceElementId)` | ISet<ElementId> |
| `ZoneEquipmentData GetZoneEquipmentData()` | `zoneEquipment.GetZoneEquipmentData()` | ZoneEquipmentData |
| `Void MoveSpaceToEquipment(Document, ISet<ElementId>, ElementId, ElementId)` | `ZoneEquipment.MoveSpaceToEquipment(document, analyticalSpaceSet, originalZoneEquipmentId, targetZoneEquipmentId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
