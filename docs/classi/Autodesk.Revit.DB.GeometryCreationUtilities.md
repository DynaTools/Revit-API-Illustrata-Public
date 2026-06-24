---
title: GeometryCreationUtilities
classe: Autodesk.Revit.DB.GeometryCreationUtilities
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# GeometryCreationUtilities

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Solid CreateBlendGeometry(CurveLoop, CurveLoop, ICollection<VertexPair>, SolidOptions)` | `GeometryCreationUtilities.CreateBlendGeometry(firstLoop, secondLoop, vertexPairs, solidOptions)` | Solid |
| `Solid CreateBlendGeometry(CurveLoop, CurveLoop, ICollection<VertexPair>)` | `GeometryCreationUtilities.CreateBlendGeometry(firstLoop, secondLoop, vertexPairs)` | Solid |
| `Solid CreateExtrusionGeometry(IList<CurveLoop>, XYZ, Double, SolidOptions)` | `GeometryCreationUtilities.CreateExtrusionGeometry(profileLoops, extrusionDir, extrusionDist, solidOptions)` | Solid |
| `Solid CreateExtrusionGeometry(IList<CurveLoop>, XYZ, Double)` | `GeometryCreationUtilities.CreateExtrusionGeometry(profileLoops, extrusionDir, extrusionDist)` | Solid |
| `Solid CreateFixedReferenceSweptGeometry(CurveLoop, Int32, Double, IList<CurveLoop>, XYZ, SolidOptions)` | `GeometryCreationUtilities.CreateFixedReferenceSweptGeometry(sweepPath, pathAttachmentCrvIdx, pathAttachmentParam, profileLoops, fixedReferenceDirection, solidOptions)` | Solid |
| `Solid CreateFixedReferenceSweptGeometry(CurveLoop, Int32, Double, IList<CurveLoop>, XYZ)` | `GeometryCreationUtilities.CreateFixedReferenceSweptGeometry(sweepPath, pathAttachmentCrvIdx, pathAttachmentParam, profileLoops, fixedReferenceDirection)` | Solid |
| `Solid CreateLoftGeometry(IList<CurveLoop>, SolidOptions)` | `GeometryCreationUtilities.CreateLoftGeometry(profileLoops, solidOptions)` | Solid |
| `Solid CreateRevolvedGeometry(Frame, IList<CurveLoop>, Double, Double, SolidOptions)` | `GeometryCreationUtilities.CreateRevolvedGeometry(coordinateFrame, profileLoops, startAngle, endAngle, solidOptions)` | Solid |
| `Solid CreateRevolvedGeometry(Frame, IList<CurveLoop>, Double, Double)` | `GeometryCreationUtilities.CreateRevolvedGeometry(coordinateFrame, profileLoops, startAngle, endAngle)` | Solid |
| `Solid CreateSweptBlendGeometry(Curve, IList<Double>, IList<CurveLoop>, IList<ICollection<VertexPair>>, SolidOptions)` | `GeometryCreationUtilities.CreateSweptBlendGeometry(pathCurve, pathParams, profileLoops, vertexPairs, solidOptions)` | Solid |
| `Solid CreateSweptBlendGeometry(Curve, IList<Double>, IList<CurveLoop>, IList<ICollection<VertexPair>>)` | `GeometryCreationUtilities.CreateSweptBlendGeometry(pathCurve, pathParams, profileLoops, vertexPairs)` | Solid |
| `Solid CreateSweptGeometry(CurveLoop, Int32, Double, IList<CurveLoop>, SolidOptions)` | `GeometryCreationUtilities.CreateSweptGeometry(sweepPath, pathAttachmentCrvIdx, pathAttachmentParam, profileLoops, solidOptions)` | Solid |
| `Solid CreateSweptGeometry(CurveLoop, Int32, Double, IList<CurveLoop>)` | `GeometryCreationUtilities.CreateSweptGeometry(sweepPath, pathAttachmentCrvIdx, pathAttachmentParam, profileLoops)` | Solid |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
