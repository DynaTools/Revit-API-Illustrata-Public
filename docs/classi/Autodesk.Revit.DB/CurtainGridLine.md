---
title: CurtainGridLine
classe: Autodesk.Revit.DB.CurtainGridLine
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.HostObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# CurtainGridLine

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `CurveArray AllSegmentCurves { get; }` | `curtainGridLine.AllSegmentCurves` | CurveArray |
| `CurveArray ExistingSegmentCurves { get; }` | `curtainGridLine.ExistingSegmentCurves` | CurveArray |
| `Curve FullCurve { get; }` | `curtainGridLine.FullCurve` | Curve |
| `Boolean IsUGridLine { get; }` | `curtainGridLine.IsUGridLine` | Boolean |
| `Boolean Lock { get; set; }` | `curtainGridLine.Lock` | Boolean |
| `CurveArray SkippedSegmentCurves { get; }` | `curtainGridLine.SkippedSegmentCurves` | CurveArray |
| `Void AddAllSegments()` | `curtainGridLine.AddAllSegments()` | Void |
| `ElementSet AddMullions(Curve, MullionType, Boolean)` | `curtainGridLine.AddMullions(segment, mullionType, oneSegmentOnly)` | ElementSet |
| `Void AddSegment(Curve)` | `curtainGridLine.AddSegment(curve)` | Void |
| `Void RemoveSegment(Curve)` | `curtainGridLine.RemoveSegment(curve)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
