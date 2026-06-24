---
title: CurveUV
classe: Autodesk.Revit.DB.CurveUV
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# CurveUV

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsBound { get; }` | `curveUV.IsBound` | Boolean |
| `Boolean IsValidObject { get; }` | `curveUV.IsValidObject` | Boolean |
| `Curve As3DCurveInXYPlane()` | `curveUV.As3DCurveInXYPlane()` | Curve |
| `IList<UV> ComputeDerivatives(Double, Boolean)` | `curveUV.ComputeDerivatives(parameter, normalized)` | IList<UV> |
| `CurveUV Create(Curve)` | `CurveUV.Create(curve3D)` | CurveUV |
| `Void Dispose()` | `curveUV.Dispose()` | Void |
| `UV Evaluate(Double, Boolean)` | `curveUV.Evaluate(parameter, normalized)` | UV |
| `Double GetEndParameter(Int32)` | `curveUV.GetEndParameter(index)` | Double |
| `CurveUV Transform(Transform2D)` | `curveUV.Transform(trfUV)` | CurveUV |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
