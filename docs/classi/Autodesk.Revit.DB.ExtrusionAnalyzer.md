---
title: ExtrusionAnalyzer
classe: Autodesk.Revit.DB.ExtrusionAnalyzer
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# ExtrusionAnalyzer

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double EndParameter { get; }` | `extrusionAnalyzer.EndParameter` | Double |
| `XYZ ExtrusionDirection { get; }` | `extrusionAnalyzer.ExtrusionDirection` | XYZ |
| `Boolean IsValidObject { get; }` | `extrusionAnalyzer.IsValidObject` | Boolean |
| `Double StartParameter { get; }` | `extrusionAnalyzer.StartParameter` | Double |
| `IDictionary<Face, ExtrusionAnalyzerFaceAlignment> CalculateFaceAlignment()` | `extrusionAnalyzer.CalculateFaceAlignment()` | IDictionary<Face, ExtrusionAnalyzerFaceAlignment> |
| `ExtrusionAnalyzer Create(Solid, Plane, XYZ)` | `ExtrusionAnalyzer.Create(solidGeometry, plane, direction)` | ExtrusionAnalyzer |
| `Void Dispose()` | `extrusionAnalyzer.Dispose()` | Void |
| `Face GetExtrusionBase()` | `extrusionAnalyzer.GetExtrusionBase()` | Face |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
