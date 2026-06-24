---
title: InternalDefinition
classe: Autodesk.Revit.DB.InternalDefinition
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Definition
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 12
---

# InternalDefinition

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `BuiltInParameter BuiltInParameter { get; }` | `internalDefinition.BuiltInParameter` | BuiltInParameter |
| `ElementId Id { get; }` | `internalDefinition.Id` | ElementId |
| `Boolean IsValidObject { get; }` | `internalDefinition.IsValidObject` | Boolean |
| `String Name { get; }` | `internalDefinition.Name` | String |
| `Boolean VariesAcrossGroups { get; }` | `internalDefinition.VariesAcrossGroups` | Boolean |
| `Boolean Visible { get; }` | `internalDefinition.Visible` | Boolean |
| `Void Dispose()` | `internalDefinition.Dispose()` | Void |
| `ForgeTypeId GetGroupTypeId()` | `internalDefinition.GetGroupTypeId()` | ForgeTypeId |
| `ForgeTypeId GetParameterTypeId()` | `internalDefinition.GetParameterTypeId()` | ForgeTypeId |
| `ForgeTypeId GetTypeId()` | `internalDefinition.GetTypeId()` | ForgeTypeId |
| `ICollection<ElementId> SetAllowVaryBetweenGroups(Document, Boolean)` | `internalDefinition.SetAllowVaryBetweenGroups(document, allowVaryBetweenGroups)` | ICollection<ElementId> |
| `Void SetGroupTypeId(ForgeTypeId)` | `internalDefinition.SetGroupTypeId(groupTypeId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
