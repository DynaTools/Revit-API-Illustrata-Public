---
title: RebarShapeDefinitionBySegments
classe: Autodesk.Revit.DB.Structure.RebarShapeDefinitionBySegments
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Structure.RebarShapeDefinition
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 17
---

# RebarShapeDefinitionBySegments

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 MajorSegmentIndex { get; set; }` | `rebarShapeDefinitionBySegments.MajorSegmentIndex` | Int32 |
| `Int32 NumberOfSegments { get; }` | `rebarShapeDefinitionBySegments.NumberOfSegments` | Int32 |
| `Int32 NumberOfVertices { get; }` | `rebarShapeDefinitionBySegments.NumberOfVertices` | Int32 |
| `Void AddBendDefaultRadius(Int32, RebarShapeVertexTurn, RebarShapeBendAngle)` | `rebarShapeDefinitionBySegments.AddBendDefaultRadius(vertexIndex, turn, angle)` | Void |
| `Void AddBendVariableRadius(Int32, RebarShapeVertexTurn, RebarShapeBendAngle, ElementId, Boolean)` | `rebarShapeDefinitionBySegments.AddBendVariableRadius(vertexIndex, turn, angle, paramId, measureIncludingBarThickness)` | Void |
| `Void AddConstraintParallelToSegment(Int32, ElementId, Boolean, Boolean)` | `rebarShapeDefinitionBySegments.AddConstraintParallelToSegment(iSegment, paramId, measureToOutsideOfBend0, measureToOutsideOfBend1)` | Void |
| `Void AddConstraintToSegment(Int32, ElementId, Double, Double, Int32, Boolean, Boolean)` | `rebarShapeDefinitionBySegments.AddConstraintToSegment(iSegment, paramId, constraintDirCoordX, constraintDirCoordY, signOfZCoordOfCrossProductOfConstraintDirBySegmentDir, measureToOutsideOfBend0, measureToOutsideOfBend1)` | Void |
| `Void AddListeningDimensionBendToBend(ElementId, Double, Double, Int32, Int32, Int32, Int32)` | `rebarShapeDefinitionBySegments.AddListeningDimensionBendToBend(paramId, constraintDirCoordX, constraintDirCoordY, iSegment0, iEnd0, iSegment1, iEnd1)` | Void |
| `Void AddListeningDimensionSegmentToBend(ElementId, Double, Double, Int32, Int32, Int32)` | `rebarShapeDefinitionBySegments.AddListeningDimensionSegmentToBend(paramId, constraintDirCoordX, constraintDirCoordY, iSegment0, iSegment1, iEnd1)` | Void |
| `Void AddListeningDimensionSegmentToSegment(ElementId, Double, Double, Int32, Int32)` | `rebarShapeDefinitionBySegments.AddListeningDimensionSegmentToSegment(paramId, constraintDirCoordX, constraintDirCoordY, iSegment0, iSegment1)` | Void |
| `RebarShapeSegment GetSegment(Int32)` | `rebarShapeDefinitionBySegments.GetSegment(segmentIndex)` | RebarShapeSegment |
| `RebarShapeVertex GetVertex(Int32)` | `rebarShapeDefinitionBySegments.GetVertex(vertexIndex)` | RebarShapeVertex |
| `Void RemoveParameterFromSegment(Int32, ElementId)` | `rebarShapeDefinitionBySegments.RemoveParameterFromSegment(iSegment, paramId)` | Void |
| `Void SetSegmentAs180DegreeBend(Int32, ElementId, Boolean)` | `rebarShapeDefinitionBySegments.SetSegmentAs180DegreeBend(iSegment, paramId, measureToOutsideOfBend)` | Void |
| `Void SetSegmentAs180DegreeBend(Int32)` | `rebarShapeDefinitionBySegments.SetSegmentAs180DegreeBend(iSegment)` | Void |
| `Void SetSegmentFixedDirection(Int32, Double, Double)` | `rebarShapeDefinitionBySegments.SetSegmentFixedDirection(iSegment, vecCoordX, vecCoordY)` | Void |
| `Void SetSegmentVariableDirection(Int32)` | `rebarShapeDefinitionBySegments.SetSegmentVariableDirection(iSegment)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
