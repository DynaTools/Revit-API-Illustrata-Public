---
title: JoinGeometryUtils
classe: Autodesk.Revit.DB.JoinGeometryUtils
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 6
---

# JoinGeometryUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean AreElementsJoined(Document, Element, Element)` | `JoinGeometryUtils.AreElementsJoined(document, firstElement, secondElement)` | Boolean |
| `ICollection<ElementId> GetJoinedElements(Document, Element)` | `JoinGeometryUtils.GetJoinedElements(document, element)` | ICollection<ElementId> |
| `Boolean IsCuttingElementInJoin(Document, Element, Element)` | `JoinGeometryUtils.IsCuttingElementInJoin(document, firstElement, secondElement)` | Boolean |
| `Void JoinGeometry(Document, Element, Element)` | `JoinGeometryUtils.JoinGeometry(document, firstElement, secondElement)` | Void |
| `Void SwitchJoinOrder(Document, Element, Element)` | `JoinGeometryUtils.SwitchJoinOrder(document, firstElement, secondElement)` | Void |
| `Void UnjoinGeometry(Document, Element, Element)` | `JoinGeometryUtils.UnjoinGeometry(document, firstElement, secondElement)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
