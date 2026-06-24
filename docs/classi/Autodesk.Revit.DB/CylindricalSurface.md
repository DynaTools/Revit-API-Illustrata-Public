---
title: CylindricalSurface
classe: Autodesk.Revit.DB.CylindricalSurface
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Surface
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# CylindricalSurface

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ Axis { get; }` | `cylindricalSurface.Axis` | XYZ |
| `XYZ Origin { get; }` | `cylindricalSurface.Origin` | XYZ |
| `Double Radius { get; }` | `cylindricalSurface.Radius` | Double |
| `XYZ XDir { get; }` | `cylindricalSurface.XDir` | XYZ |
| `XYZ YDir { get; }` | `cylindricalSurface.YDir` | XYZ |
| `CylindricalSurface Create(Frame, Double)` | `CylindricalSurface.Create(frameOfReference, radius)` | CylindricalSurface |
| `Frame GetFrameOfReference()` | `cylindricalSurface.GetFrameOfReference()` | Frame |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
