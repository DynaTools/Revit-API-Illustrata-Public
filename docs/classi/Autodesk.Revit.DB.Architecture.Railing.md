---
title: Railing
classe: Autodesk.Revit.DB.Architecture.Railing
namespace: Autodesk.Revit.DB.Architecture
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 22
---

# Railing

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean CanReset { get; }` | `railing.CanReset` | Boolean |
| `Boolean Flipped { get; }` | `railing.Flipped` | Boolean |
| `Boolean HasHost { get; }` | `railing.HasHost` | Boolean |
| `ElementId HostId { get; set; }` | `railing.HostId` | ElementId |
| `Boolean IsDefault { get; }` | `railing.IsDefault` | Boolean |
| `ElementId TopRail { get; }` | `railing.TopRail` | ElementId |
| `ISet<ElementId> Create(Document, ElementId, ElementId, ElementId, RailingPlacementPosition)` | `Railing.Create(document, multistoryStairsId, levelId, railingTypeId, placePosition)` | ISet<ElementId> |
| `Railing Create(Document, CurveLoop, ElementId, ElementId)` | `Railing.Create(document, curveLoop, railingTypeId, baseLevelId)` | Railing |
| `ICollection<ElementId> Create(Document, ElementId, ElementId, RailingPlacementPosition)` | `Railing.Create(document, stairsOrRampId, railingTypeId, placePosition)` | ICollection<ElementId> |
| `Void Flip()` | `railing.Flip()` | Void |
| `IList<ElementId> GetHandRails()` | `railing.GetHandRails()` | IList<ElementId> |
| `ISet<ElementId> GetMultistoryStairsPlacementLevels()` | `railing.GetMultistoryStairsPlacementLevels()` | ISet<ElementId> |
| `IList<Curve> GetPath()` | `railing.GetPath()` | IList<Curve> |
| `Subelement GetSubelementOnLevel(ElementId)` | `railing.GetSubelementOnLevel(levelId)` | Subelement |
| `Boolean IsValidHostForNewRailing(Document, ElementId)` | `Railing.IsValidHostForNewRailing(document, elementId)` | Boolean |
| `Boolean IsValidPathForRailing(CurveLoop)` | `Railing.IsValidPathForRailing(curveLoop)` | Boolean |
| `Boolean RailingCanBeHostedByElement(ElementId)` | `railing.RailingCanBeHostedByElement(hostId)` | Boolean |
| `Void RemoveHost()` | `railing.RemoveHost()` | Void |
| `Void Reset()` | `railing.Reset()` | Void |
| `Void ResetSupportPosition()` | `railing.ResetSupportPosition()` | Void |
| `Void SetMultistoryStairsPlacementLevels(ISet<ElementId>)` | `railing.SetMultistoryStairsPlacementLevels(levelIds)` | Void |
| `Void SetPath(CurveLoop)` | `railing.SetPath(curveLoop)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
