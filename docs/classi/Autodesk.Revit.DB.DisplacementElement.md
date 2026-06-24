---
title: DisplacementElement
classe: Autodesk.Revit.DB.DisplacementElement
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 23
---

# DisplacementElement

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId ParentId { get; }` | `displacementElement.ParentId` | ElementId |
| `Boolean CanCategoryBeDisplaced(ElementId)` | `DisplacementElement.CanCategoryBeDisplaced(categoryId)` | Boolean |
| `Boolean CanElementsBeAddedToDisplacementSet(ICollection<ElementId>)` | `displacementElement.CanElementsBeAddedToDisplacementSet(toDisplace)` | Boolean |
| `Boolean CanElementsBeDisplaced(View, ICollection<ElementId>)` | `DisplacementElement.CanElementsBeDisplaced(view, elementIds)` | Boolean |
| `Boolean CanElementsBeDisplaced(View, ICollection<ElementId>, ElementId&)` | `DisplacementElement.CanElementsBeDisplaced(view, elementIds, commonDisplacedElementId)` | Boolean |
| `DisplacementElement Create(Document, ICollection<ElementId>, XYZ, View, DisplacementElement)` | `DisplacementElement.Create(document, elementsToDisplace, displacement, ownerDBView, parentDisplacementElement)` | DisplacementElement |
| `XYZ GetAbsoluteDisplacement()` | `displacementElement.GetAbsoluteDisplacement()` | XYZ |
| `ICollection<ElementId> GetAdditionalElementsToDisplace(Document, View, ElementId)` | `DisplacementElement.GetAdditionalElementsToDisplace(document, view, idToDisplace)` | ICollection<ElementId> |
| `IList<DisplacementElement> GetChildren()` | `displacementElement.GetChildren()` | IList<DisplacementElement> |
| `ICollection<ElementId> GetDisplacedElementIds()` | `displacementElement.GetDisplacedElementIds()` | ICollection<ElementId> |
| `ICollection<ElementId> GetDisplacedElementIds(View)` | `DisplacementElement.GetDisplacedElementIds(view)` | ICollection<ElementId> |
| `ICollection<ElementId> GetDisplacedElementIdsFromAllChildren()` | `displacementElement.GetDisplacedElementIdsFromAllChildren()` | ICollection<ElementId> |
| `ElementId GetDisplacementElementId(View, ElementId)` | `DisplacementElement.GetDisplacementElementId(view, id)` | ElementId |
| `ICollection<ElementId> GetDisplacementElementIds(View)` | `DisplacementElement.GetDisplacementElementIds(view)` | ICollection<ElementId> |
| `XYZ GetRelativeDisplacement()` | `displacementElement.GetRelativeDisplacement()` | XYZ |
| `Boolean IsAllowedAsDisplacedElement(Element)` | `DisplacementElement.IsAllowedAsDisplacedElement(element)` | Boolean |
| `Boolean IsElementDisplacedInView(View, ElementId)` | `DisplacementElement.IsElementDisplacedInView(view, id)` | Boolean |
| `Boolean IsNotEmpty(ICollection<ElementId>)` | `DisplacementElement.IsNotEmpty(elementIds)` | Boolean |
| `Boolean IsValidAsParentInView(View, DisplacementElement)` | `DisplacementElement.IsValidAsParentInView(view, parent)` | Boolean |
| `Void RemoveDisplacedElement(Element)` | `displacementElement.RemoveDisplacedElement(ElemToRemove)` | Void |
| `Void ResetDisplacedElements()` | `displacementElement.ResetDisplacedElements()` | Void |
| `Void SetDisplacedElementIds(ICollection<ElementId>)` | `displacementElement.SetDisplacedElementIds(displacedElemIds)` | Void |
| `Void SetRelativeDisplacement(XYZ)` | `displacementElement.SetRelativeDisplacement(displacement)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
