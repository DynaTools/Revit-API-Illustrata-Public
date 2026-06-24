---
title: HostedSweep
classe: Autodesk.Revit.DB.HostedSweep
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.HostObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# HostedSweep

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double Angle { get; set; }` | `hostedSweep.Angle` | Double |
| `Boolean HorizontalFlipped { get; }` | `hostedSweep.HorizontalFlipped` | Boolean |
| `Double HorizontalOffset { get; set; }` | `hostedSweep.HorizontalOffset` | Double |
| `Double Length { get; }` | `hostedSweep.Length` | Double |
| `Curve ReferenceCurve { get; }` | `hostedSweep.ReferenceCurve` | Curve |
| `Boolean VerticalFlipped { get; }` | `hostedSweep.VerticalFlipped` | Boolean |
| `Double VerticalOffset { get; set; }` | `hostedSweep.VerticalOffset` | Double |
| `Void AddSegment(Reference)` | `hostedSweep.AddSegment(targetRef)` | Void |
| `Double GetEndPointParameter(Reference, Int32)` | `hostedSweep.GetEndPointParameter(targetRef, endIdx)` | Double |
| `Void HorizontalFlip()` | `hostedSweep.HorizontalFlip()` | Void |
| `Void RemoveSegment(Reference)` | `hostedSweep.RemoveSegment(targetRef)` | Void |
| `Boolean SetEndPointParameter(Reference, Int32, Double)` | `hostedSweep.SetEndPointParameter(targetRef, endIdx, param)` | Boolean |
| `Void VerticalFlip()` | `hostedSweep.VerticalFlip()` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
