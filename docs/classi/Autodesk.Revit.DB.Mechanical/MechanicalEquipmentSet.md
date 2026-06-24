---
title: MechanicalEquipmentSet
classe: Autodesk.Revit.DB.Mechanical.MechanicalEquipmentSet
namespace: Autodesk.Revit.DB.Mechanical
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# MechanicalEquipmentSet

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `EquipmentClassification Classification { get; }` | `mechanicalEquipmentSet.Classification` | EquipmentClassification |
| `Int32 OnDuty { get; set; }` | `mechanicalEquipmentSet.OnDuty` | Int32 |
| `Int32 OnStandby { get; set; }` | `mechanicalEquipmentSet.OnStandby` | Int32 |
| `Void Add(ISet<ElementId>)` | `mechanicalEquipmentSet.Add(elemIds)` | Void |
| `Boolean AreElementsNotConnectedInSeries(Document, ISet<ElementId>)` | `MechanicalEquipmentSet.AreElementsNotConnectedInSeries(document, elemIds)` | Boolean |
| `Boolean AreValidMembers(Document, ISet<ElementId>)` | `MechanicalEquipmentSet.AreValidMembers(document, memberIds)` | Boolean |
| `MechanicalEquipmentSet Create(Document, ElementId, ISet<ElementId>)` | `MechanicalEquipmentSet.Create(document, typeId, memberIds)` | MechanicalEquipmentSet |
| `ISet<ElementId> GetMembers()` | `mechanicalEquipmentSet.GetMembers()` | ISet<ElementId> |
| `Void Remove(ISet<ElementId>)` | `mechanicalEquipmentSet.Remove(elemIds)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
