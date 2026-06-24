---
title: BeamSystem
classe: Autodesk.Revit.DB.BeamSystem
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 14
---

# BeamSystem

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `BeamSystemType BeamSystemType { get; set; }` | `beamSystem.BeamSystemType` | BeamSystemType |
| `FamilySymbol BeamType { get; set; }` | `beamSystem.BeamType` | FamilySymbol |
| `XYZ Direction { get; }` | `beamSystem.Direction` | XYZ |
| `Double Elevation { get; set; }` | `beamSystem.Elevation` | Double |
| `LayoutRule LayoutRule { get; set; }` | `beamSystem.LayoutRule` | LayoutRule |
| `Level Level { get; set; }` | `beamSystem.Level` | Level |
| `CurveArray Profile { get; set; }` | `beamSystem.Profile` | CurveArray |
| `BeamSystem BeamBelongsTo(FamilyInstance)` | `BeamSystem.BeamBelongsTo(beam)` | BeamSystem |
| `BeamSystem Create(Document, IList<Curve>, Level, Int32, Boolean)` | `BeamSystem.Create(document, profile, level, curveIndexForDirection, is3d)` | BeamSystem |
| `BeamSystem Create(Document, IList<Curve>, Level, XYZ, Boolean)` | `BeamSystem.Create(document, profile, level, direction, is3d)` | BeamSystem |
| `BeamSystem Create(Document, IList<Curve>, SketchPlane, XYZ, Boolean)` | `BeamSystem.Create(document, profile, sketchPlane, direction, is3d)` | BeamSystem |
| `BeamSystem Create(Document, IList<Curve>, SketchPlane, Int32)` | `BeamSystem.Create(document, profile, sketchPlane, curveIndexForDirection)` | BeamSystem |
| `Void DropBeamSystem(BeamSystem)` | `BeamSystem.DropBeamSystem(beamSystem)` | Void |
| `ICollection<ElementId> GetBeamIds()` | `beamSystem.GetBeamIds()` | ICollection<ElementId> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
