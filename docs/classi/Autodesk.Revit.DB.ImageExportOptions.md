---
title: ImageExportOptions
classe: Autodesk.Revit.DB.ImageExportOptions
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 18
---

# ImageExportOptions

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ExportRange ExportRange { get; set; }` | `imageExportOptions.ExportRange` | ExportRange |
| `String FilePath { get; set; }` | `imageExportOptions.FilePath` | String |
| `FitDirectionType FitDirection { get; set; }` | `imageExportOptions.FitDirection` | FitDirectionType |
| `ImageFileType HLRandWFViewsFileType { get; set; }` | `imageExportOptions.HLRandWFViewsFileType` | ImageFileType |
| `ImageResolution ImageResolution { get; set; }` | `imageExportOptions.ImageResolution` | ImageResolution |
| `Boolean IsValidObject { get; }` | `imageExportOptions.IsValidObject` | Boolean |
| `Int32 PixelSize { get; set; }` | `imageExportOptions.PixelSize` | Int32 |
| `ImageFileType ShadowViewsFileType { get; set; }` | `imageExportOptions.ShadowViewsFileType` | ImageFileType |
| `Boolean ShouldCreateWebSite { get; set; }` | `imageExportOptions.ShouldCreateWebSite` | Boolean |
| `String ViewName { get; set; }` | `imageExportOptions.ViewName` | String |
| `Int32 Zoom { get; set; }` | `imageExportOptions.Zoom` | Int32 |
| `ZoomFitType ZoomType { get; set; }` | `imageExportOptions.ZoomType` | ZoomFitType |
| `Void Dispose()` | `imageExportOptions.Dispose()` | Void |
| `String GetFileName(Document, ElementId)` | `ImageExportOptions.GetFileName(aDoc, dbViewId)` | String |
| `IList<ElementId> GetViewsAndSheets()` | `imageExportOptions.GetViewsAndSheets()` | IList<ElementId> |
| `Boolean IsValidFileName(String)` | `ImageExportOptions.IsValidFileName(filePath)` | Boolean |
| `Boolean IsValidForSaveToProjectAsImage(ImageExportOptions, Document)` | `ImageExportOptions.IsValidForSaveToProjectAsImage(options, doc)` | Boolean |
| `Void SetViewsAndSheets(IList<ElementId>)` | `imageExportOptions.SetViewsAndSheets(viewsAndSheets)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
