---
title: NumberSystem
classe: Autodesk.Revit.DB.NumberSystem
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# NumberSystem

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double JustifyOffset { get; set; }` | `numberSystem.JustifyOffset` | Double |
| `NumberSystemJustifyOption JustifyOption { get; set; }` | `numberSystem.JustifyOption` | NumberSystemJustifyOption |
| `NumberSystemDisplayRule NumberDisplayRule { get; set; }` | `numberSystem.NumberDisplayRule` | NumberSystemDisplayRule |
| `LinkElementId NumberedElementId { get; }` | `numberSystem.NumberedElementId` | LinkElementId |
| `TagOrientation NumberOrientation { get; set; }` | `numberSystem.NumberOrientation` | TagOrientation |
| `LinkElementId PlacementLevelId { get; }` | `numberSystem.PlacementLevelId` | LinkElementId |
| `Double ReferenceOffset { get; set; }` | `numberSystem.ReferenceOffset` | Double |
| `NumberSystem Create(Document, ElementId, LinkElementId, StairsNumberSystemReferenceOption, LinkElementId)` | `NumberSystem.Create(document, viewId, hostElementId, referenceOption, placementLevelId)` | NumberSystem |
| `NumberSystem Create(Document, ElementId, LinkElementId, Reference)` | `NumberSystem.Create(document, viewId, numberedElementId, referenceCurve)` | NumberSystem |
| `Reference GetReferencePick()` | `numberSystem.GetReferencePick()` | Reference |
| `Void SetReferencePick(Reference)` | `numberSystem.SetReferencePick(referencePick)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
