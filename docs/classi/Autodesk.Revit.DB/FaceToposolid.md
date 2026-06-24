---
title: FaceToposolid
classe: Autodesk.Revit.DB.FaceToposolid
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.HostObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 4
---

# FaceToposolid

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `FaceToposolid Create(Document, ElementId, ElementId, IList<Reference>)` | `FaceToposolid.Create(document, toposolidTypeId, levelId, faceReferences)` | FaceToposolid |
| `IList<Reference> GetReferencedFaces()` | `faceToposolid.GetReferencedFaces()` | IList<Reference> |
| `Void SetFaceReferences(IList<Reference>)` | `faceToposolid.SetFaceReferences(faceReferences)` | Void |
| `Void UpdateToFace()` | `faceToposolid.UpdateToFace()` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
