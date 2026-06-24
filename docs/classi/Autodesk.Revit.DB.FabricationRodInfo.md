---
title: FabricationRodInfo
classe: Autodesk.Revit.DB.FabricationRodInfo
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 18
---

# FabricationRodInfo

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean CanRodsBeHosted { get; set; }` | `fabricationRodInfo.CanRodsBeHosted` | Boolean |
| `Boolean IsAttachedToStructure { get; }` | `fabricationRodInfo.IsAttachedToStructure` | Boolean |
| `Boolean IsValidObject { get; }` | `fabricationRodInfo.IsValidObject` | Boolean |
| `Int32 RodCount { get; }` | `fabricationRodInfo.RodCount` | Int32 |
| `Void AttachToHanger(ElementId, Int32, XYZ)` | `fabricationRodInfo.AttachToHanger(hangerId, rodIndex, position)` | Void |
| `Void AttachToStructure()` | `fabricationRodInfo.AttachToStructure()` | Void |
| `Void Dispose()` | `fabricationRodInfo.Dispose()` | Void |
| `Double GetBearerExtension(Int32)` | `fabricationRodInfo.GetBearerExtension(rodIndex)` | Double |
| `LinkElementId GetRodAttachedElementId(Int32)` | `fabricationRodInfo.GetRodAttachedElementId(rodIndex)` | LinkElementId |
| `XYZ GetRodEndPosition(Int32)` | `fabricationRodInfo.GetRodEndPosition(rodIndex)` | XYZ |
| `Double GetRodLength(Int32)` | `fabricationRodInfo.GetRodLength(rodIndex)` | Double |
| `Double GetRodStructureExtension(Int32)` | `fabricationRodInfo.GetRodStructureExtension(rodIndex)` | Double |
| `Boolean IsRodLockedWithHost(Int32)` | `fabricationRodInfo.IsRodLockedWithHost(rodIndex)` | Boolean |
| `Void SetBearerExtension(Int32, Double)` | `fabricationRodInfo.SetBearerExtension(rodIndex, length)` | Void |
| `Void SetRodEndPosition(Int32, XYZ)` | `fabricationRodInfo.SetRodEndPosition(rodIndex, position)` | Void |
| `Boolean SetRodLength(Int32, Double)` | `fabricationRodInfo.SetRodLength(rodIndex, newLength)` | Boolean |
| `Void SetRodLockedWithHost(Int32, Boolean)` | `fabricationRodInfo.SetRodLockedWithHost(rodIndex, locked)` | Void |
| `Boolean SetRodStructureExtension(Int32, Double)` | `fabricationRodInfo.SetRodStructureExtension(rodIndex, extension)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
