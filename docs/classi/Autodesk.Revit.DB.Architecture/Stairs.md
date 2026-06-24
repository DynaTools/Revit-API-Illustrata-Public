---
title: Stairs
classe: Autodesk.Revit.DB.Architecture.Stairs
namespace: Autodesk.Revit.DB.Architecture
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 16
---

# Stairs

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double ActualRiserHeight { get; }` | `stairs.ActualRiserHeight` | Double |
| `Int32 ActualRisersNumber { get; }` | `stairs.ActualRisersNumber` | Int32 |
| `Double ActualTreadDepth { get; set; }` | `stairs.ActualTreadDepth` | Double |
| `Int32 ActualTreadsNumber { get; }` | `stairs.ActualTreadsNumber` | Int32 |
| `Double BaseElevation { get; }` | `stairs.BaseElevation` | Double |
| `Int32 DesiredRisersNumber { get; set; }` | `stairs.DesiredRisersNumber` | Int32 |
| `Double Height { get; set; }` | `stairs.Height` | Double |
| `ElementId MultistoryStairsId { get; }` | `stairs.MultistoryStairsId` | ElementId |
| `Int32 NumberOfStories { get; }` | `stairs.NumberOfStories` | Int32 |
| `Double TopElevation { get; }` | `stairs.TopElevation` | Double |
| `ICollection<ElementId> GetAssociatedRailings()` | `stairs.GetAssociatedRailings()` | ICollection<ElementId> |
| `ICollection<ElementId> GetStairsLandings()` | `stairs.GetStairsLandings()` | ICollection<ElementId> |
| `ICollection<ElementId> GetStairsRuns()` | `stairs.GetStairsRuns()` | ICollection<ElementId> |
| `ICollection<ElementId> GetStairsSupports()` | `stairs.GetStairsSupports()` | ICollection<ElementId> |
| `Boolean IsByComponent(Document, ElementId)` | `Stairs.IsByComponent(document, stairsId)` | Boolean |
| `Boolean IsInEditMode()` | `stairs.IsInEditMode()` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
