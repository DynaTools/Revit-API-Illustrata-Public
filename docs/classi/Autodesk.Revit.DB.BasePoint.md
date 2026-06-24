---
title: BasePoint
classe: Autodesk.Revit.DB.BasePoint
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 6
---

# BasePoint

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean Clipped { get; set; }` | `basePoint.Clipped` | Boolean |
| `Boolean IsShared { get; }` | `basePoint.IsShared` | Boolean |
| `XYZ Position { get; }` | `basePoint.Position` | XYZ |
| `XYZ SharedPosition { get; set; }` | `basePoint.SharedPosition` | XYZ |
| `BasePoint GetProjectBasePoint(Document)` | `BasePoint.GetProjectBasePoint(cda)` | BasePoint |
| `BasePoint GetSurveyPoint(Document)` | `BasePoint.GetSurveyPoint(cda)` | BasePoint |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
