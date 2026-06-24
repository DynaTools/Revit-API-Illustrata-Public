---
title: PointOnPlane
classe: Autodesk.Revit.DB.PointOnPlane
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.PointElementReference
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# PointOnPlane

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double Offset { get; set; }` | `pointOnPlane.Offset` | Double |
| `UV Position { get; set; }` | `pointOnPlane.Position` | UV |
| `UV XVec { get; set; }` | `pointOnPlane.XVec` | UV |
| `Reference GetPlaneReference()` | `pointOnPlane.GetPlaneReference()` | Reference |
| `Boolean IsValidPlaneReference(Document, Reference)` | `PointOnPlane.IsValidPlaneReference(doc, planeReference)` | Boolean |
| `PointOnPlane NewPointOnPlane(Document, Reference, XYZ, XYZ)` | `PointOnPlane.NewPointOnPlane(doc, planeReference, position, xvec)` | PointOnPlane |
| `Void SetPlaneReference(Reference)` | `pointOnPlane.SetPlaneReference(planeReference)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
