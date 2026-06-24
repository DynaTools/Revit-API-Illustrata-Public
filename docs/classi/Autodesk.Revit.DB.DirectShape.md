---
title: DirectShape
classe: Autodesk.Revit.DB.DirectShape
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 49
---

# DirectShape

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String ApplicationDataId { get; set; }` | `directShape.ApplicationDataId` | String |
| `String ApplicationId { get; set; }` | `directShape.ApplicationId` | String |
| `ElementId TypeId { get; }` | `directShape.TypeId` | ElementId |
| `Void AddExternallyTaggedGeometry(ExternallyTaggedGeometryObject)` | `directShape.AddExternallyTaggedGeometry(externallyTaggedGeometry)` | Void |
| `Void AddReferenceCurve(Curve, DirectShapeReferenceOptions)` | `directShape.AddReferenceCurve(refCurve, options)` | Void |
| `Void AddReferenceCurve(Curve)` | `directShape.AddReferenceCurve(refCurve)` | Void |
| `Void AddReferencePlane(Plane, BoundingBoxUV, DirectShapeReferenceOptions)` | `directShape.AddReferencePlane(refPlane, boundingBoxUV, options)` | Void |
| `Void AddReferencePlane(Plane, DirectShapeReferenceOptions)` | `directShape.AddReferencePlane(refPlane, options)` | Void |
| `Void AddReferencePlane(Plane, BoundingBoxUV)` | `directShape.AddReferencePlane(refPlane, boundingBoxUV)` | Void |
| `Void AddReferencePlane(Plane)` | `directShape.AddReferencePlane(refPlane)` | Void |
| `Void AddReferencePoint(XYZ, DirectShapeReferenceOptions)` | `directShape.AddReferencePoint(refPoint, options)` | Void |
| `Void AddReferencePoint(XYZ)` | `directShape.AddReferencePoint(refPoint)` | Void |
| `Void AppendShape(ShapeBuilder)` | `directShape.AppendShape(ShapeBuilder)` | Void |
| `Void AppendShape(IList<GeometryObject>, DirectShapeTargetViewType)` | `directShape.AppendShape(pGeomArr, viewType)` | Void |
| `Void AppendShape(IList<GeometryObject>)` | `directShape.AppendShape(pGeomArr)` | Void |
| `Boolean AreOptionsValid(DirectShapeOptions)` | `directShape.AreOptionsValid(options)` | Boolean |
| `Boolean AreOptionsValidForTransientDirectShape(DirectShapeOptions)` | `directShape.AreOptionsValidForTransientDirectShape(options)` | Boolean |
| `Boolean AreValidDirectShapeReferenceOptions(DirectShapeReferenceOptions)` | `directShape.AreValidDirectShapeReferenceOptions(options)` | Boolean |
| `Boolean CanCreateParts()` | `directShape.CanCreateParts()` | Boolean |
| `DirectShape CreateElement(Document, ElementId)` | `DirectShape.CreateElement(document, categoryId)` | DirectShape |
| `DirectShape CreateElementInstance(Document, ElementId, ElementId, String, Transform)` | `DirectShape.CreateElementInstance(document, typeId, categoryId, definitionId, trf)` | DirectShape |
| `IList<GeometryObject> CreateGeometryInstance(Document, String, Transform)` | `DirectShape.CreateGeometryInstance(document, definition_id, trf)` | IList<GeometryObject> |
| `ExternallyTaggedGeometryObject GetExternallyTaggedGeometry(ExternalGeometryId)` | `directShape.GetExternallyTaggedGeometry(externalId)` | ExternallyTaggedGeometryObject |
| `Reference GetExternallyTaggedReference(ExternalGeometryId)` | `directShape.GetExternallyTaggedReference(externalId)` | Reference |
| `DirectShapeOptions GetOptions()` | `directShape.GetOptions()` | DirectShapeOptions |
| `Boolean HasExternalGeometry(ExternalGeometryId)` | `directShape.HasExternalGeometry(externalId)` | Boolean |
| `Boolean HasExternallyTaggedReference(ExternalGeometryId)` | `directShape.HasExternallyTaggedReference(externalId)` | Boolean |
| `Boolean IsSupportedDocument(Document)` | `DirectShape.IsSupportedDocument(document)` | Boolean |
| `Boolean IsValidCategoryId(ElementId, Document)` | `DirectShape.IsValidCategoryId(categoryId, doc)` | Boolean |
| `Boolean IsValidGeometry(Solid)` | `directShape.IsValidGeometry(Geom)` | Boolean |
| `Boolean IsValidReferenceCurve(Curve)` | `DirectShape.IsValidReferenceCurve(curve)` | Boolean |
| `Boolean IsValidReferencePlaneBoundingBoxUV(BoundingBoxUV)` | `DirectShape.IsValidReferencePlaneBoundingBoxUV(boundingBoxUV)` | Boolean |
| `Boolean IsValidShape(IList<GeometryObject>, DirectShapeTargetViewType)` | `directShape.IsValidShape(shape, viewType)` | Boolean |
| `Boolean IsValidShape(IList<GeometryObject>)` | `directShape.IsValidShape(shape)` | Boolean |
| `Boolean IsValidShape(ExternallyTaggedGeometryObject)` | `directShape.IsValidShape(externallyTaggedGeometry)` | Boolean |
| `Boolean IsValidTypeId(ElementId)` | `directShape.IsValidTypeId(typeId)` | Boolean |
| `Boolean IsValidUsage(ExternallyTaggedGeometryObject)` | `directShape.IsValidUsage(externallyTaggedGeometry)` | Boolean |
| `Void RemoveAllReferenceObjects()` | `directShape.RemoveAllReferenceObjects()` | Void |
| `Void RemoveExternallyTaggedGeometry(ExternalGeometryId)` | `directShape.RemoveExternallyTaggedGeometry(externalId)` | Void |
| `Void RemoveReferenceObject(ExternalGeometryId)` | `directShape.RemoveReferenceObject(externalId)` | Void |
| `Void RemoveReferenceObject(String)` | `directShape.RemoveReferenceObject(refName)` | Void |
| `Void ResetExternallyTaggedGeometry()` | `directShape.ResetExternallyTaggedGeometry()` | Void |
| `Void SetName(String)` | `directShape.SetName(name)` | Void |
| `Void SetOptions(DirectShapeOptions)` | `directShape.SetOptions(options)` | Void |
| `Void SetShape(ShapeBuilder)` | `directShape.SetShape(pBuilder)` | Void |
| `Void SetShape(IList<GeometryObject>, DirectShapeTargetViewType)` | `directShape.SetShape(pGeomArr, viewType)` | Void |
| `Void SetShape(IList<GeometryObject>)` | `directShape.SetShape(pGeomArr)` | Void |
| `Void SetTypeId(ElementId)` | `directShape.SetTypeId(typeId)` | Void |
| `Void UpdateExternallyTaggedGeometry(ExternallyTaggedGeometryObject)` | `directShape.UpdateExternallyTaggedGeometry(externallyTaggedGeometry)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
