---
title: AnalysisDisplayStyle
classe: Autodesk.Revit.DB.Analysis.AnalysisDisplayStyle
namespace: Autodesk.Revit.DB.Analysis
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 29
---

# AnalysisDisplayStyle

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `AnalysisDisplayStyle CreateAnalysisDisplayStyle(Document, String, AnalysisDisplayDeformedShapeSettings, AnalysisDisplayColorSettings, AnalysisDisplayLegendSettings)` | `AnalysisDisplayStyle.CreateAnalysisDisplayStyle(document, name, deformedShapeSettings, colorSettings, legendSettings)` | AnalysisDisplayStyle |
| `AnalysisDisplayStyle CreateAnalysisDisplayStyle(Document, String, AnalysisDisplayVectorSettings, AnalysisDisplayColorSettings, AnalysisDisplayLegendSettings)` | `AnalysisDisplayStyle.CreateAnalysisDisplayStyle(document, name, vectorSettings, colorSettings, legendSettings)` | AnalysisDisplayStyle |
| `AnalysisDisplayStyle CreateAnalysisDisplayStyle(Document, String, AnalysisDisplayDiagramSettings, AnalysisDisplayColorSettings, AnalysisDisplayLegendSettings)` | `AnalysisDisplayStyle.CreateAnalysisDisplayStyle(document, name, diagramSettings, colorSettings, legendSettings)` | AnalysisDisplayStyle |
| `AnalysisDisplayStyle CreateAnalysisDisplayStyle(Document, String, AnalysisDisplayMarkersAndTextSettings, AnalysisDisplayColorSettings, AnalysisDisplayLegendSettings)` | `AnalysisDisplayStyle.CreateAnalysisDisplayStyle(document, name, markersAndTextSettings, colorSettings, legendSettings)` | AnalysisDisplayStyle |
| `AnalysisDisplayStyle CreateAnalysisDisplayStyle(Document, String, AnalysisDisplayColoredSurfaceSettings, AnalysisDisplayColorSettings, AnalysisDisplayLegendSettings)` | `AnalysisDisplayStyle.CreateAnalysisDisplayStyle(document, name, coloredSurfaceSettings, colorSettings, legendSettings)` | AnalysisDisplayStyle |
| `ElementId FindByName(Document, String)` | `AnalysisDisplayStyle.FindByName(document, name)` | ElementId |
| `AnalysisDisplayColoredSurfaceSettings GetColoredSurfaceSettings()` | `analysisDisplayStyle.GetColoredSurfaceSettings()` | AnalysisDisplayColoredSurfaceSettings |
| `AnalysisDisplayColorSettings GetColorSettings()` | `analysisDisplayStyle.GetColorSettings()` | AnalysisDisplayColorSettings |
| `AnalysisDisplayDeformedShapeSettings GetDeformedShapeSettings()` | `analysisDisplayStyle.GetDeformedShapeSettings()` | AnalysisDisplayDeformedShapeSettings |
| `AnalysisDisplayDiagramSettings GetDiagramSettings()` | `analysisDisplayStyle.GetDiagramSettings()` | AnalysisDisplayDiagramSettings |
| `ICollection<ElementId> GetElements(Document)` | `AnalysisDisplayStyle.GetElements(document)` | ICollection<ElementId> |
| `AnalysisDisplayLegendSettings GetLegendSettings()` | `analysisDisplayStyle.GetLegendSettings()` | AnalysisDisplayLegendSettings |
| `AnalysisDisplayMarkersAndTextSettings GetMarkersAndTextSettings()` | `analysisDisplayStyle.GetMarkersAndTextSettings()` | AnalysisDisplayMarkersAndTextSettings |
| `AnalysisDisplayVectorSettings GetVectorSettings()` | `analysisDisplayStyle.GetVectorSettings()` | AnalysisDisplayVectorSettings |
| `Boolean HasColoredSurfaceSettings()` | `analysisDisplayStyle.HasColoredSurfaceSettings()` | Boolean |
| `Boolean HasDeformedShapeSettings()` | `analysisDisplayStyle.HasDeformedShapeSettings()` | Boolean |
| `Boolean HasDiagramSettings()` | `analysisDisplayStyle.HasDiagramSettings()` | Boolean |
| `Boolean HasMarkersAndTextSettings()` | `analysisDisplayStyle.HasMarkersAndTextSettings()` | Boolean |
| `Boolean HasVectorSettings()` | `analysisDisplayStyle.HasVectorSettings()` | Boolean |
| `Boolean IsNameUnique(Document, String, AnalysisDisplayStyle)` | `AnalysisDisplayStyle.IsNameUnique(document, name, excludedElement)` | Boolean |
| `Boolean IsTextTypeIdValid(ElementId, Document)` | `AnalysisDisplayStyle.IsTextTypeIdValid(textTypeId, doc)` | Boolean |
| `Void SetColoredSurfaceSettings(AnalysisDisplayColoredSurfaceSettings)` | `analysisDisplayStyle.SetColoredSurfaceSettings(coloredSurfaceSettings)` | Void |
| `Void SetColorSettings(AnalysisDisplayColorSettings)` | `analysisDisplayStyle.SetColorSettings(colorSettings)` | Void |
| `Void SetDeformedShapeSettings(AnalysisDisplayDeformedShapeSettings)` | `analysisDisplayStyle.SetDeformedShapeSettings(deformedShapeSettings)` | Void |
| `Void SetDiagramSettings(AnalysisDisplayDiagramSettings)` | `analysisDisplayStyle.SetDiagramSettings(diagramSettings)` | Void |
| `Void SetLegendSettings(AnalysisDisplayLegendSettings)` | `analysisDisplayStyle.SetLegendSettings(legendSettings)` | Void |
| `Void SetMarkersAndTextSettings(AnalysisDisplayMarkersAndTextSettings)` | `analysisDisplayStyle.SetMarkersAndTextSettings(markersAndTextSettings)` | Void |
| `Void SetName(String)` | `analysisDisplayStyle.SetName(name)` | Void |
| `Void SetVectorSettings(AnalysisDisplayVectorSettings)` | `analysisDisplayStyle.SetVectorSettings(vectorSettings)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
