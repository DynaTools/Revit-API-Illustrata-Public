---
title: InsulationLiningBase
classe: Autodesk.Revit.DB.InsulationLiningBase
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.MEPCurve
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 5
---

# InsulationLiningBase

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId HostElementId { get; }` | `insulationLiningBase.HostElementId` | ElementId |
| `Double Thickness { get; set; }` | `insulationLiningBase.Thickness` | Double |
| `ICollection<ElementId> GetInsulationIds(Document, ElementId)` | `InsulationLiningBase.GetInsulationIds(document, elemId)` | ICollection<ElementId> |
| `ICollection<ElementId> GetLiningIds(Document, ElementId)` | `InsulationLiningBase.GetLiningIds(document, elemId)` | ICollection<ElementId> |
| `Boolean IsValidThickness(Double)` | `InsulationLiningBase.IsValidThickness(thickness)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
