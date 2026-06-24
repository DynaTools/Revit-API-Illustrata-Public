---
title: Parameter
classe: Autodesk.Revit.DB.Parameter
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 29
---

# Parameter

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Definition Definition { get; }` | `parameter.Definition` | Definition |
| `Element Element { get; }` | `parameter.Element` | Element |
| `Guid GUID { get; }` | `parameter.GUID` | Guid |
| `Boolean HasValue { get; }` | `parameter.HasValue` | Boolean |
| `ElementId Id { get; }` | `parameter.Id` | ElementId |
| `Boolean IsReadOnly { get; }` | `parameter.IsReadOnly` | Boolean |
| `Boolean IsShared { get; }` | `parameter.IsShared` | Boolean |
| `StorageType StorageType { get; }` | `parameter.StorageType` | StorageType |
| `Boolean UserModifiable { get; }` | `parameter.UserModifiable` | Boolean |
| `Double AsDouble()` | `parameter.AsDouble()` | Double |
| `ElementId AsElementId()` | `parameter.AsElementId()` | ElementId |
| `Int32 AsInteger()` | `parameter.AsInteger()` | Int32 |
| `Void AssociateWithGlobalParameter(ElementId)` | `parameter.AssociateWithGlobalParameter(gpId)` | Void |
| `String AsString()` | `parameter.AsString()` | String |
| `String AsValueString(FormatOptions)` | `parameter.AsValueString(formatOptions)` | String |
| `String AsValueString()` | `parameter.AsValueString()` | String |
| `Boolean CanBeAssociatedWithGlobalParameter(ElementId)` | `parameter.CanBeAssociatedWithGlobalParameter(gpId)` | Boolean |
| `Boolean CanBeAssociatedWithGlobalParameters()` | `parameter.CanBeAssociatedWithGlobalParameters()` | Boolean |
| `Boolean ClearValue()` | `parameter.ClearValue()` | Boolean |
| `Void DissociateFromGlobalParameter()` | `parameter.DissociateFromGlobalParameter()` | Void |
| `ElementId GetAssociatedGlobalParameter()` | `parameter.GetAssociatedGlobalParameter()` | ElementId |
| `ForgeTypeId GetTypeId()` | `parameter.GetTypeId()` | ForgeTypeId |
| `ForgeTypeId GetUnitTypeId()` | `parameter.GetUnitTypeId()` | ForgeTypeId |
| `Boolean Set(ElementId)` | `parameter.Set(value)` | Boolean |
| `Boolean Set(Double)` | `parameter.Set(value)` | Boolean |
| `Boolean Set(Int32)` | `parameter.Set(value)` | Boolean |
| `Boolean Set(String)` | `parameter.Set(value)` | Boolean |
| `List<Parameter> SetMultiple(IList<Tuple<Parameter, ParameterValue>>)` | `Parameter.SetMultiple(values)` | List<Parameter> |
| `Boolean SetValueString(String)` | `parameter.SetValueString(valueString)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
