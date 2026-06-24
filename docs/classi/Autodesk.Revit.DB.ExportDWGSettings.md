---
title: ExportDWGSettings
classe: Autodesk.Revit.DB.ExportDWGSettings
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# ExportDWGSettings

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ExportDWGSettings Create(Document, String, DXFExportOptions)` | `ExportDWGSettings.Create(document, name, options)` | ExportDWGSettings |
| `ExportDWGSettings Create(Document, String, DWGExportOptions)` | `ExportDWGSettings.Create(document, name, options)` | ExportDWGSettings |
| `ExportDWGSettings Create(Document, String)` | `ExportDWGSettings.Create(document, name)` | ExportDWGSettings |
| `ExportDWGSettings FindByName(Document, String)` | `ExportDWGSettings.FindByName(aDoc, name)` | ExportDWGSettings |
| `ExportDWGSettings GetActivePredefinedSettings(Document)` | `ExportDWGSettings.GetActivePredefinedSettings(aDoc)` | ExportDWGSettings |
| `DWGExportOptions GetDWGExportOptions()` | `exportDWGSettings.GetDWGExportOptions()` | DWGExportOptions |
| `DXFExportOptions GetDXFExportOptions()` | `exportDWGSettings.GetDXFExportOptions()` | DXFExportOptions |
| `IList<String> ListNames(Document)` | `ExportDWGSettings.ListNames(aDoc)` | IList<String> |
| `Void SetDWGExportOptions(DWGExportOptions)` | `exportDWGSettings.SetDWGExportOptions(options)` | Void |
| `Void SetDXFExportOptions(DXFExportOptions)` | `exportDWGSettings.SetDXFExportOptions(options)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
