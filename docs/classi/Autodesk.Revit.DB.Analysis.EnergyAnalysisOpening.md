---
title: EnergyAnalysisOpening
classe: Autodesk.Revit.DB.Analysis.EnergyAnalysisOpening
namespace: Autodesk.Revit.DB.Analysis
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 17
---

# EnergyAnalysisOpening

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String CADLinkUniqueId { get; }` | `energyAnalysisOpening.CADLinkUniqueId` | String |
| `String CADObjectUniqueId { get; }` | `energyAnalysisOpening.CADObjectUniqueId` | String |
| `XYZ Corner { get; }` | `energyAnalysisOpening.Corner` | XYZ |
| `Double Height { get; }` | `energyAnalysisOpening.Height` | Double |
| `String OpeningId { get; }` | `energyAnalysisOpening.OpeningId` | String |
| `String OpeningName { get; }` | `energyAnalysisOpening.OpeningName` | String |
| `EnergyAnalysisOpeningType OpeningType { get; }` | `energyAnalysisOpening.OpeningType` | EnergyAnalysisOpeningType |
| `String OriginatingElementDescription { get; }` | `energyAnalysisOpening.OriginatingElementDescription` | String |
| `LinkElementId OriginatingElementId { get; }` | `energyAnalysisOpening.OriginatingElementId` | LinkElementId |
| `String OriginatingElementName { get; }` | `energyAnalysisOpening.OriginatingElementName` | String |
| `gbXMLOpeningType Type { get; }` | `energyAnalysisOpening.Type` | gbXMLOpeningType |
| `Double Width { get; }` | `energyAnalysisOpening.Width` | Double |
| `EnergyAnalysisSurface GetAnalyticalSurface()` | `energyAnalysisOpening.GetAnalyticalSurface()` | EnergyAnalysisSurface |
| `EnergyAnalysisConstruction GetConstruction()` | `energyAnalysisOpening.GetConstruction()` | EnergyAnalysisConstruction |
| `Polyloop GetPolyloop()` | `energyAnalysisOpening.GetPolyloop()` | Polyloop |
| `IList<Polyloop> GetPolyloops()` | `energyAnalysisOpening.GetPolyloops()` | IList<Polyloop> |
| `EnergyAnalysisWindowType GetWindowType()` | `energyAnalysisOpening.GetWindowType()` | EnergyAnalysisWindowType |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
