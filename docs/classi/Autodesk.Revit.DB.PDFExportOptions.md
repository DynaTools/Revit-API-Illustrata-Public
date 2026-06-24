---
title: PDFExportOptions
classe: Autodesk.Revit.DB.PDFExportOptions
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 28
---

# PDFExportOptions

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean AlwaysUseRaster { get; set; }` | `pDFExportOptions.AlwaysUseRaster` | Boolean |
| `ColorDepthType ColorDepth { get; set; }` | `pDFExportOptions.ColorDepth` | ColorDepthType |
| `Boolean Combine { get; set; }` | `pDFExportOptions.Combine` | Boolean |
| `PDFExportQualityType ExportQuality { get; set; }` | `pDFExportOptions.ExportQuality` | PDFExportQualityType |
| `String FileName { get; set; }` | `pDFExportOptions.FileName` | String |
| `Boolean HideCropBoundaries { get; set; }` | `pDFExportOptions.HideCropBoundaries` | Boolean |
| `Boolean HideReferencePlane { get; set; }` | `pDFExportOptions.HideReferencePlane` | Boolean |
| `Boolean HideScopeBoxes { get; set; }` | `pDFExportOptions.HideScopeBoxes` | Boolean |
| `Boolean HideUnreferencedViewTags { get; set; }` | `pDFExportOptions.HideUnreferencedViewTags` | Boolean |
| `Boolean IsValidObject { get; }` | `pDFExportOptions.IsValidObject` | Boolean |
| `Boolean MaskCoincidentLines { get; set; }` | `pDFExportOptions.MaskCoincidentLines` | Boolean |
| `Double OriginOffsetX { get; set; }` | `pDFExportOptions.OriginOffsetX` | Double |
| `Double OriginOffsetY { get; set; }` | `pDFExportOptions.OriginOffsetY` | Double |
| `ExportPaperFormat PaperFormat { get; set; }` | `pDFExportOptions.PaperFormat` | ExportPaperFormat |
| `PageOrientationType PaperOrientation { get; set; }` | `pDFExportOptions.PaperOrientation` | PageOrientationType |
| `PaperPlacementType PaperPlacement { get; set; }` | `pDFExportOptions.PaperPlacement` | PaperPlacementType |
| `RasterQualityType RasterQuality { get; set; }` | `pDFExportOptions.RasterQuality` | RasterQualityType |
| `Boolean ReplaceHalftoneWithThinLines { get; set; }` | `pDFExportOptions.ReplaceHalftoneWithThinLines` | Boolean |
| `Boolean StopOnError { get; set; }` | `pDFExportOptions.StopOnError` | Boolean |
| `Boolean ViewLinksInBlue { get; set; }` | `pDFExportOptions.ViewLinksInBlue` | Boolean |
| `Int32 ZoomPercentage { get; set; }` | `pDFExportOptions.ZoomPercentage` | Int32 |
| `ZoomType ZoomType { get; set; }` | `pDFExportOptions.ZoomType` | ZoomType |
| `Void Dispose()` | `pDFExportOptions.Dispose()` | Void |
| `Boolean GetExportInBackground()` | `pDFExportOptions.GetExportInBackground()` | Boolean |
| `IList<TableCellCombinedParameterData> GetNamingRule()` | `pDFExportOptions.GetNamingRule()` | IList<TableCellCombinedParameterData> |
| `Boolean IsValidNamingRule(IList<TableCellCombinedParameterData>)` | `PDFExportOptions.IsValidNamingRule(namingRule)` | Boolean |
| `Void SetExportInBackground(Boolean)` | `pDFExportOptions.SetExportInBackground(exportInBackground)` | Void |
| `Void SetNamingRule(IList<TableCellCombinedParameterData>)` | `pDFExportOptions.SetNamingRule(namingRule)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
