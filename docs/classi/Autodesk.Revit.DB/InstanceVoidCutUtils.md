---
title: InstanceVoidCutUtils
classe: Autodesk.Revit.DB.InstanceVoidCutUtils
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# InstanceVoidCutUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Void AddInstanceVoidCut(Document, Element, Element)` | `InstanceVoidCutUtils.AddInstanceVoidCut(document, element, cuttingInstance)` | Void |
| `Boolean CanBeCutWithVoid(Element)` | `InstanceVoidCutUtils.CanBeCutWithVoid(element)` | Boolean |
| `ICollection<ElementId> GetCuttingVoidInstances(Element)` | `InstanceVoidCutUtils.GetCuttingVoidInstances(element)` | ICollection<ElementId> |
| `ICollection<ElementId> GetElementsBeingCut(Element)` | `InstanceVoidCutUtils.GetElementsBeingCut(cuttingInstance)` | ICollection<ElementId> |
| `Boolean InstanceVoidCutExists(Element, Element)` | `InstanceVoidCutUtils.InstanceVoidCutExists(element, cuttingInstance)` | Boolean |
| `Boolean IsVoidInstanceCuttingElement(Element)` | `InstanceVoidCutUtils.IsVoidInstanceCuttingElement(element)` | Boolean |
| `Void RemoveInstanceVoidCut(Document, Element, Element)` | `InstanceVoidCutUtils.RemoveInstanceVoidCut(document, element, cuttingInstance)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
