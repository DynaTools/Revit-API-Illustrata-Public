---
title: PolyLine
classe: Autodesk.Revit.DB.PolyLine
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.GeometryObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# PolyLine

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 NumberOfCoordinates { get; }` | `polyLine.NumberOfCoordinates` | Int32 |
| `PolyLine Clone()` | `polyLine.Clone()` | PolyLine |
| `PolyLine Create(IList<XYZ>)` | `PolyLine.Create(coordinates)` | PolyLine |
| `XYZ Evaluate(Double)` | `polyLine.Evaluate(param)` | XYZ |
| `XYZ GetCoordinate(Int32)` | `polyLine.GetCoordinate(index)` | XYZ |
| `IList<XYZ> GetCoordinates()` | `polyLine.GetCoordinates()` | IList<XYZ> |
| `Outline GetOutline()` | `polyLine.GetOutline()` | Outline |
| `PolyLine GetTransformed(Transform)` | `polyLine.GetTransformed(transform)` | PolyLine |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
