---
title: DirectShapeType
classe: Autodesk.Revit.DB.DirectShapeType
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.ElementType
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 41
---

# DirectShapeType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `DirectShapeTypeUserAssignability UserAssignability { get; set; }` | `directShapeType.UserAssignability` | DirectShapeTypeUserAssignability |
| `Void AddExternallyTaggedGeometry(ExternallyTaggedGeometryObject)` | `directShapeType.AddExternallyTaggedGeometry(externallyTaggedGeometry)` | Void |
| `Void AddReferenceCurve(Curve, DirectShapeReferenceOptions)` | `directShapeType.AddReferenceCurve(refCurve, options)` | Void |
| `Void AddReferenceCurve(Curve)` | `directShapeType.AddReferenceCurve(refCurve)` | Void |
| `Void AddReferencePlane(Plane, BoundingBoxUV, DirectShapeReferenceOptions)` | `directShapeType.AddReferencePlane(refPlane, boundingBoxUV, options)` | Void |
| `Void AddReferencePlane(Plane, DirectShapeReferenceOptions)` | `directShapeType.AddReferencePlane(refPlane, options)` | Void |
| `Void AddReferencePlane(Plane, BoundingBoxUV)` | `directShapeType.AddReferencePlane(refPlane, boundingBoxUV)` | Void |
| `Void AddReferencePlane(Plane)` | `directShapeType.AddReferencePlane(refPlane)` | Void |
| `Void AddReferencePoint(XYZ, DirectShapeReferenceOptions)` | `directShapeType.AddReferencePoint(refPoint, options)` | Void |
| `Void AddReferencePoint(XYZ)` | `directShapeType.AddReferencePoint(refPoint)` | Void |
| `Void AppendShape(ShapeBuilder)` | `directShapeType.AppendShape(ShapeBuilder)` | Void |
| `Void AppendShape(IList<GeometryObject>, DirectShapeTargetViewType)` | `directShapeType.AppendShape(pGeomArr, viewType)` | Void |
| `Void AppendShape(IList<GeometryObject>)` | `directShapeType.AppendShape(pGeomArr)` | Void |
| `Boolean AreOptionsValid(DirectShapeTypeOptions)` | `directShapeType.AreOptionsValid(options)` | Boolean |
| `Boolean AreValidDirectShapeReferenceOptions(DirectShapeReferenceOptions)` | `directShapeType.AreValidDirectShapeReferenceOptions(options)` | Boolean |
| `Boolean CanChangeFamilyName()` | `directShapeType.CanChangeFamilyName()` | Boolean |
| `Boolean CanCreateParts()` | `directShapeType.CanCreateParts()` | Boolean |
| `DirectShapeType Create(Document, String, ElementId, DirectShapeTypeOptions)` | `DirectShapeType.Create(document, name, categoryId, options)` | DirectShapeType |
| `DirectShapeType Create(Document, String, ElementId)` | `DirectShapeType.Create(document, name, categoryId)` | DirectShapeType |
| `ExternallyTaggedGeometryObject GetExternallyTaggedGeometry(ExternalGeometryId)` | `directShapeType.GetExternallyTaggedGeometry(externalId)` | ExternallyTaggedGeometryObject |
| `Reference GetExternallyTaggedReference(ExternalGeometryId)` | `directShapeType.GetExternallyTaggedReference(externalId)` | Reference |
| `DirectShapeTypeOptions GetOptions()` | `directShapeType.GetOptions()` | DirectShapeTypeOptions |
| `Boolean HasExternalGeometry(ExternalGeometryId)` | `directShapeType.HasExternalGeometry(externalId)` | Boolean |
| `Boolean HasExternallyTaggedReference(ExternalGeometryId)` | `directShapeType.HasExternallyTaggedReference(externalId)` | Boolean |
| `Boolean IsValidReferenceCurve(Curve)` | `DirectShapeType.IsValidReferenceCurve(curve)` | Boolean |
| `Boolean IsValidReferencePlaneBoundingBoxUV(BoundingBoxUV)` | `DirectShapeType.IsValidReferencePlaneBoundingBoxUV(boundingBoxUV)` | Boolean |
| `Boolean IsValidShape(ExternallyTaggedGeometryObject)` | `directShapeType.IsValidShape(externallyTaggedGeometry)` | Boolean |
| `Boolean IsValidShape(IList<GeometryObject>, DirectShapeTargetViewType)` | `directShapeType.IsValidShape(shape, viewType)` | Boolean |
| `Boolean IsValidShape(IList<GeometryObject>)` | `directShapeType.IsValidShape(shape)` | Boolean |
| `Boolean IsValidUsage(ExternallyTaggedGeometryObject)` | `directShapeType.IsValidUsage(externallyTaggedGeometry)` | Boolean |
| `Void RemoveAllReferenceObjects()` | `directShapeType.RemoveAllReferenceObjects()` | Void |
| `Void RemoveExternallyTaggedGeometry(ExternalGeometryId)` | `directShapeType.RemoveExternallyTaggedGeometry(externalId)` | Void |
| `Void RemoveReferenceObject(ExternalGeometryId)` | `directShapeType.RemoveReferenceObject(externalId)` | Void |
| `Void RemoveReferenceObject(String)` | `directShapeType.RemoveReferenceObject(refName)` | Void |
| `Void ResetExternallyTaggedGeometry()` | `directShapeType.ResetExternallyTaggedGeometry()` | Void |
| `Void SetFamilyName(String)` | `directShapeType.SetFamilyName(name)` | Void |
| `Void SetOptions(DirectShapeTypeOptions)` | `directShapeType.SetOptions(options)` | Void |
| `Void SetShape(ShapeBuilder)` | `directShapeType.SetShape(pBuilder)` | Void |
| `Void SetShape(IList<GeometryObject>, DirectShapeTargetViewType)` | `directShapeType.SetShape(pGeomArr, viewType)` | Void |
| `Void SetShape(IList<GeometryObject>)` | `directShapeType.SetShape(pGeomArr)` | Void |
| `Void UpdateExternallyTaggedGeometry(ExternallyTaggedGeometryObject)` | `directShapeType.UpdateExternallyTaggedGeometry(externallyTaggedGeometry)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
