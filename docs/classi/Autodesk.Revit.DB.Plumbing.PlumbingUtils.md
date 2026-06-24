---
title: PlumbingUtils
classe: Autodesk.Revit.DB.Plumbing.PlumbingUtils
namespace: Autodesk.Revit.DB.Plumbing
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# PlumbingUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId BreakCurve(Document, ElementId, XYZ)` | `PlumbingUtils.BreakCurve(document, pipeId, ptBreak)` | ElementId |
| `Boolean ConnectPipePlaceholdersAtCross(Document, Connector, Connector, Connector, Connector)` | `PlumbingUtils.ConnectPipePlaceholdersAtCross(document, connector1, connector2, connector3, connector4)` | Boolean |
| `Boolean ConnectPipePlaceholdersAtCross(Document, ElementId, ElementId, ElementId)` | `PlumbingUtils.ConnectPipePlaceholdersAtCross(document, placeholder1Id, placeholder2Id, placeholder3Id)` | Boolean |
| `Boolean ConnectPipePlaceholdersAtCross(Document, ElementId, ElementId)` | `PlumbingUtils.ConnectPipePlaceholdersAtCross(document, placeholder1Id, placeholder2Id)` | Boolean |
| `Boolean ConnectPipePlaceholdersAtElbow(Document, Connector, Connector)` | `PlumbingUtils.ConnectPipePlaceholdersAtElbow(document, connector1, connector2)` | Boolean |
| `Boolean ConnectPipePlaceholdersAtElbow(Document, ElementId, ElementId)` | `PlumbingUtils.ConnectPipePlaceholdersAtElbow(document, placeholder1Id, placeholder2Id)` | Boolean |
| `Boolean ConnectPipePlaceholdersAtTee(Document, Connector, Connector, Connector)` | `PlumbingUtils.ConnectPipePlaceholdersAtTee(document, connector1, connector2, connector3)` | Boolean |
| `Boolean ConnectPipePlaceholdersAtTee(Document, ElementId, ElementId)` | `PlumbingUtils.ConnectPipePlaceholdersAtTee(document, placeholder1Id, placeholder2Id)` | Boolean |
| `ICollection<ElementId> ConvertPipePlaceholders(Document, ICollection<ElementId>)` | `PlumbingUtils.ConvertPipePlaceholders(document, placeholderIds)` | ICollection<ElementId> |
| `Boolean HasOpenConnector(Document, ElementId)` | `PlumbingUtils.HasOpenConnector(document, elemId)` | Boolean |
| `Void PlaceCapOnOpenEnds(Document, ElementId, ElementId)` | `PlumbingUtils.PlaceCapOnOpenEnds(document, elemId, typeId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
