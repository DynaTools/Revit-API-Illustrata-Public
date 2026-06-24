---
title: DGNExportOptions
classe: Autodesk.Revit.DB.DGNExportOptions
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.BaseExportOptions
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# DGNExportOptions

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `DGNFileFormat FileVersion { get; set; }` | `dGNExportOptions.FileVersion` | DGNFileFormat |
| `Boolean MergedViews { get; set; }` | `dGNExportOptions.MergedViews` | Boolean |
| `String SeedName { get; set; }` | `dGNExportOptions.SeedName` | String |
| `Boolean WorkingUnits { get; set; }` | `dGNExportOptions.WorkingUnits` | Boolean |
| `ExportLineweightTable GetExportLineweightTable()` | `dGNExportOptions.GetExportLineweightTable()` | ExportLineweightTable |
| `DGNExportOptions GetPredefinedOptions(Document, String)` | `DGNExportOptions.GetPredefinedOptions(document, setup)` | DGNExportOptions |
| `IList<String> GetPredefinedSetupNames(Document)` | `DGNExportOptions.GetPredefinedSetupNames(document)` | IList<String> |
| `Void SetExportLineweightTable(ExportLineweightTable)` | `dGNExportOptions.SetExportLineweightTable(lineweightTable)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
