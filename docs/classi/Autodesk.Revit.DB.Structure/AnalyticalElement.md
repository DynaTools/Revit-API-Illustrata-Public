---
title: AnalyticalElement
classe: Autodesk.Revit.DB.Structure.AnalyticalElement
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 12
---

# AnalyticalElement

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `AnalyzeAs AnalyzeAs { get; set; }` | `analyticalElement.AnalyzeAs` | AnalyzeAs |
| `ElementId MaterialId { get; set; }` | `analyticalElement.MaterialId` | ElementId |
| `AnalyticalStructuralRole StructuralRole { get; set; }` | `analyticalElement.StructuralRole` | AnalyticalStructuralRole |
| `Curve GetCurve()` | `analyticalElement.GetCurve()` | Curve |
| `Reference GetReference(AnalyticalModelSelector)` | `analyticalElement.GetReference(selector)` | Reference |
| `Transform GetTransform()` | `analyticalElement.GetTransform()` | Transform |
| `Boolean IsSingleCurve()` | `analyticalElement.IsSingleCurve()` | Boolean |
| `Boolean IsValidAnalyzeAs(AnalyzeAs)` | `analyticalElement.IsValidAnalyzeAs(analyzeAs)` | Boolean |
| `Boolean IsValidSelector(AnalyticalModelSelector)` | `analyticalElement.IsValidSelector(selector)` | Boolean |
| `Boolean IsValidStructuralRole(AnalyticalStructuralRole)` | `analyticalElement.IsValidStructuralRole(structuralRole)` | Boolean |
| `Boolean IsValidTransform(Transform)` | `analyticalElement.IsValidTransform(trf)` | Boolean |
| `Void SetTransform(Transform)` | `analyticalElement.SetTransform(trf)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
