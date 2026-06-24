---
title: DetailElementOrderUtils
classe: Autodesk.Revit.DB.DetailElementOrderUtils
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# DetailElementOrderUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean AreDetailElements(Document, View, ICollection<ElementId>)` | `DetailElementOrderUtils.AreDetailElements(document, view, detailElementIds)` | Boolean |
| `Void BringForward(Document, View, ICollection<ElementId>)` | `DetailElementOrderUtils.BringForward(document, view, detailElementIds)` | Void |
| `Void BringForward(Document, View, ElementId)` | `DetailElementOrderUtils.BringForward(document, view, detailElementId)` | Void |
| `Void BringToFront(Document, View, ICollection<ElementId>)` | `DetailElementOrderUtils.BringToFront(document, view, detailElementIds)` | Void |
| `Void BringToFront(Document, View, ElementId)` | `DetailElementOrderUtils.BringToFront(document, view, detailElementId)` | Void |
| `IList<ElementId> GetDrawOrderForDetails(View, ISet<ElementId>)` | `DetailElementOrderUtils.GetDrawOrderForDetails(view, detailIdsToSort)` | IList<ElementId> |
| `Boolean IsDetailElement(Document, View, ElementId)` | `DetailElementOrderUtils.IsDetailElement(document, view, detailElementId)` | Boolean |
| `Void SendBackward(Document, View, ICollection<ElementId>)` | `DetailElementOrderUtils.SendBackward(document, view, detailElementIds)` | Void |
| `Void SendBackward(Document, View, ElementId)` | `DetailElementOrderUtils.SendBackward(document, view, detailElementId)` | Void |
| `Void SendToBack(Document, View, ICollection<ElementId>)` | `DetailElementOrderUtils.SendToBack(document, view, detailElementIds)` | Void |
| `Void SendToBack(Document, View, ElementId)` | `DetailElementOrderUtils.SendToBack(document, view, detailElementId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
