---
title: DividedPath
classe: Autodesk.Revit.DB.DividedPath
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 33
---

# DividedPath

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double BeginningIndent { get; set; }` | `dividedPath.BeginningIndent` | Double |
| `Boolean DisplayNodeNumbers { get; set; }` | `dividedPath.DisplayNodeNumbers` | Boolean |
| `Boolean DisplayNodes { get; set; }` | `dividedPath.DisplayNodes` | Boolean |
| `Boolean DisplayReferenceCurves { get; set; }` | `dividedPath.DisplayReferenceCurves` | Boolean |
| `Double Distance { get; set; }` | `dividedPath.Distance` | Double |
| `Double EndIndent { get; set; }` | `dividedPath.EndIndent` | Double |
| `Int32 FixedNumberOfPoints { get; set; }` | `dividedPath.FixedNumberOfPoints` | Int32 |
| `Boolean Flipped { get; }` | `dividedPath.Flipped` | Boolean |
| `Boolean IsClosedLoop { get; }` | `dividedPath.IsClosedLoop` | Boolean |
| `Boolean IsCyclical { get; }` | `dividedPath.IsCyclical` | Boolean |
| `Double MaximumDistance { get; set; }` | `dividedPath.MaximumDistance` | Double |
| `DividedPathMeasurementType MeasurementType { get; set; }` | `dividedPath.MeasurementType` | DividedPathMeasurementType |
| `Double MinimumDistance { get; set; }` | `dividedPath.MinimumDistance` | Double |
| `Int32 NumberOfPoints { get; }` | `dividedPath.NumberOfPoints` | Int32 |
| `SpacingRuleJustification SpacingRuleJustification { get; set; }` | `dividedPath.SpacingRuleJustification` | SpacingRuleJustification |
| `SpacingRuleLayout SpacingRuleLayout { get; set; }` | `dividedPath.SpacingRuleLayout` | SpacingRuleLayout |
| `Double TotalPathLength { get; }` | `dividedPath.TotalPathLength` | Double |
| `Boolean AreCurveReferencesConnected(Document, IList<Reference>)` | `DividedPath.AreCurveReferencesConnected(document, curveReferences)` | Boolean |
| `DividedPath Create(Document, IList<Reference>, ICollection<ElementId>)` | `DividedPath.Create(document, curveReferences, intersectors)` | DividedPath |
| `DividedPath Create(Document, IList<Reference>)` | `DividedPath.Create(document, curveReferences)` | DividedPath |
| `Void Flip()` | `dividedPath.Flip()` | Void |
| `ICollection<ElementId> GetIntersectingElements()` | `dividedPath.GetIntersectingElements()` | ICollection<ElementId> |
| `Boolean IsCurveReferenceValid(Document, Reference)` | `DividedPath.IsCurveReferenceValid(document, curveReference)` | Boolean |
| `Boolean IsIntersectorValidForCreation(Document, ElementId)` | `DividedPath.IsIntersectorValidForCreation(document, intersector)` | Boolean |
| `Boolean IsIntersectorValidForDividedPath(ElementId)` | `dividedPath.IsIntersectorValidForDividedPath(intersector)` | Boolean |
| `Boolean IsValidBeginningIndent(Double)` | `dividedPath.IsValidBeginningIndent(beginningIndent)` | Boolean |
| `Boolean IsValidEndIndent(Double)` | `dividedPath.IsValidEndIndent(endIndent)` | Boolean |
| `Boolean IsValidFixedNumberOfPoints(Int32)` | `DividedPath.IsValidFixedNumberOfPoints(fixedNumberOfPoints)` | Boolean |
| `Boolean IsValidMeasurementType(DividedPathMeasurementType)` | `dividedPath.IsValidMeasurementType(measurementType)` | Boolean |
| `Boolean IsValidSpacingRuleJustification(SpacingRuleJustification)` | `dividedPath.IsValidSpacingRuleJustification(justification)` | Boolean |
| `Boolean IsValidSpacingRuleLayout(SpacingRuleLayout)` | `dividedPath.IsValidSpacingRuleLayout(layout)` | Boolean |
| `IList<IList<Reference>> SeparateReferencesIntoConnectedReferences(Document, IList<Reference>)` | `DividedPath.SeparateReferencesIntoConnectedReferences(document, curveReferences)` | IList<IList<Reference>> |
| `Void SetIntersectingElements(ICollection<ElementId>)` | `dividedPath.SetIntersectingElements(intersectors)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
