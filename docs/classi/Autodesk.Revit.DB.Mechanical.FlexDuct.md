---
title: FlexDuct
classe: Autodesk.Revit.DB.Mechanical.FlexDuct
namespace: Autodesk.Revit.DB.Mechanical
eredita: Autodesk.Revit.DB.MEPCurve
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# FlexDuct

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ EndTangent { get; set; }` | `flexDuct.EndTangent` | XYZ |
| `FlexDuctType FlexDuctType { get; set; }` | `flexDuct.FlexDuctType` | FlexDuctType |
| `IList<XYZ> Points { get; set; }` | `flexDuct.Points` | IList<XYZ> |
| `XYZ StartTangent { get; set; }` | `flexDuct.StartTangent` | XYZ |
| `FlexDuct Create(Document, ElementId, ElementId, ElementId, XYZ, XYZ, IList<XYZ>)` | `FlexDuct.Create(document, systemTypeId, ductTypeId, levelId, startTangent, endTangent, points)` | FlexDuct |
| `FlexDuct Create(Document, ElementId, ElementId, ElementId, IList<XYZ>)` | `FlexDuct.Create(document, systemTypeId, ductTypeId, levelId, points)` | FlexDuct |
| `Boolean IsFlexDuctTypeId(Document, ElementId)` | `FlexDuct.IsFlexDuctTypeId(document, ductTypeId)` | Boolean |
| `Boolean IsHVACSystemTypeId(Document, ElementId)` | `FlexDuct.IsHVACSystemTypeId(document, systemTypeId)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
