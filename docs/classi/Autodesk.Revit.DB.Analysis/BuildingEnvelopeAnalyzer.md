---
title: BuildingEnvelopeAnalyzer
classe: Autodesk.Revit.DB.Analysis.BuildingEnvelopeAnalyzer
namespace: Autodesk.Revit.DB.Analysis
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 6
---

# BuildingEnvelopeAnalyzer

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `buildingEnvelopeAnalyzer.IsValidObject` | Boolean |
| `BuildingEnvelopeAnalyzer Create(Document, BuildingEnvelopeAnalyzerOptions)` | `BuildingEnvelopeAnalyzer.Create(document, options)` | BuildingEnvelopeAnalyzer |
| `Void Dispose()` | `buildingEnvelopeAnalyzer.Dispose()` | Void |
| `IList<LinkElementId> GetBoundingElements()` | `buildingEnvelopeAnalyzer.GetBoundingElements()` | IList<LinkElementId> |
| `IList<LinkElementId> GetBoundingElementsForSpaceVolume(Int32)` | `buildingEnvelopeAnalyzer.GetBoundingElementsForSpaceVolume(spaceVolume)` | IList<LinkElementId> |
| `IList<XYZ> GetCenterPointsForConnectedGridCellsInSpaceVolume(Int32)` | `buildingEnvelopeAnalyzer.GetCenterPointsForConnectedGridCellsInSpaceVolume(spaceVolume)` | IList<XYZ> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
