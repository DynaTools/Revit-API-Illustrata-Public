---
title: CableTray
classe: Autodesk.Revit.DB.Electrical.CableTray
namespace: Autodesk.Revit.DB.Electrical
eredita: Autodesk.Revit.DB.Electrical.CableTrayConduitBase
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 6
---

# CableTray

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ CurveNormal { get; set; }` | `cableTray.CurveNormal` | XYZ |
| `Double RungSpace { get; set; }` | `cableTray.RungSpace` | Double |
| `CableTray Create(Document, ElementId, XYZ, XYZ, ElementId)` | `CableTray.Create(document, cabletrayType, startPoint, endPoint, levelId)` | CableTray |
| `CableTrayShape GetShapeType()` | `cableTray.GetShapeType()` | CableTrayShape |
| `Boolean IsValidCableTrayType(Document, ElementId)` | `CableTray.IsValidCableTrayType(document, cabletrayType)` | Boolean |
| `Boolean IsValidRungSpace(Double)` | `cableTray.IsValidRungSpace(rungSpace)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
