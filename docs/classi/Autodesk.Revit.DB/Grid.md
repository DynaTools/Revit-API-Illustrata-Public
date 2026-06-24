---
title: Grid
classe: Autodesk.Revit.DB.Grid
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.DatumPlane
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 6
---

# Grid

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Curve Curve { get; }` | `grid.Curve` | Curve |
| `Boolean IsCurved { get; }` | `grid.IsCurved` | Boolean |
| `Grid Create(Document, Arc)` | `Grid.Create(document, arc)` | Grid |
| `Grid Create(Document, Line)` | `Grid.Create(document, line)` | Grid |
| `Outline GetExtents()` | `grid.GetExtents()` | Outline |
| `Void SetVerticalExtents(Double, Double)` | `grid.SetVerticalExtents(bottom, top)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
