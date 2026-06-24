---
title: Part
classe: Autodesk.Revit.DB.Part
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# Part

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean Excluded { get; set; }` | `part.Excluded` | Boolean |
| `ElementId OriginalCategoryId { get; set; }` | `part.OriginalCategoryId` | ElementId |
| `PartMaker PartMaker { get; }` | `part.PartMaker` | PartMaker |
| `Boolean CanOffsetFace(Face)` | `part.CanOffsetFace(face)` | Boolean |
| `Double GetFaceOffset(Face)` | `part.GetFaceOffset(face)` | Double |
| `ICollection<LinkElementId> GetSourceElementIds()` | `part.GetSourceElementIds()` | ICollection<LinkElementId> |
| `ICollection<ElementId> GetSourceElementOriginalCategoryIds()` | `part.GetSourceElementOriginalCategoryIds()` | ICollection<ElementId> |
| `Void ResetFaceOffset(Face)` | `part.ResetFaceOffset(face)` | Void |
| `Void ResetPartShape()` | `part.ResetPartShape()` | Void |
| `Void SetFaceOffset(Face, Double)` | `part.SetFaceOffset(face, offset)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
