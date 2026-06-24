---
title: Form
classe: Autodesk.Revit.DB.Form
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.GenericForm
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 43
---

# Form

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean AreProfilesConstrained { get; set; }` | `form.AreProfilesConstrained` | Boolean |
| `Double BaseOffset { get; set; }` | `form.BaseOffset` | Double |
| `ReferenceArray CurveLoopReferencesOnProfile { get; }` | `form.CurveLoopReferencesOnProfile` | ReferenceArray |
| `Boolean HasOneOrMoreReferenceProfiles { get; }` | `form.HasOneOrMoreReferenceProfiles` | Boolean |
| `Boolean HasOpenGeometry { get; }` | `form.HasOpenGeometry` | Boolean |
| `Boolean IsInXRayMode { get; set; }` | `form.IsInXRayMode` | Boolean |
| `Int32 PathCurveCount { get; }` | `form.PathCurveCount` | Int32 |
| `Reference PathCurveReference { get; }` | `form.PathCurveReference` | Reference |
| `Int32 ProfileCount { get; }` | `form.ProfileCount` | Int32 |
| `Int32 ProfileCurveLoopCount { get; }` | `form.ProfileCurveLoopCount` | Int32 |
| `Double TopOffset { get; set; }` | `form.TopOffset` | Double |
| `Void AddEdge(Reference, Reference)` | `form.AddEdge(startPointReference, endPointReference)` | Void |
| `Void AddEdge(Reference, Double, Reference, Double)` | `form.AddEdge(startEdgeReference, startParam, endEdgeReference, endParam)` | Void |
| `Void AddEdge(Reference, XYZ)` | `form.AddEdge(faceReference, point)` | Void |
| `Int32 AddProfile(Reference, Double)` | `form.AddProfile(edgeReference, param)` | Int32 |
| `Boolean CanManipulateProfile(Int32)` | `form.CanManipulateProfile(profileIndex)` | Boolean |
| `Boolean CanManipulateSubElement(Reference)` | `form.CanManipulateSubElement(subElementReference)` | Boolean |
| `Void ConstrainProfiles(Int32)` | `form.ConstrainProfiles(primaryProfileIndex)` | Void |
| `Void DeleteProfile(Int32)` | `form.DeleteProfile(profileIndex)` | Void |
| `Void DeleteSubElement(Reference)` | `form.DeleteSubElement(subElementReference)` | Void |
| `ReferenceArray GetControlPoints(Reference)` | `form.GetControlPoints(curveOrEdgeOrFaceReference)` | ReferenceArray |
| `ReferenceArray GetCurvesAndEdgesReference(Reference)` | `form.GetCurvesAndEdgesReference(pointReference)` | ReferenceArray |
| `Int32 GetPathCurveIndexByCurveReference(Reference)` | `form.GetPathCurveIndexByCurveReference(curveReference)` | Int32 |
| `Void GetProfileAndCurveLoopIndexFromReference(Reference, Int32&, Int32&)` | `form.GetProfileAndCurveLoopIndexFromReference(curveOrEdgeReference, profileIndex, curveLoopIndex)` | Void |
| `Boolean IsAutoCreaseEdge(Reference)` | `form.IsAutoCreaseEdge(edgeReference)` | Boolean |
| `Boolean IsBeginningFace(Reference)` | `form.IsBeginningFace(faceReference)` | Boolean |
| `Boolean IsConnectingEdge(Reference)` | `form.IsConnectingEdge(edgeReference)` | Boolean |
| `Boolean IsCurveReference(Reference)` | `form.IsCurveReference(curveReference)` | Boolean |
| `Boolean IsEdgeReference(Reference)` | `form.IsEdgeReference(edgeReference)` | Boolean |
| `Boolean IsEndFace(Reference)` | `form.IsEndFace(faceReference)` | Boolean |
| `Boolean IsFaceReference(Reference)` | `form.IsFaceReference(faceReference)` | Boolean |
| `Boolean IsProfileEdge(Reference)` | `form.IsProfileEdge(curveOrEdgeReference)` | Boolean |
| `Boolean IsReferenceOnlyProfile(Int32)` | `form.IsReferenceOnlyProfile(profileIndex)` | Boolean |
| `Boolean IsSideFace(Reference)` | `form.IsSideFace(faceReference)` | Boolean |
| `Boolean IsVertexReference(Reference)` | `form.IsVertexReference(vertexReference)` | Boolean |
| `Void MoveProfile(Int32, XYZ)` | `form.MoveProfile(profileIndex, offset)` | Void |
| `Void MoveSubElement(Reference, XYZ)` | `form.MoveSubElement(subElementReference, offset)` | Void |
| `Void Rehost(SketchPlane, XYZ)` | `form.Rehost(sketchPlane, location)` | Void |
| `Void Rehost(Reference, XYZ)` | `form.Rehost(hostRef, location)` | Void |
| `Void RotateProfile(Int32, Line, Double)` | `form.RotateProfile(profileIndex, axis, angle)` | Void |
| `Void RotateSubElement(Reference, Line, Double)` | `form.RotateSubElement(subElementReference, axis, angle)` | Void |
| `Void ScaleProfile(Int32, Double, XYZ)` | `form.ScaleProfile(profileIndex, factor, origin)` | Void |
| `Void ScaleSubElement(Reference, Double, XYZ)` | `form.ScaleSubElement(subElementReference, factor, origin)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
