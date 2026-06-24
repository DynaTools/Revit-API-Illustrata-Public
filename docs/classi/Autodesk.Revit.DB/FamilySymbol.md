---
title: FamilySymbol
classe: Autodesk.Revit.DB.FamilySymbol
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.InsertableObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# FamilySymbol

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Family Family { get; }` | `familySymbol.Family` | Family |
| `Boolean IsActive { get; }` | `familySymbol.IsActive` | Boolean |
| `StructuralMaterialType StructuralMaterialType { get; }` | `familySymbol.StructuralMaterialType` | StructuralMaterialType |
| `Void Activate()` | `familySymbol.Activate()` | Void |
| `Boolean CanHaveStructuralSection()` | `familySymbol.CanHaveStructuralSection()` | Boolean |
| `IList<FamilyPointLocation> GetFamilyPointLocations()` | `familySymbol.GetFamilyPointLocations()` | IList<FamilyPointLocation> |
| `StructuralSection GetStructuralSection()` | `familySymbol.GetStructuralSection()` | StructuralSection |
| `FamilyThermalProperties GetThermalProperties()` | `familySymbol.GetThermalProperties()` | FamilyThermalProperties |
| `Boolean HasThermalProperties()` | `familySymbol.HasThermalProperties()` | Boolean |
| `Void SetStructuralSection(StructuralSection)` | `familySymbol.SetStructuralSection(structuralSection)` | Void |
| `Void SetThermalProperties(FamilyThermalProperties)` | `familySymbol.SetThermalProperties(thermalProperties)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
