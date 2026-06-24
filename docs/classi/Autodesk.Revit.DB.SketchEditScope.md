---
title: SketchEditScope
classe: Autodesk.Revit.DB.SketchEditScope
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.EditScope
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 5
---

# SketchEditScope

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsElementWithoutSketch(ElementId)` | `sketchEditScope.IsElementWithoutSketch(elementId)` | Boolean |
| `Boolean IsSketchEditingSupported(ElementId)` | `sketchEditScope.IsSketchEditingSupported(sketchId)` | Boolean |
| `Boolean IsSketchEditingSupportedForSketchBasedElement(ElementId)` | `sketchEditScope.IsSketchEditingSupportedForSketchBasedElement(elemId)` | Boolean |
| `Void Start(ElementId)` | `sketchEditScope.Start(sketchId)` | Void |
| `Void StartWithNewSketch(ElementId)` | `sketchEditScope.StartWithNewSketch(elementId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
