---
title: FamilyManager
classe: Autodesk.Revit.DB.FamilyManager
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 39
---

# FamilyManager

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `FamilyType CurrentType { get; set; }` | `familyManager.CurrentType` | FamilyType |
| `FamilyParameter Parameter { get; }` | `familyManager.Parameter` | FamilyParameter |
| `FamilyParameter Parameter { get; }` | `familyManager.Parameter` | FamilyParameter |
| `FamilyParameter Parameter { get; }` | `familyManager.Parameter` | FamilyParameter |
| `FamilyParameter Parameter { get; }` | `familyManager.Parameter` | FamilyParameter |
| `FamilyParameterSet Parameters { get; }` | `familyManager.Parameters` | FamilyParameterSet |
| `FamilyTypeSet Types { get; }` | `familyManager.Types` | FamilyTypeSet |
| `FamilyParameter AddParameter(String, ForgeTypeId, Category, Boolean)` | `familyManager.AddParameter(parameterName, groupTypeId, familyCategory, isInstance)` | FamilyParameter |
| `FamilyParameter AddParameter(String, ForgeTypeId, ForgeTypeId, Boolean)` | `familyManager.AddParameter(parameterName, groupTypeId, specTypeId, isInstance)` | FamilyParameter |
| `FamilyParameter AddParameter(ExternalDefinition, ForgeTypeId, Boolean)` | `familyManager.AddParameter(familyDefinition, groupTypeId, isInstance)` | FamilyParameter |
| `Void AssociateElementParameterToFamilyParameter(Parameter, FamilyParameter)` | `familyManager.AssociateElementParameterToFamilyParameter(elementParameter, familyParameter)` | Void |
| `Boolean CanElementParameterBeAssociated(Parameter)` | `familyManager.CanElementParameterBeAssociated(elementParameter)` | Boolean |
| `Void DeleteCurrentType()` | `familyManager.DeleteCurrentType()` | Void |
| `FamilyParameter GetAssociatedFamilyParameter(Parameter)` | `familyManager.GetAssociatedFamilyParameter(elementParameter)` | FamilyParameter |
| `FamilyParameter GetParameter(ForgeTypeId)` | `familyManager.GetParameter(parameterTypeId)` | FamilyParameter |
| `IList<FamilyParameter> GetParameters()` | `familyManager.GetParameters()` | IList<FamilyParameter> |
| `Boolean IsParameterLockable(FamilyParameter)` | `familyManager.IsParameterLockable(familyParameter)` | Boolean |
| `Boolean IsParameterLocked(FamilyParameter)` | `familyManager.IsParameterLocked(familyParameter)` | Boolean |
| `Boolean IsUserAssignableParameterGroup(ForgeTypeId)` | `familyManager.IsUserAssignableParameterGroup(groupTypeId)` | Boolean |
| `Void MakeInstance(FamilyParameter)` | `familyManager.MakeInstance(familyParameter)` | Void |
| `Void MakeNonReporting(FamilyParameter)` | `familyManager.MakeNonReporting(familyParameter)` | Void |
| `Void MakeReporting(FamilyParameter)` | `familyManager.MakeReporting(familyParameter)` | Void |
| `Void MakeType(FamilyParameter)` | `familyManager.MakeType(familyParameter)` | Void |
| `FamilyType NewType(String)` | `familyManager.NewType(typeName)` | FamilyType |
| `Void RemoveParameter(FamilyParameter)` | `familyManager.RemoveParameter(familyParameter)` | Void |
| `Void RenameCurrentType(String)` | `familyManager.RenameCurrentType(typeName)` | Void |
| `Void RenameParameter(FamilyParameter, String)` | `familyManager.RenameParameter(familyParameter, name)` | Void |
| `Void ReorderParameters(IList<FamilyParameter>)` | `familyManager.ReorderParameters(parameters)` | Void |
| `FamilyParameter ReplaceParameter(FamilyParameter, String, ForgeTypeId, Boolean)` | `familyManager.ReplaceParameter(currentParameter, parameterName, groupTypeId, isInstance)` | FamilyParameter |
| `FamilyParameter ReplaceParameter(FamilyParameter, ExternalDefinition, ForgeTypeId, Boolean)` | `familyManager.ReplaceParameter(currentParameter, familyDefinition, groupTypeId, isInstance)` | FamilyParameter |
| `Void Set(FamilyParameter, ElementId)` | `familyManager.Set(familyParameter, value)` | Void |
| `Void Set(FamilyParameter, Double)` | `familyManager.Set(familyParameter, value)` | Void |
| `Void Set(FamilyParameter, String)` | `familyManager.Set(familyParameter, value)` | Void |
| `Void Set(FamilyParameter, Int32)` | `familyManager.Set(familyParameter, value)` | Void |
| `Void SetDescription(FamilyParameter, String)` | `familyManager.SetDescription(familyParameter, description)` | Void |
| `Void SetFormula(FamilyParameter, String)` | `familyManager.SetFormula(familyParameter, formula)` | Void |
| `Void SetParameterLocked(FamilyParameter, Boolean)` | `familyManager.SetParameterLocked(familyParameter, locked)` | Void |
| `Void SetValueString(FamilyParameter, String)` | `familyManager.SetValueString(familyParameter, value)` | Void |
| `Void SortParameters(ParametersOrder)` | `familyManager.SortParameters(order)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
