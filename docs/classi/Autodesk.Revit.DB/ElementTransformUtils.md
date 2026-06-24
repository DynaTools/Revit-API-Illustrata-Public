---
title: ElementTransformUtils
classe: Autodesk.Revit.DB.ElementTransformUtils
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# ElementTransformUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean CanMirrorElement(Document, ElementId)` | `ElementTransformUtils.CanMirrorElement(ADoc, elemId)` | Boolean |
| `Boolean CanMirrorElements(Document, ICollection<ElementId>)` | `ElementTransformUtils.CanMirrorElements(ADoc, elemIds)` | Boolean |
| `ICollection<ElementId> CopyElement(Document, ElementId, XYZ)` | `ElementTransformUtils.CopyElement(document, elementToCopy, translation)` | ICollection<ElementId> |
| `ICollection<ElementId> CopyElements(View, ICollection<ElementId>, View, Transform, CopyPasteOptions)` | `ElementTransformUtils.CopyElements(sourceView, elementsToCopy, destinationView, additionalTransform, options)` | ICollection<ElementId> |
| `ICollection<ElementId> CopyElements(Document, ICollection<ElementId>, Document, Transform, CopyPasteOptions)` | `ElementTransformUtils.CopyElements(sourceDocument, elementsToCopy, destinationDocument, transform, options)` | ICollection<ElementId> |
| `ICollection<ElementId> CopyElements(Document, ICollection<ElementId>, XYZ)` | `ElementTransformUtils.CopyElements(document, elementsToCopy, translation)` | ICollection<ElementId> |
| `Transform GetTransformFromViewToView(View, View)` | `ElementTransformUtils.GetTransformFromViewToView(sourceView, destinationView)` | Transform |
| `Void MirrorElement(Document, ElementId, Plane)` | `ElementTransformUtils.MirrorElement(document, elementToMirror, plane)` | Void |
| `IList<ElementId> MirrorElements(Document, ICollection<ElementId>, Plane, Boolean)` | `ElementTransformUtils.MirrorElements(document, elementsToMirror, plane, mirrorCopies)` | IList<ElementId> |
| `Void MoveElement(Document, ElementId, XYZ)` | `ElementTransformUtils.MoveElement(document, elementToMove, translation)` | Void |
| `Void MoveElements(Document, ICollection<ElementId>, XYZ)` | `ElementTransformUtils.MoveElements(document, elementsToMove, translation)` | Void |
| `Void RotateElement(Document, ElementId, Line, Double)` | `ElementTransformUtils.RotateElement(document, elementToRotate, axis, angle)` | Void |
| `Void RotateElements(Document, ICollection<ElementId>, Line, Double)` | `ElementTransformUtils.RotateElements(document, elementsToRotate, axis, angle)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
