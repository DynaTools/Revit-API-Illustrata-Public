---
title: SlabShapeEditor
classe: Autodesk.Revit.DB.SlabShapeEditor
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 17
---

# SlabShapeEditor

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEnabled { get; }` | `slabShapeEditor.IsEnabled` | Boolean |
| `Boolean IsValidObject { get; }` | `slabShapeEditor.IsValidObject` | Boolean |
| `SlabShapeCreaseArray SlabShapeCreases { get; }` | `slabShapeEditor.SlabShapeCreases` | SlabShapeCreaseArray |
| `SlabShapeVertexArray SlabShapeVertices { get; }` | `slabShapeEditor.SlabShapeVertices` | SlabShapeVertexArray |
| `SlabShapeVertex AddPoint(XYZ)` | `slabShapeEditor.AddPoint(point)` | SlabShapeVertex |
| `IList<SlabShapeVertex> AddPoints(IList<XYZ>)` | `slabShapeEditor.AddPoints(points)` | IList<SlabShapeVertex> |
| `IList<SlabShapeCrease> AddSplitLine(SlabShapeVertex, SlabShapeVertex)` | `slabShapeEditor.AddSplitLine(startVertex, endVertex)` | IList<SlabShapeCrease> |
| `Void CreateCreasesFromFoldingLines(Element, IList<Reference>)` | `slabShapeEditor.CreateCreasesFromFoldingLines(hostObj, references)` | Void |
| `Boolean DeletePoint(SlabShapeVertex)` | `slabShapeEditor.DeletePoint(vertex)` | Boolean |
| `Void Dispose()` | `slabShapeEditor.Dispose()` | Void |
| `SlabShapeVertex DrawPoint(XYZ)` | `slabShapeEditor.DrawPoint(location)` | SlabShapeVertex |
| `SlabShapeCreaseArray DrawSplitLine(SlabShapeVertex, SlabShapeVertex)` | `slabShapeEditor.DrawSplitLine(startVertex, endVertex)` | SlabShapeCreaseArray |
| `Void Enable()` | `slabShapeEditor.Enable()` | Void |
| `Void ModifySubElement(SlabShapeCrease, Double)` | `slabShapeEditor.ModifySubElement(crease, offset)` | Void |
| `Void ModifySubElement(SlabShapeVertex, Double)` | `slabShapeEditor.ModifySubElement(vertex, offset)` | Void |
| `Void PickSupport(Line)` | `slabShapeEditor.PickSupport(gLine)` | Void |
| `Void ResetSlabShape()` | `slabShapeEditor.ResetSlabShape()` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
