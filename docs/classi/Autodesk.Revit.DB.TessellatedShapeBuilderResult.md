---
title: TessellatedShapeBuilderResult
classe: Autodesk.Revit.DB.TessellatedShapeBuilderResult
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# TessellatedShapeBuilderResult

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean AreObjectsAvailable { get; }` | `tessellatedShapeBuilderResult.AreObjectsAvailable` | Boolean |
| `Boolean HasInvalidData { get; }` | `tessellatedShapeBuilderResult.HasInvalidData` | Boolean |
| `Boolean IsValidObject { get; }` | `tessellatedShapeBuilderResult.IsValidObject` | Boolean |
| `TessellatedShapeBuilderOutcome Outcome { get; }` | `tessellatedShapeBuilderResult.Outcome` | TessellatedShapeBuilderOutcome |
| `Void Dispose()` | `tessellatedShapeBuilderResult.Dispose()` | Void |
| `IList<GeometryObject> GetGeometricalObjects()` | `tessellatedShapeBuilderResult.GetGeometricalObjects()` | IList<GeometryObject> |
| `IList<TessellatedBuildIssue> GetIssuesForFaceSet(Int32)` | `tessellatedShapeBuilderResult.GetIssuesForFaceSet(setIndex)` | IList<TessellatedBuildIssue> |
| `Int32 GetNumberOfFaceSets()` | `tessellatedShapeBuilderResult.GetNumberOfFaceSets()` | Int32 |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
