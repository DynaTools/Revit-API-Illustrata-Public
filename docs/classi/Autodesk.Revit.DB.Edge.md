---
title: Edge
classe: Autodesk.Revit.DB.Edge
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.GeometryObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 15
---

# Edge

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double ApproximateLength { get; }` | `edge.ApproximateLength` | Double |
| `Reference Reference { get; }` | `edge.Reference` | Reference |
| `Curve AsCurve()` | `edge.AsCurve()` | Curve |
| `Curve AsCurveFollowingFace(Face)` | `edge.AsCurveFollowingFace(faceForDir)` | Curve |
| `Transform ComputeDerivatives(Double)` | `edge.ComputeDerivatives(parameter)` | Transform |
| `XYZ Evaluate(Double)` | `edge.Evaluate(param)` | XYZ |
| `UV EvaluateOnFace(Double, Face)` | `edge.EvaluateOnFace(param, face)` | UV |
| `CurveUV GetCurveUV(Int32, Transform2D)` | `edge.GetCurveUV(index, transform)` | CurveUV |
| `CurveUV GetCurveUV(Int32)` | `edge.GetCurveUV(index)` | CurveUV |
| `Reference GetEndPointReference(Int32)` | `edge.GetEndPointReference(index)` | Reference |
| `Face GetFace(Int32)` | `edge.GetFace(index)` | Face |
| `Boolean IsFlippedOnFace(Face)` | `edge.IsFlippedOnFace(face)` | Boolean |
| `Boolean IsFlippedOnFace(Int32)` | `edge.IsFlippedOnFace(index)` | Boolean |
| `IList<XYZ> Tessellate()` | `edge.Tessellate()` | IList<XYZ> |
| `IList<UV> TessellateOnFace(Face)` | `edge.TessellateOnFace(face)` | IList<UV> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
