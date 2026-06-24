---
title: FamilyItemFactory
classe: Autodesk.Revit.Creation.FamilyItemFactory
namespace: Autodesk.Revit.Creation
eredita: Autodesk.Revit.Creation.ItemFactoryBase
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 30
---

# FamilyItemFactory

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Dimension NewAngularDimension(View, Arc, Reference, Reference, DimensionType)` | `familyItemFactory.NewAngularDimension(view, arc, firstRef, secondRef, dimensionType)` | Dimension |
| `Dimension NewAngularDimension(View, Arc, Reference, Reference)` | `familyItemFactory.NewAngularDimension(view, arc, firstRef, secondRef)` | Dimension |
| `Dimension NewArcLengthDimension(View, Arc, Reference, Reference, Reference, DimensionType)` | `familyItemFactory.NewArcLengthDimension(view, arc, arcRef, firstRef, secondRef, dimensionType)` | Dimension |
| `Dimension NewArcLengthDimension(View, Arc, Reference, Reference, Reference)` | `familyItemFactory.NewArcLengthDimension(view, arc, arcRef, firstRef, secondRef)` | Dimension |
| `Blend NewBlend(Boolean, CurveArray, CurveArray, SketchPlane)` | `familyItemFactory.NewBlend(isSolid, profile1, profile2, sketchPlane)` | Blend |
| `Control NewControl(ControlShape, View, XYZ)` | `familyItemFactory.NewControl(controlShape, view, origin)` | Control |
| `CurveByPoints NewCurveByPoints(ReferencePointArray)` | `familyItemFactory.NewCurveByPoints(points)` | CurveByPoints |
| `Dimension NewDiameterDimension(View, Reference, XYZ)` | `familyItemFactory.NewDiameterDimension(view, arcRef, origin)` | Dimension |
| `Extrusion NewExtrusion(Boolean, CurveArrArray, SketchPlane, Double)` | `familyItemFactory.NewExtrusion(isSolid, profile, sketchPlane, end)` | Extrusion |
| `Form NewExtrusionForm(Boolean, ReferenceArray, XYZ)` | `familyItemFactory.NewExtrusionForm(isSolid, profile, direction)` | Form |
| `Form NewFormByCap(Boolean, ReferenceArray)` | `familyItemFactory.NewFormByCap(isSolid, profile)` | Form |
| `Form NewFormByThickenSingleSurface(Boolean, Form, XYZ)` | `familyItemFactory.NewFormByThickenSingleSurface(isSolid, singleSurfaceForm, thickenDir)` | Form |
| `Dimension NewLinearDimension(View, Line, ReferenceArray, DimensionType)` | `familyItemFactory.NewLinearDimension(view, line, references, dimensionType)` | Dimension |
| `Dimension NewLinearDimension(View, Line, ReferenceArray)` | `familyItemFactory.NewLinearDimension(view, line, references)` | Dimension |
| `Form NewLoftForm(Boolean, ReferenceArrayArray)` | `familyItemFactory.NewLoftForm(isSolid, profiles)` | Form |
| `ModelText NewModelText(String, ModelTextType, SketchPlane, XYZ, HorizontalAlign, Double)` | `familyItemFactory.NewModelText(text, modelTextType, sketchPlane, position, horizontalAlign, depth)` | ModelText |
| `Opening NewOpening(Element, CurveArray)` | `familyItemFactory.NewOpening(host, profile)` | Opening |
| `Dimension NewRadialDimension(View, Reference, XYZ, DimensionType)` | `familyItemFactory.NewRadialDimension(view, arcRef, origin, dimensionType)` | Dimension |
| `Dimension NewRadialDimension(View, Reference, XYZ)` | `familyItemFactory.NewRadialDimension(view, arcRef, origin)` | Dimension |
| `ReferencePoint NewReferencePoint(PointElementReference)` | `familyItemFactory.NewReferencePoint(A_0)` | ReferencePoint |
| `ReferencePoint NewReferencePoint(Transform)` | `familyItemFactory.NewReferencePoint(A_0)` | ReferencePoint |
| `ReferencePoint NewReferencePoint(XYZ)` | `familyItemFactory.NewReferencePoint(A_0)` | ReferencePoint |
| `Revolution NewRevolution(Boolean, CurveArrArray, SketchPlane, Line, Double, Double)` | `familyItemFactory.NewRevolution(isSolid, profile, sketchPlane, axis, startAngle, endAngle)` | Revolution |
| `FormArray NewRevolveForms(Boolean, ReferenceArray, Reference, Double, Double)` | `familyItemFactory.NewRevolveForms(isSolid, profile, axis, startAngle, endAngle)` | FormArray |
| `Sweep NewSweep(Boolean, ReferenceArray, SweepProfile, Int32, ProfilePlaneLocation)` | `familyItemFactory.NewSweep(isSolid, path, profile, profileLocationCurveIndex, profilePlaneLocation)` | Sweep |
| `Sweep NewSweep(Boolean, CurveArray, SketchPlane, SweepProfile, Int32, ProfilePlaneLocation)` | `familyItemFactory.NewSweep(isSolid, path, pathPlane, profile, profileLocationCurveIndex, profilePlaneLocation)` | Sweep |
| `SweptBlend NewSweptBlend(Boolean, Reference, SweepProfile, SweepProfile)` | `familyItemFactory.NewSweptBlend(isSolid, path, bottomProfile, topProfile)` | SweptBlend |
| `SweptBlend NewSweptBlend(Boolean, Curve, SketchPlane, SweepProfile, SweepProfile)` | `familyItemFactory.NewSweptBlend(isSolid, path, pathPlane, bottomProfile, topProfile)` | SweptBlend |
| `Form NewSweptBlendForm(Boolean, ReferenceArray, ReferenceArrayArray)` | `familyItemFactory.NewSweptBlendForm(isSolid, path, profiles)` | Form |
| `SymbolicCurve NewSymbolicCurve(Curve, SketchPlane)` | `familyItemFactory.NewSymbolicCurve(curve, sketchPlane)` | SymbolicCurve |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
