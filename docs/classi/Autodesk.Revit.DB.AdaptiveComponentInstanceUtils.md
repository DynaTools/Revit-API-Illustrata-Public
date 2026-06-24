---
title: AdaptiveComponentInstanceUtils
classe: Autodesk.Revit.DB.AdaptiveComponentInstanceUtils
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# AdaptiveComponentInstanceUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `FamilyInstance CreateAdaptiveComponentInstance(Document, FamilySymbol)` | `AdaptiveComponentInstanceUtils.CreateAdaptiveComponentInstance(doc, famSymb)` | FamilyInstance |
| `IList<ElementId> GetInstancePlacementPointElementRefIds(FamilyInstance)` | `AdaptiveComponentInstanceUtils.GetInstancePlacementPointElementRefIds(famInst)` | IList<ElementId> |
| `IList<ElementId> GetInstancePointElementRefIds(FamilyInstance)` | `AdaptiveComponentInstanceUtils.GetInstancePointElementRefIds(famInst)` | IList<ElementId> |
| `IList<ElementId> GetInstanceShapeHandlePointElementRefIds(FamilyInstance)` | `AdaptiveComponentInstanceUtils.GetInstanceShapeHandlePointElementRefIds(famInst)` | IList<ElementId> |
| `Boolean HasAdaptiveFamilySymbol(FamilyInstance)` | `AdaptiveComponentInstanceUtils.HasAdaptiveFamilySymbol(famInst)` | Boolean |
| `Boolean IsAdaptiveComponentInstance(FamilyInstance)` | `AdaptiveComponentInstanceUtils.IsAdaptiveComponentInstance(famInst)` | Boolean |
| `Boolean IsAdaptiveFamilySymbol(FamilySymbol)` | `AdaptiveComponentInstanceUtils.IsAdaptiveFamilySymbol(famSymb)` | Boolean |
| `Boolean IsInstanceFlipped(FamilyInstance)` | `AdaptiveComponentInstanceUtils.IsInstanceFlipped(famInst)` | Boolean |
| `Void MoveAdaptiveComponentInstance(FamilyInstance, Transform, Boolean)` | `AdaptiveComponentInstanceUtils.MoveAdaptiveComponentInstance(famInst, trf, unHost)` | Void |
| `Void SetInstanceFlipped(FamilyInstance, Boolean)` | `AdaptiveComponentInstanceUtils.SetInstanceFlipped(famInst, flip)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
