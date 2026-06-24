---
title: ViewSystemsAnalysisReport
classe: Autodesk.Revit.DB.Analysis.ViewSystemsAnalysisReport
namespace: Autodesk.Revit.DB.Analysis
eredita: Autodesk.Revit.DB.View
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# ViewSystemsAnalysisReport

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `DateTime AnalysisDateAndTime { get; }` | `viewSystemsAnalysisReport.AnalysisDateAndTime` | DateTime |
| `SystemsAnalysisReportStyle ReportStyle { get; set; }` | `viewSystemsAnalysisReport.ReportStyle` | SystemsAnalysisReportStyle |
| `String SystemsAnalysisOutputFolder { get; }` | `viewSystemsAnalysisReport.SystemsAnalysisOutputFolder` | String |
| `String SystemsAnalysisWorkflowFile { get; }` | `viewSystemsAnalysisReport.SystemsAnalysisWorkflowFile` | String |
| `String WeatherFile { get; }` | `viewSystemsAnalysisReport.WeatherFile` | String |
| `Void CancelSystemsAnalysis(Document, ElementId)` | `ViewSystemsAnalysisReport.CancelSystemsAnalysis(document, reportElement)` | Void |
| `ViewSystemsAnalysisReport Create(Document, String)` | `ViewSystemsAnalysisReport.Create(document, viewName)` | ViewSystemsAnalysisReport |
| `ElementId GetLatestSystemsAnalysisReport(Document)` | `ViewSystemsAnalysisReport.GetLatestSystemsAnalysisReport(document)` | ElementId |
| `String GetReportContent()` | `viewSystemsAnalysisReport.GetReportContent()` | String |
| `Boolean IsAnalysisCompleted()` | `viewSystemsAnalysisReport.IsAnalysisCompleted()` | Boolean |
| `Void RequestSystemsAnalysis(SystemsAnalysisOptions)` | `viewSystemsAnalysisReport.RequestSystemsAnalysis(options)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
