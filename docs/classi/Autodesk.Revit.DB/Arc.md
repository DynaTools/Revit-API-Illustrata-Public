---
title: Arc
classe: Autodesk.Revit.DB.Arc
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Curve
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# Arc

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ Center { get; }` | `arc.Center` | XYZ |
| `XYZ Normal { get; }` | `arc.Normal` | XYZ |
| `Double Radius { get; }` | `arc.Radius` | Double |
| `XYZ XDirection { get; }` | `arc.XDirection` | XYZ |
| `XYZ YDirection { get; }` | `arc.YDirection` | XYZ |
| `Arc Create(XYZ, XYZ, XYZ)` | `Arc.Create(end0, end1, pointOnArc)` | Arc |
| `Arc Create(Plane, Double, Double, Double)` | `Arc.Create(plane, radius, startAngle, endAngle)` | Arc |
| `Arc Create(XYZ, Double, Double, Double, XYZ, XYZ)` | `Arc.Create(center, radius, startAngle, endAngle, xAxis, yAxis)` | Arc |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
