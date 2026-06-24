---
title: IFCExportOptions
classe: Autodesk.Revit.DB.IFCExportOptions
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# IFCExportOptions

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean ExportBaseQuantities { get; set; }` | `iFCExportOptions.ExportBaseQuantities` | Boolean |
| `String FamilyMappingFile { get; set; }` | `iFCExportOptions.FamilyMappingFile` | String |
| `IFCVersion FileVersion { get; set; }` | `iFCExportOptions.FileVersion` | IFCVersion |
| `ElementId FilterViewId { get; set; }` | `iFCExportOptions.FilterViewId` | ElementId |
| `Boolean IsValidObject { get; }` | `iFCExportOptions.IsValidObject` | Boolean |
| `Int32 SpaceBoundaryLevel { get; set; }` | `iFCExportOptions.SpaceBoundaryLevel` | Int32 |
| `Boolean WallAndColumnSplitting { get; set; }` | `iFCExportOptions.WallAndColumnSplitting` | Boolean |
| `Void AddOption(String, String)` | `iFCExportOptions.AddOption(name, value)` | Void |
| `Void Assign(IFCExportOptions)` | `iFCExportOptions.Assign(sourceOptions)` | Void |
| `Void Dispose()` | `iFCExportOptions.Dispose()` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
