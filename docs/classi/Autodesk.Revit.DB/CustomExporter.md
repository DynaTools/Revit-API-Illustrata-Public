---
title: CustomExporter
classe: Autodesk.Revit.DB.CustomExporter
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# CustomExporter

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `DisplayStyle Export2DForceDisplayStyle { get; set; }` | `customExporter.Export2DForceDisplayStyle` | DisplayStyle |
| `Boolean Export2DGeometricObjectsIncludingPatternLines { get; set; }` | `customExporter.Export2DGeometricObjectsIncludingPatternLines` | Boolean |
| `Boolean Export2DIncludingAnnotationObjects { get; set; }` | `customExporter.Export2DIncludingAnnotationObjects` | Boolean |
| `Boolean IncludeGeometricObjects { get; set; }` | `customExporter.IncludeGeometricObjects` | Boolean |
| `Boolean IsValidObject { get; }` | `customExporter.IsValidObject` | Boolean |
| `Boolean ShouldStopOnError { get; set; }` | `customExporter.ShouldStopOnError` | Boolean |
| `Void Dispose()` | `customExporter.Dispose()` | Void |
| `Void Export(IList<ElementId>)` | `customExporter.Export(viewIds)` | Void |
| `Void Export(View)` | `customExporter.Export(view)` | Void |
| `Boolean IsRenderingSupported()` | `CustomExporter.IsRenderingSupported()` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
