---
title: FilledRegion
classe: Autodesk.Revit.DB.FilledRegion
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# FilledRegion

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsMasking { get; }` | `filledRegion.IsMasking` | Boolean |
| `FilledRegion Create(Document, ElementId, SketchPlane, IList<CurveLoop>)` | `FilledRegion.Create(document, typeId, sketchPlane, boundaries)` | FilledRegion |
| `FilledRegion Create(Document, ElementId, ElementId, IList<CurveLoop>)` | `FilledRegion.Create(document, typeId, viewId, boundaries)` | FilledRegion |
| `FilledRegion CreateMaskingRegion(Document, SketchPlane, IList<CurveLoop>)` | `FilledRegion.CreateMaskingRegion(document, sketchPlane, boundaries)` | FilledRegion |
| `FilledRegion CreateMaskingRegion(Document, ElementId, IList<CurveLoop>)` | `FilledRegion.CreateMaskingRegion(document, viewId, boundaries)` | FilledRegion |
| `IList<CurveLoop> GetBoundaries()` | `filledRegion.GetBoundaries()` | IList<CurveLoop> |
| `IList<ElementId> GetValidLineStyleIdsForFilledRegion(Document)` | `FilledRegion.GetValidLineStyleIdsForFilledRegion(document)` | IList<ElementId> |
| `Boolean IsValidFilledRegionTypeId(Document, ElementId)` | `FilledRegion.IsValidFilledRegionTypeId(document, typeId)` | Boolean |
| `Boolean IsValidLineStyleIdForFilledRegion(Document, ElementId)` | `FilledRegion.IsValidLineStyleIdForFilledRegion(document, lineStyleId)` | Boolean |
| `Void SetLineStyleId(ElementId)` | `filledRegion.SetLineStyleId(lineStyleId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
