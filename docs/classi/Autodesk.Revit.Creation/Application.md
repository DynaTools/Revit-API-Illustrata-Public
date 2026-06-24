---
title: Application
classe: Autodesk.Revit.Creation.Application
namespace: Autodesk.Revit.Creation
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 53
---

# Application

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `AreaCreationData NewAreaCreationData(ViewPlan, UV)` | `application.NewAreaCreationData(areaView, point)` | AreaCreationData |
| `BoundingBoxUV NewBoundingBoxUV(Double, Double, Double, Double)` | `application.NewBoundingBoxUV(min_u, min_v, max_u, max_v)` | BoundingBoxUV |
| `BoundingBoxUV NewBoundingBoxUV()` | `application.NewBoundingBoxUV()` | BoundingBoxUV |
| `BoundingBoxXYZ NewBoundingBoxXYZ()` | `application.NewBoundingBoxXYZ()` | BoundingBoxXYZ |
| `CategorySet NewCategorySet()` | `application.NewCategorySet()` | CategorySet |
| `Color NewColor()` | `application.NewColor()` | Color |
| `CombinableElementArray NewCombinableElementArray()` | `application.NewCombinableElementArray()` | CombinableElementArray |
| `CurveArrArray NewCurveArrArray()` | `application.NewCurveArrArray()` | CurveArrArray |
| `CurveArray NewCurveArray()` | `application.NewCurveArray()` | CurveArray |
| `CurveLoopsProfile NewCurveLoopsProfile(CurveArrArray)` | `application.NewCurveLoopsProfile(curveLoops)` | CurveLoopsProfile |
| `DoubleArray NewDoubleArray()` | `application.NewDoubleArray()` | DoubleArray |
| `DWFExportOptions NewDWFExportOptions()` | `application.NewDWFExportOptions()` | DWFExportOptions |
| `DWFXExportOptions NewDWFXExportOptions()` | `application.NewDWFXExportOptions()` | DWFXExportOptions |
| `ElementId NewElementId()` | `application.NewElementId()` | ElementId |
| `ElementSet NewElementSet()` | `application.NewElementSet()` | ElementSet |
| `FaceArray NewFaceArray()` | `application.NewFaceArray()` | FaceArray |
| `FamilyInstanceCreationData NewFamilyInstanceCreationData(FamilySymbol, IList<XYZ>)` | `application.NewFamilyInstanceCreationData(symbol, adaptivePoints)` | FamilyInstanceCreationData |
| `FamilyInstanceCreationData NewFamilyInstanceCreationData(Face, Line, FamilySymbol)` | `application.NewFamilyInstanceCreationData(face, position, symbol)` | FamilyInstanceCreationData |
| `FamilyInstanceCreationData NewFamilyInstanceCreationData(Face, XYZ, XYZ, FamilySymbol)` | `application.NewFamilyInstanceCreationData(face, location, referenceDirection, symbol)` | FamilyInstanceCreationData |
| `FamilyInstanceCreationData NewFamilyInstanceCreationData(XYZ, FamilySymbol, XYZ, Element, StructuralType)` | `application.NewFamilyInstanceCreationData(location, symbol, referenceDirection, host, structuralType)` | FamilyInstanceCreationData |
| `FamilyInstanceCreationData NewFamilyInstanceCreationData(XYZ, FamilySymbol, Element, Level, StructuralType)` | `application.NewFamilyInstanceCreationData(location, symbol, host, level, structuralType)` | FamilyInstanceCreationData |
| `FamilyInstanceCreationData NewFamilyInstanceCreationData(XYZ, FamilySymbol, Element, StructuralType)` | `application.NewFamilyInstanceCreationData(location, symbol, host, structuralType)` | FamilyInstanceCreationData |
| `FamilyInstanceCreationData NewFamilyInstanceCreationData(XYZ, FamilySymbol, Level, StructuralType)` | `application.NewFamilyInstanceCreationData(location, symbol, level, structuralType)` | FamilyInstanceCreationData |
| `FamilyInstanceCreationData NewFamilyInstanceCreationData(Curve, FamilySymbol, Level, StructuralType)` | `application.NewFamilyInstanceCreationData(curve, symbol, level, structuralType)` | FamilyInstanceCreationData |
| `FamilyInstanceCreationData NewFamilyInstanceCreationData(XYZ, FamilySymbol, StructuralType)` | `application.NewFamilyInstanceCreationData(location, symbol, structuralType)` | FamilyInstanceCreationData |
| `FamilySymbolProfile NewFamilySymbolProfile(FamilySymbol)` | `application.NewFamilySymbolProfile(familySymbol)` | FamilySymbolProfile |
| `FBXExportOptions NewFBXExportOptions()` | `application.NewFBXExportOptions()` | FBXExportOptions |
| `GBXMLImportOptions NewGBXMLImportOptions()` | `application.NewGBXMLImportOptions()` | GBXMLImportOptions |
| `Options NewGeometryOptions()` | `application.NewGeometryOptions()` | Options |
| `InstanceBinding NewInstanceBinding(CategorySet)` | `application.NewInstanceBinding(categorySet)` | InstanceBinding |
| `InstanceBinding NewInstanceBinding()` | `application.NewInstanceBinding()` | InstanceBinding |
| `IntersectionResultArray NewIntersectionResultArray()` | `application.NewIntersectionResultArray()` | IntersectionResultArray |
| `PointOnEdge NewPointOnEdge(Reference, PointLocationOnCurve)` | `application.NewPointOnEdge(edgeReference, locationOnCurve)` | PointOnEdge |
| `PointOnEdgeEdgeIntersection NewPointOnEdgeEdgeIntersection(Reference, Reference)` | `application.NewPointOnEdgeEdgeIntersection(edgeReference1, edgeReference2)` | PointOnEdgeEdgeIntersection |
| `PointOnEdgeFaceIntersection NewPointOnEdgeFaceIntersection(Reference, Reference, Boolean)` | `application.NewPointOnEdgeFaceIntersection(edgeReference, faceReference, orientWithEdge)` | PointOnEdgeFaceIntersection |
| `PointOnFace NewPointOnFace(Reference, UV)` | `application.NewPointOnFace(faceReference, uv)` | PointOnFace |
| `PointOnPlane NewPointOnPlane(Reference, UV, UV, Double)` | `application.NewPointOnPlane(planeReference, position, xvec, offset)` | PointOnPlane |
| `PointRelativeToPoint NewPointRelativeToPoint(Reference)` | `application.NewPointRelativeToPoint(hostPointReference)` | PointRelativeToPoint |
| `ProjectPosition NewProjectPosition(Double, Double, Double, Double)` | `application.NewProjectPosition(ew, ns, elevation, angle)` | ProjectPosition |
| `ReferenceArray NewReferenceArray()` | `application.NewReferenceArray()` | ReferenceArray |
| `ReferencePointArray NewReferencePointArray()` | `application.NewReferencePointArray()` | ReferencePointArray |
| `SpaceSet NewSpaceSet()` | `application.NewSpaceSet()` | SpaceSet |
| `TypeBinding NewTypeBinding(CategorySet)` | `application.NewTypeBinding(categorySet)` | TypeBinding |
| `TypeBinding NewTypeBinding()` | `application.NewTypeBinding()` | TypeBinding |
| `UV NewUV(UV)` | `application.NewUV(uv)` | UV |
| `UV NewUV(Double, Double)` | `application.NewUV(u, v)` | UV |
| `UV NewUV()` | `application.NewUV()` | UV |
| `VertexIndexPair NewVertexIndexPair(Int32, Int32)` | `application.NewVertexIndexPair(iTop, iBottom)` | VertexIndexPair |
| `VertexIndexPairArray NewVertexIndexPairArray()` | `application.NewVertexIndexPairArray()` | VertexIndexPairArray |
| `ViewSet NewViewSet()` | `application.NewViewSet()` | ViewSet |
| `XYZ NewXYZ(XYZ)` | `application.NewXYZ(xyz)` | XYZ |
| `XYZ NewXYZ(Double, Double, Double)` | `application.NewXYZ(x, y, z)` | XYZ |
| `XYZ NewXYZ()` | `application.NewXYZ()` | XYZ |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
