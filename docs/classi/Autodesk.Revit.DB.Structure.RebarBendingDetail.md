---
title: RebarBendingDetail
classe: Autodesk.Revit.DB.Structure.RebarBendingDetail
namespace: Autodesk.Revit.DB.Structure
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 19
---

# RebarBendingDetail

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Void AddHosts(Element, IList<Reference>)` | `RebarBendingDetail.AddHosts(bendingDetail, references)` | Void |
| `Element Create(Document, ElementId, ElementId, Int32, RebarBendingDetailType, XYZ, Double)` | `RebarBendingDetail.Create(document, viewId, reinforcementElementId, reinforcementElementSubelementKey, bendingDetailType, position, rotation)` | Element |
| `Reference GetHost(Element)` | `RebarBendingDetail.GetHost(bendingDetail)` | Reference |
| `IList<Reference> GetHosts(Element)` | `RebarBendingDetail.GetHosts(bendingDetail)` | IList<Reference> |
| `XYZ GetPosition(Element)` | `RebarBendingDetail.GetPosition(bendingDetail)` | XYZ |
| `Double GetRotation(Element)` | `RebarBendingDetail.GetRotation(bendingDetail)` | Double |
| `XYZ GetTagRelativePosition(Element)` | `RebarBendingDetail.GetTagRelativePosition(bendingDetail)` | XYZ |
| `Double GetTagRelativeRotation(Element)` | `RebarBendingDetail.GetTagRelativeRotation(bendingDetail)` | Double |
| `Boolean IsBendingDetail(Element)` | `RebarBendingDetail.IsBendingDetail(bendingDetail)` | Boolean |
| `Boolean IsRealisticBendingDetail(Element)` | `RebarBendingDetail.IsRealisticBendingDetail(bendingDetail)` | Boolean |
| `Boolean IsSchematicBendingDetail(Element)` | `RebarBendingDetail.IsSchematicBendingDetail(bendingDetail)` | Boolean |
| `Void RemoveHosts(Element, IList<Reference>)` | `RebarBendingDetail.RemoveHosts(bendingDetail, references)` | Void |
| `Void ResetAnnotationPositions(Element)` | `RebarBendingDetail.ResetAnnotationPositions(bendingDetail)` | Void |
| `Void ResetTagRelativePosition(Element)` | `RebarBendingDetail.ResetTagRelativePosition(bendingDetail)` | Void |
| `Void SetHost(Element, Reference)` | `RebarBendingDetail.SetHost(bendingDetail, reference)` | Void |
| `Void SetPosition(Element, XYZ)` | `RebarBendingDetail.SetPosition(bendingDetail, position)` | Void |
| `Void SetRotation(Element, Double)` | `RebarBendingDetail.SetRotation(bendingDetail, rotation)` | Void |
| `Void SetTagRelativePosition(Element, XYZ)` | `RebarBendingDetail.SetTagRelativePosition(bendingDetail, relativeOffset)` | Void |
| `Void SetTagRelativeRotation(Element, Double)` | `RebarBendingDetail.SetTagRelativeRotation(bendingDetail, rotation)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
