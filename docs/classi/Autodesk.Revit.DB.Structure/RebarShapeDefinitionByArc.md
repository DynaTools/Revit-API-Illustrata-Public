---
title: RebarShapeDefinitionByArc
classe: Autodesk.Revit.DB.Structure.RebarShapeDefinitionByArc
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Structure.RebarShapeDefinition
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# RebarShapeDefinitionByArc

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `RebarShapeDefinitionByArcType Type { get; set; }` | `rebarShapeDefinitionByArc.Type` | RebarShapeDefinitionByArcType |
| `Void AddConstraintArcLength(ElementId)` | `rebarShapeDefinitionByArc.AddConstraintArcLength(paramId)` | Void |
| `Void AddConstraintChordLength(ElementId)` | `rebarShapeDefinitionByArc.AddConstraintChordLength(paramId)` | Void |
| `Void AddConstraintCircumference(ElementId, RebarShapeArcReferenceType)` | `rebarShapeDefinitionByArc.AddConstraintCircumference(paramId, arcRefType)` | Void |
| `Void AddConstraintDiameter(ElementId, RebarShapeArcReferenceType)` | `rebarShapeDefinitionByArc.AddConstraintDiameter(paramId, arcRefType)` | Void |
| `Void AddConstraintRadius(ElementId, RebarShapeArcReferenceType)` | `rebarShapeDefinitionByArc.AddConstraintRadius(paramId, arcRefType)` | Void |
| `Void AddConstraintSagittaLength(ElementId)` | `rebarShapeDefinitionByArc.AddConstraintSagittaLength(paramId)` | Void |
| `IList<RebarShapeConstraint> GetConstraints()` | `rebarShapeDefinitionByArc.GetConstraints()` | IList<RebarShapeConstraint> |
| `Void SetArcTypeSpiral(Double, Double, Int32, Int32)` | `rebarShapeDefinitionByArc.SetArcTypeSpiral(height, pitch, baseFinishingTurns, topFinishingTurns)` | Void |
| `Void SetConstraints(IList<RebarShapeConstraint>)` | `rebarShapeDefinitionByArc.SetConstraints(constraints)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
