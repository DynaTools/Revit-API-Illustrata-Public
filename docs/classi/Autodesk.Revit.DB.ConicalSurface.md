---
title: ConicalSurface
classe: Autodesk.Revit.DB.ConicalSurface
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Surface
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# ConicalSurface

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ Axis { get; }` | `conicalSurface.Axis` | XYZ |
| `Double HalfAngle { get; }` | `conicalSurface.HalfAngle` | Double |
| `XYZ Origin { get; }` | `conicalSurface.Origin` | XYZ |
| `XYZ XDir { get; }` | `conicalSurface.XDir` | XYZ |
| `XYZ YDir { get; }` | `conicalSurface.YDir` | XYZ |
| `ConicalSurface Create(Frame, Double)` | `ConicalSurface.Create(frameOfReference, halfAngle)` | ConicalSurface |
| `Frame GetFrameOfReference()` | `conicalSurface.GetFrameOfReference()` | Frame |
| `Boolean IsValidConeAngle(Double)` | `ConicalSurface.IsValidConeAngle(halfAngle)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
