---
title: Subelement
classe: Autodesk.Revit.DB.Subelement
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 21
---

# Subelement

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Category Category { get; }` | `subelement.Category` | Category |
| `Document Document { get; }` | `subelement.Document` | Document |
| `Element Element { get; }` | `subelement.Element` | Element |
| `Boolean IsValidObject { get; }` | `subelement.IsValidObject` | Boolean |
| `ElementId TypeId { get; }` | `subelement.TypeId` | ElementId |
| `String UniqueId { get; }` | `subelement.UniqueId` | String |
| `Boolean CanHaveTypeAssigned()` | `subelement.CanHaveTypeAssigned()` | Boolean |
| `Void ChangeTypeId(ElementId)` | `subelement.ChangeTypeId(typeId)` | Void |
| `Subelement Create(Document, Reference)` | `Subelement.Create(aDoc, reference)` | Subelement |
| `Void Dispose()` | `subelement.Dispose()` | Void |
| `IList<ElementId> GetAllParameters()` | `subelement.GetAllParameters()` | IList<ElementId> |
| `BoundingBoxXYZ GetBoundingBox(View)` | `subelement.GetBoundingBox(dbView)` | BoundingBoxXYZ |
| `GeometryObject GetGeometryObject(View)` | `subelement.GetGeometryObject(dbView)` | GeometryObject |
| `ParameterValue GetParameterValue(ElementId)` | `subelement.GetParameterValue(parameterId)` | ParameterValue |
| `Reference GetReference()` | `subelement.GetReference()` | Reference |
| `ISet<ElementId> GetValidTypes()` | `subelement.GetValidTypes()` | ISet<ElementId> |
| `Boolean HasParameter(ElementId)` | `subelement.HasParameter(parameterId)` | Boolean |
| `Boolean IsParameterModifiable(ElementId)` | `subelement.IsParameterModifiable(parameterId)` | Boolean |
| `Boolean IsValidSubelementReference(Document, Reference)` | `Subelement.IsValidSubelementReference(aDoc, reference)` | Boolean |
| `Boolean IsValidType(ElementId)` | `subelement.IsValidType(typeId)` | Boolean |
| `Void SetParameterValue(ElementId, ParameterValue)` | `subelement.SetParameterValue(parameterId, pValue)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
