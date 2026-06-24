---
title: SketchPlane
classe: Autodesk.Revit.DB.SketchPlane
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 6
---

# SketchPlane

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsSuitableForModelElements { get; }` | `sketchPlane.IsSuitableForModelElements` | Boolean |
| `SketchPlane Create(Document, ElementId)` | `SketchPlane.Create(document, datumId)` | SketchPlane |
| `SketchPlane Create(Document, Reference)` | `SketchPlane.Create(document, planarFaceReference)` | SketchPlane |
| `SketchPlane Create(Document, Plane)` | `SketchPlane.Create(document, plane)` | SketchPlane |
| `Plane GetPlane()` | `sketchPlane.GetPlane()` | Plane |
| `Reference GetPlaneReference()` | `sketchPlane.GetPlaneReference()` | Reference |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
