---
title: SolidSolidCutUtils
classe: Autodesk.Revit.DB.SolidSolidCutUtils
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# SolidSolidCutUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Void AddCutBetweenSolids(Document, Element, Element, Boolean)` | `SolidSolidCutUtils.AddCutBetweenSolids(document, solidToBeCut, cuttingSolid, splitFacesOfCuttingSolid)` | Void |
| `Void AddCutBetweenSolids(Document, Element, Element)` | `SolidSolidCutUtils.AddCutBetweenSolids(document, solidToBeCut, cuttingSolid)` | Void |
| `Boolean CanElementCutElement(Element, Element, CutFailureReason&)` | `SolidSolidCutUtils.CanElementCutElement(cuttingElement, cutElement, reason)` | Boolean |
| `Boolean CutExistsBetweenElements(Element, Element, Boolean&)` | `SolidSolidCutUtils.CutExistsBetweenElements(first, second, firstCutsSecond)` | Boolean |
| `ICollection<ElementId> GetCuttingSolids(Element)` | `SolidSolidCutUtils.GetCuttingSolids(element)` | ICollection<ElementId> |
| `ICollection<ElementId> GetSolidsBeingCut(Element)` | `SolidSolidCutUtils.GetSolidsBeingCut(element)` | ICollection<ElementId> |
| `Boolean IsAllowedForSolidCut(Element)` | `SolidSolidCutUtils.IsAllowedForSolidCut(element)` | Boolean |
| `Boolean IsElementFromAppropriateContext(Element)` | `SolidSolidCutUtils.IsElementFromAppropriateContext(element)` | Boolean |
| `Void RemoveCutBetweenSolids(Document, Element, Element)` | `SolidSolidCutUtils.RemoveCutBetweenSolids(document, first, second)` | Void |
| `Void SplitFacesOfCuttingSolid(Element, Element, Boolean)` | `SolidSolidCutUtils.SplitFacesOfCuttingSolid(first, second, split)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
