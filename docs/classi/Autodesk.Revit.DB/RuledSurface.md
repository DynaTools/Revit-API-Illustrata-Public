---
title: RuledSurface
classe: Autodesk.Revit.DB.RuledSurface
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Surface
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# RuledSurface

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Surface Create(Curve, XYZ)` | `RuledSurface.Create(profileCurve, point)` | Surface |
| `Surface Create(Curve, Curve)` | `RuledSurface.Create(profileCurve1, profileCurve2)` | Surface |
| `Curve GetFirstProfileCurve()` | `ruledSurface.GetFirstProfileCurve()` | Curve |
| `XYZ GetFirstProfilePoint()` | `ruledSurface.GetFirstProfilePoint()` | XYZ |
| `Curve GetSecondProfileCurve()` | `ruledSurface.GetSecondProfileCurve()` | Curve |
| `XYZ GetSecondProfilePoint()` | `ruledSurface.GetSecondProfilePoint()` | XYZ |
| `Boolean HasFirstProfilePoint()` | `ruledSurface.HasFirstProfilePoint()` | Boolean |
| `Boolean HasSecondProfilePoint()` | `ruledSurface.HasSecondProfilePoint()` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
