---
title: MassLevelData
classe: Autodesk.Revit.DB.Analysis.MassLevelData
namespace: Autodesk.Revit.DB.Analysis
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# MassLevelData

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId ConceptualConstructionId { get; set; }` | `massLevelData.ConceptualConstructionId` | ElementId |
| `Boolean ConceptualConstructionIsByEnergyData { get; set; }` | `massLevelData.ConceptualConstructionIsByEnergyData` | Boolean |
| `ElementId MaterialId { get; set; }` | `massLevelData.MaterialId` | ElementId |
| `MassSurfaceDataMaterialType MaterialType { get; set; }` | `massLevelData.MaterialType` | MassSurfaceDataMaterialType |
| `Double NExteriorSurfaceArea { get; }` | `massLevelData.NExteriorSurfaceArea` | Double |
| `Double NLevelFafArea { get; }` | `massLevelData.NLevelFafArea` | Double |
| `Double NLevelPerimeter { get; }` | `massLevelData.NLevelPerimeter` | Double |
| `Double NVolume { get; }` | `massLevelData.NVolume` | Double |
| `ElementId OwningMassId { get; }` | `massLevelData.OwningMassId` | ElementId |
| `String StrUsage { get; set; }` | `massLevelData.StrUsage` | String |
| `Boolean IsEmpty()` | `massLevelData.IsEmpty()` | Boolean |
| `Boolean IsMassFamilyInstance(Document, ElementId)` | `MassLevelData.IsMassFamilyInstance(document, id)` | Boolean |
| `Boolean IsValidConceptualConstructionTypeElement(ElementId)` | `massLevelData.IsValidConceptualConstructionTypeElement(id)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
