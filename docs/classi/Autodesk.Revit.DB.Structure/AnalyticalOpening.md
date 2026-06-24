---
title: AnalyticalOpening
classe: Autodesk.Revit.DB.Structure.AnalyticalOpening
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Structure.AnalyticalSurfaceBase
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 3
---

# AnalyticalOpening

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId PanelId { get; }` | `analyticalOpening.PanelId` | ElementId |
| `AnalyticalOpening Create(Document, CurveLoop, ElementId)` | `AnalyticalOpening.Create(aDoc, curveLoop, panelId)` | AnalyticalOpening |
| `Boolean IsCurveLoopValidForAnalyticalOpening(CurveLoop, Document, ElementId)` | `AnalyticalOpening.IsCurveLoopValidForAnalyticalOpening(loop, aDoc, panelId)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
