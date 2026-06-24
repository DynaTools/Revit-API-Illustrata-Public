---
title: ItemFactoryBase
classe: Autodesk.Revit.Creation.ItemFactoryBase
namespace: Autodesk.Revit.Creation
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 22
---

# ItemFactoryBase

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Dimension NewAlignment(View, Reference, Reference)` | `itemFactoryBase.NewAlignment(view, reference1, reference2)` | Dimension |
| `DetailCurve NewDetailCurve(View, Curve)` | `itemFactoryBase.NewDetailCurve(view, geometryCurve)` | DetailCurve |
| `DetailCurveArray NewDetailCurveArray(View, CurveArray)` | `itemFactoryBase.NewDetailCurveArray(view, geometryCurveArray)` | DetailCurveArray |
| `Dimension NewDimension(View, Line, ReferenceArray, DimensionType)` | `itemFactoryBase.NewDimension(view, line, references, dimensionType)` | Dimension |
| `Dimension NewDimension(View, Line, ReferenceArray)` | `itemFactoryBase.NewDimension(view, line, references)` | Dimension |
| `FamilyInstance NewFamilyInstance(Line, FamilySymbol, View)` | `itemFactoryBase.NewFamilyInstance(line, symbol, specView)` | FamilyInstance |
| `FamilyInstance NewFamilyInstance(XYZ, FamilySymbol, View)` | `itemFactoryBase.NewFamilyInstance(origin, symbol, specView)` | FamilyInstance |
| `FamilyInstance NewFamilyInstance(Reference, Line, FamilySymbol)` | `itemFactoryBase.NewFamilyInstance(reference, position, symbol)` | FamilyInstance |
| `FamilyInstance NewFamilyInstance(Reference, XYZ, XYZ, FamilySymbol)` | `itemFactoryBase.NewFamilyInstance(reference, location, referenceDirection, symbol)` | FamilyInstance |
| `FamilyInstance NewFamilyInstance(Face, Line, FamilySymbol)` | `itemFactoryBase.NewFamilyInstance(face, position, symbol)` | FamilyInstance |
| `FamilyInstance NewFamilyInstance(Face, XYZ, XYZ, FamilySymbol)` | `itemFactoryBase.NewFamilyInstance(face, location, referenceDirection, symbol)` | FamilyInstance |
| `FamilyInstance NewFamilyInstance(XYZ, FamilySymbol, StructuralType)` | `itemFactoryBase.NewFamilyInstance(location, symbol, structuralType)` | FamilyInstance |
| `FamilyInstance NewFamilyInstance(XYZ, FamilySymbol, Level, StructuralType)` | `itemFactoryBase.NewFamilyInstance(location, symbol, level, structuralType)` | FamilyInstance |
| `FamilyInstance NewFamilyInstance(XYZ, FamilySymbol, Element, StructuralType)` | `itemFactoryBase.NewFamilyInstance(location, symbol, host, structuralType)` | FamilyInstance |
| `FamilyInstance NewFamilyInstance(XYZ, FamilySymbol, XYZ, Element, StructuralType)` | `itemFactoryBase.NewFamilyInstance(location, symbol, referenceDirection, host, structuralType)` | FamilyInstance |
| `ICollection<ElementId> NewFamilyInstances2(List<FamilyInstanceCreationData>)` | `itemFactoryBase.NewFamilyInstances2(dataList)` | ICollection<ElementId> |
| `Group NewGroup(ICollection<ElementId>)` | `itemFactoryBase.NewGroup(elementIds)` | Group |
| `ModelCurve NewModelCurve(Curve, SketchPlane)` | `itemFactoryBase.NewModelCurve(geometryCurve, sketchPlane)` | ModelCurve |
| `ModelCurveArray NewModelCurveArray(CurveArray, SketchPlane)` | `itemFactoryBase.NewModelCurveArray(geometryCurveArray, sketchPlane)` | ModelCurveArray |
| `ReferencePlane NewReferencePlane(XYZ, XYZ, XYZ, View)` | `itemFactoryBase.NewReferencePlane(bubbleEnd, freeEnd, cutVec, pView)` | ReferencePlane |
| `ReferencePlane NewReferencePlane2(XYZ, XYZ, XYZ, View)` | `itemFactoryBase.NewReferencePlane2(bubbleEnd, freeEnd, thirdPnt, pView)` | ReferencePlane |
| `Group PlaceGroup(XYZ, GroupType)` | `itemFactoryBase.PlaceGroup(location, groupType)` | Group |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
