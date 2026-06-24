---
title: Floor
classe: Autodesk.Revit.DB.Floor
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.CeilingAndFloor
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# Floor

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `FloorType FloorType { get; set; }` | `floor.FloorType` | FloorType |
| `ElementId SketchId { get; }` | `floor.SketchId` | ElementId |
| `SlabShapeEditor SlabShapeEditor { get; }` | `floor.SlabShapeEditor` | SlabShapeEditor |
| `Double SpanDirectionAngle { get; set; }` | `floor.SpanDirectionAngle` | Double |
| `Floor Create(Document, IList<CurveLoop>, ElementId, ElementId)` | `Floor.Create(document, profile, floorTypeId, levelId)` | Floor |
| `Floor Create(Document, IList<CurveLoop>, ElementId, ElementId, Boolean, Line, Double)` | `Floor.Create(document, profile, floorTypeId, levelId, isStructural, slopeArrow, slope)` | Floor |
| `ElementId GetDefaultFloorType(Document, Boolean)` | `Floor.GetDefaultFloorType(document, isFoundation)` | ElementId |
| `XYZ GetNormalAtVerticalProjectionPoint(XYZ, FloorFace)` | `floor.GetNormalAtVerticalProjectionPoint(modelLocation, floorFace)` | XYZ |
| `SlabShapeEditor GetSlabShapeEditor()` | `floor.GetSlabShapeEditor()` | SlabShapeEditor |
| `ICollection<ElementId> GetSpanDirectionSymbolIds()` | `floor.GetSpanDirectionSymbolIds()` | ICollection<ElementId> |
| `XYZ GetVerticalProjectionPoint(XYZ, FloorFace)` | `floor.GetVerticalProjectionPoint(modelLocation, floorFace)` | XYZ |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
