---
title: RebarHostData
classe: Autodesk.Revit.DB.Structure.RebarHostData
namespace: Autodesk.Revit.DB.Structure
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 19
---

# RebarHostData

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `rebarHostData.IsValidObject` | Boolean |
| `Void Dispose()` | `rebarHostData.Dispose()` | Void |
| `IList<AreaReinforcement> GetAreaReinforcementsInHost()` | `rebarHostData.GetAreaReinforcementsInHost()` | IList<AreaReinforcement> |
| `RebarCoverType GetCommonCoverType()` | `rebarHostData.GetCommonCoverType()` | RebarCoverType |
| `RebarCoverType GetCoverType(Reference)` | `rebarHostData.GetCoverType(face)` | RebarCoverType |
| `IList<Reference> GetExposedFaces()` | `rebarHostData.GetExposedFaces()` | IList<Reference> |
| `IList<FabricArea> GetFabricAreasInHost()` | `rebarHostData.GetFabricAreasInHost()` | IList<FabricArea> |
| `IList<FabricSheet> GetFabricSheetsInHost()` | `rebarHostData.GetFabricSheetsInHost()` | IList<FabricSheet> |
| `IList<PathReinforcement> GetPathReinforcementsInHost()` | `rebarHostData.GetPathReinforcementsInHost()` | IList<PathReinforcement> |
| `IList<RebarContainer> GetRebarContainersInHost()` | `rebarHostData.GetRebarContainersInHost()` | IList<RebarContainer> |
| `RebarHostData GetRebarHostData(Element)` | `RebarHostData.GetRebarHostData(host)` | RebarHostData |
| `ISet<ElementId> GetRebarHostDirectNeighbors(Element)` | `RebarHostData.GetRebarHostDirectNeighbors(hostElement)` | ISet<ElementId> |
| `IList<Rebar> GetRebarsInHost()` | `rebarHostData.GetRebarsInHost()` | IList<Rebar> |
| `Boolean IsFaceExposed(Reference)` | `rebarHostData.IsFaceExposed(face)` | Boolean |
| `Boolean IsReferenceContainedByAValidHost(Document, Reference)` | `RebarHostData.IsReferenceContainedByAValidHost(doc, reference)` | Boolean |
| `Boolean IsValidHost(Element)` | `RebarHostData.IsValidHost(element)` | Boolean |
| `Boolean IsValidHost()` | `rebarHostData.IsValidHost()` | Boolean |
| `Void SetCommonCoverType(RebarCoverType)` | `rebarHostData.SetCommonCoverType(coverType)` | Void |
| `Void SetCoverType(Reference, RebarCoverType)` | `rebarHostData.SetCoverType(face, coverType)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
