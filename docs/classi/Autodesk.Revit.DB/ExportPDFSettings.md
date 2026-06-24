---
title: ExportPDFSettings
classe: Autodesk.Revit.DB.ExportPDFSettings
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# ExportPDFSettings

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ExportPDFSettings Create(Document, String, PDFExportOptions)` | `ExportPDFSettings.Create(document, name, options)` | ExportPDFSettings |
| `ExportPDFSettings FindByName(Document, String)` | `ExportPDFSettings.FindByName(document, name)` | ExportPDFSettings |
| `ExportPDFSettings GetActivePredefinedSettings(Document)` | `ExportPDFSettings.GetActivePredefinedSettings(document)` | ExportPDFSettings |
| `PDFExportOptions GetOptions()` | `exportPDFSettings.GetOptions()` | PDFExportOptions |
| `Boolean IsValidName(Document, String)` | `ExportPDFSettings.IsValidName(document, name)` | Boolean |
| `IList<String> ListNames(Document)` | `ExportPDFSettings.ListNames(document)` | IList<String> |
| `Void SetOptions(PDFExportOptions)` | `exportPDFSettings.SetOptions(options)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
