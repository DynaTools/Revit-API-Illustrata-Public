---
title: MechanicalSystem
classe: Autodesk.Revit.DB.Mechanical.MechanicalSystem
namespace: Autodesk.Revit.DB.Mechanical
eredita: Autodesk.Revit.DB.MEPSystem
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# MechanicalSystem

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Connector BaseEquipmentConnector { get; set; }` | `mechanicalSystem.BaseEquipmentConnector` | Connector |
| `ElementSet DuctNetwork { get; }` | `mechanicalSystem.DuctNetwork` | ElementSet |
| `Boolean IsWellConnected { get; }` | `mechanicalSystem.IsWellConnected` | Boolean |
| `DuctSystemType SystemType { get; }` | `mechanicalSystem.SystemType` | DuctSystemType |
| `MechanicalSystem Create(Document, ElementId, String)` | `MechanicalSystem.Create(ADocument, typeId, name)` | MechanicalSystem |
| `MechanicalSystem Create(Document, ElementId)` | `MechanicalSystem.Create(ADocument, typeId)` | MechanicalSystem |
| `Double GetFlow()` | `mechanicalSystem.GetFlow()` | Double |
| `Double GetStaticPressure()` | `mechanicalSystem.GetStaticPressure()` | Double |
| `Boolean IsPressureDropServerMissing()` | `mechanicalSystem.IsPressureDropServerMissing()` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
