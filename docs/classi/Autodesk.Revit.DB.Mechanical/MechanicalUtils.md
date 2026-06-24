---
title: MechanicalUtils
classe: Autodesk.Revit.DB.Mechanical.MechanicalUtils
namespace: Autodesk.Revit.DB.Mechanical
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# MechanicalUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId BreakCurve(Document, ElementId, XYZ)` | `MechanicalUtils.BreakCurve(document, ductId, ptBreak)` | ElementId |
| `Boolean ConnectAirTerminalOnDuct(Document, ElementId, ElementId)` | `MechanicalUtils.ConnectAirTerminalOnDuct(document, airTerminalId, ductCurveId)` | Boolean |
| `Boolean ConnectDuctPlaceholdersAtCross(Document, Connector, Connector, Connector, Connector)` | `MechanicalUtils.ConnectDuctPlaceholdersAtCross(document, connector1, connector2, connector3, connector4)` | Boolean |
| `Boolean ConnectDuctPlaceholdersAtCross(Document, ElementId, ElementId, ElementId)` | `MechanicalUtils.ConnectDuctPlaceholdersAtCross(document, placeholder1Id, placeholder2Id, placeholder3Id)` | Boolean |
| `Boolean ConnectDuctPlaceholdersAtCross(Document, ElementId, ElementId)` | `MechanicalUtils.ConnectDuctPlaceholdersAtCross(document, placeholder1Id, placeholder2Id)` | Boolean |
| `Boolean ConnectDuctPlaceholdersAtElbow(Document, Connector, Connector)` | `MechanicalUtils.ConnectDuctPlaceholdersAtElbow(document, connector1, connector2)` | Boolean |
| `Boolean ConnectDuctPlaceholdersAtElbow(Document, ElementId, ElementId)` | `MechanicalUtils.ConnectDuctPlaceholdersAtElbow(document, placeholder1Id, placeholder2Id)` | Boolean |
| `Boolean ConnectDuctPlaceholdersAtTee(Document, Connector, Connector, Connector)` | `MechanicalUtils.ConnectDuctPlaceholdersAtTee(document, connector1, connector2, connector3)` | Boolean |
| `Boolean ConnectDuctPlaceholdersAtTee(Document, ElementId, ElementId)` | `MechanicalUtils.ConnectDuctPlaceholdersAtTee(document, placeholder1Id, placeholder2Id)` | Boolean |
| `ICollection<ElementId> ConvertDuctPlaceholders(Document, ICollection<ElementId>)` | `MechanicalUtils.ConvertDuctPlaceholders(document, placeholderIds)` | ICollection<ElementId> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
