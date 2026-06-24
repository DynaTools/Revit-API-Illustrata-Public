---
title: ViewSection
classe: Autodesk.Revit.DB.ViewSection
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.View
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# ViewSection

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `View CreateCallout(Document, ElementId, ElementId, XYZ, XYZ)` | `ViewSection.CreateCallout(document, parentViewId, viewFamilyTypeId, point1, point2)` | View |
| `ViewSection CreateDetail(Document, ElementId, BoundingBoxXYZ)` | `ViewSection.CreateDetail(document, viewFamilyTypeId, sectionBox)` | ViewSection |
| `Void CreateReferenceCallout(Document, ElementId, ElementId, XYZ, XYZ)` | `ViewSection.CreateReferenceCallout(document, parentViewId, viewIdToReference, point1, point2)` | Void |
| `Void CreateReferenceSection(Document, ElementId, ElementId, XYZ, XYZ)` | `ViewSection.CreateReferenceSection(document, parentViewId, viewIdToReference, headPoint, tailPoint)` | Void |
| `ViewSection CreateSection(Document, ElementId, BoundingBoxXYZ)` | `ViewSection.CreateSection(document, viewFamilyTypeId, sectionBox)` | ViewSection |
| `Boolean IsParentViewValidForCallout(Document, ElementId)` | `ViewSection.IsParentViewValidForCallout(document, parentViewId)` | Boolean |
| `Boolean IsSplitSection()` | `viewSection.IsSplitSection()` | Boolean |
| `Boolean IsViewFamilyTypeValidForCallout(Document, ElementId, ElementId)` | `ViewSection.IsViewFamilyTypeValidForCallout(document, viewFamilyTypeId, parentViewId)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
