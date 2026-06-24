---
title: Line
classe: Autodesk.Revit.DB.Line
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Curve
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 4
---

# Line

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ Direction { get; }` | `line.Direction` | XYZ |
| `XYZ Origin { get; }` | `line.Origin` | XYZ |
| `Line CreateBound(XYZ, XYZ)` | `Line.CreateBound(endpoint1, endpoint2)` | Line |
| `Line CreateUnbound(XYZ, XYZ)` | `Line.CreateUnbound(origin, direction)` | Line |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
