---
title: GeometryInstance
classe: Autodesk.Revit.DB.GeometryInstance
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.GeometryObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# GeometryInstance

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `GeometryElement SymbolGeometry { get; }` | `geometryInstance.SymbolGeometry` | GeometryElement |
| `Transform Transform { get; }` | `geometryInstance.Transform` | Transform |
| `Document GetDocument()` | `geometryInstance.GetDocument()` | Document |
| `GeometryElement GetInstanceGeometry(Transform)` | `geometryInstance.GetInstanceGeometry(transform)` | GeometryElement |
| `GeometryElement GetInstanceGeometry()` | `geometryInstance.GetInstanceGeometry()` | GeometryElement |
| `GeometryElement GetSymbolGeometry(Transform)` | `geometryInstance.GetSymbolGeometry(transform)` | GeometryElement |
| `GeometryElement GetSymbolGeometry()` | `geometryInstance.GetSymbolGeometry()` | GeometryElement |
| `SymbolGeometryId GetSymbolGeometryId()` | `geometryInstance.GetSymbolGeometryId()` | SymbolGeometryId |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
