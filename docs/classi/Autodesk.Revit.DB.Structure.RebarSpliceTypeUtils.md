---
title: RebarSpliceTypeUtils
classe: Autodesk.Revit.DB.Structure.RebarSpliceTypeUtils
namespace: Autodesk.Revit.DB.Structure
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# RebarSpliceTypeUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementType CreateRebarSpliceType(Document, String)` | `RebarSpliceTypeUtils.CreateRebarSpliceType(document, typeName)` | ElementType |
| `IList<ElementId> GetAllRebarSpliceTypes(Document)` | `RebarSpliceTypeUtils.GetAllRebarSpliceTypes(document)` | IList<ElementId> |
| `Double GetLapLengthMultiplier(Document, ElementId)` | `RebarSpliceTypeUtils.GetLapLengthMultiplier(document, rebarSpliceTypeId)` | Double |
| `RebarSpliceShiftOption GetShiftOption(Document, ElementId)` | `RebarSpliceTypeUtils.GetShiftOption(document, rebarSpliceTypeId)` | RebarSpliceShiftOption |
| `Double GetStaggerLengthMultiplier(Document, ElementId)` | `RebarSpliceTypeUtils.GetStaggerLengthMultiplier(document, rebarSpliceTypeId)` | Double |
| `Void SetLapLengthMultiplier(Document, ElementId, Double)` | `RebarSpliceTypeUtils.SetLapLengthMultiplier(document, rebarSpliceTypeId, lapLengthMultiplier)` | Void |
| `Void SetShiftOption(Document, ElementId, RebarSpliceShiftOption)` | `RebarSpliceTypeUtils.SetShiftOption(document, rebarSpliceTypeId, shiftOption)` | Void |
| `Void SetStaggerLengthMultiplier(Document, ElementId, Double)` | `RebarSpliceTypeUtils.SetStaggerLengthMultiplier(document, rebarSpliceTypeId, staggerLengthMultiplier)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
