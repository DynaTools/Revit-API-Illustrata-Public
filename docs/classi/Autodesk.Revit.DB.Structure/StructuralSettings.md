---
title: StructuralSettings
classe: Autodesk.Revit.DB.Structure.StructuralSettings
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 18
---

# StructuralSettings

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double BoundaryConditionAreaAndLineSymbolSpacing { get; set; }` | `structuralSettings.BoundaryConditionAreaAndLineSymbolSpacing` | Double |
| `ElementId BoundaryConditionFamilySymbolFixed { get; set; }` | `structuralSettings.BoundaryConditionFamilySymbolFixed` | ElementId |
| `ElementId BoundaryConditionFamilySymbolPinned { get; set; }` | `structuralSettings.BoundaryConditionFamilySymbolPinned` | ElementId |
| `ElementId BoundaryConditionFamilySymbolRoller { get; set; }` | `structuralSettings.BoundaryConditionFamilySymbolRoller` | ElementId |
| `ElementId BoundaryConditionFamilySymbolUserDefined { get; set; }` | `structuralSettings.BoundaryConditionFamilySymbolUserDefined` | ElementId |
| `ElementId BraceAboveSymbol { get; set; }` | `structuralSettings.BraceAboveSymbol` | ElementId |
| `ElementId BraceBelowSymbol { get; set; }` | `structuralSettings.BraceBelowSymbol` | ElementId |
| `Double BraceParallelLineOffset { get; set; }` | `structuralSettings.BraceParallelLineOffset` | Double |
| `ElementId KickerBraceSymbol { get; set; }` | `structuralSettings.KickerBraceSymbol` | ElementId |
| `Boolean ShowBraceAbove { get; set; }` | `structuralSettings.ShowBraceAbove` | Boolean |
| `Boolean ShowBraceBelow { get; set; }` | `structuralSettings.ShowBraceBelow` | Boolean |
| `Double SymbolicCutbackForBeamAndTruss { get; set; }` | `structuralSettings.SymbolicCutbackForBeamAndTruss` | Double |
| `Double SymbolicCutbackForBrace { get; set; }` | `structuralSettings.SymbolicCutbackForBrace` | Double |
| `Double SymbolicCutbackForColumn { get; set; }` | `structuralSettings.SymbolicCutbackForColumn` | Double |
| `Boolean UseLoadsDisplayScaling { get; set; }` | `structuralSettings.UseLoadsDisplayScaling` | Boolean |
| `XYZ GetLoadForceVectorReprLine(LoadType, XYZ)` | `structuralSettings.GetLoadForceVectorReprLine(loadType, forceVector)` | XYZ |
| `StructuralSettings GetStructuralSettings(Document)` | `StructuralSettings.GetStructuralSettings(doc)` | StructuralSettings |
| `Void SetValuesForLoadsDisplayScaling(Double, Double, Double, Double)` | `structuralSettings.SetValuesForLoadsDisplayScaling(minimumLoadValue, minimumForceLineLength, maximumLoadValue, maximumForceLineLength)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
