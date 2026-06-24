---
title: ExportDGNSettings
classe: Autodesk.Revit.DB.ExportDGNSettings
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# ExportDGNSettings

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ExportDGNSettings Create(Document, String, DGNExportOptions)` | `ExportDGNSettings.Create(document, name, options)` | ExportDGNSettings |
| `ExportDGNSettings Create(Document, String)` | `ExportDGNSettings.Create(document, name)` | ExportDGNSettings |
| `ExportDGNSettings FindByName(Document, String)` | `ExportDGNSettings.FindByName(aDoc, name)` | ExportDGNSettings |
| `ExportDGNSettings GetActivePredefinedSettings(Document)` | `ExportDGNSettings.GetActivePredefinedSettings(aDoc)` | ExportDGNSettings |
| `DGNExportOptions GetDGNExportOptions()` | `exportDGNSettings.GetDGNExportOptions()` | DGNExportOptions |
| `IList<String> ListNames(Document)` | `ExportDGNSettings.ListNames(aDoc)` | IList<String> |
| `Void SetDGNExportOptions(DGNExportOptions)` | `exportDGNSettings.SetDGNExportOptions(options)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
