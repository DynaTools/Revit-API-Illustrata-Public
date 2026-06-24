---
title: DisplacementPath
classe: Autodesk.Revit.DB.DisplacementPath
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 6
---

# DisplacementPath

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 AncestorIdx { get; set; }` | `displacementPath.AncestorIdx` | Int32 |
| `DisplacementPathStyle PathStyle { get; set; }` | `displacementPath.PathStyle` | DisplacementPathStyle |
| `ElementId Create(Document, DisplacementElement, Reference, Double)` | `DisplacementPath.Create(aDoc, displacementElement, reference, param)` | ElementId |
| `Boolean IsValidParam(Double)` | `DisplacementPath.IsValidParam(param)` | Boolean |
| `Boolean IsValidReference(DisplacementElement, Reference)` | `DisplacementPath.IsValidReference(displacementElement, reference)` | Boolean |
| `Void SetAnchorPoint(DisplacementElement, Reference, Double)` | `displacementPath.SetAnchorPoint(displacementElement, reference, param)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
