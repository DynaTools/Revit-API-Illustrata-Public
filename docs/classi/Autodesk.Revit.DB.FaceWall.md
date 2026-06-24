---
title: FaceWall
classe: Autodesk.Revit.DB.FaceWall
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.HostObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 3
---

# FaceWall

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `FaceWall Create(Document, ElementId, WallLocationLine, Reference)` | `FaceWall.Create(document, wallType, locationLine, faceReference)` | FaceWall |
| `Boolean IsValidFaceReferenceForFaceWall(Document, Reference)` | `FaceWall.IsValidFaceReferenceForFaceWall(document, faceReference)` | Boolean |
| `Boolean IsWallTypeValidForFaceWall(Document, ElementId)` | `FaceWall.IsWallTypeValidForFaceWall(document, wallType)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
