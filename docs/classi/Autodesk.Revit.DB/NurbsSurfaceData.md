---
title: NurbsSurfaceData
classe: Autodesk.Revit.DB.NurbsSurfaceData
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 12
---

# NurbsSurfaceData

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 DegreeU { get; }` | `nurbsSurfaceData.DegreeU` | Int32 |
| `Int32 DegreeV { get; }` | `nurbsSurfaceData.DegreeV` | Int32 |
| `Boolean IsRational { get; }` | `nurbsSurfaceData.IsRational` | Boolean |
| `Boolean IsValidObject { get; }` | `nurbsSurfaceData.IsValidObject` | Boolean |
| `Boolean ReverseOrientation { get; }` | `nurbsSurfaceData.ReverseOrientation` | Boolean |
| `NurbsSurfaceData Create(Int32, Int32, IList<Double>, IList<Double>, IList<XYZ>, IList<Double>, Boolean)` | `NurbsSurfaceData.Create(degreeU, degreeV, knotsU, knotsV, controlPoints, weights, bReverseOrientation)` | NurbsSurfaceData |
| `Void Dispose()` | `nurbsSurfaceData.Dispose()` | Void |
| `IList<XYZ> GetControlPoints()` | `nurbsSurfaceData.GetControlPoints()` | IList<XYZ> |
| `IList<Double> GetKnotsU()` | `nurbsSurfaceData.GetKnotsU()` | IList<Double> |
| `IList<Double> GetKnotsV()` | `nurbsSurfaceData.GetKnotsV()` | IList<Double> |
| `IList<Double> GetWeights()` | `nurbsSurfaceData.GetWeights()` | IList<Double> |
| `Boolean IsValid()` | `nurbsSurfaceData.IsValid()` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
